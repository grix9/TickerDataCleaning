import pandas as pd

#Merge csvs on company, sum percentage on each company? 

barronsnew = pd.read_csv('barronsnew.csv')
cknew = pd.read_csv('cknew.csv')
spglobalnew = pd.read_csv('spglobalnew.csv')
sustainnew = pd.read_csv('sustainnew.csv')
timenew = pd.read_csv('timenew.csv')

#Add Reciprocal Rank Fusion column = 1/(rank+60)

def rank(df):
    rank = []
    count = 1
    for row in df['company']:
        rank.append(count)
        count += 1
    df['rank'] = rank

def rrf(df):
    df['rrf'] = 1 / (df['rank'] + 60)
    return(df)

rank(barronsnew)
rrf(barronsnew)
#print(barronsnew.head())
#barronsnew.to_csv('barronsfinal.csv', index=False)

rank(cknew)
rrf(cknew)
#cknew.to_csv('ckfinal.csv', index=False)

rank(spglobalnew)
rrf(spglobalnew)
#spglobalnew.to_csv('spglobalfinal.csv', index=False)

rank(sustainnew)
rrf(sustainnew)
#sustainnew.to_csv('sustainfinal.csv', index=False)

rank(timenew)
rrf(timenew)
#timenew.to_csv('timefinal.csv', index=False)

dfs = [barronsnew, cknew, spglobalnew, sustainnew, timenew]
combined = pd.concat(dfs)
#print(combined.head())
#print(len(combined))

final_scores = combined.groupby('company')['rrf'].sum().reset_index()
print(final_scores.sort_values(by='rrf', ascending=False))
final_scores.to_csv('finalranking.csv', index=False)