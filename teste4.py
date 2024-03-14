from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # Importa a classe Service
import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Esse código tem como objetivo 
testar o download do projeto selecionado
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
div_projetos = navegador.find_element('xpath', '//*[@id="root"]/main/div/div[3]')#localiza a div que contém os projetos
primeiro_elemento = div_projetos.find_element('xpath', './*[1]').click()#seleciona o primeiro elemento filho dentro da div
sleep(5)

# Testa a funcionalidade de baixar o projeto
div_pop_up = navegador.find_element('xpath', '/html/body/div[20]/div[3]/div') #localiza a div que contém o pop up
footer_pop_up = navegador.find_element('xpath', '/html/body/div[20]/div[3]/div/footer') #localiza o footer do pop up
link_download = footer_pop_up.find_element('xpath', './/a').click() #seleciona o link de download dentro do footer pop up
sleep(2) 

# Diretório de downloads padrão
diretorio_downloads = os.path.expanduser('~') + '/Downloads/'

# Verifique se existe um arquivo com a extensão .crdownload (que indica que o download está em andamento)
try:
    arquivos_em_andamento = glob.glob(diretorio_downloads + '*.crdownload')
    assert arquivos_em_andamento, "O download não foi iniciado."
    print("Caso de teste 004 obteve sucesso!") #se houver o arquivo .crdownload, o caso de teste teve sucesso
except AssertionError as e:
    print(str(e))