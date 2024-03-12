from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # Importa a classe Service

'''
Esse código tem como objetivo 
testar a impossibilidade de busca quando colocado o nome inválido na aba de “Buscar tags”
'''

servico = Service(ChromeDriverManager().install())  #Cria uma instância de Service
navegador = webdriver.Chrome(service=servico)

navegador.get('https://front-end-squad11.vercel.app/')

navegador.find_element('xpath',' //*[@id=":r0:"]').send_keys('teste1@hotmail.com') #emailLogin

sleep(2)

navegador.find_element('xpath',' //*[@id=":r1:"] ').send_keys('12345678') #senhaLogin

sleep(2)

navegador.find_element('xpath',' //*[@id=":r2:"]').click() #botaoentrar

sleep(5)


# Entra na aba Descobrir
navegador.find_element('xpath','//*[@id="root"]/main/header/div[1]/div/a[2]').click() 

sleep(5)

# Testa a impossibilidade de buscar po Nome do autor
navegador.find_element('xpath', '//*[@id="outlined-helperText"]').send_keys('Lucas')


sleep(2)
