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
#searchcompany = from companydf
#searchcompany = 'Accent'
#match = process.extractOne(searchcompany, companylist)
#print(match[0])

def match_company(target, source):
    new_list = []
    for rows in target['company']:
        match = process.extractOne(rows, companylist)
        new_list.append(match[0])
    return(new_list)
        #print(match[0])

sustaindf['company'] = match_company(sustaindf, companylist)
print(sustaindf)

timematchdf = match_company(timedf, companylist)
barronsmatchdf = match_company(barronsdf, companylist)
spglobalmatchdf = match_company(spglobaldf, companylist)
corknightsmatchdf = match_company(corporatedf, companylist)

#merge df with match company names to sp500 to populate ticker column
sustaindropdf = sustaindf.drop(['ticker'], axis=1)
sustaintickerdf = pd.merge(sustaindropdf, sp500df, on='company')
print(sustaintickerdf)