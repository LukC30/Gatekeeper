# Gatekeeper - API de Autenticação

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red)
![Pytest](https://img.shields.io/badge/Pytest-7.0%2B-blueviolet)

O Gatekeeper é uma API de autenticação robusta e escalável, construída com FastAPI. Ele foi projetado para ser o "guardião principal" da sua aplicação, gerenciando usuários e autenticação de forma centralizada. Atualmente, funciona como uma API que pode ser integrada a outros serviços, com o objetivo de evoluir para um Auth Gateway completo.

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
  - [Tecnologias](#tecnologias)
  - [Arquitetura](#arquitetura)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Como Começar](#como-começar)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
- [Uso](#uso)
  - [Executando a Aplicação](#executando-a-aplicação)
  - [Endpoints da API](#endpoints-da-api)
- [Testes](#testes)

## Sobre o Projeto

Este projeto fornece uma base sólida para gerenciamento de usuários, incluindo criação e consulta. Ele utiliza uma arquitetura limpa e desacoplada, facilitando a manutenção e a adição de novas funcionalidades. A segurança é uma prioridade, com senhas sendo criptografadas antes da persistência no banco de dados.

### Tecnologias

O backend é construído com as seguintes tecnologias:

- **[FastAPI](https://fastapi.tiangolo.com/):** Framework web moderno e de alta performance para a construção de APIs.
- **[SQLModel](https://sqlmodel.tiangolo.com/):** Biblioteca para interagir com bancos de dados SQL a partir de modelos Python, combinando SQLAlchemy e Pydantic.
- **[SQLAlchemy](https://www.sqlalchemy.org/):** ORM para comunicação com o banco de dados de forma assíncrona.
- **[Pydantic](https://docs.pydantic.dev/):** Para validação de dados e gerenciamento de configurações.
- **[Uvicorn](https://www.uvicorn.org/):** Servidor ASGI para executar a aplicação FastAPI.
- **[Pytest](https://docs.pytest.org/):** Framework para a escrita de testes automatizados.
- **[python-dotenv](https://pypi.org/project/python-dotenv/):** Para gerenciar variáveis de ambiente.

### Arquitetura

O projeto segue uma arquitetura em camadas para separar as responsabilidades:

- **Router (`app/users/router.py`):** Define os endpoints da API, recebe as requisições HTTP e retorna as respostas. Delega a lógica de negócio para a camada de serviço.
- **Service (`app/users/service.py`):** Contém a lógica de negócio da aplicação. Orquestra as operações, como criptografar senhas e chamar o repositório para interagir com o banco de dados.
- **Repository (`app/users/repository.py`):** Responsável pela comunicação com o banco de dados. Abstrai as consultas SQL e as operações de CRUD (Criar, Ler, Atualizar, Deletar).
- **DTO (Data Transfer Object) (`app/users/dto.py`):** Define a estrutura dos dados que são transferidos entre o cliente e a API.
- **Mapper (`app/users/mapper.py`):** Converte os DTOs para os modelos do banco de dados e vice-versa.
- **Dependency Injection (`app/config/dependencies.py`):** O FastAPI gerencia as dependências, injetando instâncias de serviços e repositórios onde são necessárias, promovendo o baixo acoplamento.

## Estrutura de Diretórios

```
Gatekeeper/
├── app/
│   ├── config/
│   │   ├── config.py         # Carrega configurações do .env
│   │   ├── database.py       # Configuração do banco de dados e engine SQLAlchemy
│   │   ├── dependencies.py   # Injeção de dependências (serviços, repositórios)
│   │   └── lifespan.py       # Gerenciador de ciclo de vida da aplicação
│   ├── models/
│   │   └── user_model.py     # Modelo de dados do usuário (SQLModel)
│   ├── users/
│   │   ├── dto.py            # DTOs para entrada e saída de dados do usuário
│   │   ├── interface.py      # Interface (classe base abstrata) para o repositório
│   │   ├── mapper.py         # Mapeador entre DTO e Modelo
│   │   ├── repository.py     # Implementação do repositório de usuário
│   │   ├── router.py         # Endpoints da API para usuários
│   │   └── service.py        # Lógica de negócio para usuários
│   └── utils/
│       └── auth_utils.py     # Funções utilitárias (ex: criptografia de senha)
├── tests/
│   ├── test_userRepository.py # Testes unitários para o repositório
│   ├── test_userService.py    # Testes unitários para o serviço
│   └── test_userRouter.py     # Testes de integração para o router
└── main.py                   # Ponto de entrada da aplicação FastAPI
```

## Como Começar

Siga estas instruções para ter uma cópia do projeto rodando localmente.

### Pré-requisitos

- Python 3.10 ou superior
- Pip (gerenciador de pacotes do Python)
- Um banco de dados MySQL

### Instalação

1. **Clone o repositório:**
   ```sh
   git clone <url-do-seu-repositorio>
   cd Gatekeeper
   ```

2. **Crie e ative um ambiente virtual:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   Crie um arquivo `requirements.txt` com as dependências do projeto e execute:
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` na raiz do projeto, baseado no exemplo abaixo, e preencha com as credenciais do seu banco de dados.

   **.env.example**
   ```
   USER_DB=root
   PASSWORD=sua_senha_secreta
   HOST=localhost
   PORT=3306
   DATABASE=gatekeeper_db
   ```

## Uso

### Executando a Aplicação

Com o ambiente virtual ativado e o arquivo `.env` configurado, inicie o servidor a partir da raiz do projeto:

```sh
python main.py
```

O servidor Uvicorn iniciará, e a API estará disponível em `http://127.0.0.1:8000`. A documentação interativa (Swagger UI) pode ser acessada em `http://127.0.0.1:8000/docs`.

### Endpoints da API

#### Usuários (`/user`)

- **`POST /user/`**
  - **Descrição:** Cria um novo usuário.
  - **Corpo da Requisição:**
    ```json
    {
      "email": "user@example.com",
      "senha": "uma_senha_forte"
    }
    ```
  - **Resposta (Sucesso - 201 Created):**
    ```json
    {
      "email": "user@example.com",
      "id": 1
    }
    ```

- **`GET /user/{email}`**
  - **Descrição:** Busca um usuário pelo seu email.
  - **Parâmetro de URL:** `email` (string)
  - **Resposta (Sucesso - 200 OK):**
    ```json
    {
      "email": "user@example.com",
      "id": 1
    }
    ```

## Testes

O projeto utiliza `pytest` para testes unitários e de integração. Para executar os testes, certifique-se de ter as dependências de desenvolvimento instaladas e execute o seguinte comando na raiz do projeto:

```sh
pytest
```

Os testes cobrem as camadas de repositório, serviço e rotas, utilizando mocks para isolar as unidades e garantir que cada componente funcione como esperado.

---
