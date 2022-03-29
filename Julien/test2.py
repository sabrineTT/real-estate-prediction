# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 10:33:48 2022

@author: kju78
"""


"""
obj : Récuperer les titres et les liens externes d'une page wikipedia

"""

import requests                                           
from bs4 import BeautifulSoup

URL="https://www.logic-immo.com/vente-immobilier-paris-75,100_1/options/groupprptypesids=1,2,6,7,12"
page=requests.get(URL)                                   #scraping de la page
soup = BeautifulSoup(page.content, "html.parser")        #recupere contenu de la page | parser: analyse syntaxique type html

results = soup.find(id="lists-offer")                    #trouve element html 'bodyContent'

adresses=results.find_all("div", class_="announcePropertyLocation")
price=results.find_all("span", class_="announceDtlPrice")

# dimensions= results.find_all("span", class_="linkToFa")  #trouve toutes les balises <span> de class 'mw-headline' dans le bodyContent
# nbrPieces= results.find_all("span", class_="linkToFa")

# prices=results.find_all("a", class_="linkToFa")

# print("\nDimensions :")
# for dimension in dimensions :                                    
#     dimension_url = dimension["href"]                           
#     page_dimension=requests.get(dimension_url)
#     dimension_soup = BeautifulSoup(page_dimension.content, "html.parser")
#     dimension_results = dimension_soup.find("li", {"class":"infoDtl"})
#     new_dimension=dimension_results.find("em")
#     print(new_dimension.text.strip())                          
                                 
# print("\nnbrPieces :")
# for nbrPiece in nbrPieces :                                    
#     nbrPiece_url = nbrPiece["href"]                           
#     page_nbrPiece=requests.get(nbrPiece_url)
#     nbrPiece_soup = BeautifulSoup(page_nbrPiece.content, "html.parser")
#     nbrPiece_results = nbrPiece_soup.find("span", {"class":"dtlTitle"})
#     new_nbrPiece=nbrPiece_results.find("em")
#     print(new_nbrPiece.text.strip()) 
                        
print("\nAdresses :")
for adresse in adresses:                                    
    print(adresse.text.strip()) 
    
print("\nPrix")
for price in prices :
    print(price.text.strip())
    
# print("\nPrix :")
# for price in prices:
#     price_url = price["href"]                           
#     page_prix=requests.get(price_url)   
#     new_soup = BeautifulSoup(page_prix.content, "html.parser")
#     new_results = new_soup.find("div", {"class":"offerDetailContainer"})
#     new_price=new_results.find("span", class_="infoPrice")
#     print(new_price.text.strip())


        
        
        
        
        
        
        
    