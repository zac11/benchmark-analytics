import os; HERE=os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(HERE,'prep.py')).read()); exec(open(os.path.join(HERE,'style.py')).read())
import numpy as np
SF['cohort']=SF.benchmark_family.map(F.set_index('benchmark_family').first_seen).dt.year
SF['yr']=SF.date.dt.year
SF['coh']=SF.cohort.where(SF.cohort>=2023,2022)
ct=pd.crosstab(SF.yr,SF.coh).loc[2023:2026]
sh=ct.div(ct.sum(1),axis=0)*100
fig=canvas('Chart 5 · Churn','Benchmark Stratigraphy',
 f'Each year\'s launch-post citations, layered by the year the benchmark first\nappeared. {sh.loc[2026,2026]:.0f}% of what labs cited in 2026 had never appeared in a launch\npost before 2026. Pre-ChatGPT benchmarks are almost extinct.','5/6')
ax=fig.add_axes([0.10,0.16,0.80,0.57])
pal={2022:'#5B3A8C',2023:'#4C8DFF',2024:'#2DD4BF',2025:ACC2,2026:ACC}
names={2022:'Born 2018–22 (pre-ChatGPT)',2023:'Born 2023',2024:'Born 2024',2025:'Born 2025',2026:'Born 2026'}
x=np.arange(len(sh)); bottom=np.zeros(len(sh))
for c in sh.columns:
    v=sh[c].values
    ax.bar(x,v,bottom=bottom,color=pal[c],width=0.72,edgecolor=BG,lw=2,label=names[c])
    for i,(vv,b) in enumerate(zip(v,bottom)):
        if vv>=4: ax.text(i,b+vv/2,f'{vv:.0f}%',ha='center',va='center',fontsize=15 if vv>10 else 12,fontweight='bold',color=BG if c in (2024,2025,2026) else FG,family='Space Grotesk')
    bottom+=v
for i,(y,t) in enumerate(ct.sum(1).items()): ax.text(i,102,f'{t:,} citations',ha='center',fontsize=12,color=MUTED)
ax.set_xticks(x); ax.set_xticklabels([str(y) for y in sh.index],fontsize=18,fontweight='bold',color=FG,family='Space Grotesk')
ax.set_ylim(0,107); ax.set_yticks([]); ax.spines['left'].set_visible(False); ax.spines['bottom'].set_visible(False); ax.tick_params(length=0)
ax.legend(loc='upper center',bbox_to_anchor=(0.5,-0.07),ncol=3,frameon=False,fontsize=12,handlelength=1.2)
fig.savefig(OUT+'05_benchmark_stratigraphy.png',dpi=200)
print(ct); print(sh.round(1))
