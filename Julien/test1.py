# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:31:42 2022

@author: kju78
"""

"""
obj : Récuperer les titres et les liens externes d'une page wikipedia

"""

import requests                                           
from bs4 import BeautifulSoup

URL="https://fr.wikipedia.org/wiki/%C3%89cole_sp%C3%A9ciale_de_m%C3%A9canique_et_d%27%C3%A9lectricit%C3%A9"
page=requests.get(URL)                                   #scraping de la page
soup = BeautifulSoup(page.content, "html.parser")        #recupere contenu de la page | parser: analyse syntaxique type html

results = soup.find(id="bodyContent")                    #trouve element html 'bodyContent'
titres = results.find_all("span", class_="mw-headline")  #trouve toutes les balises <span> de class 'mw-headline' dans le bodyContent
liens = results.find_all("a",class_="mw-redirect")       #idem avec <a> et class 'mw-redirect'

print("\nTitres :\n")
for titre in titres :                                    #parcours de la liste des titres trouvés
    print(titre.text.strip())                            # .text retourne uniquement le contenu text (supprime les balises)
                                                         # .strip()supprimes les " " inutiles en début et fin       
print("\nLiens :\n")
for lien in liens:
        lien_url = lien["href"]                          #[href] extrait le lien href 
        print(lien_url)
    
    
    