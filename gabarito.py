# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Biblioteca para manipular o teclado e mouse
import pyautogui
#Biblioteca para manipular o tempo ao longo do tempo
import time

#Para pausar o código do pyautogui, só colocar o mouse no canto superior esquerdo por 5segundos.

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=685, y=451)
# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=955, y=638) # clique no botao de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
#Biblioteca para analisar e manipular dados
#Além de importar você pode renomear ele com "AS [NOME]"
import pandas as pd

#Existe também bibliotecas OPENPYXL que manipula arquivos CSV e XML. Com openpyxl, você pode acessar e manipular planilhas, células, linhas e colunas, bem como formatar células, gráficos e tabelas dinâmicas.
#Existe também a NUMPY que é uma biblioteca 

#Pandas deve lê o arquivo CSV
tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher (linha e coluna)
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo 
    pyautogui.write(str(tabela.loc[linha, "marca"])) #O tabela.lock é do pandas
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"] #Condicional para verificar se é NAN (not a number).
    if not pd.isna(obs): #Se não for branco, escreva, senão, vá para a próxima etapa
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
