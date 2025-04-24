# 🧩 PokéDex Web API

Bem-vindo à **PokéDex Web API**! Este projeto combina o poder da **FastAPI** com a simplicidade do **frontend estático** para criar uma Pokédex dinâmica, navegável e cheia de estilo — tudo containerizado com Docker! 🐳

## 🚀 Visão Geral

A aplicação busca dados da PokéAPI, armazena num banco SQLite local e exibe tudo em uma interface leve, com filtros, ordenação e paginação. Ideal para estudos, portfólio ou só porque você é fã de Pokémon mesmo. 😄

---

## 🗂️ Estrutura do Projeto

├── app/ # Backend em FastAPI ├── frontend/ # Frontend (HTML + JS + CSS + Nginx) ├── pokemon.db # Banco de dados SQLite ├── requirements.txt # Dependências do Python ├── Dockerfile # Backend Dockerfile ├── docker-compose.yml # Orquestrador dos serviços

---

## 🔧 Como Rodar Localmente

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Passo a passo

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd projeto-pokemon/
   
2. Suba os containers:
   docker-compose up --build
3. Acesse:

🖥️ Frontend: http://localhost:8080

⚙️ Documentação da API (Swagger): http://localhost:8000/docs

🧪 Tecnologias Usadas

🐍 FastAPI

🐬 SQLite

🐳 Docker & Docker Compose

🕸️ HTML, CSS e JavaScript Vanilla

🧭 Nginx

📜 Licença
Distribuído sob a licença MIT. Veja LICENSE para mais detalhes.
