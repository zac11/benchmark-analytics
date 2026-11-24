import os; HERE=os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(HERE,'prep.py')).read()); exec(open(os.path.join(HERE,'style.py')).read())
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
fam_np=F.set_index('benchmark_family').n_providers
SF['excl']=SF.benchmark_family.map(fam_np)==1
s=SF[SF.date>=pd.Timestamp('2024-01-01')]
anns=A[A.date>=pd.Timestamp('2024-01-01')].groupby('provider').size()
top=[b for b in F.sort_values('announcements',ascending=False).benchmark_family if b!='Bench'][:16]
M=s[s.benchmark_family.isin(top)].groupby(['provider','benchmark_family']).ann.nunique().unstack(fill_value=0).reindex(columns=top,fill_value=0)
M=M.div(anns,axis=0)*100
ex=SF.groupby('provider').excl.mean()*100
order=ex.sort_values(ascending=False).index
M=M.reindex(order)
fig=canvas('Chart 6 · Fingerprints','Every Lab Grades\nIts Own Homework',
 'Left: share of each lab\'s 2024–26 launch posts citing the 16 most common benchmarks.\nRight: share of a lab\'s benchmark citations that no other lab ever uses.','6/6')
ax=fig.add_axes([0.20,0.13,0.56,0.54])
cm=LinearSegmentedColormap.from_list('x',[BG,'#2A1B4A','#7A2E8C',ACC,'#FFD1E8'])
ax.imshow(M.values,cmap=cm,aspect='auto',vmin=0,vmax=100)
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        v=M.values[i,j]
        if v>=1: ax.text(j,i,f'{v:.0f}',ha='center',va='center',fontsize=9.5,color=BG if v>65 else FG,fontweight='bold')
ax.set_yticks(range(len(order))); ax.set_yticklabels(order,fontsize=13,color=FG,fontweight='bold')
ax.set_xticks(range(len(top))); ax.set_xticklabels(top,rotation=55,ha='right',fontsize=11,color=FG,rotation_mode='anchor')
for i,p in enumerate(order): ax.get_yticklabels()[i].set_color(PROV.get(p,FG))
ax.set_xticks(np.arange(-.5,len(top)),minor=True); ax.set_yticks(np.arange(-.5,len(order)),minor=True)
ax.grid(which='minor',color=BG,lw=2); ax.tick_params(which='both',length=0)
for sp in ax.spines.values(): sp.set_visible(False)
ax2=fig.add_axes([0.78,0.13,0.16,0.54],sharey=ax)
ax2.barh(range(len(order)),ex[order].values,color=[PROV.get(p,FG) for p in order],height=0.62)
for i,v in enumerate(ex[order].values): ax2.text(v+2,i,f'{v:.0f}%',va='center',fontsize=13,fontweight='bold',family='Space Grotesk')
ax2.set_xlim(0,80); ax2.axis('off')
ax2.text(0,-0.95,'HOME-GROWN',fontsize=11,color=ACC,fontweight='bold')
ax.text(0,-0.95,'% OF LAUNCHES CITING',fontsize=11,color=ACC,fontweight='bold')
fig.savefig(OUT+'06_lab_fingerprints.png',dpi=200)
print(M.round(0)); print(ex.round(1)); print(anns)
