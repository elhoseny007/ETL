import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('D:/Desktop/web_scraping/countries_population.csv')
df.info()
head=df.head(10)
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

#analysis
df_analysis=df.iloc[1:,:-1]
population_by_countries=df_analysis.groupby('Countries')['Population'].max().nlargest(10)
plt.figure(figsize=(20,10))
# نقوم بتخزين الرسم في متغير ax
ax = population_by_countries.plot(kind='bar', color='blue')
plt.bar_label(ax.containers[0], padding=3, labels=[f'{v/1e9:.1f}bn' for v in population_by_countries.values], fontsize=10, fontweight='bold')
plt.title('max of population by countries')
plt.xlabel('countries')
plt.ylabel('population')
plt.show()

#percentage
pers_by_countries=df_analysis.groupby('Countries')['As_percent'].max().nlargest(10)
plt.figure(figsize=(20,10))
ax2=pers_by_countries.plot(kind='bar',color='green')
plt.bar_label(ax2.containers[0], padding=3, labels=[f'{v/1000000:.1f}bn' for v in pers_by_countries.values], fontsize=10, fontweight='bold')
plt.title('population ratio by countries')
plt.xlabel('countries')
plt.ylabel('population')
plt.show()

#population by source
count_of_source=df_analysis.groupby('Source')['Countries'].count().sort_values(ascending=True).nlargest(5)
plt.figure(figsize=(20,10))
ax3=plt.barh(count_of_source.index,count_of_source.values,color='green')
plt.title('count of source')
plt.xlabel('countries')
plt.ylabel('source')

#leniar
yearly_pop = df.groupby(df['Date'].dt.year)['Population'].sum()
plt.figure(figsize=(20,10))
ax = plt.gca()
plt.plot(yearly_pop.index, yearly_pop.values, color='#1a237e', marker='o', linewidth=2, markersize=6)
plt.fill_between(yearly_pop.index, yearly_pop.values, color='#1a237e', alpha=0.3)
plt.title('Sum of Population by Year', loc='left', fontsize=14)
plt.xlabel('Year')
plt.ylabel('Sum of Population')
df.to_csv('D:/Desktop/web_scraping/clean_data.csv',index=False,quoting=0,encoding='utf-8-sig')