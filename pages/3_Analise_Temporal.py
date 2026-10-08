import streamlit as st
import plotly.express as px
from db import load_data

df=load_data()
st.title('📅 Análise temporal')
with st.sidebar:
    inicio=st.slider('Ano inicial',int(df.ano.min()),int(df.ano.max()),int(df.ano.min()))
    fim=st.slider('Ano final',int(df.ano.min()),int(df.ano.max()),int(df.ano.max()))
f=df[(df.ano>=inicio)&(df.ano<=fim)]
g=f.groupby('data',as_index=False).agg(salario_medio=('salario_medio','mean'),vagas=('quantidade_vagas','sum'))
col1,col2=st.columns(2)
with col1:
    st.plotly_chart(px.line(g,x='data',y='salario_medio',markers=False,title='Evolução mensal do salário médio'),use_container_width=True)
with col2:
    st.plotly_chart(px.line(g,x='data',y='vagas',title='Evolução mensal das vagas'),use_container_width=True)
annual=f.groupby('ano',as_index=False).agg(salario_medio=('salario_medio','mean'),vagas=('quantidade_vagas','sum'))
st.dataframe(annual.round(2),use_container_width=True,hide_index=True)
if len(annual)>=2:
    pct=(annual.iloc[-1].salario_medio/annual.iloc[0].salario_medio-1)*100
    st.info(f'Entre {int(annual.iloc[0].ano)} e {int(annual.iloc[-1].ano)}, o salário médio variou {pct:.2f}%.')
