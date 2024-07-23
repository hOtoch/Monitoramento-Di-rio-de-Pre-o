from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait # WAIT EXPLICITO
from selenium.common.exceptions import * # importa as exceptions
from selenium.webdriver.support import expected_conditions as ec
from utils import format_price_text
from datetime import date
import openpyxl

def iniciar_driver():

    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600','--incognito']

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1
    })

    for arg in arguments:
        chrome_options.add_argument(arg)

    # inicializando o webdriver
    driver = webdriver.Chrome(options=chrome_options)
    
    wait = WebDriverWait(
        driver,
        10, # tempo em que vai esperar ate lançar a exception
        poll_frequency= 1, # tempo em que ira tentar realizar uma ação
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )
    
    return driver, wait

driver, wait = iniciar_driver()

driver.get('https://www.google.com/search?q=playstation+5')


# Criando a planilha e o sheet Preços
workbook = openpyxl.Workbook()
del workbook['Sheet']
workbook.create_sheet('Preços')

sheet_precos = workbook['Preços']
sheet_precos.append(['Produto','Data atual','Valor','Link'])

# Pegando a data atual
date_formated = date.today().strftime("%d/%m/%Y")

# Elementos retornados pela pesquisa no google
elements_searched = wait.until(ec.visibility_of_all_elements_located((By.XPATH,"//div[@class='mnr-c c3mZkd pla-unit']")))

for element in elements_searched:
    link_element = element.find_element(By.XPATH,'./a[2]')
    name_element = element.find_element(By.XPATH,".//div[@class='rwVHAc itPOE']//span[@class='pymv4e']")
    
    link = link_element.get_attribute('href')
    name = name_element.text
    
    try: # Caso nao esteja em promoção
        price_element = element.find_element(By.XPATH,".//div[@class='rwVHAc itPOE']//span[@class='e10twf']")
    except Exception as e: # Caso esteja em promoção
        price_element = element.find_element(By.XPATH,".//div[@class='rwVHAc itPOE']//span[@class='e10twf ONTJqd']")
        
    price = format_price_text(price_element.text)
    
    sheet_precos.append([name,date_formated,price,link])

workbook.save("precos_play5.xlsx")
driver.close()
