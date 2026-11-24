import os; HERE=os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(HERE,'prep.py')).read()); exec(open(os.path.join(HERE,'style.py')).read())
import numpy as np
f=F.copy()
def cat(r):
    if r.n_providers>=10: return 3
    if r.n_providers>=2: return 2
    if r.announcements>=2: return 1
    return 0
f['cat']=f.apply(cat,axis=1); f=f.sort_values(['cat','announcements'],ascending=[False,False])
n=len(f); cols=32; rows=int(np.ceil(n/cols))
fig=canvas('Chart 1 · Fragmentation','The Benchmark\nTower of Babel',
 f'Frontier labs have cited {n:,} different benchmarks in launch posts.\n{(f.n_providers==1).sum():,} of them ({(f.n_providers==1).mean():.0%}) were used by only one lab. Only {(f.cat==3).sum()} are shared\nby 10 or more of the 11 labs.','1/6')
ax=fig.add_axes([0.06,0.215,0.88,0.505]); ax.set_xlim(-1,cols); ax.set_ylim(rows,-1); ax.axis('off'); ax.set_aspect('equal')
colors={3:ACC,2:ACC2,1:'#4A5571',0:'#2A3247'}
for i,(c,a) in enumerate(zip(f.cat,f.announcements)):
    x,y=i%cols,i//cols
    if c==3: ax.scatter(x,y,s=260,color=ACC,alpha=0.25,lw=0)
    ax.scatter(x,y,s=95 if c else 70,color=colors[c],lw=0)
counts=f.cat.value_counts()
labels=[(3,'Used by 10+ labs — the shared language'),(2,'Used by 2–9 labs'),(1,'One lab only, reused'),(0,'Used once, never again')]
for k,(c,l) in enumerate(labels):
    y=0.165-k*0.03
    fig.text(0.075,y,'●',color=colors[c],fontsize=20,va='center')
    fig.text(0.105,y,f'{counts.get(c,0):>4,}',fontsize=16,fontweight='bold',va='center',family='Space Grotesk')
    fig.text(0.17,y,l,fontsize=14,va='center',color=FG if c>=2 else MUTED)
top=f[f.cat==3].benchmark_family.tolist()
fig.text(0.60,0.165,'THE COMMON TONGUE',color=ACC,fontsize=12,fontweight='bold',va='center')
fig.text(0.60,0.145,'\n'.join([', '.join(top[i:i+3]) for i in range(0,len(top),3)]),fontsize=12.5,va='top',color=FG,linespacing=1.6)
fig.savefig(OUT+'01_tower_of_babel.png',dpi=200)
print(n,counts.to_dict(),top)
