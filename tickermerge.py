import pandas as pd
from rapidfuzz import process

sp500df = pd.read_csv('SP500.csv')
barronsdf = pd.read_csv('Barrons100.csv')
corporatedf = pd.read_csv('CorporateKnights20.csv')
spglobaldf = pd.read_csv('S&PGlobal47.csv')
sustaindf = pd.read_csv('SustainabilityOnline10.csv')
timedf = pd.read_csv('Time116.csv')

#Create list of company names for matching
companylist = sp500df.company.tolist()

#Match company names with correct title
def match_company(target, source):
    threshold = 80
    new_list = []
    for company in target:
        match, score, index = process.extractOne(company, source)
        if score >= threshold:
            new_list.append(match)
        else:
            new_list.append('No Match')
    return new_list

def drop_nomatch(df):
    for company in df['company']:
         if company == 'No Match':
            df.drop(df[df['company'] == company].index, inplace=True)
    return df


def check_dupes(df):
    duplicate_rows = df[df.duplicated(subset=['company'], keep=False)]
    print(duplicate_rows)

#Sustainability Online
newsustainlist = match_company(sustaindf['company'], companylist)
sustaindf['company'] = newsustainlist
drop_nomatch(sustaindf)
sustaindropdf = sustaindf.drop(['ticker'], axis=1)
sustaintickerdf = pd.merge(sustaindropdf, sp500df, on='company')
check_dupes(sustaintickerdf)
#print(sustaintickerdf.head())
#sustaintickerdf.to_csv('sustainnew.csv', index=False)

#Time
newtimelist = match_company(timedf['company'], companylist)
timedf['company'] = newtimelist
drop_nomatch(timedf)
timedropdf = timedf.drop(['ticker'], axis=1)
timetickerdf = pd.merge(timedropdf, sp500df, on='company')
check_dupes(timetickerdf)
#print(timetickerdf.head())
#timetickerdf.to_csv('timenew.csv', index =False)

#Barrons
newbarronslist = match_company(barronsdf['company'], companylist)
barronsdf['company'] = newbarronslist
drop_nomatch(barronsdf)
barronsdropdf = barronsdf.drop(['ticker'], axis=1)
barronstickerdf = pd.merge(barronsdropdf, sp500df, on='company')
check_dupes(barronstickerdf)
#print(barronstickerdf.head())
#barronstickerdf.to_csv('barronsnew.csv', index=False)

#SPGlobal
newspgloballist = match_company(spglobaldf['company'], companylist)
spglobaldf['company'] = newspgloballist
drop_nomatch(spglobaldf)
spglobaldropdf = spglobaldf.drop(['ticker'], axis=1)
spglobaltickerdf = pd.merge(spglobaldropdf, sp500df, on='company')
check_dupes(spglobaltickerdf)
#print(spglobaltickerdf.head())
#spglobaltickerdf.to_csv('spglobalnew.csv', index=False)

#Corporate Knights
newcklist = match_company(corporatedf['company'], companylist)
corporatedf['company'] = newcklist
drop_nomatch(corporatedf)
ckdropdf = corporatedf.drop(['ticker'], axis=1)
cktickerdf = pd.merge(ckdropdf, sp500df, on='company')
check_dupes(cktickerdf)
#print(cktickerdf.head())
#cktickerdf.to_csv('cknew.csv', index=False)