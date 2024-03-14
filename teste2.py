from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # Importa a classe Service
from selenium.webdriver.common.by import By

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
sleep(7)


# Entra na aba Descobrir
navegador.find_element('xpath','//*[@id="root"]/main/header/div[1]/div/a[2]').click() 
sleep(5)

# Testa a funcionalidade de visualizar o projeto
div_projetos = navegador.find_element('xpath', '//*[@id="root"]/main/div/div[3]')#localiza a div que contém os projetos
primeiro_elemento = div_projetos.find_element('xpath', './*[1]')
sleep(5)

# Obtém o src da imagem de pré-visualização
img_primeiro_elemento = primeiro_elemento.find_element('xpath', './/img')
src_pre_visualizacao = img_primeiro_elemento.get_attribute('src')
sleep(2)

# Obtém o nome do autor e data da pré-visualização do primeiro elemento
div1 = primeiro_elemento.find_element('xpath', './/div')
div2 = div1.find_element('xpath', './/div')
nome_pre_visualizacao = div2.find_element('xpath', './/p').get_attribute('innerText')
sleep(3)

# Testa a funcionalidade de visualizar o projeto
primeiro_elemento.click()
sleep(5)

# Obtém o src da imagem do pop-up
src_pop_up = navegador.find_element('xpath', 'html/body//div[last()]/div[3]/div/div/img').get_attribute('src') #como a div do primeiro elemento muda a depnder de quantos projetos tem, foi acrescentado o [last()] para buscar sempre a última div, que corresponde ao primeiro projeto aparente
sleep(2)

# Obtém o nome do autor e data do pop up
nome_pop_up = navegador.find_element('xpath', '/html/body//div[last()]/div[3]/div/div/div/div[1]/p').get_attribute('innerText')

# verifica se a imagem, nome a data da pré-visualização são os mesmos do pop-up
try:
    # Compara os srcs
    assert src_pre_visualizacao == src_pop_up, "As imagens de pré-visualização e do pop-up são diferentes."
    print('Imagens são compatíveis')
    assert nome_pre_visualizacao == nome_pop_up, "Os nomes e as datas de pré-visualização e do pop-up são diferentes."
    print('Nomes e datas são compatíveis', '\nNome e data pré-visualização: ', nome_pre_visualizacao, '\nNome e data do pop up: ', nome_pop_up)
    print('Caso de teste 002 obteve sucesso!')
except AssertionError as e:
    print(str(e))