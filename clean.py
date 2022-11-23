import pandas as pd
import numpy as ny

df = pd.read_csv(r'crop.csv', sep=',')
# print(df)

# print(df.head())
# print(df['SiteID'])

df.dropna(subset=['SiteID'], inplace = True)
df.dropna(subset=['Location'], inplace = True)

filt1 = (df['SiteID']==188) & (df['Location']!='AURN Bristol Centre')
filt2 = (df['SiteID']==203) & (df['Location']!='Brislington Depot')
filt3 = (df['SiteID']==206) & (df['Location']!='Rupert Street')
filt4 = (df['SiteID']==209) & (df['Location']!='IKEA M32')
filt5 = (df['SiteID']==213) & (df['Location']!='Old Market')
filt6 = (df['SiteID']==215) & (df['Location']!='Parson Street School')
filt7 = (df['SiteID']==228) & (df['Location']!='Temple Meads Station')
filt8 = (df['SiteID']==270) & (df['Location']!='Wells Road')
filt9 = (df['SiteID']==271) & (df['Location']!='Trailer Portway P&R')
filt10 = (df['SiteID']==375) & (df['Location']!='Newfoundland Road Police Station')
filt11 = (df['SiteID']==395) & (df['Location']!="Shiner's Garage")
filt12 = (df['SiteID']==452) & (df['Location']!='AURN St Pauls')
filt13 = (df['SiteID']==447) & (df['Location']!='Bath Road')
filt14 = (df['SiteID']==459) & (df['Location']!='Cheltenham Road \ Station Road')
filt15 = (df['SiteID']==463) & (df['Location']!='Fishponds Road')
filt16 = (df['SiteID']==481) & (df['Location']!='CREATE Centre Roof')
filt17 = (df['SiteID']==500) & (df['Location']!='Temple Way')
filt18 = (df['SiteID']==501) & (df['Location']!='Colston Avenue')


df.drop(index = df[filt1].index, inplace = True)
df.drop(index = df[filt2].index, inplace = True)
df.drop(index = df[filt3].index, inplace = True)
df.drop(index = df[filt4].index, inplace = True)
df.drop(index = df[filt5].index, inplace = True)
df.drop(index = df[filt6].index, inplace = True)
df.drop(index = df[filt7].index, inplace = True)
df.drop(index = df[filt8].index, inplace = True)
df.drop(index = df[filt9].index, inplace = True)
df.drop(index = df[filt10].index, inplace = True)
df.drop(index = df[filt11].index, inplace = True)
df.drop(index = df[filt12].index, inplace = True)
df.drop(index = df[filt13].index, inplace = True)
df.drop(index = df[filt14].index, inplace = True)
df.drop(index = df[filt15].index, inplace = True)
df.drop(index = df[filt16].index, inplace = True)
df.drop(index = df[filt17].index, inplace = True)
df.drop(index = df[filt18].index, inplace = True)

df.to_csv('clean.csv', sep = ',', index=True)
print(df)


#print difference between data sets
