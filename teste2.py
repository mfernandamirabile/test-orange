from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # Importa a classe Service

'''
Esse código tem como objetivo 
testar a visualização e informações do projeto selecionado
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

# Testa a funcionalidade de visualizar o projeto
navegador.find_element('xpath', '//*[@id="root"]/main/div/div[3]/button[1]/img').click()
sleep(2)

# Verifica se nenhum elemento correspondente ao resultado da busca é encontrado
try:
    resultados = navegador.find_elements('xpath', '/html/body/div[19]/div[3]/div/div/img') # verifica se é a mesma imagem da pré-visualização 
    assert resultados is not None, "Imagem não é a mesma da pré-visualização."
    print('Caso de teste 002 obteve sucesso!')
try:
    resultados = navegador.find_elements('xpath', '/html/body/div[19]/div[3]/div/div/img') # verifica se é a mesma imagem da pré-visualização 
    assert resultados is not None, "Imagem não é a mesma da pré-visualização."
    print('Caso de teste 002 obteve sucesso!')
except AssertionError as e:
    print(str(e))