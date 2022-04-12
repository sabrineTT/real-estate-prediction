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
fin = 1
page = debut

# =============================================================================
# Listes de stockage :
# =============================================================================


datas_list = []
url_list = []
datas_list_temp = []


terrasse_list = []
parking_list = []
cave_list = []
ascenseur_list = []
gardien_list = []
renove_list = []
box_list = []


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
estate_type_list = [] 

# =============================================================================
# Scraping :
# =============================================================================

while debut <= page <= fin:  # boucle pour 5 pages differentes

    url = 'https://www.logic-immo.com/vente-immobilier-paris-75,100_1/options/groupprptypesids=1/page=%d'%(page)  # adresse de la page scrappee
    driver.get(url)  # ouverture avec driver

    pb = [9,19,29,39,49]

    if page == debut or page in pb or page % 10 == 0 :
        time.sleep(12)  # pause
    else:
        time.sleep(3)
    
    links = driver.find_elements_by_xpath("//a[@class='add-to-selection']")
    scrap = driver.find_elements_by_xpath("//a[@class='linkToFa']")
    
    page += 1
    
    for l in range(len(links)):
        infos = links[l].get_attribute('onclick')
        infos_list.append(infos)    
    
    for s in range(len(scrap)):
        new_url = scrap[s].get_attribute('href')
        url_list.append(new_url)


for i in range(len(url_list)) :
    driver.get(url_list[i])
    datas = driver.find_elements_by_xpath("//span[@class='dtlTechiqueItmLabel']")
    time.sleep(6)
    for data in datas :
        datas_list_temp.append(data.text)
    datas_list.append(datas_list_temp)
    datas_list_temp = []
    

driver.close()  # fermeture de la fenetre de scraping
    

# =============================================================================
# Collecte des nouvelles données
# =============================================================================

for datas in datas_list :
            
        if 'Cave' in datas :
            cave_list.append(1)
        else : 
            cave_list.append(-1)
            
        if 'Ascenseur' in datas :
            ascenseur_list.append(1)
        else : 
            ascenseur_list.append(-1)
            
        if 'Gardien' in datas :
            gardien_list.append(1)
        else : 
            gardien_list.append(-1)
            
        if 'Renové' in datas :
            renove_list.append(1)
        else : 
            renove_list.append(-1)
            
        if 'Box' in datas :
            box_list.append(1)
        else : 
            box_list.append(-1)
            
        if 'Terrasse/Balcon' in datas :
            terrasse_list.append(1)
        else : 
            terrasse_list.append(-1)
         
        if 'Parking' in datas :
            parking_list.append(1)
        else : 
            parking_list.append(-1)
            
            
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
    estate_type = info.partition("estate_type")[2][2]


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
        floor_nb = -1 #-1 si NaN
        
    if client_type == 'pro' :
        client_type = 1 #toujour vendeur pro
    else :
        client_type = 0
        
    classe_energetique = ['A','B','C','D','E','F','G']
    if energy_letter not in classe_energetique :
        energy_letter = 0 #0 si Nan
    elif energy_letter == 'A' :
        energy_letter = 1
    elif energy_letter == 'B' :
        energy_letter = 2
    elif energy_letter == 'C' :
        energy_letter = 3
    elif energy_letter == 'D' :
        energy_letter = 4
    elif energy_letter == 'E' :
        energy_letter = 5
    elif energy_letter == 'F' :
        energy_letter = 6
    elif energy_letter == 'G' :
        energy_letter = 7
    
    if estate_type == "'" :
        estate_type = -1
    elif estate_type == 9 :
        estate_type = 3
    
    # appartement / studios : 1
    # maison / villa : 2
    # loft : 3
    
    nb_bedrooms_list.append(nb_bedrooms)
    nb_rooms_list.append(nb_rooms)
    energy_letter_list.append(energy_letter)
    photos_nb_list.append(photos_nb)
    floor_nb_list.append(floor_nb)
    client_type_list.append(client_type)
    price_list.append(price)
    space_list.append(space)
    estate_postalcode_list.append(estate_postalcode)
    estate_type_list.append(estate_type)

# # =============================================================================
# # Création du dataframe :
# # =============================================================================

df = pd.DataFrame(list(zip(space_list, nb_rooms_list, nb_bedrooms_list, price_list, estate_postalcode_list, energy_letter_list, photos_nb_list, floor_nb_list,estate_type_list, client_type_list, terrasse_list, parking_list, cave_list, ascenseur_list, gardien_list, renove_list, box_list)),columns=['Superficie (m2)', 'Nombre Pieces', 'Nombre Chambres', 'Prix (Euros)', 'Code Postal', 'Classe Energetique', 'Nombre Photos', 'Etage', 'Type de Bien', 'Type Vendeur', 'Terrasse', 'Parking', 'Cave', 'Ascenseur', 'Gardien', 'Renove', 'Box'])  # creation d'une base de donnees
print(df)  # affichage de la base
df.to_csv(r'C:\Users\kju78\Documents\ESME Sudria\Ingé 2\ESME Sudria - Ingé 2\Projet - Machine Learning Immobilier\Scraping\logicimmo.csv',index=False)  # converti base pandas en fichier csv


