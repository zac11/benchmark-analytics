import os; HERE=os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(HERE,'prep.py')).read()); exec(open(os.path.join(HERE,'style.py')).read())
import numpy as np
fig=plt.figure(figsize=(W,H))
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
rng=np.random.default_rng(7)
a=A.dropna(subset=['date'])
x=(a.date-pd.Timestamp('2018-01-01')).dt.days/ (pd.Timestamp('2027-01-01')-pd.Timestamp('2018-01-01')).days
y=0.075+a.benchmarks_named/92*0.25
for p,c in PROV.items():
    m=a.provider==p
    ax.scatter(0.04+0.92*x[m],y[m],s=a.benchmarks_named[m]*6+20,color=c,alpha=0.22,lw=0)
    ax.scatter(0.04+0.92*x[m],y[m],s=12,color=c,alpha=0.9,lw=0)
ax.text(0.07,0.92,'AN ANALYSIS OF 197 FRONTIER-MODEL LAUNCH POSTS · 2018–2026',fontsize=13,color=ACC,fontweight='bold')
ax.text(0.065,0.885,'The\nBenchmark\nWars',fontsize=88,fontweight='bold',family='Space Grotesk',va='top',linespacing=0.92)
ax.text(0.07,0.575,'How AI labs keep score, and why the scoreboard\nkeeps changing.',fontsize=19,color=MUTED,va='top',linespacing=1.4)
stats=[('1,024','benchmarks cited'),('83%','used by only one lab'),('2.4×','more benchmarks per launch\nthan in 2023'),('66%','of 2026 citations are\nbrand-new benchmarks')]
for i,(n,l) in enumerate(stats):
    cx=0.07+i*0.225
    ax.text(cx,0.475,n,fontsize=34,fontweight='bold',family='Space Grotesk',color=[ACC,ACC2,ACC3,'#19C37D'][i],va='top')
    ax.text(cx,0.425,l,fontsize=12,color=FG,va='top',linespacing=1.35)
ax.text(0.07,0.03,'Swipe →  6 charts',fontsize=13,color=FG,fontweight='bold')
ax.text(0.93,0.03,'THE BENCHMARK WARS',fontsize=11,color=MUTED,ha='right',fontweight='bold')
fig.savefig(OUT+'00_cover.png',dpi=200)
