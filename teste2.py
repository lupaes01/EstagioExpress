import streamlit as st
import sqlite3 
import pandas as pd
import plotly.graph_objects as go
from pyxlsb import open_workbook as open_xlsb
import matplotlib.pyplot as plt


def respteste2():
    conn = sqlite3.connect('EstagioExpress.db')
    c = conn.cursor()
    contartudo = 'SELECT COUNT(peg8) FROM teste2'
    c.execute(contartudo)
    resultado = c.fetchall() 
    for i in resultado: 
        total = int(str(i[0]))

    # Pergunta 8
    peg8 = "SELECT (peg8) FROM teste2"
    c.execute(peg8)
    rows = c.fetchall()  
    palavra = rows
    resp18 = int(palavra.count(('Sempre',)))
    resp28 = int(palavra.count(('Algumas',)))
    resp38 = int(palavra.count(('Nunca',)))
    conn.commit() 
    média18 = (resp18/total)
    média28 = (resp28/total)
    média38 = (resp38/total)

    # Pergunta 9
    peg9 = "SELECT (peg9) FROM teste2"
    c.execute(peg9)
    rows = c.fetchall()  
    palavra = rows
    resp19 = int(palavra.count(('Sim, gosto de inovar',)))
    resp29 = int(palavra.count(('As vezes',)))
    resp39 = int(palavra.count(('Não, gosto de permanecer o padrão acostumado',)))
    conn.commit() 
    média19 = (resp19/total)
    média29 = (resp29/total)
    média39 = (resp39/total)

    # Pergunta 10
    peg10 = "SELECT (peg10) FROM teste2"
    c.execute(peg10)
    rows = c.fetchall()  
    palavra = rows
    resp110 = int(palavra.count(('Sim',)))
    resp210 = int(palavra.count(('Depende da mudança',)))
    resp310 = int(palavra.count(('Não',)))
    conn.commit() 
    média110 = (resp110/total)
    média210 = (resp210/total)
    média310 = (resp310/total)

    # Pergunta 11
    peg11 = "SELECT (peg11) FROM teste2"
    c.execute(peg11)
    rows = c.fetchall()  
    palavra = rows
    resp111 = int(palavra.count(('Rotineiro',)))
    resp211 = int(palavra.count(('Multifuncional',)))
    conn.commit() 
    média111 = (resp111/total)
    média211 = (resp211/total)

    # Pergunta 12
    peg12 = "SELECT (peg12) FROM teste2"
    c.execute(peg12)
    rows = c.fetchall()  
    palavra = rows
    resp112 = int(palavra.count(('Individuais',)))
    resp212 = int(palavra.count(('Colaborativos',)))
    conn.commit() 
    média112 = (resp112/total)
    média212 = (resp212/total)

    # Pergunta 13
    peg13 = "SELECT (peg13) FROM teste2"
    c.execute(peg13)
    rows = c.fetchall()  
    palavra = rows
    resp113 = int(palavra.count(('Normalmente sim',)))
    resp213 = int(palavra.count(('Varia muito de situação para situação',)))
    resp313 = int(palavra.count(('Tenho dificuldade',)))
    conn.commit() 
    média113 = (resp113/total)
    média213 = (resp213/total)
    média313 = (resp313/total)
    
    # Pergunta 14
    peg14 = "SELECT (peg14) FROM teste2"
    c.execute(peg14)
    rows = c.fetchall()  
    palavra = rows
    resp114 = int(palavra.count(('Sim',)))
    resp214 = int(palavra.count(('Não',)))
    conn.commit() 
    média114 = (resp114/total)
    média214 = (resp214/total)

    # Pergunta 15
    peg15 = "SELECT (peg15) FROM teste2"
    c.execute(peg15)
    rows = c.fetchall()  
    palavra = rows
    resp115 = int(palavra.count(('Sim, tenho facilidade',)))
    resp215 = int(palavra.count(('Não, tenho dificuldade',)))
    conn.commit() 
    média115 = (resp115/total)
    média215 = (resp215/total)

    # Pergunta 16
    peg16 = "SELECT (peg16) FROM teste2"
    c.execute(peg16)
    rows = c.fetchall()  
    palavra = rows
    resp116 = int(palavra.count(('Não entrego',)))
    resp216 = int(palavra.count(('Entrego mal feito',)))
    resp316 = int(palavra.count(('Entrego o trabalho em atraso',)))
    conn.commit() 
    média116 = (resp116/total)
    média216 = (resp216/total)
    média316 = (resp316/total)


    st.markdown(""" <style> .font {                                          
                font-size:20px ; font-family: 'Cooper Black'; color: #FCD44C;} 
                </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Participar de atividades extracurriculares</p>', unsafe_allow_html=True)
    fig = go.Figure()  
    fig.add_trace(go.Bar(x=('Sempre','Algumas','Nunca'), y=(média18,média28,média38), name='Respostas'))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<p class="font">Buscar novas alternativas para resolver problemas</p>', unsafe_allow_html=True)
    fig = go.Figure()  
    fig.add_trace(go.Bar(x=('Sim, gosto de inovar','As vezes','Não, gosto de permanecer o padrão acostumado'), y=(média19,média29,média39), name='Respostas'))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<p class="font">Adapta a mudanças inesperadas</p>', unsafe_allow_html=True)
    fig = go.Figure()  
    fig.add_trace(go.Bar(x=('Sim','Depende da mudança','Não'), y=(média110,média210,média310), name='Respostas'))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<p class="font">Trabalho rotineiro ou multifuncional</p>', unsafe_allow_html=True)
    fig = go.Figure()  
    fig.add_trace(go.Bar(x=('Rotineiro','Multifuncional'), y=(média111,média211), name='Respostas'))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<p class="font">Projetos individuais ou colaborativos</p>', unsafe_allow_html=True)
    fig = go.Figure()  
    fig.add_trace(go.Bar(x=('Individuais','Colaborativos'), y=(média112,média212), name='Respostas'))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<p class="font">Se preparar para situações novas ou desconhecidas</p>', unsafe_allow_html=True)
    fig = go.Figure()  
    fig.add_trace(go.Bar(x=('Normalmente sim','Varia muito de situação para situação','Tenho dificuldade'), y=(média113,média213,média313), name='Respostas'))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<p class="font">Se adapta em trabalho com pessoas com estilos de trabalho diferentes</p>', unsafe_allow_html=True)
    fig = go.Figure()  
    fig.add_trace(go.Bar(x=('Sim','Não'), y=(média114,média214), name='Respostas'))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<p class="font">Se adapta a trabalhar com prazos apertados ou com cronogramas curtos</p>', unsafe_allow_html=True)
    fig = go.Figure()  
    fig.add_trace(go.Bar(x=('Sim, tenho facilidade','Não, tenho dificuldade'), y=(média115,média215), name='Respostas'))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<p class="font">SITUAÇÃO: Você teve algum problema particular e não vai conseguir entregar o trabalho dentro do prazo, o que faz?</p>', unsafe_allow_html=True)
    fig = go.Figure()  
    fig.add_trace(go.Bar(x=('Não entrego', 'Entrego mal feito', 'Entrego o trabalho em atraso'), y=(média116,média216,média316), name='Respostas'))
    st.plotly_chart(fig, use_container_width=True)

    st.write('Veja abaixo a tabela de dados com as respostas de cada  estagiário')
    tabela= "SELECT * FROM teste2"
    c.execute(tabela)
    resultado = c.fetchall()
    df = pd.DataFrame(resultado, columns=['Atividade Extracurricular','Resolver problemas','Mudanças inesperadas','Trabalho','Projetos','Situações novas','Adapta a estilos de trabalho', 'Adata a prazos curtos','Situação'])
    st.write(df)
    conn.commit() 
if __name__ == '__main__':
	respteste2()
        


