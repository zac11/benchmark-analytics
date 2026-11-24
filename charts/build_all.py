import glob, os, runpy
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), 'visuals')

for script in sorted(glob.glob(os.path.join(HERE, 'c[0-9].py'))):
    print('rendering', os.path.basename(script))
    runpy.run_path(script)

pages = sorted(glob.glob(os.path.join(OUT, '0*.png')))
ims = [Image.open(f).convert('RGB').resize((1080, 1350), Image.LANCZOS) for f in pages]
ims[0].save(os.path.join(OUT, 'benchmark_wars_carousel.pdf'), save_all=True, append_images=ims[1:], resolution=100)
print('wrote carousel with', len(ims), 'pages')
