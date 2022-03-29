# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 12:00:13 2022

@author: kju78
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.headless = True  # hide GUI
options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
options.add_argument("start-maximized")  # ensure window is full-screen

driver = webdriver.Chrome("C:/Users/kju78/Documents/ESME Sudria/Ingé 2/ESME Sudria - Ingé 2/Projet - Machine Learning Immobilier/Scraping/chromedriver")
page=1

datas_list = []
prices_list = []

while page<=3:
    
    url = 'https://www.logic-immo.com/vente-immobilier-paris-75,100_1/options/groupprptypesids=1,2,6,7,12/page=%d'%(page)
    driver.get(url)

    time.sleep(15) 

    datas = driver.find_elements_by_xpath('//a[@class="linkToFa"]')
    prices = driver.find_elements_by_xpath('//span[@class="announceDtlPrice"]')
    page += 1
  
    for d in range(len(datas)):
        datas_list.append(datas[d].text)        
    
    for p in range(len(prices)):
        prices_list.append(prices[p].text)
    

driver.close()

# print(datas_list)
# print(prices_list)

df = pd.DataFrame(list(zip(datas_list, prices_list)),columns =['Datas', 'Prices'])
print(df)
df.to_csv(r'C:\Users\kju78\Documents\ESME Sudria\Ingé 2\ESME Sudria - Ingé 2\Projet - Machine Learning Immobilier\Scraping\logicimmo.csv', index = False)


