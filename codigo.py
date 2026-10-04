# titulo sistema
# secao cadastar vendas
    # Campo data
    # Campo vendedor - Ana, Bruno, Carla
    # Campo Produto - Notebook, Fone, Celular 
    # Campo quantidade
    # Campo valor
    # Campo botao cadastrar vendas
        # quando clicar no botão adiccionar a venda na tabela.
# secao vendas cadastradas
    #Tabela de vendas = base de dados

# dashboard
    # Card de faturamento total
    # Grafico de  Coluna
    # Grafico de Pizza

# Biblioteca utilizadas steamlit - pandas - plotly

import streamlit as st
import pandas as pd
import plotly.express as px

#carregar base de venda
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

#secao de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("")
vendedor = st.sidebar.selectbox("Vendedor",["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto",["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade",step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Vendas")

# logica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv('vendas.csv', index=False)
    st.success("Vendas Cadastrada com Sucesso")

#secao de visualizar vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

# secao Dashboard
st.write("## Dashboard")

# Card de faturamento total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total",f"R${faturamento}")

# Grafico de  Coluna
grafico1 = px.bar(tabela_vendas,x="vendedor", y= "valor", color="produto")
st.plotly_chart(grafico1)

# Grafico de Pizza
grafico2 = px.pie(tabela_vendas,names="produto", values="valor")
st.plotly_chart(grafico2)