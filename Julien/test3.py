# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 12:00:13 2022

@author: kju78
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import re

options = Options()
options.headless = True  # etre prive
options.add_argument("--window-size=1920,1080")  # dimension fenetre
options.add_argument("start-maximized")  # mise en plein ecran de la fenetre

driver = webdriver.Chrome("C:/Users/kju78/Documents/ESME Sudria/Ingé 2/ESME Sudria - Ingé 2/Projet - Machine Learning Immobilier/Scraping/chromedriver")  # adresse driver chrome

# =============================================================================
# Variables a definir :
# =============================================================================

page = 1  # variable pour indentation nombre de page parcourues
debut = 1
fin = 5

# =============================================================================

datas_list = []  # listes vides pour stocker datas scrapees
prices_list = []
nombre_pieces_list = []
superficie_list = []
clean_prices_list = []
arrondiessements_list = []

# =============================================================================
# Scraping :
# =============================================================================

while debut <= page <= fin:  # boucle pour 5 pages differentes

    url = 'https://www.logic-immo.com/vente-immobilier-paris-75,100_1/options/groupprptypesids=1/page=%d'%(page)  # adresse de la page scrappee
    driver.get(url)  # ouverture avec driver

    if page == debut:
        time.sleep(12)  # pause
    else:
        time.sleep(3)

    datas = driver.find_elements_by_xpath('//a[@class="linkToFa"]')  # recupere tous les elements avec une borne a et une classe "linktofa"
    prices = driver.find_elements_by_xpath('//span[@class="announceDtlPrice"]')
    arrondiessements = driver.find_elements_by_xpath('//div[@class="announcePropertyLocation"]')

    page += 1

    for d in range(len(datas)):
        datas_list.append(datas[d].text)  # ajoute chaque element recupere au dessus dans une liste defenie avant

    for p in range(len(prices)):
        prices_list.append(prices[p].text)

    for a in range(len(arrondiessements)):
        arrondiessements_list.append(arrondiessements[a].text)

driver.close()  # fermeture de la fenetre de scraping

# =============================================================================
# Nettoyage des données :
# =============================================================================

for data in datas_list:
    digit = re.findall(r"\d", data)  # recupere uniquement les chiffres de data

    nombre_pieces = digit[-1] + "p"  # le dernier chiffre correspond au nombre de pieces
    nombre_pieces_list.append(nombre_pieces)
    del digit[-1]  # retire le nombre de piece de data

    superficie = ("".join(digit)) + "m2"  # concatene les chiffres restant dans data sans separateur
    superficie_list.append(superficie)

for price in prices_list:
    clean_data = re.sub("\€", "", price) + "Euros"  # supprime le signe €
    clean_prices_list.append(clean_data)

df = pd.DataFrame(list(zip(superficie_list, nombre_pieces_list, clean_prices_list, arrondiessements_list)),columns=['Superficie', 'Nombre Piece', 'Prix', 'Code Postal'])  # creation d'une base de donnees
print(df)  # affichage de la base
df.to_csv(r'C:\Users\kju78\Documents\ESME Sudria\Ingé 2\ESME Sudria - Ingé 2\Projet - Machine Learning Immobilier\Scraping\logicimmo.csv',index=False)  # converti base pandas en fichier csv




