from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.headless = True  # etre prive
options.add_argument("--window-size=1920,1080")  # dimension fenetre
options.add_argument("start-maximized")  # mise en plein ecran de la fenetre

driver = webdriver.Chrome(
    "/Users/sabrinethibert/Desktop/COURS/ESME/Ingé 2/Projets/chromedriver")  # adresse driver chrome

# =============================================================================
# Variables a definir :
# =============================================================================

debut = 417  # variable pour indentation nombre de page parcourues - a changer
fin = 428

page = debut  # a laisser

# =============================================================================
# Listes de stockage :
# =============================================================================


datas_list = []  # info recuperee sur chaque page annonce
url_list = []  # url de chaque annonce
datas_list_temp = []  # info d'une seule page annonce (=>chaque page aura sa liste d'info)

terrasse_list = []  # infos recuperees sur les pages annonces
parking_list = []
cave_list = []
ascenseur_list = []
gardien_list = []
renove_list = []
box_list = []

infos_list = []  # infos sur page principales concatenees en un block str
nb_bedrooms_list = []  # listes pour stockages des infos issues du block str
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

while debut <= page <= fin:  # boucle pour n pages differentes
    try:
        url = 'https://www.logic-immo.com/vente-immobilier-paris-75,100_1/options/groupprptypesids=1/page=%d' % (
            page)  # adresse de la page scrappee
        driver.get(url)  # ouverture avec driver

        pb = [9, 19, 29, 39, 49]  # pages avec test anti-robot

        if page == debut or page in pb or page % 10 == 0:
            time.sleep(8)  # pause
        else:
            time.sleep(8)

        links = driver.find_elements_by_xpath("//a[@class='add-to-selection']")  # scrape des infos
        scrap = driver.find_elements_by_xpath("//a[@class='linkToFa']")  # scrap des urls

        page += 1
        compteur = 1

        for l in range(len(links)):  # parcours des infos scrapee
            infos = links[l].get_attribute('onclick')  # recolte donnees de l'attribut 'onclick'
            infos_list.append(infos)  # ajout sur liste de donnees

        for s in range(len(scrap)):  # parcours liens recoltes
            new_url = scrap[s].get_attribute('href')  # recolte donnees de l'attribut 'href' => lien
            url_list.append(new_url)  # ajout du lien a la liste url

    except WebDriverException:
        pass

for i in range(len(url_list)):  # parcours de la liste des liens recoltes
    try:
        driver.get(url_list[i])  # driver avec nouvel url

        delais = [8, 15, 23, 31, 39, 47, 55, 62, 70, 78,
                  86]  # page avec controle anti-robot => toute les 7-8 pages => tous i+=8

        if i in delais:
            time.sleep(8)
        else:
            time.sleep(8)

        datas = driver.find_elements_by_xpath("//span[@class='dtlTechiqueItmLabel']")  # scrape infos sur nouvelle page

        for data in datas:  # parcours les infos recuperees sur la page
            datas_list_temp.append(data.text)  # ajout a liste temporaire la valeur text
        datas_list.append(datas_list_temp)  # ajout liste temporaire a liste globale (=> chaque page à sa liste d'infos)
        datas_list_temp = []  # vide la liste temporaire

        print("iteration actuelle : ", compteur, "/", len(url_list) + 1)
        compteur +=1

    except WebDriverException:
        pass


driver.close()  # fermeture de la fenetre de scraping

# =============================================================================
# Collecte des nouvelles données
# =============================================================================

for datas in datas_list:  # parcours de chaque sous liste (=> chaque page annonce)

    if 'Cave' in datas:  # si 'str' apparait dans sous liste
        cave_list.append(1)  # ajout de 1 dans liste associee
    else:
        cave_list.append(-1)  # sinon ajout de -1

    if 'Ascenseur' in datas:
        ascenseur_list.append(1)
    else:
        ascenseur_list.append(-1)

    if 'Gardien' in datas:
        gardien_list.append(1)
    else:
        gardien_list.append(-1)

    if 'Renové' in datas:
        renove_list.append(1)
    else:
        renove_list.append(-1)

    if 'Box' in datas:
        box_list.append(1)
    else:
        box_list.append(-1)

    if 'Terrasse/Balcon' in datas:
        terrasse_list.append(1)
    else:
        terrasse_list.append(-1)

    if 'Parking' in datas:
        parking_list.append(1)
    else:
        parking_list.append(-1)

# =============================================================================
# Nettoyage des données :
# =============================================================================

for info in infos_list:  # parcours liste infos pages recherche

    nb_rooms = info.partition("nb_rooms")[2][
        2]  # .particition[2] coupe la liste a 'str' et se place a droite, [2] recupere la valeur 3 idx plus loin
    nb_bedrooms = info.partition("nb_bedrooms")[2][2]
    energy_letter = info.partition("energy_letter")[2][3]
    photos_nb = info.partition("photos_nb")[2][2]
    floor_nb = info.partition("floor_nb")[2][2]
    client_type = info.partition("client_type")[2][3]
    price = info.partition("price")[2][2]
    space = info.partition("space")[2][2]
    estate_postalcode = info.partition("estate_postalcode")[2][3]
    estate_type = info.partition("estate_type")[2][2]

    if info.partition("energy_letter")[2][
        4] != "'":  # verfiie que la valeur suivante a celle selectionnee n'est pas une info utile
        energy_letter += info.partition("energy_letter")[2][4]

    if info.partition("photos_nb")[2][3] != "'" and info.partition("photos_nb")[2][3] != ",":
        photos_nb += info.partition("photos_nb")[2][3]

    for i in range(4, len(info.partition("client_type")[2])):
        if info.partition("client_type")[2][i] != "'":
            client_type += info.partition("client_type")[2][i]
        else:
            break

    for i in range(3, len(info.partition("price")[2])):
        if info.partition("price")[2][i] != ",":
            price += info.partition("price")[2][i]
        else:
            break

    for i in range(3, len(info.partition("space")[2])):
        if info.partition("space")[2][i] != ",":
            space += info.partition("space")[2][i]
        else:
            break

    for i in range(4, len(info.partition("estate_postalcode")[2])):
        if info.partition("estate_postalcode")[2][i] != "'":
            estate_postalcode += info.partition("estate_postalcode")[2][i]
        else:
            break

    if floor_nb == "'":
        floor_nb = -1  # -1 si NaN

    if client_type == 'pro':
        client_type = 1  # toujour vendeur pro
    else:
        client_type = 0

    classe_energetique = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # convertir en int pour dataframe
    if energy_letter not in classe_energetique:
        energy_letter = 0  # 0 si Nan
    elif energy_letter == 'A':
        energy_letter = 1
    elif energy_letter == 'B':
        energy_letter = 2
    elif energy_letter == 'C':
        energy_letter = 3
    elif energy_letter == 'D':
        energy_letter = 4
    elif energy_letter == 'E':
        energy_letter = 5
    elif energy_letter == 'F':
        energy_letter = 6
    elif energy_letter == 'G':
        energy_letter = 7

    if estate_type == "'":
        estate_type = -1
    elif estate_type == 9:
        estate_type = 3

    # appartement / studios : 1
    # maison / villa : 2
    # loft : 3

    nb_bedrooms_list.append(nb_bedrooms)  # ajout des donnees nettoyees et completes aux listes correspondantes
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

df = pd.DataFrame(list(
    zip(space_list, nb_rooms_list, nb_bedrooms_list, price_list, estate_postalcode_list, energy_letter_list,
        photos_nb_list, floor_nb_list, estate_type_list, client_type_list, terrasse_list, parking_list, cave_list,
        ascenseur_list, gardien_list, renove_list, box_list)),
    columns=['Superficie (m2)', 'Nombre Pieces', 'Nombre Chambres', 'Prix (Euros)', 'Code Postal',
             'Classe Energetique', 'Nombre Photos', 'Etage', 'Type de Bien', 'Type Vendeur', 'Terrasse',
             'Parking', 'Cave', 'Ascenseur', 'Gardien', 'Renove',
             'Box'])  # creation d'une base de donnees
print(df)  # affichage de la base
df.to_csv(
    r'/Users/sabrinethibert/Desktop/COURS/ESME/Ingé 2/Projets/real-estate-prediction/sabrine/logicimmo.csv',
    index=False)  # converti base pandas en fichier csv
