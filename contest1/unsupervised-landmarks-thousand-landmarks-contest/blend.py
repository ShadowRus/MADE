import pandas as pd
from tqdm import tqdm

sub1=pd.read_csv('../HW1/Submissions/sub_resnet101.csv')
sub2=pd.read_csv('../HW1/Submissions/sub_resnet152.csv')

columns = sub1.columns[1:]

for col_name in tqdm(columns):
    a = (sub1[col_name]+sub2[col_name])/2
    sub1[col_name] =round(a).astype('int32')

sub1.to_csv('blend_Rusakov.csv', index=False)
