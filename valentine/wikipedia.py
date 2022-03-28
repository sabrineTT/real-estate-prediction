import requests
from bs4 import BeautifulSoup


# Scrapping wikipedia
'''

wikipedia_url = 'https://fr.wikipedia.org/wiki/Transformations_de_Paris_sous_le_Second_Empire'
html_text = requests.get(wikipedia_url).text
soup = BeautifulSoup(html_text, 'html.parser')

titre_articles = soup.find_all("span", class_="mw-headline")
for titre in titre_articles:
    print(titre.get_text(strip=True))



Scrapping logic immo soup
'''

Logic_url = 'https://www.logic-immo.com/vente-immobilier-paris-75,100_1/options/groupprptypesids=1,2,6,7,12'
html_text = requests.get(Logic_url).text
soup = BeautifulSoup(html_text, 'html.parser')

print(soup)

Annonces = []

table = soup.find('div', attrs={"id": "lists-offer"})
print(table)

for row in table.findAll('div', attrs={'class': 'announceContent'}):

    annonce = {}

    x1 = row.findChildren("span", attrs={"class": "announceDtlPrice"})
    for i in x1:
        annonce['Prix'] = i.get_text(separator="  #")
    x2 = row.findChildren("div", attrs={"class": "announcePropertyLocation"})
    for i in x2:
        annonce['Location'] = i.text
    x3 = row.findChildren("span", attrs={"class": "announceDtlInfosPropertyType"})
    for i in x3:
        annonce['Type'] = i.text
    x4 = row.findChildren("span", attrs={"class": "announceDtlInfos announceDtlInfosArea"})
    for i in x1:
        annonce['Area'] = i.text
    x5 = row.findChildren("span", attrs={"class": "announceDtlInfos announceDtlInfosNbRooms"})
    for i in x1:
        annonce['NbRoom'] = i.text
    Annonces.append(annonce)

print(Annonces)










# annonce['prix']=row.span(attrs = {"class" : "announceDtlPrice"}).text

# Annonces.append(annonce)

# print(Annonces)


