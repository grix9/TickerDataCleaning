import pandas as pd
from rapidfuzz import process

sp500df = pd.read_csv('SP500.csv')

barronsdf = pd.read_csv('Barrons100.csv')
corporatedf = pd.read_csv('CorporateKnights20.csv')
spglobaldf = pd.read_csv('S&PGlobal47.csv')
sustaindf = pd.read_csv('SustainabilityOnline10.csv')
timedf = pd.read_csv('Time116.csv')

#print(sp500df.head())
#print(barronsdf.head())
#print(corporatedf.head())
#print(spglobaldf.head())
#print(sustaindf.head())
#print(timedf.head())

#make companylist from sp500df
companylist = sp500df.company.tolist()

#Verify company names and create new list for column
def match_company(target, source):
    new_list = []
    for rows in target['company']:
        match = process.extractOne(rows, companylist)
        new_list.append(match[0])
    return(new_list)

sustaindf['company'] = match_company(sustaindf, companylist)
timedf['company'] = match_company(timedf, companylist)
barronsdf['company'] = match_company(barronsdf, companylist)
spglobaldf['company'] = match_company(spglobaldf, companylist)
corporatedf['company'] = match_company(corporatedf, companylist)

#merge df with match company names to sp500 to populate ticker column
sustaindropdf = sustaindf.drop(['ticker'], axis=1)
sustaintickerdf = pd.merge(sustaindropdf, sp500df, on='company')
if sustaintickerdf['company'].nunique() != 10:
    print('Check results for duplicates')
#print(sustaintickerdf)
#sustaintickerdf.to_csv('sustainnew.csv', index=False)

timedropdf = timedf.drop(['ticker'], axis=1)
timetickerdf = pd.merge(timedropdf, sp500df, on='company')
if timetickerdf['company'].nunique() != 116:
    print('Check results for duplicates')
#timedropdf.to_csv('timenew.csv', index =False)

barronsdropdf = barronsdf.drop(['ticker'], axis=1)
barronstickerdf = pd.merge(barronsdropdf, sp500df, on='company')
#print(barronstickerdf)

spglobaldropdf = spglobaldf.drop(['ticker'], axis=1)
spglobaltickerdf = pd.merge(spglobaldropdf, sp500df, on='company')
#print(spglobaltickerdf)

ckdropdf = corporatedf.drop(['ticker'], axis=1)
cktickerdf = pd.merge(ckdropdf, sp500df, on='company')
#print(cktickerdf)