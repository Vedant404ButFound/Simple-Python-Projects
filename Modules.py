import pandas as pd
import re
import os

txtPath = r'C:\Users\{username}\Desktop\requirements.txt'
csvPath = r"F:\Python\Practice programms\Modules.csv"
with open(csvPath,'w') as f:
    f.write("Module name,Version")
df = pd.read_csv(csvPath)
os.system(f"pip freeze > {txtPath}")
with open(txtPath,'r',encoding='utf-8') as f:
    content = f.read()
modules = re.findall(r'[a-z A-Z 0-9 ]+=+',content)
version = re.findall(r'==+[0-9 .]+',content)

for i in range(len(modules)):
    df.loc[i,"Module name"] = modules[i][:-2]
    df.loc[i,"Version"] = version[i][2:]
df.to_csv(csvPath,index=False)
