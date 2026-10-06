# Relation-extraction dependency figure with path-centric pruning levels (data-d = distance from shortest path).
def width(t): return max(len(t)*8.2,16)
toks=[('Alice','s',0),('Chen','s',0),('who','',2),('grew','',1),('up','',2),('near','',3),('Beijing','',2),('never','',1),('worked','',0),('for','',1),('Acme','o',0)]
arcs=[(0,1,'flat'),(8,0,'nsubj'),(0,3,'acl:relcl'),(3,2,'nsubj'),(3,4,'compound:prt'),(3,6,'obl'),(6,5,'case'),(8,7,'advmod'),(8,10,'obl'),(10,9,'case')]
path={(8,0),(8,10)}
x0=24; gap=30; unit=24; xs=[]; ws=[]; x=x0
for t,_,_ in toks:
    w=width(t); ws.append(w); xs.append(x+w/2); x+=w+gap
W=int(x+10)
spans=[(min(h,d),max(h,d)) for h,d,_ in arcs]; lev={}
for i in sorted(range(len(arcs)), key=lambda i: spans[i][1]-spans[i][0]):
    a,b=spans[i]; lev[i]=1+max([lev[j] for j in lev if spans[j][0]>=a and spans[j][1]<=b],default=0)
    if arcs[i][2]=='compound:prt': lev[i]+=1
base=max(lev.values())*unit+44
o=[]; labels=[]
for i,(h,d,rel) in enumerate(arcs):
    hx=xs[h]+(5 if d>h else -5); dx=xs[d]; hgt=lev[i]*unit+6; top=base-hgt
    dd=max(toks[h][2],toks[d][2]); onp=(h,d) in path
    cls='arc-path' if onp else 'arc'
    mx=(hx+dx)/2; my=top-hgt*0.08; tw=len(rel)*6.2+8
    o.append(f'<g class="rx" data-d="{dd}"><path d="M {hx:.1f} {base} C {hx:.1f} {top-hgt*0.33:.1f}, {dx:.1f} {top-hgt*0.33:.1f}, {dx:.1f} {base-1}" class="{cls}" marker-end="url(#{"rep" if onp else "ud"})"/></g>')
    labels.append(f'<g class="rx" data-d="{dd}"><rect x="{mx-tw/2:.1f}" y="{my-9:.1f}" width="{tw:.1f}" height="13" rx="3" class="lblbg"/>'
             f'<text x="{mx:.1f}" y="{my+1.5:.1f}" text-anchor="middle" class="rel{" path-txt" if onp else ""}">{rel}</text></g>')
o+=labels
rx=xs[8]
o.append(f'<line x1="{rx:.1f}" y1="10" x2="{rx:.1f}" y2="{base-1}" class="arc" marker-end="url(#ud)"/><text x="{rx+6:.1f}" y="18" class="rel">root</text>')
for i,(t,role,d) in enumerate(toks):
    cx=xs[i]
    box = 'ent' if role else ('neg' if t=='never' else 'tkbg')
    o.append(f'<g class="rx" data-d="{d}"><rect x="{cx-ws[i]/2-4:.1f}" y="{base+4}" width="{ws[i]+8:.1f}" height="24" rx="5" class="{box}"/>'
             f'<text x="{cx:.1f}" y="{base+21}" text-anchor="middle" class="tok{" path-tok" if d==0 and not role else ""}{" neg-tok" if t=="never" else ""}">{t}</text></g>')
    if t=='never': negx=(cx, ws[i])
# entity labels
sx=(xs[0]+xs[1])/2
o.append(f'<text x="{sx:.1f}" y="{base+46}" text-anchor="middle" class="sm hl-txt">subject</text>')
o.append(f'<text x="{xs[10]:.1f}" y="{base+46}" text-anchor="middle" class="sm hl-txt">object</text>')
nx,nw=negx
o.append(f'<rect x="{nx-nw/2-4:.1f}" y="{base+4}" width="{nw+8:.1f}" height="24" rx="5" class="neg-ghost"/>')
o.append(f'<text x="{nx:.1f}" y="{base+46}" text-anchor="middle" class="sm neg-lbl">negation</text>')
o.append(f'<text x="{nx:.1f}" y="{base+46}" text-anchor="middle" class="sm neg-lbl-off">negation, dropped</text>')
H=int(base+56)
svg=f'''<svg id="refig" data-k="1" viewBox="0 0 {W} {H}" role="img" aria-label="Dependency tree of Alice Chen, who grew up near Beijing, never worked for Acme. The shortest path between the subject Alice Chen and the object Acme runs through worked, two arcs long, even though eight words separate them in the sentence. The word never hangs one step off that path.">
<defs>
<marker id="rep" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="th-fill"/></marker>
</defs>
{chr(10).join(o)}
</svg>'''
open('/tmp/pb/re.svg','w').write(svg); print(W,H)
