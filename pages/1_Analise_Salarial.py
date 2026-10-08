import streamlit as st
import plotly.express as px
from db import load_data

df = load_data()
st.title('💰 Análise salarial')
with st.sidebar:
    cargos = st.multiselect('Cargo', sorted(df.cargo.unique()), default=sorted(df.cargo.unique()))
    senioridades = st.multiselect('Senioridade', sorted(df.senioridade.unique()), default=sorted(df.senioridade.unique()))
    tecnologias = st.multiselect('Tecnologia', sorted(df.tecnologia.unique()), default=sorted(df.tecnologia.unique()))
f = df[df.cargo.isin(cargos) & df.senioridade.isin(senioridades) & df.tecnologia.isin(tecnologias)]
col1,col2,col3 = st.columns(3)
col1.metric('Salário médio', f"R$ {f.salario_medio.mean():,.2f}".replace(',','X').replace('.',',').replace('X','.'))
col2.metric('Maior salário médio por cargo', f"R$ {f.groupby('cargo').salario_medio.mean().max():,.2f}".replace(',','X').replace('.',',').replace('X','.'))
col3.metric('Mediana salarial', f"R$ {f.salario_medio.median():,.2f}".replace(',','X').replace('.',',').replace('X','.'))
col1,col2 = st.columns(2)
with col1:
    g=f.groupby(['cargo','senioridade'],as_index=False).salario_medio.mean()
    st.plotly_chart(px.bar(g,x='cargo',y='salario_medio',color='senioridade',barmode='group',title='Salário por cargo e senioridade'),use_container_width=True)
with col2:
    g=f.groupby('tecnologia',as_index=False).salario_medio.mean().sort_values('salario_medio')
    st.plotly_chart(px.bar(g,x='salario_medio',y='tecnologia',orientation='h',title='Salário médio por tecnologia'),use_container_width=True)
st.dataframe(f.groupby(['cargo','senioridade']).salario_medio.agg(['mean','median','min','max']).round(2).reset_index(),use_container_width=True,hide_index=True)
