import requests
import pandas as pd
from bs4 import BeautifulSoup

wiki_url = 'https://fr.wikipedia.org/wiki/Liste_des_villes_du_Japon_par_nombre_d%27habitants'
html_text = requests.get(wiki_url).text
soup = BeautifulSoup(html_text, 'html.parser')

# On créer une liste vides qui contiendra les datas des villes
data_villes = []

# On récupère les en-têtes du tableau HTML
list_header = []
header = soup.find_all("table")[0].find("tr")

for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue

# On récupère les données du tableau HTML
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data_villes.append(sub_data)

# On sauvegarde les données du tableau HTML dans un dataFrame pandas
tableau_donnees_villes = pd.DataFrame(data=data_villes, columns=list_header)

# Et on converti le dataFrame en fichier CSV
tableau_donnees_villes.to_csv('villes_japon.csv')