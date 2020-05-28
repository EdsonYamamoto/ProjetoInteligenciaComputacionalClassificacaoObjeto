from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import wget

local = 'coletaDados/dados/'

switcher = {
    9: "COINS",
    10: "PAINTINGS",
    11: "PRINTS",
    12: "DRAWINGS",
    13: "PHOTOGRAPHS",
    14: "SCULPTURE",
    15: "TEXTILES",
    16: "ARCHIVAL_MATERIAL"
}

web = webdriver.Chrome('coletaDados/chromedriver.exe')
web.get('http://apps.harvardartmuseums.org/art-explorer/')
web.implicitly_wait(30) # Carrega o site

time.sleep(5) # Espera
web.find_element_by_id('sets-button').click()

for obj in [9,10,11,14,15]: # Troca a classificação
    print(switcher.get(obj))
    for count in range(0,201): # Quantidade de imagem por classificação

        NaoTemImagem = True  
        while(NaoTemImagem): # apenas troca se a imagem não estava vazia.
            try:
                web.find_elements_by_class_name('interest-button')[obj].click()
                time.sleep(2) # Garantir que a imagem foi trocado

                img = web.find_element_by_xpath('//div[@id="random-set"]//img')
                src = img.get_attribute('src')

                NaoTemImagem = (src == "http://apps.harvardartmuseums.org/art-explorer/img/no_image.png")

                if(not NaoTemImagem): # A imagem foi encontrado?
                    wget.download(src, local + switcher.get(obj) +'/'+(str(count+1))+'.png')
            except:
                NaoTemImagem = True 
web.quit()