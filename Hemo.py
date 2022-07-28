import pandas as pd
import os
import streamlit as st
import time
from PIL import Image
import datetime

def app():
    st.title('Página Inicial')
    
    st.write('### Seja Bem-vindo')
    st.write(''' Para iniciar uso da ferramenta é preciso cadastrar o nome do Cliente, com a finalidade do preenchimento do relatório final para os indicadores de dose do serviço de Hemodinâmica. Caso o cliente, já esteja cadastrado clique em Salvar Dados.
        
    ''')
    form = st.form(key='my_form', clear_on_submit=True)
    cliente = form.text_input('Digite o nome do cliente',
                              help='Digite o nome por extenso!',
                              placeholder = 'Digite aqui')
    cod = form.text_input('Digite o código do cliente', 
                         placeholder = 'Digite o número do cliente aqui')
    
    arquivo = st.session_state['diretorio'] + st.session_state['cadastro']
    
    save_button = form.form_submit_button('Salvar dados')
    
    if save_button: 
        #Formatando a data do relatório
        m = datetime.date.today().month
        if m == 1:
            month = 'Janeiro'
        elif m == 2:
            month = 'Fevereiro'
        elif m == 3:
            month = 'Março'
        elif m == 4:
            month = 'Abril'
        elif m == 5:
            month = 'Maio'
        elif m == 6:
            month = 'Junho'
        elif m == 7:
            month = 'Julho'
        elif m == 8:
            month = 'Agosto'
        elif m == 9:
            month = 'Setembro'
        elif m == 10:
            month = 'Outubro'
        elif m == 11:
            month = 'Novembro'
        elif m == 12:
            month = 'Dezembro'
        
        graficos_philips = f'{st.session_state.graficos}\Philips'
        graficos_siemens = f'{st.session_state.graficos}\Siemens Artis One'
        grafico_mes = f'{st.session_state.graficos}\Siemens Artis One\{month}'
        grafico_mes_philips = f'{st.session_state.graficos}\Philips\{month}'
        
        try: 
            os.makedirs(st.session_state['graficos'],  exist_ok = True)
        except OSError as error:
            st.write('Diretório não pode ser criado')
            
        try: 
            os.makedirs(graficos_philips,  exist_ok = True)
        except OSError as error:
            st.write('Diretório não pode ser criado')
            
        try: 
            os.makedirs(graficos_siemens,  exist_ok = True)
        except OSError as error:
            st.write('Diretório não pode ser criado')
            
        try: 
            os.makedirs(grafico_mes,  exist_ok = True)
        except OSError as error:
            st.write('Diretório não pode ser criado')
            
        try: 
            os.makedirs(grafico_mes_philips,  exist_ok = True)
        except OSError as error:
            st.write('Diretório não pode ser criado')
            
        try: 
            os.makedirs(st.session_state['relatorio'],  exist_ok = True)
        except OSError as error:
            st.write('Diretório não pode ser criado')
        
        
        df = pd.read_csv(arquivo, sep=";")
        df.loc[len(df.index)] = [cod, cliente]
        df.to_csv(arquivo, sep=";",index=False)
        
        with st.spinner('Carregando...'):
            time.sleep(1.2)
        st.success('Informações preenchidas e salvas com sucesso!')
        
        
    
    
    
   