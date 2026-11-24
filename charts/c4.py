import os; HERE=os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(HERE,'prep.py')).read()); exec(open(os.path.join(HERE,'style.py')).read())
import numpy as np, matplotlib.dates as mdates
END=pd.Timestamp('2026-11-18'); CUT=END-pd.DateOffset(months=6)
f=F[(F.announcements>=9)&(F.benchmark_family!='Bench')].sort_values('first_seen').reset_index(drop=True)
LA=set(zip(A.date,A.provider))
RC=R.assign(provider=R.Provider.replace({'Alibaba':'Alibaba Qwen','Mistral AI':'Mistral'}),fam=R['Benchmark (counting label)'].str.lower())
RC=RC[[k in LA for k in zip(RC.date,RC.provider)]]
f['last_seen']=pd.concat([f.last_seen,f.benchmark_family.str.lower().map(RC.groupby('fam').date.max())],axis=1).max(axis=1)
f['dead']=f.last_seen<CUT
fig=canvas('Chart 4 · Lifespans','The Benchmark Graveyard',
 f'Every launch-post citation of the {len(f)} most-cited benchmarks. Grey rows (†) have\nnot appeared in any launch post for 6+ months. {f.dead.sum()} of {len(f)} are already gone, and\nSWE-bench Verified, the coding benchmark of 2025, is close behind.','4/6')
ax=fig.add_axes([0.30,0.09,0.64,0.66])
ycol={2020:'#4C8DFF',2021:'#4C8DFF',2023:'#4C8DFF',2024:'#2DD4BF',2025:ACC2,2026:ACC}
for i,r in f.iterrows():
    d=pd.concat([SF[SF.benchmark_family==r.benchmark_family].date,RC[RC.fam==r.benchmark_family.lower()].date]).dropna().drop_duplicates()
    c=DIM if r.dead else ycol.get(r.first_seen.year,FG)
    ax.plot([r.first_seen,r.last_seen if r.dead else END],[i,i],color=c,lw=1.2,alpha=0.9 if not r.dead else 0.8,ls='-' if not r.dead else (0,(2,2)))
    if not r.dead: ax.plot([r.first_seen,END],[i,i],color=c,lw=7,alpha=0.08,solid_capstyle='round')
    ax.scatter(d,[i]*len(d),s=34,color=c if not r.dead else '#5A6480',lw=0,zorder=3)
    lab=('† ' if r.dead else '')+r.benchmark_family
    ax.text(-0.01,i,lab,transform=ax.get_yaxis_transform(),ha='right',va='center',fontsize=11.5,color=MUTED if r.dead else FG,fontweight='normal' if r.dead else 'bold')
    if r.dead: ax.text(r.last_seen+pd.Timedelta(days=25),i,f'last cited {r.last_seen:%b %Y}',fontsize=9.5,color='#6B7590',va='center')
ax.set_ylim(len(f)-0.4,-0.8); ax.set_yticks([])
ax.set_xlim(pd.Timestamp('2020-03-01'),END+pd.Timedelta(days=20))
ax.xaxis.set_major_locator(mdates.YearLocator()); ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.grid(axis='x',color=GRID,lw=0.8); ax.spines['left'].set_visible(False); ax.tick_params(length=0)
ax.xaxis.tick_top()
from matplotlib.lines import Line2D
h=[Line2D([],[],marker='o',ls='',color=ycol[y],ms=8) for y in [2023,2024,2025,2026]]+[Line2D([],[],marker='o',ls='',color='#5A6480',ms=8)]
ax.legend(h,['Born ≤2023','Born 2024','Born 2025','Born 2026','Retired'],ncol=5,loc='upper center',bbox_to_anchor=(0.32,-0.01),frameon=False,fontsize=11,handletextpad=0.1,columnspacing=1.0)
fig.savefig(OUT+'04_benchmark_graveyard.png',dpi=200)
print(f[['benchmark_family','first_seen','last_seen','dead','announcements']].to_string())
