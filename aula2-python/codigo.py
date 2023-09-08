# Passo a passo do Projeto
# Passo 1: Entar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivo/login

import pyautogui
import time

# pyautogui.write ->escreve um texto
# pyautogui.press -> apetar 1 tecla
# pyautogui -> clicar em algun lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.3

# abri o navegador (chome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2 : Fazer login
# selecionar o campo de email
pyautogui.click(x=795, y=502)
# escrever o seu email
pyautogui.write("danielsplira@gmail.com")
pyautogui.press("tab")  # passando pro próximo campo
pyautogui.write("dsp128962")
pyautogui.click(x=123, y=123)  # clique no botão de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastar
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastar um produto
for linha in tabela.index:
    # clicar no campo de ódigo
    pyautogui.click(x=1868, y=122)
    # Pegar da tabla o valor do campo que a gente quer preecher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # Passa para o proximo campo
    pyautogui.press("tab")
    # Passa para o proximo campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
     pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")  # cadastar o produto (boão enviar)
   # dar scroll de tudo para cima
    pyautogui.scroll(5000)
   # Passo 5: Repetir o processo de cadastro até o fim
