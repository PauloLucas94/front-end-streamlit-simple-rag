import streamlit as st
from dotenv import load_dotenv
import requests
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# URL da sua API
API_URL = os.getenv('API_URL')

st.title("Assistente ERP - Banco de Dados")

# Entrada do usuário
user_input = st.text_input("Digite suas dúvidas:")

if st.button("Enviar"):
    if user_input:
        try:
            # Enviar a requisição para a API
            headers = {"Content-Type": "application/json"}  # Cabeçalho necessário
            payload = {"question": user_input}  # Mesma estrutura do curl

            # Fazer a requisição POST
            response = requests.post(API_URL, headers=headers, json=payload, timeout=120)
            
            # Verificar status da resposta
            if response.status_code == 200:
                st.success("Connection to API successful.")
                st.json(response.json())  # Exibir a resposta completa
                bot_response = response.json().get("response", "Campo 'context' não encontrado.")
                st.success(f"Bot: {bot_response}")
            else:
                st.error(f"Erro na API: {response.status_code} - {response.text}")
        except requests.exceptions.Timeout:
            st.error("Connection Timeout.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error to connect API: {e}")
    else:
        st.warning("Por favor, insira uma mensagem antes de enviar.")
