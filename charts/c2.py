import os; HERE=os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(HERE,'prep.py')).read()); exec(open(os.path.join(HERE,'style.py')).read())
import numpy as np, matplotlib.dates as mdates
a=A.dropna(subset=['date']).sort_values('date').copy()
fig=canvas('Chart 2 · Inflation','Benchmark Inflation',
 'Number of distinct benchmarks named in each launch post.\nThe average 2026 launch cites 17 benchmarks, 2.4× the 2023 average.\nOne Qwen release cited 92.','2/6')
ax=fig.add_axes([0.10,0.10,0.84,0.66])
for p,c in PROV.items():
    s=a[a.provider==p]; ax.scatter(s.date,s.benchmarks_named,s=70,color=c,alpha=0.85,lw=0,label=p,zorder=3)
yr=a.groupby(a.date.dt.year).benchmarks_named.mean()
yr=yr[yr.index>=2023]
xs=[pd.Timestamp(f'{y}-07-01') for y in yr.index]
for w,al in [(14,0.06),(8,0.12),(4,0.3)]: ax.plot(xs,yr.values,color=FG,lw=w,alpha=al,zorder=2)
ax.plot(xs,yr.values,color=FG,lw=2,zorder=4,marker='o',ms=7)
for x,v in zip(xs,yr.values): ax.text(x,v+5.5,f'avg {v:.1f}',ha='center',fontsize=12,fontweight='bold',color=FG,path_effects=outline(),zorder=5)
ann=[('Qwen3.5','Qwen3.5 · 92',(-130,-10)),('Qwen3.8-Max','Qwen3.8-Max · 79',(-40,22)),('GPT-5.2','GPT-5.2 · 51',(-120,25)),('GPT-1','GPT-1 · 15',(15,25)),('GPT-3','GPT-3 · 21',(10,30))]
for m,t,off in ann:
    r=a[a.model==m].iloc[0]
    ax.annotate(t,(r.date,r.benchmarks_named),xytext=off,textcoords='offset points',fontsize=12.5,color=FG,fontweight='bold',
        arrowprops=dict(arrowstyle='-',color=MUTED,lw=0.8),path_effects=outline())
ax.set_ylim(-3,100); ax.set_xlim(pd.Timestamp('2018-03-01'),pd.Timestamp('2026-12-31')); ax.set_ylabel('Benchmarks named in launch post',fontsize=13)
ax.xaxis.set_major_locator(mdates.YearLocator()); ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.grid(axis='y',color=GRID,lw=0.8); ax.spines['left'].set_visible(False); ax.tick_params(length=0)
leg=ax.legend(ncol=4,loc='upper left',bbox_to_anchor=(0,1.0),frameon=False,fontsize=11.5,handletextpad=0.2,columnspacing=1.0,markerscale=1.1)
fig.savefig(OUT+'02_benchmark_inflation.png',dpi=200)
print(yr)
