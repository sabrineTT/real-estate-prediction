import requests     # importe la librairie qui fait des requetes
from bs4 import BeautifulSoup  # importe la librairie beautiful soup


# Scrapping wikipedia
'''

wikipedia_url = 'https://fr.wikipedia.org/wiki/Transformations_de_Paris_sous_le_Second_Empire' #on met l'url dans la variable
html_text = requests.get(wikipedia_url).text   # on recupere le code html de la page dans une variable
soup = BeautifulSoup(html_text, 'html.parser')   # on lance l'analyse sur le code html

titre_articles = soup.find_all("span", class_="mw-headline")   # find all recherche tout les elément de type span avec la classe mw-headline
for titre in titre_articles:       # on passe sur tout les élements trouvés qui sont dans la variable titres articles
    print(titre.get_text(strip=True))    # on récupère uniqument le texte qu'il y a dans les balises trouvées et on print



Scrapping logic immo soup
'''

# meme chose pour les 3 lignes suivantes

Logic_url = 'https://www.logic-immo.com/vente-immobilier-paris-75,100_1/options/groupprptypesids=1,2,6,7,12'
html_text = requests.get(Logic_url).text
soup = BeautifulSoup(html_text, 'html.parser')

# print(soup) # ca print le code html dans la console

Annonces = []  # on creer une liste annonces qui va lister toutes les annonces

table = soup.find('div', attrs={"id": "lists-offer"})  # on recupere la div qui a l'id list-offer
# print(table)

for row in table.find_all('div', attrs={'class': 'announceContent'}):  #on cherche toute les balises qui ont announcecontent et on va faire pour chaque element de la liste :

    annonce = {}   # on crée un dictionnaire, ca servira pour chaque annonce a lister le prix la surface etc

    x1 = row.findChildren("span", attrs={"class": "announceDtlPrice"}) # on cherche dans les "enfants" de l'élément les span de class announceDtlPrice
    for i in x1:
        annonce['Prix'] = " ".join(i.get_text().split()) # on recupere le texte de la balises span et on met dans le dictionnaire

    x2 = row.findChildren("div", attrs={"class": "announcePropertyLocation"})
    for i in x2:
        annonce['Location'] = " ".join(i.get_text().split())

    x3 = row.findChildren("span", attrs={"class": "announceDtlInfosPropertyType"})
    for i in x3:
        annonce['Type'] = " ".join(i.get_text().split())
    x4 = row.findChildren("span", attrs={"class": "announceDtlInfos announceDtlInfosArea"})
    for i in x4:
        annonce['Area'] = " ".join(i.get_text().split())
    x5 = row.findChildren("span", attrs={"class": "announceDtlInfos announceDtlInfosNbRooms"})
    for i in x5:
        annonce['NbRoom'] = " ".join(i.get_text().split())
    Annonces.append(annonce) # on ajoute le dictionnaire a la liste
# il y a autant de dictionnaire que de liste.

print(Annonces) #on print la liste
print(len(Annonces))

'''
Probleme 1 :
beauifulsoup n'est pas dynamique donc ne va pas chercher les autres annonces si elles sont sur plusieurs pages.

Probleme 2 :
si un pop up apparait type accepter les cookies, la page html capter est cette page pop up et non la page voulue.
Beautifulsoup ne trouvera donc pas les element avec les .find
'''

