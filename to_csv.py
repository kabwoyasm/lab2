from pathlib import Path
import pandas as pd
import json

inp= Path('/mnt/data/PHASE 6 extracted data.txt')
lines=inp.read_text(encoding='utf-8').splitlines()
rows=[]
header=lines[0].split('\t')
for line in lines[1:]:
    parts=line.split('\t',5)
    if len(parts)<6: continue
    rec=dict(zip(header,parts))
    try:
        data=json.loads(rec['extracted_data'])
        rec['extracted_data']=json.dumps(data,ensure_ascii=False)
    except: pass
    rows.append(rec)
df=pd.DataFrame(rows)
out='/mnt/data/PHASE_6_extracted_data.csv'
df.to_csv(out,index=False)
print(len(df))
