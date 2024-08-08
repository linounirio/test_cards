import streamlit as st
import pandas as pd
import altair as lt
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_navigation_bar import st_navbar

st.set_page_config(layout='wide')

cario_tutor = pd.read_csv('relat_fs01_carioca01_tutor.csv')
rio_tutor = pd.read_csv('relat_fs01_rio01_tutor.csv')
fase01 = pd.read_excel('relatorio_fase01_acaocidada.xlsx')

def tutores():
    import streamlit as st
    import pandas as pd
    import altair as lt
    import matplotlib.pyplot as plt
    import plotly.express as px
    carioca_df = pd.DataFrame(cario_tutor)
    rio_df = pd.DataFrame(rio_tutor)
    with open('styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    
    col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])

    
    with col1:
        c_selecao = st.selectbox(label='trailer carioca', 
                                options=carioca_df.columns,
                                index=None,
                                key='selecao_carioca',
                                placeholder='escolha uma opção', 
                                label_visibility='hidden')
        st.write("saida station", st.session_state.selecao_carioca)

        if st.session_state.selecao_carioca:
            st.metric(label=f'total de atendimentos', value=carioca_df[st.session_state.selecao_carioca].count())
    with col2:
        c_selecao = st.selectbox(label='trailer rio', 
                                options=rio_df.columns,
                                index=None,
                                placeholder='escolha uma opção', 
                                label_visibility='hidden')

    #st.title("teste tutores")

def agendamentos():
    import streamlit as st
    import pandas as pd
    import altair as lt
    import matplotlib.pyplot as plt
    import plotly.express as px
    
    st.title("teste agendamentos")

navbar = st_navbar(['censo_tutores','agendamentos'])
paginas ={
    'censo_tutores':tutores,
    'agendamentos':agendamentos,
}
paginas[navbar]()
