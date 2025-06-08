import streamlit as st
from db import produtos

st.title(' Cadastro de Produtos')

with st.form('cadastrar-produto') as form:
    nome = st.text_input('Nome', placeholder='Nome do produto')
    preco = st.number_input('Preço')
    quantidade = st.number_input('quantidade', step=1)
    categoria = st.selectbox(
        'categoria', index=None,
        placeholder='Selecione uma opção',
        options=['Alimentos', 'Informatica', 'Higiene', 'Textil']
    )

    button = st.form_submit_button('cadastrar')

    if button:
        produto = {
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade,
            'categoria': categoria
        }
        produtos.append(produto)
