from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/valentinesallet/Desktop/pourEssayer/chromedriver')
driver.get("https://fr.wikipedia.org/wiki/Transformations_de_Paris_sous_le_Second_Empire")


sleep(5)
'''
search_bar = driver.find_element_by_name("inputLocality")
search_bar.send_keys("75000")
search_bar.send_keys(Keys.ENTER)

'''
'''
is_last_page = False
while not is_last_page:
'''
offers = driver.find_elements_by_css_selector("span.mw-headline")
for offer in offers:
    texte=offer.text
    print(texte)
