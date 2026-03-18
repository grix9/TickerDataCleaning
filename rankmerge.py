import pandas as pd

#Merge csvs on company, sum percentage on each company? 

barronsnew = pd.read_csv('barronsnew.csv')
cknew = pd.read_csv('cknew.csv')
spglobalnew = pd.read_csv('spglobalnew.csv')
sustainnew = pd.read_csv('sustainnew.csv')
timenew = pd.read_csv('timenew.csv')

dfs = [barronsnew, cknew, spglobalnew, sustainnew, timenew]
combined = pd.concat(dfs)
print(combined.head())
print(len(combined))