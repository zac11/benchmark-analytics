import pandas as pd, numpy as np, re, warnings
warnings.filterwarnings('ignore')
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,'data')+os.sep
OUT=os.path.join(ROOT,'visuals')+os.sep
os.makedirs(OUT,exist_ok=True)
A=pd.read_excel(D+'frontier_benchmarks.xlsx','Announcements (chronological)')
S=pd.read_excel(D+'frontier_benchmarks.xlsx','All benchmark scores')
F=pd.read_excel(D+'frontier_benchmarks.xlsx','Benchmark frequency')
R=pd.read_csv(D+'frontier-model-benchmark-results.csv')
L=pd.read_excel(D+'frontier-model-benchmarks.xlsx','Launches')
BI=pd.read_excel(D+'frontier-model-benchmarks.xlsx','Benchmark index')
A['date']=pd.to_datetime(A.date,errors='coerce'); S['date']=pd.to_datetime(S.date,errors='coerce')
F['first_seen']=pd.to_datetime(F.first_seen); F['last_seen']=pd.to_datetime(F.last_seen)
S['ann']=S.date.astype(str)+'|'+S.provider+'|'+S.model
SF=S.drop_duplicates(['ann','benchmark_family'])
R['date']=pd.to_datetime(R['Date as published'],errors='coerce')
def first_num(s):
    m=re.search(r'-?\d+(?:\.\d+)?',str(s).replace(',',''))
    return float(m.group()) if m else np.nan
R['v']=R['Result / published scale'].map(first_num)
