import streamlit as st
import plotly.express as px
from db import load_data

df=load_data()
st.title('📊 Análise de vagas e demanda')
with st.sidebar:
    regioes=st.multiselect('Região',sorted(df.regiao.unique()),default=sorted(df.regiao.unique()))
    setores=st.multiselect('Setor',sorted(df.empresa_setor.unique()),default=sorted(df.empresa_setor.unique()))
    demandas=st.multiselect('Nível de demanda',sorted(df.nivel_demanda.unique()),default=sorted(df.nivel_demanda.unique()))
f=df[df.regiao.isin(regioes)&df.empresa_setor.isin(setores)&df.nivel_demanda.isin(demandas)]
col1,col2,col3=st.columns(3)
col1.metric('Vagas acumuladas',f"{f.quantidade_vagas.sum():,}".replace(',','.'))
col2.metric('Região líder em vagas',f.groupby('regiao').quantidade_vagas.sum().idxmax())
col3.metric('Demanda predominante',f.nivel_demanda.mode().iat[0])
col1,col2=st.columns(2)
with col1:
    g=f.groupby('regiao',as_index=False).quantidade_vagas.sum().sort_values('quantidade_vagas')
    st.plotly_chart(px.bar(g,x='quantidade_vagas',y='regiao',orientation='h',title='Vagas por região'),use_container_width=True)
with col2:
    g=f.groupby('nivel_demanda',as_index=False).quantidade_vagas.sum()
    st.plotly_chart(px.pie(g,names='nivel_demanda',values='quantidade_vagas',title='Distribuição das vagas por demanda'),use_container_width=True)
g=f.groupby(['ano','nivel_demanda'],as_index=False).quantidade_vagas.sum()
st.plotly_chart(px.line(g,x='ano',y='quantidade_vagas',color='nivel_demanda',markers=True,title='Evolução das vagas por nível de demanda'),use_container_width=True)
