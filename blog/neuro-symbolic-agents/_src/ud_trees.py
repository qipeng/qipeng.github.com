# Interactive UD arc diagrams: tokens/arcs carry data-p (sentence pair) and data-g (alignment group).
def width(t):
    return max(sum(15 if ord(ch)>0x2e80 else 8.2 for ch in t),16)

def diagram(pair, tokens, arcs, root, hl, y0, x0=120, gap=16, unit=22, label='', sub='', ja=False):
    xs=[];x=x0;ws=[]
    for t,g,grp in tokens:
        w=max(width(t), width(g)*0.78 if g else 0); ws.append(w); xs.append(x+w/2); x+=w+gap
    spans=[(min(h,d),max(h,d)) for h,d,_ in arcs]
    lev={}
    for i in sorted(range(len(arcs)), key=lambda i: spans[i][1]-spans[i][0]):
        a,b=spans[i]
        lev[i]=1+max([lev[j] for j in lev if spans[j][0]>=a and spans[j][1]<=b],default=0)
    base=y0+max(lev.values())*unit+34
    out=[f'<text x="16" y="{base+18}" class="lbl" font-weight="500">{label}</text>']
    if sub: out.append(f'<text x="16" y="{base+36}" class="sm mut">{sub}</text>')
    # arcs first (under tokens)
    for i,(h,d,rel) in enumerate(arcs):
        hx=xs[h]+(5 if d>h else -5); dx=xs[d]; hgt=lev[i]*unit+6; top=base-hgt
        cls='arc-hl' if (d in hl and (h in hl or rel in ('amod','acl','acl:relcl'))) else 'arc'
        g=tokens[d][2]
        mx=(hx+dx)/2; my=top-hgt*0.08; tw=len(rel)*6.2+8
        out.append(f'<g class="ua" data-p="{pair}" data-g="{g}" tabindex="-1">'
                   f'<path d="M {hx:.1f} {base} C {hx:.1f} {top-hgt*0.33:.1f}, {dx:.1f} {top-hgt*0.33:.1f}, {dx:.1f} {base-1}" class="{cls}" marker-end="url(#{"udh" if cls=="arc-hl" else "ud"})"/>'
                   f'<path d="M {hx:.1f} {base} C {hx:.1f} {top-hgt*0.33:.1f}, {dx:.1f} {top-hgt*0.33:.1f}, {dx:.1f} {base-1}" class="hit"/>'
                   f'<rect x="{mx-tw/2:.1f}" y="{my-9:.1f}" width="{tw:.1f}" height="13" rx="3" class="lblbg"/>'
                   f'<text x="{mx:.1f}" y="{my+1.5:.1f}" text-anchor="middle" class="rel{" hl-txt" if cls=="arc-hl" else ""}">{rel}</text></g>')
    rx=xs[root]
    out.append(f'<line x1="{rx:.1f}" y1="{y0+6}" x2="{rx:.1f}" y2="{base-1}" class="arc" marker-end="url(#ud)"/>')
    out.append(f'<text x="{rx+6:.1f}" y="{y0+14}" class="rel">root</text>')
    for i,(t,g,grp) in enumerate(tokens):
        cx=xs[i]; lang=' lang="ja"' if ja else ''
        out.append(f'<g class="ut" data-p="{pair}" data-g="{grp}" tabindex="0" role="button" aria-label="{t}">'
                   f'<rect x="{cx-ws[i]/2-4:.1f}" y="{base+4}" width="{ws[i]+8:.1f}" height="24" rx="5" class="{"hl-soft" if i in hl else "tkbg"}"/>'
                   f'<text x="{cx:.1f}" y="{base+21}" text-anchor="middle" class="tok"{lang}>{t}</text>'
                   + (f'<text x="{cx:.1f}" y="{base+42}" text-anchor="middle" class="sm mut gl">{g}</text>' if g else '') + '</g>')
    pos={i:(xs[i],base) for i in range(len(tokens))}
    return out, base, pos, max(xs)+max(ws)

def align(pair, en_tok, en_pos, ja_tok, ja_pos, ja_top):
    out=[]
    for i,(t,_,g) in enumerate(en_tok):
        for j,(u,_,h) in enumerate(ja_tok):
            if g==h and g not in ('none',):
                x1,b1=en_pos[i]; x2,b2=ja_pos[j]
                out.append(f'<line x1="{x1:.1f}" y1="{b1+30}" x2="{x2:.1f}" y2="{b2+2}" class="al" data-p="{pair}" data-g="{g}"/>')
    return out

parts=[]; aligns=[]; y=6; W=0
en1=[('Make','','make'),('the','','the'),('world','','world'),('a','','a'),('better','','mod'),('place','','place')]
a1=[(0,2,'obj'),(2,1,'det'),(0,5,'xcomp'),(5,3,'det'),(5,4,'amod')]
o,b_en1,p_en1,r=diagram('s1',en1,a1,0,{4},y,label='English',sub='sentence 1'); parts+=o; W=max(W,r)
ja1=[('世界','world','world'),('を','ACC','world'),('より','more','mod'),('良い','good','mod'),('場所','place','place'),('に','DAT','place'),('する','make','make')]
b1=[(6,0,'obj'),(0,1,'case'),(6,4,'obl'),(4,5,'case'),(4,3,'acl'),(3,2,'advmod')]
y2=b_en1+52+8
o,b_ja1,p_ja1,r=diagram('s1',ja1,b1,6,{2,3},y2,label='日本語',sub='sentence 1',ja=True); parts+=o; W=max(W,r)
aligns+=align('s1',en1,p_en1,ja1,p_ja1,y2)
y_mid=b_ja1+52+8
y3=y_mid+26
en2=[('Make','','make'),('the','','the'),('world','','world'),('a','','a'),('place','','place'),('where','','where'),('humankind','','hum'),('and','','and'),('nature','','nat'),('coexist','','co'),('in','','harm'),('harmony','','harm')]
a2=[(0,2,'obj'),(2,1,'det'),(0,4,'xcomp'),(4,3,'det'),(4,9,'acl:relcl'),(9,5,'advmod'),(9,6,'nsubj'),(6,8,'conj'),(8,7,'cc'),(9,11,'obl'),(11,10,'case')]
o,b_en2,p_en2,r=diagram('s2',en2,a2,0,{5,6,7,8,9,10,11},y3,label='English',sub='sentence 2'); parts+=o; W=max(W,r)
ja2=[('世界','world','world'),('を','ACC','world'),('人類','humankind','hum'),('と','and','and'),('自然','nature','nat'),('が','NOM','ga'),('調和して','in harmony','harm'),('共存する','coexist','co'),('場所','place','place'),('に','DAT','place'),('する','make','make')]
b2=[(10,0,'obj'),(0,1,'case'),(10,8,'obl'),(8,9,'case'),(8,7,'acl'),(7,2,'nsubj'),(2,4,'conj'),(4,3,'cc'),(4,5,'case'),(7,6,'advcl')]
y4=b_en2+52+8
o,b_ja2,p_ja2,r=diagram('s2',ja2,b2,10,{2,3,4,5,6,7},y4,label='日本語',sub='sentence 2',ja=True); parts+=o; W=max(W,r)
aligns+=align('s2',en2,p_en2,ja2,p_ja2,y4)
W=int(W+16); H=int(b_ja2+52+4)
svg=f'''<svg id="udfig" viewBox="0 0 {W} {H}" role="group" aria-label="Interactive Universal Dependencies analyses of Make the world a better place and Make the world a place where humankind and nature coexist in harmony, in English and Japanese. Hover or focus a word or an arc to highlight its counterpart in the other language.">
<defs>
<marker id="ud" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="mut-fill"/></marker>
<marker id="udh" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="hl-fill"/></marker>
</defs>
<line x1="16" x2="{W-16}" y1="{y_mid}" y2="{y_mid}" class="rule" stroke-dasharray="3 4"/>
<g class="aligns">{"".join(aligns)}</g>
{chr(10).join(parts)}
</svg>'''
open('/tmp/pb/ud2.svg','w').write(svg); print(W,H)
