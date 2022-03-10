import os
import glob
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from dotenv import load_dotenv 

load_dotenv() # add this line
name=os.getenv('NAME_')
name=name.split(",")
#path=[r"C:Blow_nose",r"C:Brush_hair", r"C:Drink_water"]
df = pd.DataFrame()
k = 0
#os.getcwd()

path=os.getenv('PATH_')
for p in name:
    os.chdir(path)
    os.chdir(p)
    file_extension = '.csv'
    all_filenames = [i for i in glob.glob(f"*{file_extension}")]
    for f in all_filenames:
        temp = pd.read_csv(f, names=['x', 'y', 'z'])
        temp['sample'] = k
        temp['activity'] = f'{p[2:]}'
        df = df.append([temp], ignore_index=True)
        k = k + 1
V=[]
for i in range(k):
    sp = df[df['sample']==i]
    sp = sp.drop(['activity'], axis=1)
    #sp.describes
    V.append(sp.values)
print(V)
#db = DBSCAN(eps=0.3, min_samples=10).fit(V)