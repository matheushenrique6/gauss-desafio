# Projeto Pokémon API

Este projeto consiste em uma API desenvolvida com **FastAPI** e um frontend simples em HTML, CSS e JavaScript. Ele consome dados da PokéAPI e os exibe em uma interface web com funcionalidades de filtro, ordenação e paginação.

## Requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Estrutura do Projeto

 ├── app/ # Backend FastAPI ├── frontend/ # Frontend HTML/CSS/JS com Nginx ├── pokemon.db # Banco de dados SQLite ├── Dockerfile # Dockerfile do backend ├── docker-compose.yml # Orquestração dos containers ├── requirements.txt # Dependências Python

## Instruções de Execução

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd teste2
### 2.Subir o projeto com Docker Compose
docker-compose up --build
### 3. Acessar a aplicação
Frontend: http://localhost:8080

API Docs (Swagger): http://localhost:8000/docs

# Tecnologias Usadas
FastAPI

SQLite

Docker & Docker Compose

HTML/CSS/JavaScript

Nginx