import pandas as pd
from fuzzywuzzy import process

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

testdf = pd.merge(sp500df, sustaindf, how='inner', on='company')
print(testdf.head())