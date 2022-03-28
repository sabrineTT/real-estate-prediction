from time import sleep # on importe la fonction sleep pour faire une pause dans l'exec du programme
from selenium import webdriver  # on importe webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/valentinesallet/Desktop/pourEssayer/chromedriver')   #on utilise le fichier executable chromedriver qui va pouvoir ouvrir la fenetre chrome
driver.get("https://fr.wikipedia.org/wiki/Transformations_de_Paris_sous_le_Second_Empire")  # on ouvre la fenetre chrome a l'adresse url voulue


sleep(5) # on attend 5 sec le temps que la page s'ouvre


offers = driver.find_elements_by_css_selector("span.mw-headline") # on recherche les elements avec le selector la balise span et la classe mw-headline
for offer in offers: # on parcours tout les elements que l'on a trouver
    texte=offer.text # on recupere le texte uniquement de la balise
    print(texte) # on print


'''
ici un des avantage de selenium c'est que l'on peut entrer du texte dans une barre de recherche de maniere automatiser ou meme cliquer sur entrée etc

search_bar = driver.find_element_by_name("inputLocality")
search_bar.send_keys("75000")
search_bar.send_keys(Keys.ENTER)

'''

'''
Probleme :
les sites peuvent etre proteger et detecte lorsqu'un bot essaye d'atteindre le site (comme ce que 'on fait) on doit donc résoudre un captcha 
manuellement ce qui fait que le code perd sa fonction première qui est l'automatisation
'''