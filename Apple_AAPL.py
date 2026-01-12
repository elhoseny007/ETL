import requests 
from bs4 import BeautifulSoup
import csv
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'}
website=requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population',headers=headers)

def main(website):
    src=website.content
    soup=BeautifulSoup(src,'lxml')
    countries_info=[]
    table = soup.find('table', {'class':'wikitable'})
    if table is None:
        print("not existing")
    else:
        print("تم العثور على الجدول")
    def historical_data(table):
        worlds=table.contents[3].find('b').text.strip()
        print(worlds)
        rows = table.find_all('tr')[1:]
        for row in rows:
            cols = row.find_all('td')
            if len(cols)<2:
                continue
            country_cell=cols[0].get_text(strip=True)
            population=cols[1].get_text(strip=True)
            as_percent=cols[2].get_text(strip=True)
            Date=cols[3].get_text(strip=True)
            source=cols[4].get_text(strip=True)
            Notes=cols[5].get_text(strip=True)
            countries_info.append({'Countries':country_cell,'Population':population,
                                   'As_percent':as_percent,'Date':Date,
                                   'Source':source,'Note':Notes
                                   })
    historical_data(table)
    keys=countries_info[0].keys()
    
    with open('D:\Desktop\web_scraping/countries_population.csv','w') as output_files:
        dict_writer=csv.DictWriter(output_files, keys)
        dict_writer.writeheader()
        dict_writer.writerows(countries_info) 
main(website)
