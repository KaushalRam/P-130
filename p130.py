import pandas as pd
import csv

df = pd.read_csv('final.csv')

df.columns
df.drop(['Unnamed:0','Unnamed:5','Star_Name:6','Distance:7','Mass:8','Mass:9'],axis = 1, inplace= True)
final_data = df.dropna()
final_data.reset_index(drop=True, inplace=True)
final_data.to_csv('final_data.csv')