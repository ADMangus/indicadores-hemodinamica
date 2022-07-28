import Hemo
import siemens
import philips
import relatorio
import relatorio_medico
import streamlit as st

from configparser import ConfigParser
from PIL import Image

#Layout
st.set_page_config(layout="wide")

config = ConfigParser()
config.read("hsnc.ini")
nome_equipamento_philips = config['lista_equipamentos']['philips']
nome_equipamento_siemens = config['lista_equipamentos']['siemens']
g = config['path']['path_graph']
relat = config['path']['path_relatorio']
img = config['path']['imagem']
dire = config['path']['diretorio']
cadastro_clientes = config['lista_equipamentos']['cadastro_clientes']


if 'philips'  not in st.session_state:
    st.session_state['philips'] = nome_equipamento_philips
    
if 'siemens'  not in st.session_state:
    st.session_state['siemens'] = nome_equipamento_siemens

if 'imagem' not in st.session_state:
    st.session_state['imagem'] = img
    
if 'graficos' not in st.session_state:
    st.session_state['graficos'] = g
    
if 'relatorio' not in st.session_state:
    st.session_state['relatorio'] = relat
    
if 'diretorio' not in st.session_state:
    st.session_state['diretorio'] = dire
    
if 'cadastro' not in st.session_state:
    st.session_state['cadastro'] = cadastro_clientes
 

PAGES = { "Página Inicial": Hemo,
         "Indicadores gerais para o Siemens": siemens,
         "Indicadores gerais para o Philips": philips,
         "Relatório dos Equipamentos": relatorio,
         "Relatório por Médico": relatorio_medico
}

st.sidebar.title('Navegação')
selection = st.sidebar.selectbox("O que você deseja executar?", list(PAGES.keys()))
st.sidebar.button('📬 Reportar erro')
st.sidebar.markdown("""---""")
st.sidebar.write('*Desenvolvido por Arthur D. Mangussi*')
aa = Image.open(st.session_state['imagem'])
st.sidebar.image(aa,  width=10, use_column_width = True)
img = '<img src=https://github.com/ADMangus/indicadores-hemodinamica/blob/main/nucleorad.png?raw=true>'
st.sidebar.image(img)


page = PAGES[selection]
page.app()







