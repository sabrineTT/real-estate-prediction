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
options.headless = True  # etre prive
options.add_argument("--window-size=1920,1080")  # dimension fenetre
options.add_argument("start-maximized")  # mise en plein ecran de la fenetre

driver = webdriver.Chrome("C:/Users/kju78/Documents/ESME Sudria/Ingé 2/ESME Sudria - Ingé 2/Projet - Machine Learning Immobilier/Scraping/chromedriver") #adresse driver chrome
page=1 #variable pour indentation nombre de page parcourues

datas_list = [] #listes vides pour stocker datas scrapees
prices_list = []

while page<=3: #boucle pour 3 pages differentes
    
    url = 'https://www.logic-immo.com/vente-immobilier-paris-75,100_1/options/groupprptypesids=1,2,6,7,12/page=%d'%(page) #adresse de la page scrappee
    driver.get(url) #ouverture avec driver

    time.sleep(15) #pause

    datas = driver.find_elements_by_xpath('//a[@class="linkToFa"]') #recupere tous les elements avec une borne a et une classe "linktofa"
    prices = driver.find_elements_by_xpath('//span[@class="announceDtlPrice"]')
    page += 1
  
    for d in range(len(datas)):
        datas_list.append(datas[d].text) #ajoute chaque element recupere au dessus dans une liste defenie avant
    
    for p in range(len(prices)):
        prices_list.append(prices[p].text)
    

driver.close() #fermeture de la fenetre de scraping

# print(datas_list)
# print(prices_list)

df = pd.DataFrame(list(zip(datas_list, prices_list)),columns =['Datas', 'Prices']) #creation d'une base de donnees
print(df) #affichage de la base
df.to_csv(r'C:\Users\kju78\Documents\ESME Sudria\Ingé 2\ESME Sudria - Ingé 2\Projet - Machine Learning Immobilier\Scraping\logicimmo.csv', index = False) #converti base pandas en fichier csv


