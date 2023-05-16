import streamlit as st
from PIL import Image

def main():
    st.markdown(""" <style> .font {                                          
	        font-size:45px ; font-family: 'Cooper Black'; color: #FCD44C;} 
			</style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">SEJA BEM VINDO AO ESTÁGIO EXPRESS</p>', unsafe_allow_html=True)
    logo = Image.open('logo (1).png')
    st.sidebar.image(logo,  width=270)
    menu = ["Cadastro da Empresa","Área do Estagiário","Área da Empresa","Cadastre-se"]
    pag = st.sidebar.selectbox("Menu",menu)

if __name__ == '__main__':
	main()