import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('D:/Desktop/web_scraping/countries_population.csv')
df['Population'] = df['Population'].astype(str).str.replace(',', '').str.replace('"','').str.strip()
df['Population']=df['Population'].astype(int)
df['Date']=pd.to_datetime(df['Date'],format='mixed')
df['Source']=df['Source'].str.replace(' ','_')
df['Countries']=df['Countries'].str.replace(' ','_')
df['As_percent']=df['As_percent'].str.replace('%','',regex=False)
df['As_percent']=pd.to_numeric(df['As_percent'])
df.info()
describe=df.describe()
is_null=df.isna().sum() #not existing 
duplicaiton=df.duplicated().sum() #not existing 

countries=df.Countries.unique()
count_sources=df.Source.value_counts()
top5_persantage=df.sort_values('As_percent',ascending=False).head(5)
lowest_persantage=df.sort_values('As_percent').head(5)
persantage_pertime=df.groupby('Date')['Population'].mean()

lower_equal_0=df[df['As_percent']==0]

df.to_csv('D:/Desktop/web_scraping/clean_data.csv',index=False,quoting=0,encoding='utf-8-sig')