'''
Introdução
Objetivo dessa atividade foi gerar 3 graficos distintos utiliando apenas dados de um mesmo Banco de Dados (BD).
o codigo deve utilizar fonte de Banco de Dados um arquivo CSV existente em dominio real e atual.
para esse codigo foi utilizado os graficos "Barra", "Linha" e TreeMap. 
o aquivo CSV utilizado foi o de volume mensal dos manaciais da Paraíba.
os dados do arquivo CSV utilizados foram "Bacia", "Açude", Município", "Capacidade Máxima", "Volume Atual".
o codigo alem de criar os graficos foi criada uma interface grafica inical com botoes no qual o usiario pode clinicar
e cada botão direciona e cria um grafico diferente, dentre os 3 selecionados para esta atividade.
'''
# Inicar o codigo realizando as importaçoes de bibliotecas(index) usando o PIP(Python Index Package)
import PySimpleGUI as sg
import requests
from tkinter import *
import numpy as np
import pandas as pd
import squarify
import matplotlib.pyplot as plt
import plotly.express as px
import networkx as nx

#site fonte (http://www.aesa.pb.gov.br/aesa-website/monitoramento/volume-mensal/?tipo=anterior) Acesso em(23/052023 15:37)


# Tratamento dos arquivo CSV - transformando o arquivo em "dataframe"
arquivo = (r'C:\Users\fisio\OneDrive\Área de Trabalho\CURSO PYTHON\Faculdade\arquivos_csv\Açudes_paraiba.csv')  # Insira o nome do seu arquivo CSV aqui
dataframe = pd.read_csv(arquivo)

# Leitura do arquivo CVS 
dataframe.head()

# Definição do grafico em Barras
def Bar_acude():

    dados_grafico = dataframe[['Açude','Bacia', 'Volume Atual', 'Capac. Máxima']]
    dados_agrupados = dados_grafico.groupby('Bacia').sum()
    dados_agrupados.plot(kind='bar')
    plt.xlabel('Bacia')
    plt.ylabel('Capac. Máxima')
    plt.ylabel('Volume Atual')
    plt.ylabel('Açude')
    plt.title('Gráfico do Volume dos Açudes - PB')
    plt.xticks(rotation=45, ha='right')
    plt.show()
    
# Definção do grafico em Linha
def Line_Acude():
    dados_grafico = dataframe[['Açude','Bacia', 'Volume Atual', 'Capac. Máxima']]
    dados_agrupados = dados_grafico.groupby('Bacia').sum()
    dados_agrupados.plot(kind='line')
    plt.xlabel('Bacia')
    plt.ylabel('Capac. Máxima')
    plt.ylabel('Volume Atual')
    plt.ylabel('Açude')
    plt.title('Gráfico do Volume das Bacias - PB')
    plt.xticks(rotation=45, ha='right')
    plt.show()

# Definição do grafico em TreeMap
def Treemap_Acude():
    fig = px.treemap(dataframe, path=['Bacia', 'Município','Açude'], values='Capac. Máxima', color='Volume Atual')
    fig.update_layout(title_text= 'TreeMap das Bacias Paraibanas -  (Bacias - Municípios - Açudes / Capacidade Máxima x Volume Atual)')
    fig.show()
    
janela = Tk()
janela.title('Sistema de Avalição Grafica dos Bacias - PB')
janela.geometry('700x90')

# Texto Orientação para botão de Graficos em Barras
texto_orientacao = Label(janela, text = 'Clique em "Bacia - Barras" para ver o Grafico em Barras dos Volumes Maximo e Volumes atuais')
texto_orientacao.grid(column=0,row=0)

# Texto Orientação para botão de Graficos em Linha
texto_orientacao = Label(janela, text = 'Clique em "Bacia - Linha" para ver o Grafico em Linha dos Volumes Maximo e Volumes atuais')
texto_orientacao.grid(column=0,row=3)

# Texto Orientação para botão de Graficos em treemap
texto_orientacao = Label(janela, text = 'Clique em "Bacia - Treemap" para ver o Grafico em Treemap dos Volumes Máximos e Volumes atuais ')
texto_orientacao.grid(column=0,row=6)

# Configuração do Butão para Graficos em Barras
botao = Button(janela,text='Bacia - Barras', command= Bar_acude)
botao.grid(column=1, row=0)

# Configuração do Butão para Graficos em Linha
botao2 = Button(janela,text='Bacia - Linha', command=Line_Acude)
botao2.grid(column=1, row=3)

# Configuração do Butão para Graficos em TreeMap
botao3 = Button(janela,text='Bacia - Treemap', command=Treemap_Acude)
botao3.grid(column=1, row=6)

# Gerador de Janela
janela.mainloop()  