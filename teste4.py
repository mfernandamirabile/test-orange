from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # Importa a classe Service
import os
import glob

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
navegador.find_element('xpath', '//*[@id="root"]/main/div/div[3]/button[1]/img').click()
sleep(5)

# Testa a funcionalidade de baixar o projeto
navegador.find_element('xpath', '/html/body/div[19]/div[3]/div/footer/a').click()
sleep(1)

# Diretório de downloads padrão
diretorio_downloads = os.path.expanduser('~') + '/Downloads/'

# Verifique se existe um arquivo com a extensão .crdownload (que indica que o download está em andamento)
try:
    arquivos_em_andamento = glob.glob(diretorio_downloads + '*.crdownload')
    assert arquivos_em_andamento, "O download não foi iniciado."
    print("Caso de teste 004 obteve sucesso!") #se houver o arquivo .crdownload, o caso de teste teve sucesso
except AssertionError as e:
    print(str(e))