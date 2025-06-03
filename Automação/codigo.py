import pyautogui as pg
import time 
import pandas

#pyautogui.click -> clicar em algum lugar
#pyautogui.press -> apertar 1 tecla
#pyautogui.write -> escreve um texto
#pyautogui.hotkey -> apertar uma combinação de teclas

pg.PAUSE = 0.3

#Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Abrir o chrome

pg.press('win')
pg.write('chrome')
pg.press('enter')

#digitar e entrar no site

pg.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pg.press('enter')

time.sleep(1)

#Passo 2: Login 

pg.click(x=762, y=426)
pg.write('bablabla@gmail.com')
pg.click(x=777, y=524)
pg.write('senha123')
pg.click(x=955, y=583)

# Passo 3: importar base de dados

tabela = pandas.read_csv('produtos.csv')

# Passo 4: registro de dados no site

for linha in tabela.index:
    pg.click(x=749, y=309)
    codigo = tabela.loc[linha, 'codigo']
    pg.write(codigo)

    pg.press('tab')
    marca = tabela.loc[linha, 'marca']
    pg.write(marca)

    pg.press('tab')
    tipo = tabela.loc[linha, 'tipo']
    pg.write(tipo)

    pg.press('tab')
    categoria = str(tabela.loc[linha, 'categoria'])
    pg.write(categoria)

    pg.press('tab')
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pg.write(preco_unitario)

    pg.press('tab')
    custo = str(tabela.loc[linha, 'custo'])
    pg.write(custo)

    pg.press('tab')
    obs = str(tabela.loc[linha, 'obs']) 

    if obs != 'nan':
        pg.write(obs)

    pg.press('tab')
    pg.press('enter')

    pg.scroll(10000)

    




 
