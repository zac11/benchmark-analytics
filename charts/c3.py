import os; HERE=os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(HERE,'prep.py')).read()); exec(open(os.path.join(HERE,'style.py')).read())
import numpy as np
bs=[('MMLU','MMLU','#8C95A8'),('HumanEval','HumanEval','#9B8CFF'),('GPQA Diamond','GPQA Diamond','#4C8DFF'),('SWE-bench Verified','SWE-bench Verified','#19C37D'),
    ('BrowseComp','BrowseComp','#2DD4BF'),('Terminal-Bench 2.0','Terminal-Bench 2.0','#FACC15'),('FrontierMath','FrontierMath','#FF8A4C'),('ARC-AGI-2','ARC-AGI-2','#FF4FA3')]
fig=canvas('Chart 3 · Saturation','The Race to the Ceiling',
 'Best score any lab has published on a benchmark, by months since that\nbenchmark first appeared in a launch post. ARC-AGI-2 went from 16% to 95%\nin 14 months. FrontierMath went from 32% to 98% in 19.','3/6')
ax=fig.add_axes([0.10,0.10,0.62,0.62])
ax.axhspan(90,100,color=ACC,alpha=0.07,lw=0); ax.text(0.5,97,'SATURATION ZONE  ≥ 90%',color=ACC,fontsize=11.5,fontweight='bold',va='center')
out=[]
for b,lab,c in bs:
    s=R[(R['Benchmark (counting label)']==b)&R.v.notna()&R.date.notna()&(R.v>0)&(R.v<=100)].sort_values('date')
    t0=min([s.date.min()]+F.loc[F.benchmark_family==b,'first_seen'].dropna().tolist()); s=s.groupby('date').v.max().cummax().reset_index()
    s['m']=(s.date-t0).dt.days/30.44
    x=list(s.m)+[ (pd.Timestamp('2026-11-18')-t0).days/30.44 ]; y=list(s.v)+[s.v.iloc[-1]]
    x=[min(v,40) for v in x]
    for w,al in [(10,0.07),(6,0.14)]: ax.step(x,y,where='post',color=c,lw=w,alpha=al)
    ax.step(x,y,where='post',color=c,lw=2.6)
    ax.scatter([x[0]],[y[0]],color=c,s=50,zorder=5)
    out.append((y[-1],lab,c,x[-1]))
    hit=s[s.v>=90]
    print(lab, s.v.iloc[0], s.v.iloc[-1], 'months to 90:', round(hit.m.iloc[0],1) if len(hit) else None)
# right labels, de-overlap
out.sort(reverse=True); ys=[]
for yv,lab,c,xe in out:
    yy=min(yv,99) if not ys else min(yv,ys[-1]-4.2)
    ys.append(yy)
for (yv,lab,c,xe),yy in zip(out,ys):
    ax.annotate(f'{lab}  {yv:.0f}%',(40,yv),xytext=(41.2,yy),fontsize=12.5,color=c,fontweight='bold',va='center',annotation_clip=False)
ax.set_xlim(0,40.5); ax.set_ylim(0,100)
ax.set_xlabel('Months since first appearance in a launch post',fontsize=13); ax.set_ylabel('Best published score (%)',fontsize=13)
ax.grid(color=GRID,lw=0.8); ax.spines['left'].set_visible(False); ax.tick_params(length=0)
fig.savefig(OUT+'03_race_to_the_ceiling.png',dpi=200)
