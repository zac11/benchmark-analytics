import matplotlib as mpl, matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import matplotlib.patheffects as pe
import glob
FONT_DIRS=[os.path.join(ROOT,'fonts'),os.path.expanduser('~/.fonts'),os.path.expanduser('~/Library/Fonts'),'/usr/share/fonts','/Library/Fonts']
for f in [f for d in FONT_DIRS for p in ('Inter-*.ttf','SpaceGrotesk-*.ttf','SpaceGrotesk.ttf') for f in glob.glob(os.path.join(d,'**',p),recursive=True)]:
    fm.fontManager.addfont(f)
BG='#0A0E1A'; FG='#EEF1F7'; MUTED='#8C95A8'; GRID='#1B2233'; DIM='#2A3247'
ACC='#FF4FA3'; ACC2='#FFB547'; ACC3='#4CC9FF'
PROV={'OpenAI':'#19C37D','Anthropic':'#FF8A4C','Google':'#4C8DFF','Meta':'#9B8CFF','Alibaba Qwen':'#FF4FA3',
      'DeepSeek':'#2DD4BF','xAI':'#E5E7EB','Mistral':'#FACC15','NVIDIA':'#A3E635','Moonshot AI':'#7DD3FC','Z.ai':'#F87171'}
mpl.rcParams.update({'font.family':'Inter','font.size':13,'text.color':FG,'axes.labelcolor':MUTED,'xtick.color':MUTED,'ytick.color':MUTED,
  'axes.facecolor':BG,'figure.facecolor':BG,'savefig.facecolor':BG,'axes.edgecolor':GRID,'axes.grid':False,
  'xtick.labelsize':12,'ytick.labelsize':12,'axes.spines.top':False,'axes.spines.right':False})
W,H=10.8,13.5
def canvas(kicker,title,sub,n_of=None):
    fig=plt.figure(figsize=(W,H))
    fig.text(0.06,0.955,kicker.upper(),fontsize=13,color=ACC,fontweight='bold',family='Inter',va='top')
    fig.text(0.06,0.932,title,fontsize=40,fontweight='bold',family='Space Grotesk',va='top',color=FG,linespacing=1.0)
    fig.text(0.06,0.932-0.054*(title.count('\n')+1)-0.008,sub,fontsize=15.5,color=MUTED,va='top',linespacing=1.45)
    fig.text(0.06,0.025,'Data: 197 official launch posts from 11 labs, Jun 2018 – Nov 2026 · scores as self-reported',fontsize=10.5,color=MUTED)
    fig.text(0.94,0.025,'THE BENCHMARK WARS'+(f'  ·  {n_of}' if n_of else ''),fontsize=10.5,color=FG,ha='right',fontweight='bold')
    fig.add_artist(plt.Line2D([0.06,0.94],[0.048,0.048],color=GRID,lw=1))
    return fig
def glow(artist_fn, color, widths=(10,6,3), alphas=(0.06,0.12,0.25)):
    for w,a in zip(widths,alphas): artist_fn(lw=w,alpha=a,color=color)
def outline(c=BG,w=4): return [pe.withStroke(linewidth=w,foreground=c)]
