import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pyxlsb import open_workbook as open_xlsb
import matplotlib.pyplot as plt
import sqlite3 


def respteste1():
    conn = sqlite3.connect('EstagioExpress.db')
    c = conn.cursor()
    # Pergunta 1
    contartudo = 'SELECT COUNT(peg1) FROM teste1'
    c.execute(contartudo)
    resultado = c.fetchall() 
    for i in resultado: 
        total = int(str(i[0]))
    peg1 = "SELECT (peg1) FROM teste1"
    c.execute(peg1)
    rows = c.fetchall()  
    palavra = rows
    contarlider = int(palavra.count(('Líder',)))
    contarliderada = int(palavra.count(('Liderada',)))
    conn.commit() 
    médialider = (contarlider/total)
    médialiderada = (contarliderada/total)

    # Pergunta 2
    teste = "SELECT AVG (peg2) FROM teste1"
    c.execute(teste)
    rows = c.fetchall() 
    for i in rows: 
        motivado = str(i[0])
    conn.commit() 

    # Pergunta 3
    teste = "SELECT AVG (peg3) FROM teste1"
    c.execute(teste)
    rows = c.fetchall() 
    for i in rows: 
        criativo = str(i[0])
    conn.commit() 

    # Pergunta 4
    teste = "SELECT AVG (peg4) FROM teste1"
    c.execute(teste)
    rows = c.fetchall() 
    for i in rows: 
        comunicar = str(i[0])
    conn.commit()

    # Pergunta 5
    teste = "SELECT AVG (peg5) FROM teste1"
    c.execute(teste)
    rows = c.fetchall() 
    for i in rows: 
        empatia = str(i[0])
    conn.commit() 

    # Pergunta 6
    teste = "SELECT AVG (peg6) FROM teste1"
    c.execute(teste)
    rows = c.fetchall() 
    for i in rows: 
        emocao = str(i[0]) 
    conn.commit() 

    # Pergunta 7
    contartudo = 'SELECT COUNT(peg7) FROM teste1'
    c.execute(contartudo)
    resultado = c.fetchall() 
    for i in resultado: 
        total7 = int(str(i[0]))
    peg7 = "SELECT (peg7) FROM teste1"
    c.execute(peg7)
    rows = c.fetchall()  
    palavra = rows
    contarprevinir = int(palavra.count(('Sim, para me previnir',)))
    contaralgumas = int(palavra.count(('Somente em algumas situações mais graves',)))
    contarnunca = int(palavra.count(('Nunca, viso solucionar o problema, independentemente se me afetar',)))
    conn.commit() 
    médiaprevinir = (contarprevinir/total7)
    médiaalgumas = (contaralgumas/total7)
    médianunca = (contarnunca/total7)

    st.markdown(""" <style> .font {                                          
                font-size:20px ; font-family: 'Cooper Black'; color: #FCD44C;} 
                </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Quantidade de pessoas que se consideram Líder ou Liderada</p>', unsafe_allow_html=True)
    fig = go.Figure()  
    fig.add_trace(go.Bar(x=('Líder','Liderado'), y=(médialider,médialiderada), name='Líder/Liderado'))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('<p class="font">De 0 (menos) a 100 (mais), o quanto o estagiário se considera:</p>', unsafe_allow_html=True)
    fig = go.Figure()  
    fig.add_trace(go.Bar(x=('Motivado e Produtivo em dias difíceis','Criativo','Comunicação ccom clareza e empatia','Empatia e Compreensão durante conflito','Lidar com emoções dos colegas'), y=(motivado,criativo,comunicar,empatia,emocao), name='Personalidade'))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('<p class="font">Diante de problema: se afasta criando distância mental</p>', unsafe_allow_html=True)
    fig = go.Figure()  
    fig.add_trace(go.Bar(x=("Sim, para me previnir","Somente em algumas situações mais graves","Nunca, viso solucionar o problema, independentemente se me afetar"), y=(médiaprevinir,médiaalgumas,médianunca), name='Ação diante de problema'))
    st.plotly_chart(fig, use_container_width=True)

    st.write('Veja abaixo a tabela de dados com as respostas de cada  estagiário')
    tabela= "SELECT * FROM teste1"
    c.execute(tabela)
    resultado = c.fetchall()
    df = pd.DataFrame(resultado, columns=['Líder/Liderado','Motivado e Produtivo nos dias difíceis','Criativo','Comunicação com clareza e empatia','Empatia e compreensão em situações de conflito','Lidar bem com as emoções dos colegas','Diante de problema: se afasta criando distância mental'])
    st.write(df)
    conn.commit() 
if __name__ == '__main__':
	respteste1()
        