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

driver = webdriver.Chrome("C:/Users/kju78/Documents/ESME Sudria/Ingé 2/ESME Sudria - Ingé 2/Projet - Machine Learning Immobilier/Scraping/chromedriver")  # adresse driver chrome

# =============================================================================
# Variables a definir :
# =============================================================================

debut = 1 # variable pour indentation nombre de page parcourues
fin = 2
page = debut

# =============================================================================
# Listes de stockage :
# =============================================================================

infos_list = []
nb_bedrooms_list = []
nb_rooms_list = []
energy_letter_list = []
photos_nb_list = []
floor_nb_list = []
client_type_list = []
price_list = []
space_list = []
estate_postalcode_list = []

# =============================================================================
# Scraping :
# =============================================================================

while debut <= page <= fin:  # boucle pour 5 pages differentes

    url = 'https://www.logic-immo.com/vente-immobilier-paris-75,100_1/options/groupprptypesids=1/page=%d'%(page)  # adresse de la page scrappee
    driver.get(url)  # ouverture avec driver

    if page % 10 == 0 or page == debut:
        time.sleep(15)  # pause
    else:
        time.sleep(5)
    
    links = driver.find_elements_by_xpath("//a[@class='add-to-selection']")
    
    page += 1
        
    for l in range(len(links)):
        infos = links[l].get_attribute('onclick')
        infos_list.append(infos)
        

driver.close()  # fermeture de la fenetre de scraping

# =============================================================================
# Nettoyage des données :
# =============================================================================
    
for info in infos_list :
    
    nb_rooms = info.partition("nb_rooms")[2][2]
    nb_bedrooms = info.partition("nb_bedrooms")[2][2]
    energy_letter = info.partition("energy_letter")[2][3]
    photos_nb = info.partition("photos_nb")[2][2]
    floor_nb = info.partition("floor_nb")[2][2]
    client_type = info.partition("client_type")[2][3]
    
    price = info.partition("price")[2][2]
    space = info.partition("space")[2][2]
    estate_postalcode = info.partition("estate_postalcode")[2][3] 

    if info.partition("energy_letter")[2][4] != "'" :
        energy_letter+=info.partition("energy_letter")[2][4]

    if info.partition("photos_nb")[2][3] != "'" and info.partition("photos_nb")[2][3] != ",":
        photos_nb+=info.partition("photos_nb")[2][3]
     
    
    for i in range(4,len(info.partition("client_type")[2])):
        if info.partition("client_type")[2][i] != "'" :
            client_type += info.partition("client_type")[2][i]
        else :
            break  
        
    for i in range(3,len(info.partition("price")[2])):
        if info.partition("price")[2][i] != "," :
            price += info.partition("price")[2][i]
        else :
            break 
    
    for i in range(3,len(info.partition("space")[2])):
        if info.partition("space")[2][i] != "," :
            space += info.partition("space")[2][i]
        else :
            break 
        
    for i in range(4,len(info.partition("estate_postalcode")[2])):
        if info.partition("estate_postalcode")[2][i] != "'" :
            estate_postalcode += info.partition("estate_postalcode")[2][i]
        else :
            break  
    
    if floor_nb == "'" :
        floor_nb = "NaN"
    
    
    nb_bedrooms_list.append(nb_bedrooms)
    nb_rooms_list.append(nb_rooms)
    energy_letter_list.append(energy_letter)
    photos_nb_list.append(photos_nb)
    floor_nb_list.append(floor_nb)
    client_type_list.append(client_type)
    price_list.append(price)
    space_list.append(space)
    estate_postalcode_list.append(estate_postalcode)

# =============================================================================
# Création du dataframe :
# =============================================================================

df = pd.DataFrame(list(zip(space_list, nb_rooms_list, nb_bedrooms_list, price_list, estate_postalcode_list, energy_letter_list, photos_nb_list, floor_nb_list, client_type_list)),columns=['Superficie (m2)', 'Nombre Pieces', 'Nombre Chambres', 'Prix (Euros)', 'Code Postal', 'Classe Energetique', 'Nombre Photos', 'Etage', 'Type Vendeur'])  # creation d'une base de donnees
print(df)  # affichage de la base
df.to_csv(r'C:\Users\kju78\Documents\ESME Sudria\Ingé 2\ESME Sudria - Ingé 2\Projet - Machine Learning Immobilier\Scraping\logicimmo.csv',index=False)  # converti base pandas en fichier csv




