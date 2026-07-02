# MedScheduler

Sistema de agendamento médico desenvolvido para auxiliar no gerenciamento de consultas, pacientes e médicos de forma simples e eficiente.

## Funcionalidades

* Cadastro de pacientes
* Cadastro de médicos
* Agendamento de consultas
* Gerenciamento de horários


## Integrantes

* [Gabriel Viell Castilho](https://github.com/GabrielViellCastilho)
* [Humberto Ishii](https://github.com/HumbertoIshii)
* [Wesley Gonçalves](https://github.com/WesleyGoncalves)

## Requisitos

- Uma conta no GitHub
- Git instalado
- IDE (recomendado: VS Code)
- Docker
- Docker Compose

---

## Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/GabrielViellCastilho/MedScheduler
cd MedScheduler
```

### 2. Variáveis de Ambiente

Copie o arquivo de variáveis:

```bash
cp .\src\.env.example .\src\.env
```

Edite o `.env`:

### 3. Subir os containers

```bash
docker compose up --build
```

### 4. Executar as migrations
Com os containers em execução, é necessário aplicar as migrations para criar e atualizar as tabelas no banco de dados.\
Em um segundo terminal rodar o comando:
```bash
docker compose exec api alembic upgrade head
```

### 5. Acessar a aplicação

API: http://localhost:8000 \
Docs: http://localhost:8000/docs

## Rodar testes

Com um container rodando em um segundo terminal rodar o comando:

```bash
docker compose exec api pytest
```
---

**FATEC São José dos Campos**\
**Análise e Desenvolvimento de Sistemas**\
**Engenharia de Software III**
