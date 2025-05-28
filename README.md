# ApiREST_Python
# 🚀 API de Usuários Simples com Flask e Faker, criada em Python

Este projeto tem como objetivo criar uma API REST simples para criar e gerenciar usuários, utilizando Python com Flask. Os dados dos usuários são gerados dinamicamente com a biblioteca Faker para facilitar os testes e o desenvolvimento.

---

## ⚙️ Tecnologias Utilizadas

- Python 
- Flask  
- Faker (para geração de dados fictícios)  
- Requests (para consumir a API)

🧠 O que o Flask faz nesse projeto?
O Flask é um framework web em Python que permite criar aplicações web e APIs de forma rápida em localhost.

Neste projeto, o Flask é responsável por:

Subir um servidor web local (http://127.0.0.1:5000)

Definir rotas URI (endpoints) como /usuarios para receber requisições HTTP (GET, POST, PUT, DELETE)

Responder com JSON, o formato padrão usado para troca de dados em APIs REST

Tratar os dados enviados e recebidos, simulando um banco de dados com uma lista em memória


---

## 🎯 Objetivos do Projeto

- Criar uma API REST básica para operações CRUD de usuários  
- Gerar dados falsos para facilitar testes e desenvolvimento  
- Demonstrar o consumo da API usando a biblioteca Requests em Python  
- Facilitar estudos e prototipagem rápida de APIs REST

_________________________________________________________________________________

## 📦 Como Rodar

💡 Dica: Use 2 terminais

- Terminal 1 rodando a API com Flask
- Terminal 2 executando o consumo da API com Requests (Scripts na pasta: CRUD_API_REST)

---

Clone o repositório:
Comando: git clone https://github.com/MaxBlooom/ApiREST_Python


Entre na pasta do projeto:
Comando: cd seu_repositorio

Instale as dependências:
Comandos: 
pip install flask
pip install faker

_________________________________________________________________________________

Scrips para requests na API

🎯 Listar todos os usuários (GET)

import requests

res = requests.get("http://127.0.0.1:5000/usuarios")
usuarios = res.json()

for u in usuarios:
    print(f"ID: {u['id']}, Nome: {u['nome']}, Email: {u['email']}")

----

🎯 Criar novo usuário (POST)

import requests

novo = {"nome": "Maxsuel Alves", "email": "maxsuel.alves@email.com"}
res = requests.post("http://127.0.0.1:5000/usuarios", json=novo)

print(res.status_code)
print(res.json())

-----

🎯 Atualizar usuário (PUT)

import requests

url = "http://127.0.0.1:5000/usuarios/12"
dados = {"nome": "Nome Atualizado", "email": "email.atualizado@email.com"}
res = requests.put(url, json=dados)

print(res.status_code)
print(res.json())

_________________________________________________________________________________


