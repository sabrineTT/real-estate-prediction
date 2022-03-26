import requests
import pandas as pd
from bs4 import BeautifulSoup

wiki_url = 'https://fr.wikipedia.org/wiki/Liste_des_villes_du_Japon_par_nombre_d%27habitants'

def html_data_to_csv(url, csv_name):
    """
    Récupère les données d'un tableau HTML d'une page web
    et les stocks dans un dataFrame pandas pour
    ensuite le convertir en tableau CSV

    :param str url: le lien de la page web
    :param str csv_name: le nom du tableau csv qu'on l'on obtiendra a la fin

    :return: un tableau CSV
    :rtype: CSV
    """
    # On récupère le fichier html du lien voulu
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    # On créer une liste vides qui contiendra les datas des villes
    data = []

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
        data.append(sub_data)

    # On sauvegarde les données du tableau HTML dans un dataFrame pandas
    tableau_donnees = pd.DataFrame(data=data, columns=list_header)

    # Et on converti le dataFrame en fichier CSV
    return (tableau_donnees.to_csv(csv_name+'.csv'))

html_data_to_csv(wiki_url, "villes_japon")