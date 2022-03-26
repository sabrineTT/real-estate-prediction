import requests
from bs4 import BeautifulSoup

vgm_url = 'https://fr.wikipedia.org/wiki/Liste_des_villes_du_Japon_par_nombre_d%27habitants'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')