import streamlit as st
import plotly.express as px
from db import load_data

st.set_page_config(page_title='Mercado de TI no Brasil', page_icon='💻', layout='wide')

df = load_data()

st.title('💻 Mercado de TI no Brasil')
st.subheader('Análise de salários, vagas, tecnologias e demanda — 2015 a 2024')
st.write('Este dashboard analisa uma base simulada do mercado brasileiro de tecnologia, permitindo explorar diferenças por região, cargo, senioridade, tecnologia, modalidade e setor.')

with st.sidebar:
    st.header('Filtros globais')
    anos = st.multiselect('Ano', sorted(df['ano'].unique()), default=sorted(df['ano'].unique()))
    regioes = st.multiselect('Região', sorted(df['regiao'].unique()), default=sorted(df['regiao'].unique()))
    cargos = st.multiselect('Cargo', sorted(df['cargo'].unique()), default=sorted(df['cargo'].unique()))
    modalidades = st.multiselect('Modalidade', sorted(df['modalidade'].unique()), default=sorted(df['modalidade'].unique()))

f = df[df['ano'].isin(anos) & df['regiao'].isin(regioes) & df['cargo'].isin(cargos) & df['modalidade'].isin(modalidades)].copy()

if f.empty:
    st.warning('Nenhum registro corresponde aos filtros selecionados.')
    st.stop()

c1,c2,c3,c4 = st.columns(4)
c1.metric('Salário médio', f"R$ {f['salario_medio'].mean():,.2f}".replace(',', 'X').replace('.', ',').replace('X','.'))
c2.metric('Vagas acumuladas', f"{f['quantidade_vagas'].sum():,}".replace(',', '.'))
c3.metric('Registros', f"{len(f):,}".replace(',', '.'))
c4.metric('Cidades', f["cidade"].nunique())

st.markdown('### Visão geral')
col1,col2 = st.columns(2)
with col1:
    anual = f.groupby('ano', as_index=False).agg(salario_medio=('salario_medio','mean'), vagas=('quantidade_vagas','sum'))
    fig = px.line(anual, x='ano', y='salario_medio', markers=True, title='Evolução do salário médio')
    fig.update_layout(yaxis_tickprefix='R$ ', hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)
with col2:
    cargo = f.groupby('cargo', as_index=False).agg(salario_medio=('salario_medio','mean')).sort_values('salario_medio')
    fig = px.bar(cargo, x='salario_medio', y='cargo', orientation='h', title='Salário médio por cargo')
    fig.update_layout(xaxis_tickprefix='R$ ')
    st.plotly_chart(fig, use_container_width=True)

st.markdown('### Principais resultados')
r1 = f.groupby('regiao')['salario_medio'].mean().sort_values(ascending=False)
r2 = f.groupby('tecnologia')['salario_medio'].mean().sort_values(ascending=False)
r3 = f.groupby('senioridade')['salario_medio'].mean().sort_values(ascending=False)
col1,col2,col3 = st.columns(3)
col1.info(f"**Região com maior salário médio:** {r1.index[0]} — R$ {r1.iloc[0]:,.2f}".replace(',', 'X').replace('.', ',').replace('X','.'))
col2.info(f"**Tecnologia com maior salário médio:** {r2.index[0]} — R$ {r2.iloc[0]:,.2f}".replace(',', 'X').replace('.', ',').replace('X','.'))
col3.info(f"**Maior média por senioridade:** {r3.index[0]} — R$ {r3.iloc[0]:,.2f}".replace(',', 'X').replace('.', ',').replace('X','.'))

st.markdown('### Dados filtrados')
st.dataframe(f.sort_values('data', ascending=False), use_container_width=True, hide_index=True)

st.markdown('### Conclusão executiva')
st.write('A análise permite comparar remuneração e volume de oportunidades sob diferentes recortes. Os resultados devem ser interpretados como tendências da base simulada, e não como estimativa oficial do mercado de trabalho brasileiro.')
