# Tiny "language model": embeddings (3-d, signed) for every prompt token, concatenated,
# -> tanh hidden layer -> softmax over the vocabulary. Trained with Adam, pure Python.
import math, random, json, sys
def run(task, seed=0, H=6, D=3, epochs=60, lr=0.02, wd=1e-3):
    rnd=random.Random(seed)
    if task=='math':
        frequent=['x','y','z','a','b','n']; rare=['θ']
        def prompt(A,B): return [A,'+',B,'=',B,'+']
    else:
        frequent=['Alice','Bob','Carol','Dave','Emma','Frank']; rare=['Ebenezer']
        def prompt(A,B): return [A,'thanked',B,'.','who','thanked','?']   # answer: A (who did the thanking)
    names=frequent+rare
    const=sorted(set(t for t in prompt('#','@') if t not in ('#','@')))
    vocab=names+const; V=len(vocab); idx={t:i for i,t in enumerate(vocab)}
    # training data: variables drawn by frequency; the rare symbol appears in ~0.2% of examples
    w=[1.0]*len(frequent)+[0.012]
    data=[]
    for _ in range(4000):
        A,B=rnd.choices(names,weights=w,k=1)[0],None
        while B is None or B==A: B=rnd.choices(names,weights=w,k=1)[0]
        data.append((prompt(A,B),A))
    L=len(data[0][0]); IN=L*D
    g=lambda s: rnd.gauss(0,s)
    E=[[g(0.5) for _ in range(D)] for _ in range(V)]
    W1=[[g(1/math.sqrt(IN)) for _ in range(IN)] for _ in range(H)]; b1=[0.0]*H
    W2=[[g(1/math.sqrt(H)) for _ in range(H)] for _ in range(V)]; b2=[0.0]*V
    params=[E,W1,W2]; vecs=[b1,b2]
    # Adam state
    import copy
    def zeros_like(M): return [[0.0]*len(r) for r in M]
    mE,vE,mW1,vW1,mW2,vW2=[zeros_like(M) for M in (E,E,W1,W1,W2,W2)]
    mb1,vb1,mb2,vb2=[0.0]*H,[0.0]*H,[0.0]*V,[0.0]*V
    b1_,b2_=0.9,0.999; t=0
    def forward(toks):
        x=[v for tk in toks for v in E[idx[tk]]]
        z=[sum(W1[j][i]*x[i] for i in range(IN))+b1[j] for j in range(H)]
        h=[math.tanh(v) for v in z]
        lg=[sum(W2[k][j]*h[j] for j in range(H))+b2[k] for k in range(V)]
        m=max(lg); ex=[math.exp(v-m) for v in lg]; Z=sum(ex); p=[e/Z for e in ex]
        return x,h,lg,p
    def adam(P,G,M,S):
        for r in range(len(P)):
            for c in range(len(P[r])):
                gg=G[r][c]+wd*P[r][c]
                M[r][c]=b1_*M[r][c]+(1-b1_)*gg; S[r][c]=b2_*S[r][c]+(1-b2_)*gg*gg
                P[r][c]-=lr*(M[r][c]/(1-b1_**t))/(math.sqrt(S[r][c]/(1-b2_**t))+1e-8)
    def adamv(P,G,M,S):
        for c in range(len(P)):
            gg=G[c]; M[c]=b1_*M[c]+(1-b1_)*gg; S[c]=b2_*S[c]+(1-b2_)*gg*gg
            P[c]-=lr*(M[c]/(1-b1_**t))/(math.sqrt(S[c]/(1-b2_**t))+1e-8)
    BS=32
    for ep in range(epochs):
        rnd.shuffle(data)
        for bi in range(0,len(data),BS):
            batch=data[bi:bi+BS]
            gE=zeros_like(E); gW1=zeros_like(W1); gW2=zeros_like(W2); gb1=[0.0]*H; gb2=[0.0]*V
            for toks,ans in batch:
                x,h,lg,p=forward(toks)
                dl=p[:]; dl[idx[ans]]-=1.0
                for k in range(V):
                    gb2[k]+=dl[k]
                    for j in range(H): gW2[k][j]+=dl[k]*h[j]
                dh=[sum(W2[k][j]*dl[k] for k in range(V)) for j in range(H)]
                dz=[dh[j]*(1-h[j]*h[j]) for j in range(H)]
                dx=[0.0]*IN
                for j in range(H):
                    gb1[j]+=dz[j]
                    for i in range(IN): gW1[j][i]+=dz[j]*x[i]; dx[i]+=W1[j][i]*dz[j]
                for pos,tk in enumerate(toks):
                    for d in range(D): gE[idx[tk]][d]+=dx[pos*D+d]
            n=len(batch)
            for G in (gE,gW1,gW2):
                for r in G:
                    for c in range(len(r)): r[c]/=n
            gb1=[v/n for v in gb1]; gb2=[v/n for v in gb2]
            t+=1
            adam(E,gE,mE,vE); adam(W1,gW1,mW1,vW1); adam(W2,gW2,mW2,vW2); adamv(b1,gb1,mb1,vb1); adamv(b2,gb2,mb2,vb2)
    # evaluate
    counts={nm:sum(1 for toks,_ in data for tk in toks if tk==nm) for nm in names}
    acc_f=[]; 
    for A in frequent:
        for B in frequent:
            if A!=B: acc_f.append(max(range(V),key=lambda k: forward(prompt(A,B))[3][k])==idx[A])
    res={'task':task,'seed':seed,'vocab':vocab,'counts':counts,'acc_frequent_pairs':sum(acc_f)/len(acc_f)}
    probes=[(frequent[0],frequent[1]),(frequent[1],frequent[0]),(frequent[2],frequent[1]),(rare[0],frequent[1]),(frequent[0],rare[0])]
    res['probes']=[]
    for A,B in probes:
        x,h,lg,p=forward(prompt(A,B)); top=sorted(range(V),key=lambda k:-p[k])[:4]
        res['probes'].append({'prompt':prompt(A,B),'answer':A,'emb':{tk:[round(v,3) for v in E[idx[tk]]] for tk in prompt(A,B)},'hidden':[round(v,3) for v in h],'top':[(vocab[k],round(p[k],4)) for k in top],'p_answer':round(p[idx[A]],4)})
    res['weights']={'E':E,'W1':W1,'b1':b1,'W2':W2,'b2':b2}
    return res
if __name__=='__main__':
    task=sys.argv[1]; seed=int(sys.argv[2]) if len(sys.argv)>2 else 0
    r=run(task,seed)
    json.dump(r,open(f'/tmp/pb/toy/{task}_{seed}.json','w'))
    print(task,seed,'acc on frequent pairs',round(r['acc_frequent_pairs'],3),'counts',r['counts'])
    for pr in r['probes']:
        print(' ',' '.join(pr['prompt']),'-> answer',pr['answer'],'p=',pr['p_answer'],'top',pr['top'])
