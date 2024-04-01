from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"

browser = webdriver.Chrome("C:/Users/manda/OneDrive/Desktop/Web Scraping/msedgedriver.exe")
browser.get(START_URL)

time.sleep(10)

scarped_data = []

def scrape():
    bright_star_table = BeautifulSoup.find("table", attrs={"class", "wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')
 
    for row in table_rows:
           table_cols = row.find_all('td')
           print(table_cols)

    for row in table_rows:
         table_cols = row.find_all('td')
    print(table_cols)
        
    for col_data in table_cols:
          print(col_data.text)

    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)

    for col_data in table_cols:
        data=col_data.text.strip()
        print(data)
    
    for row in table_rows:
        table_cols=row.find_all('td')

        temp_list=[]

    for col_data in table_cols:
         data=col_data.text.strip()
         temp_list.append(data)


    scarped_data.append(temp_list)

    
    stars_data = []

    for i in range(0,len(scarped_data)):
       
      Star_names = scarped_data[i][1]
      Distance = scarped_data[i][3]
      Mass = scarped_data[i][5]
      Radius = scarped_data[i][6]
      Lum = scarped_data[i][7]
      required_data = [Star_names, Distance, Mass, Radius, Lum] 
      stars_data.append(required_data)

headers = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']

star_df_1 = pd.DataFrame( stars_data, columns=headers)


#Convert to CSV
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")

