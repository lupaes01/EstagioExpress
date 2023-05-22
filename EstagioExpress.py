import streamlit as st
from PIL import Image
import string
import random
import smtplib
import email.message
server = smtplib.SMTP('smtp.gmail.com:587')
from dotenv import load_dotenv
import os
import plotly.graph_objects as go
import pandas as pd
from pyxlsb import open_workbook as open_xlsb
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Criar senha secreta
import hashlib
def make_hashes(passwordempresa):
	return hashlib.sha256(str.encode(passwordempresa)).hexdigest()
def make_hashes(passwordestag):
	return hashlib.sha256(str.encode(passwordestag)).hexdigest()
def check_hashes(passwordempresa,hashed_text):
	if make_hashes(passwordempresa) == hashed_text:
		return hashed_text
	return False
def check_hashes(passwordestag,hashed_text):
	if make_hashes(passwordestag) == hashed_text:
		return hashed_text
	return False

# Salvar dados no banco de dados
import sqlite3 
conn = sqlite3.connect('EstagioExpress.db')
c = conn.cursor()
def create_userempresa():
	c.execute('CREATE TABLE IF NOT EXISTS userempresa(usernameempresa TEXT, passwordempresa TEXT)')
def create_userestag():
	c.execute('CREATE TABLE IF NOT EXISTS userestag(email TEXT, usernameestag TEXT,passwordestag TEXT)')
def create_empresacod():
	c.execute('CREATE TABLE IF NOT EXISTS empresacod(empresacod TEXT)')
def create_empresa():
	c.execute('CREATE TABLE IF NOT EXISTS empresa(empresa TEXT, ramo TEXT, qtd_estag integer, emaildestino TEXT, empresacod TEXT)')
def create_teste1():
	c.execute('CREATE TABLE IF NOT EXISTS teste1(peg1 TEXT,peg2 integer,peg3 integer,peg4 integer,peg5 integer,peg6 integer,peg7 TEXT)')
def create_teste2():
	c.execute('CREATE TABLE IF NOT EXISTS teste2(peg8 TEXT,peg9 TEXT,peg10 TEXT,peg11 TEXT,peg12 TEXT,peg13 TEXT,peg14 TEXT,peg15 TEXT,peg16 TEXT)')
def create_entrevista():
    c.execute('CREATE TABLE IF NOT EXISTS RespEntrevista(importante TEXT,destaque TEXT,inconveniente TEXT,desclassificado TEXT)')

def add_userempresa(usernameempresa,passwordempresa):
	c.execute('INSERT INTO userempresa(usernameempresa,passwordempresa) VALUES (?,?)',(usernameempresa,passwordempresa))
	conn.commit()
def add_userestag(emailestag,usernameestag,passwordestag):
	c.execute('INSERT INTO userestag(email,usernameestag,passwordestag) VALUES (?,?,?)',(emailestag,usernameestag,passwordestag))
	conn.commit()
def add_empresacod(empresacod):
    c.execute('INSERT INTO empresacod(empresacod) VALUES (?)',(empresacod,))
    conn.commit()
def add_empresa (empresa,ramo,estag,emaildestino,empresacod):
    c.execute('INSERT INTO empresa(empresa,ramo,qtd_estag,emaildestino,empresacod) VALUES (?,?,?,?,?)',(empresa,ramo,estag,emaildestino,empresacod))
    conn.commit()
def add_teste1(peg1,peg2,peg3,peg4,peg5,peg6,peg7):
	c.execute('INSERT INTO teste1(peg1,peg2,peg3,peg4,peg5,peg6,peg7) VALUES (?,?,?,?,?,?,?)',(peg1,peg2,peg3,peg4,peg5,peg6,peg7))
	conn.commit()
def add_teste2(peg8,peg9,peg10,peg11,peg12,peg13,peg14,peg15,peg16):
	c.execute('INSERT INTO teste2(peg8,peg9,peg10,peg11,peg12,peg13,peg14,peg15,peg16) VALUES (?,?,?,?,?,?,?,?,?)',(peg8,peg9,peg10,peg11,peg12,peg13,peg14,peg15,peg16))
	conn.commit()
def add_entrevista(importante,destaque,inconveniente,desclassificado):
    c.execute('INSERT INTO RespEntrevista(importante,destaque,inconveniente,desclassificado) VALUES (?,?,?,?)',(importante,destaque,inconveniente,desclassificado))
    conn.commit()

def view_resp1():
	c.execute('SELECT * FROM teste1')
	data = c.fetchall()
	return data
def view_resp1():
	c.execute('SELECT * FROM teste2')
	data = c.fetchall()
	return data

def login_userempresa(usernameempresa,passwordempresa):
	c.execute('SELECT * FROM userempresa WHERE usernameempresa =? AND passwordempresa = ?',(usernameempresa,passwordempresa))
	data = c.fetchall()
	return data
def login_userestag(usernameestag,passwordestag):
	c.execute('SELECT * FROM userestag WHERE usernameestag =? AND passwordestag = ?',(usernameestag,passwordestag))
	data = c.fetchall()
	return data
def checaempresacod(empresacod):
	c.execute('SELECT * FROM empresacod WHERE empresacod =?',(empresacod,))
	data = c.fetchall()
	return data
def checaempresa(empresa,emaildestino,empresacod):
	c.execute('SELECT * FROM empresa WHERE empresa =? AND emaildestino =? AND empresacod =?',(empresa, emaildestino,empresacod))
	data = c.fetchall()
	return data

def excluir_empresa(usernameempresa,passwordempresa):
	c.execute('DELETE from userempresa WHERE usernameempresa =? AND passwordempresa =?',(usernameempresa,passwordempresa))
	conn.commit()
	conn.close()
def excluir_estag(usernameestag,passwordestag):
	c.execute('DELETE from userestag WHERE usernameestag =? AND passwordestag =?',(usernameestag,passwordestag))
	conn.commit()
	conn.close()

# Funções vaga de estágio
def create_vaga():
	c.execute('CREATE TABLE IF NOT EXISTS Vagas(titulo TEXT, descricao TEXT, local TEX, requer TEXT,datainicio DATETIME, datafim DATETIME, contato TEXT, carac1 INTEGER, carac2 INTEGER,carac3 INTEGER, carac4 INTEGER, carac5 INTEGER, carac6 INTEGER,img)')
def add_vaga(name, descricao,local, requer,datainicio, datafim, contato, carac1, carac2,carac3, carac4, carac5, carac6,empPhoto):
	c.execute('INSERT INTO Vagas(titulo, descricao,local, requer,datainicio, datafim, contato, carac1, carac2,carac3, carac4, carac5, carac6,img) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(name, descricao,local, requer,datainicio, datafim, contato, carac1, carac2,carac3, carac4, carac5, carac6,empPhoto))
	conn.commit()

# Função para converter imagem em dados binários
def convertToBinaryData(filename):  
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData
def insertBLOB(name,descricao,local, requer,datainicio,datafim, contato, carac1, carac2,carac3, carac4, carac5, carac6,photo):
    try:                  
        empPhoto = convertToBinaryData(photo)          
        create_vaga()
        add_vaga(name, descricao, local, requer,datainicio,datafim, contato, carac1, carac2,carac3, carac4, carac5, carac6, empPhoto)          
    except sqlite3.Error as error:
        print("Falha ao inserir dados blob na tabela sqlite", error)

from LayoutEmp import layout_email_empresa
from LayoutEstag import layout_email_estagiario
from teste1 import respteste1
from teste2 import respteste2





def main():
    st.markdown(""" <style> .font {                                          
	        font-size:45px ; font-family: 'Cooper Black'; color: #FCD44C;} 
			</style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">SEJA BEM VINDO AO ESTÁGIO EXPRESS</p>', unsafe_allow_html=True)
    logo = Image.open('logo (1).png')
    st.sidebar.image(logo,  width=270)
    st.sidebar.text("Escolha a área em que deseja entrar")
    menu = ["Cadastre-se","Área do Estagiário","Área da Empresa"]
    pag = st.sidebar.selectbox("Menu",menu)



    if pag == "Cadastre-se":
        st.subheader("Cadastre-se para ter acesso a todos os benefícios do Estágio Express")
        funcao = ["Usuário Estagiário","Cadastro da Empresa","Usuário Empresa"]
        selecionar = st.sidebar.selectbox("Selecione a sua função",funcao)
        if selecionar == "Usuário Estagiário":
            new_emailestag = st.text_input("Email")
            new_userestag = st.text_input("Nome")
            new_passwordestag = st.text_input("Senha",type='password')
            if st.button("Cadastre-se"):
                create_userestag()
                add_userestag(new_emailestag,new_userestag,make_hashes(new_passwordestag))
                st.success("Seu cadastro foi realizado com sucesso")
                st.info("Agora é só entrar na função que pertence")
                # Enviando email ded boas vindas
                msg = email.message.Message()
                msg['Subject'] = "SEJA BEM VINDO, {}".format(new_userestag)
                load_dotenv()
                msg['From'] = os.environ["email_meu"]
                msg['To'] = new_emailestag
                password = os.environ["senha_minha"]
                msg.add_header('Content-Type', 'text/html')
                msg.set_payload(layout_email_estagiario)
                s = smtplib.SMTP('smtp.gmail.com: 587')
                s.starttls()
                s.login(msg['From'], password)
                s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        if selecionar == "Cadastro da Empresa":
            st.write('Ficamos extremamente felizes em saber que sentiu interesse em fazer parte do time Estágio Express')
            with st.form ("Cadastre-se"):
                empresa = st.text_input(label='Nome da Empresa',placeholder="Escreva aqui o nome da empresa")
                ramo = st.selectbox(label = "Ramo da Empresa", options = ['Indústria', 'Comércio', 'Serviço','Outro'])
                estag = st.number_input(label = "Quantidade de estagiários presentes na empresa", format = "%d",step=1)
                emaildestino =st.text_input(label='Email',placeholder="Coloque um email para cadastro")
                submit_res = st.form_submit_button(label='Enviar')
                if submit_res:
                    def x (size=6, chars=string.ascii_uppercase + string.digits):
                        return ''.join(random.choice(chars) for _ in range(size))
                    empresacod = x()
                    cod = """
                    Código de acesso: {} \n
                    """.format(empresacod)
                    # ENVIANDO O EMAIL 
                    email_content = cod + layout_email_empresa
                    msg = email.message.Message()
                    msg['Subject'] = "SEJA BEM VINDO, {}".format(empresa)
                    load_dotenv()
                    msg['From'] = os.environ["email_meu"]
                    msg['To'] = emaildestino
                    password = os.environ["senha_minha"]
                    msg.add_header('Content-Type', 'text/html')
                    msg.set_payload(email_content)
                    s = smtplib.SMTP('smtp.gmail.com: 587')
                    s.starttls()
                    s.login(msg['From'], password)
                    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
                    st.info('Será enviado um código de acesso ao email cadastrado!')
                    create_empresa()
                    add_empresa(empresa,ramo,estag,emaildestino,empresacod)
                    create_empresacod()
                    add_empresacod(empresacod,)
        if selecionar == "Usuário Empresa":
            empresacod = st.sidebar.text_input("Insira o código da empresa (caso não tenha, entre primeiro na aba Cadastro da Empresa e preencha as informações)")
            if st.sidebar.checkbox("Verificar código"):
                create_empresa()
                resultado = checaempresacod(empresacod,)
                if resultado:
                    new_userempresa = st.text_input("Nome")
                    new_passwordempresa = st.text_input("Senha",type='password')
                    if st.button("Cadastre-se"):
                        create_userempresa()
                        add_userempresa(new_userempresa,make_hashes(new_passwordempresa))
                        st.success("Seu cadastro foi realizado com sucesso")
                        st.info("Agora é só entrar na função que pertence")
                else:
                    st.warning("Código incorreto")


    if pag == "Área do Estagiário":
        st.subheader("Página do Estagiário")
        usernameestag = st.sidebar.text_input("Nome")
        passwordestag = st.sidebar.text_input("Senha",type='password')
        if st.sidebar.checkbox("Logar"):
            create_userestag()
            hashed_pswd = make_hashes(passwordestag)
            result = login_userestag(usernameestag,check_hashes(passwordestag,hashed_pswd))
            if result:
                st.success("Bem vindo, {}".format(usernameestag))
                task = st.selectbox("Selecione o que deseja",["Vagas de Estágio","Teste de Personalidade e Cognitivo","Dicas de Entrevista e Vídeos Preparatórios","Como montar o seu currículo da melhor forma","Excluir conta"])
                if task == "Vagas de Estágio":
                    st.write("Encontre aqui o Estágio ideal para voce!")
                    # Converter dados binários em formato legível por humanos
                    def convert_data(data, file_name):
                        with open(file_name, 'wb') as file:
                            file.write(data)
                        img = Image.open(file_name)
                        st.image(img) 
                    try:
                        con = sqlite3.connect('EstagioExpress.db')
                        cursor = con.cursor()
                        query = "SELECT * FROM Vagas"
                        cursor.execute(query)
                        records = cursor.fetchall()
                        for row in records:    
                            # armazenando linha[0] na variável de nome
                            name = row[0]
                            descricao = row[1]
                            local = row[2]
                            requer = row[3]
                            datainicio = row[4]
                            datafim = row[5]
                            contato = row[6]
                            criatividade = row[7]
                            lideranca = row[8]
                            motivacao = row[9]
                            formacao = row[10]
                            experiencia = row[11]
                            trabequipe = row[12]                           
                            st.title(name)
                            st.write(descricao)
                            st.write('Local do estágio: {}'.format(local))
                            st.write('Requerimentos para inscrição: {}'.format(requer))
                            col1, col2 = st.columns(2)
                            with col1:
                                st.write('Início das incrições: {}'.format(datainicio))
                            with col2:
                                st.write('Fim das incrições: {}'.format(datainicio))
                            st.write('Meios para contato {}'.format(contato))
                            st.markdown(""" <style> .font {                                          
                                        font-size:30px ; font-family: 'Cooper Black'; color: #FCD44C;} 
                                        </style> """, unsafe_allow_html=True)
                            st.markdown('<p class="font">Características valorizadas na contratação, de 0 (menos valoziada) até 100 (muito valorizada)</p>', unsafe_allow_html=True)
                            # Fazer gráfico barras com características mais valorizadas na contratação
                            fig = go.Figure()  
                            fig.add_trace(go.Bar(x=('Ter criatividade no trabalho','Ter espírito de liderança','Ser motivado no trabalho','Curso superior (in)completa','Ter experiência na área da vaga','Saber trabalhar em equipe'), y=(criatividade,lideranca,motivacao,formacao,experiencia,trabequipe), name='caracteristicas_valorizadas'))
                            st.plotly_chart(fig, use_container_width=True)
                            # armazenar imagem (atualmente em formato binário)
                            col1, col2, col3 = st.columns([1,6,1])
                            with col1:
                                st.write("")
                            with col2:
                                image = row[13]
                                convert_data(image, "logo.png")
                            with col3:
                                st.write("")
                        # Se não tivermos nenhum registro (vaga de estágio) em nosso banco de dados:
                        if len(records) == 0:
                            st.write("Desculpe! Não exitem vagas de estágio disponíveis no momento. Pedimos que aguarde mais um pouco.")
                    except sqlite3.Error as error:
                        print(format(error))
                    finally:
                        if con:
                            con.close()
                            print("A conexão SQLite está fechada")	
                if task == "Teste de Personalidade e Cognitivo":
                    st.write("Faça alguns de nossos testes para te ajudar no reconhecimento da sua personalidade e do seu cognitivo para um ambiente de trabalho")
                    testes = st.selectbox("Selecione o teste desejado",['','Teste 1','Teste 2'])
                    if testes == '':
                        col1, col2, col3 = st.columns([1,6,1])
                        with col1:
                            st.write("")
                        with col2:
                            imagem = Image.open('teste.png')
                            st.image(imagem)
                        with col3:
                            st.write("")
                    if testes == 'Teste 1':
                        with st.form('Teste Autoconhecimento'):
                            peg1 = st.selectbox("Você se considera uma pessoa líder ou liderada?",['Líder','Liderada'])
                            peg2 = st.slider("De 0 (pouco) a 100 (muito), o quão você se mantém motivado e produtivo em dias difíceis")
                            peg3 = st.slider("De 0 (pouco) a 100 (muito), o quão você se considera criativo?")
                            peg4 = st.slider("De 0 (pouco) a 100 (muito), o quão você acredita se comunicar com clareza e empatia no ambiente de trabalho?")
                            peg5 = st.slider("De 0 (pouco) a 100 (muito), o quão você demonstra empatia e compreensão em situações de conflito no trabalho?")
                            peg6 = st.slider("De 0 (pouco) a 100 (muito), o quão você acredita lidar bem com as emoções dos seus colegas de trabalho?")
                            peg7 = st.selectbox("Quando está perante um problema, você se afasta um pouco, criando alguma distância mental entre você e o problema?",["Sim, para me previnir","Somente em algumas situações mais graves","Nunca, viso solucionar o problema, independentemente se me afetar"])
                            if st.form_submit_button('Enviar resposta'):
                                st.success('Resposta registrada com sucesso')
                                create_teste1()
                                add_teste1(peg1,peg2,peg3,peg4,peg5,peg6,peg7)
                    if testes == 'Teste 2':
                        with st.form('Você + Trabalho'):
                            peg8 = st.selectbox('Você busca participar de atividades extracurriculares na universidade?',['Sempre','Algumas','Nunca'])
                            peg9 = st.selectbox('Você gosta de buscar novas alternativas para resolver problemas?',['Sim, gosto de inovar','As vezes','Não, gosto de permanecer o padrão acostumado'])
                            peg10 = st.selectbox('Você se adapta bem a mudanças inesperadas no trabalho?',['Sim','Depende da mudança','Não'])
                            peg11 = st.selectbox('Você prefere um trabalho rotineiro a um multifuncional?',['Rotineiro','Multifuncional'])
                            peg12 = st.selectbox('Você prefere trabalhar em projetos individuais ou colaborativos?',['Individuais','Colaborativos'])
                            peg13 = st.selectbox('Você tem facilidade em se preparar para situações novas ou desconhecidas?',['Normalmente sim','Varia muito de situação para situação','Tenho dificuldade'])
                            peg14 = st.selectbox('Você se adapta em trabalho com pessoas com estilos de trabalho diferentes dos seus?',['Sim','Não'])
                            peg15 = st.selectbox('Você se adapta a trabalhar com prazos apertados ou com cronogramas curtos?',['Sim, tenho facilidade','Não, tenho dificuldade'])
                            peg16 = st.selectbox("Você teve algum problema particular e não vai conseguir entregar o trabalho dentro do prazo, o que você faz?", ['Não entrego', 'Entrego mal feito', 'Entrego o trabalho em atraso'])
                            if st.form_submit_button('Enviar resposta'):
                                st.success('Resposta registrada com sucesso')
                                create_teste2()
                                add_teste2(peg8,peg9,peg10,peg11,peg12,peg13,peg14,peg15,peg16)
                if task == "Dicas de Entrevista e Vídeos Preparatórios":
                    col1, col2, col3 = st.columns([1,6,1])
                    with col1:
                        st.write("")
                    with col2:
                        imagem = Image.open('fotoEntrevista.png')
                        st.image(imagem)
                    with col3:
                        st.write("")
                    st.markdown(""" <style> .font {                                          
                        font-size:30px ; font-family: 'Cooper Black'; color: #FCD44C;} 
                        </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">Respostas das empresas</p>', unsafe_allow_html=True)
                    st.write('Veja as respostas de algumas empresas com relação ao comportamento em uma entrevista de estágio')
                    def x():
                        all_summary = " ".join(s for s in summary)
                        stopwords = set(STOPWORDS)
                        stopwords.update(["da", "meu", "em", "de", "ao", "os","ser"])
                        wordcloud = WordCloud(stopwords=stopwords,
                                                                background_color="black",
                                                                width=1600, height=800).generate(all_summary)
                        fig, ax = plt.subplots(figsize=(10,6))
                        ax.imshow(wordcloud, interpolation='bilinear')
                        ax.set_axis_off()
                        plt.imshow(wordcloud)
                        wordcloud.to_file("nuvem.png")
                        imagem = Image.open('nuvem.png')
                        st.image(imagem)

                    resposta = "SELECT * FROM RespEntrevista"
                    c.execute(resposta)
                    result = c.fetchall()
                    df = pd.DataFrame(result, columns=["O que é importante", "O que destaca", "Atitudes inconveniente", "Motivos para desclassificação"])
                    col1, col2, col3, col4 = st.columns([10,10,10,10])
                    with col1:
                        st.write('O que é importante')
                        summary = df.dropna(subset=['O que é importante'], axis=0)['O que é importante']
                        x()
                    with col2:
                        st.write('O que destaca')
                        summary = df.dropna(subset=['O que destaca'], axis=0)['O que destaca']
                        x()
                    with col3:
                        st.write('Atitudes inconveniente')
                        summary = df.dropna(subset=['Atitudes inconveniente'], axis=0)['Atitudes inconveniente']
                        x()
                    with col4:
                        st.write('Desclassificação')
                        summary = df.dropna(subset=['Motivos para desclassificação'], axis=0)['Motivos para desclassificação']
                        x()
                    st.write('Veja a tabela de dados')
                    st.write(df)
                    st.markdown(""" <style> .font {                                          
                    font-size:30px ; font-family: 'Cooper Black'; color: #FCD44C;} 
                    </style> """, unsafe_allow_html=True)
                    st.markdown('<p class="font">Mais dicas de como se destacar na Entrevista</p>', unsafe_allow_html=True)
                    video_file = open('videodestacar.mp4', 'rb')
                    video_bytes = video_file.read()
                    st.video(video_bytes)
                    st.markdown('<p class="font">Mais sugestões do que NÃO fazer na Entrevista</p>', unsafe_allow_html=True)
                    video_file = open('videooquenaofazer.mp4', 'rb')
                    video_bytes = video_file.read()
                    st.video(video_bytes)
                if task == "Como montar o seu currículo da melhor forma":
                    st.subheader("Um currículo para impressionar as empresas")
                    st.write("""
                            1. Escolha um modelo de currículo simples e efetivo \n
                            2.	Estruture o currículo corretamente; \n 
                            3.	Coloque apenas as suas informações relevantes; \n
                            4.	Use as palavras-chave da vaga de emprego desejada; \n
                            5.	Ressalte as suas principais conquistas profissionais; \n
                            6.	Seja sincero e não exagere nos seus dados; \n
                            7.	Não passe de uma ou duas páginas;  \n
                            8.	Revise para garantir um currículo sem erros.""")
                    col1, col2, col3 = st.columns([1,6,1])
                    with col1:
                        st.write("")
                    with col2:
                        imagem = Image.open('fotocurriculo.png')
                        st.image(imagem)
                    with col3:
                        st.write("")
            
                if task == "Excluir conta":
                    st.write("Se você tem certeza que deseja excluir a conta, basta clicar no botão abaixo")
                    if st.checkbox("excluir"):
                        create_userestag()
                        hashed_pswd = make_hashes(passwordestag)
                        result = excluir_estag(usernameestag,check_hashes(passwordestag,hashed_pswd))
                        if result:
                            st.success("conta excluída com sucesso")
            else:
                st.warning("Nome/Senha incorretos ou acesso negado")



    if pag == "Área da Empresa":
        st.subheader("Página da Empresa")
        usernameempresa = st.sidebar.text_input("Nome")
        passwordempresa = st.sidebar.text_input("Senha",type='password')
        if st.sidebar.checkbox("Logar"):
            create_userempresa()
            hashed_pswd = make_hashes(passwordempresa)
            result = login_userempresa(usernameempresa,check_hashes(passwordempresa,hashed_pswd))
            if result:
                st.success("Bem vindo, {}".format(usernameempresa))
                task = st.selectbox("Selecione o que deseja",["Vagas de Estágio","Teste de Personalidade e Cognitivo","Dicas para uma Entrevista","Excluir conta"])
                if task == "Vagas de Estágio":
                    with st.form("Vaga de Estágio"):
                        name = st.text_input(label='Título para a Vaga de Estágio')
                        descricao = st.text_area(label='Descrição da Vaga de Estágio')
                        local = st.text_input(label="Local de estágio")
                        requer = st.text_area(label='Requerimentos para estágio')
                        datainicio = st.date_input(label="Início das incrções")
                        datafim = st.date_input(label='Fim das Inscrições')
                        contato = st.text_input(label='Contato')
                        photo = st.file_uploader('Arquivo', type=['png', 'jpg'])
                        st.write('Características valorizadas')
                        carac1 = st.slider(label='Criatividade')
                        carac2 = st.slider(label='Liderança')
                        carac3 = st.slider(label='Motivação')
                        carac4 = st.slider(label='Formação superior completa/incompleta')
                        carac5 = st.slider(label='Experiência na área')
                        carac6 = st.slider(label='Trabalho em equipe')
                        submitted = st.form_submit_button("Enviar") 
                        if submitted:  
                            st.write('Vaga de Estágio cadastrada com sucesso')
                            imagem = 'logo (1).png'
                            insertBLOB(name, descricao, local, requer,datainicio, datafim, contato, carac1, carac2, carac3, carac4, carac5, carac6, imagem)	
                if task == "Teste de Personalidade e Cognitivo":
                    st.write("Veja as respostas anônimas dos estagiários para analisar as características que mais predominam nos membros do Estagio Express")
                    menu = ['','Teste 1','Teste 2']
                    testes = st.selectbox("Testes",menu)
                    if testes == '':
                        if testes == '':
                            col1, col2, col3 = st.columns([1,6,1])
                            with col1:
                                st.write("")
                            with col2:
                                imagem = Image.open('teste.png')
                                st.image(imagem)
                            with col3:
                                st.write("")
                    if testes == 'Teste 1':
                        respteste1()
                    if testes == 'Teste 2':
                        respteste2()
                if task == "Dicas para uma Entrevista":
                    st.write('Muitos estagiários sentem dúvidas sobre o que fazer para se destacar em uma entrevista de estágio, o motivo de serem desclassificados ou o que não fazer na entrevista. Sendo assim, com base na esperiência da empresa que você representa, preencha esse formulário para responder eles')
                    with st.form('Entrevista de Estágio'):
                            importante = st.text_area('De forma geral, o que é importante para a empresa na hora da entrevista?')
                            destaque = st.text_area('O que faz um estagiário se destacar dos demais?')
                            inconveniente = st.text_area('Quais atitudes a empresa considera inconveniente para o momento da entrevista')
                            desclassificado = st.text_area('Cite alguns motivos que fazem um estagiário ser desclassificado')
                            if st.form_submit_button('Enviar resposta'):
                                st.success('Resposta registrada com sucesso')
                                create_entrevista()
                                add_entrevista(importante,destaque,inconveniente,desclassificado)
                if task == "Excluir conta":
                    st.write("Se você tem certeza que desej excluir a conta, basta clicar no botão abaixo")
                    if st.checkbox("excluir"):
                        create_userempresa()
                        hashed_pswd = make_hashes(passwordempresa)
                        result = excluir_empresa(usernameempresa,check_hashes(passwordempresa,hashed_pswd))
                        if result:
                            st.success("conta excluída com sucesso")
            else:
                st.warning("Nome/Senha incorretos ou acesso negado")

if __name__ == '__main__':
	main()