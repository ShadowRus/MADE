import pandas as pd
from tqdm import tqdm

sub = ['../HW1/Submissions/sub_resnet101.csv','../HW1/Submissions/sub_resnet152.csv']

dfs_list = []

for path in sub:
    dfs_list.append(pd.read_csv(path))

columns = dfs_list[0].columns[1:]

for col_name in tqdm(columns):
    a = dfs_list[0][col_name]
    for df in dfs_list[1:]:
        a += df[col_name]
    a /= len(dfs_list)

    dfs_list[0][col_name] = round(a).astype('int32')

dfs_list[0].to_csv('blend_Rusakov.csv', index=False)
