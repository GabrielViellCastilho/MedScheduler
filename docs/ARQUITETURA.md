# Arquitetura do Sistema

## 1. Visão Geral

O sistema será desenvolvido utilizando os princípios de **Domain-Driven Design (DDD)** e **Clean Architecture**, com o objetivo de promover baixo acoplamento, alta coesão, testabilidade e facilidade de manutenção.

A arquitetura é organizada em camadas, onde as dependências sempre apontam para o núcleo da aplicação. Dessa forma, regras de negócio permanecem independentes de frameworks, banco de dados, bibliotecas externas e detalhes de infraestrutura.

### Objetivos da Arquitetura

- Isolar as regras de negócio de tecnologias externas.
- Facilitar testes unitários e de integração.
- Permitir evolução tecnológica com mínimo impacto no domínio.
- Melhorar a organização e legibilidade do código.
- Facilitar manutenção e escalabilidade do sistema.

---

# 2. Stack Tecnológico

| Camada           | Tecnologia  | Motivo da Escolha                                                |
| ---------------- | ----------- | ---------------------------------------------------------------- |
| Linguagem        | Python 3.13 | Simplicidade, produtividade e amplo ecossistema backend          |
| Framework API    | FastAPI     | Alta performance, tipagem, validação automática e OpenAPI nativo |
| Banco de Dados   | PostgreSQL  | Relacional robusto, ideal para alto grau de relacionamentos      |
| ORM              | SQLModel    | Integra SQLAlchemy + Pydantic com produtividade e tipagem        |
| Migrações        | Alembic     | Versionamento seguro do schema do banco                          |
| Validação        | Pydantic    | Validação forte e serialização automática                        |
| Autenticação     | JWT         | Stateless, escalável e adequado para APIs REST                   |
| Testes           | Pytest      | Simples, flexível e padrão no ecossistema Python                 |
| Containerização  | Docker      | Padronização de ambiente e deploy consistente                    |
| Documentação API | Swagger     | Documentação automática gerada pelo FastAPI                      |

---

# 3. Estrutura Arquitetural

A aplicação é dividida em quatro camadas principais:

```text
Presentation
       ↓
Application
       ↓
Domain
       ↑
Infrastructure
```

## Camadas

### Domain

Contém o núcleo do sistema e todas as regras de negócio.

Esta camada não possui dependência de frameworks, banco de dados ou qualquer tecnologia externa.

### Application

Responsável por coordenar os casos de uso do sistema.

Orquestra o fluxo entre Presentation, Domain e Infrastructure.

### Infrastructure

Implementa detalhes técnicos necessários para o funcionamento da aplicação.

Inclui persistência, autenticação, integrações externas e acesso ao banco de dados.

### Presentation

Responsável pela comunicação com clientes externos, normalmente através de APIs HTTP.

Recebe requisições, valida entradas e retorna respostas.

---

# 4. Estrutura de Pastas

```text
src/
├── domain/
│   ├── entities/
│   ├── value_objects/
│   ├── services/
│   └── repositories/
│
├── application/
│   ├── use_cases/
│   ├── dtos/
│   └── interfaces/
│
├── infrastructure/
│   ├── database/
│   │   ├── models/
│   │   ├── repositories/
│   │   └── migrations/
│   ├── auth/
│   └── external/
│
├── presentation/
│   └── api/
│       ├── controllers/
│       ├── schemas/
│       └── routes/
│
└── main.py
```

---

# 5. Camada de Domínio

A camada de domínio concentra as regras de negócio da aplicação.

## entities/

Representam objetos que possuem identidade própria e ciclo de vida.

Exemplos:

- User
- Appointment
- ServiceOrder
- Customer

Características:

- Possuem identificador único.
- Mantêm estado ao longo do tempo.
- Contêm comportamento de negócio.

---

## value_objects/

Representam conceitos definidos exclusivamente por seus valores.

Exemplos:

- Email
- Money
- DateRange
- CPF

Características:

- Não possuem identidade.
- São imutáveis.
- São comparados por valor.

---

## services/

Contêm regras de negócio que não pertencem naturalmente a uma única entidade.

Exemplos:

- Cálculo de disponibilidade.
- Regras de agendamento.
- Validação de conflitos.

Características:

- Não acessam banco de dados.
- Não dependem de infraestrutura.
- Implementam lógica de negócio pura.

---

## repositories/

Contêm apenas contratos (interfaces) de persistência.

Exemplo:

```python
class UserRepository:
    def save(self, user): ...
    def find_by_id(self, user_id): ...
```

Importante:

As implementações concretas não ficam no domínio.

---

# 6. Camada de Aplicação

Responsável por implementar os casos de uso do sistema.

## use_cases/

Representam ações executadas pelos usuários.

Exemplos:

- CreateUser
- ScheduleAppointment
- CancelAppointment
- UpdateProfile

Responsabilidades:

- Orquestrar o fluxo da aplicação.
- Utilizar entidades e serviços de domínio.
- Coordenar persistência através de repositories.

---

## dtos/

Objetos de transferência de dados utilizados internamente entre camadas.

Exemplos:

- CreateUserInput
- CreateUserOutput

Benefícios:

- Desacoplamento entre API e domínio.
- Contratos explícitos entre camadas.

---

## interfaces/

Define contratos utilizados pela camada de aplicação.

Exemplos:

- Serviços de autenticação.
- Gateways externos.
- Serviços de notificação.

---

# 7. Camada de Infraestrutura

Responsável por implementar detalhes técnicos da aplicação.

---

## database/models/

Modelos de persistência utilizando SQLModel.

Exemplo:

```python
class UserModel(SQLModel, table=True):
    ...
```

Responsabilidades:

- Mapeamento para tabelas.
- Estrutura do banco de dados.
- Configuração do ORM.

---

## database/repositories/

Implementações concretas dos contratos definidos no domínio.

Exemplo:

```python
class SqlUserRepository(UserRepository):
    ...
```

Responsabilidades:

- Executar consultas.
- Persistir dados.
- Realizar mapeamento entre entidades e modelos.

---

## database/migrations/

Versionamento do schema do banco utilizando Alembic.

Responsabilidades:

- Criação de tabelas.
- Alteração de colunas.
- Evolução controlada do banco de dados.

---

## auth/

Implementações relacionadas à autenticação.

Exemplos:

- JWT Service
- Password Hasher
- Token Validator

Responsabilidades:

- Geração de tokens.
- Validação de autenticação.
- Gerenciamento de credenciais.

---

## external/

Integrações com serviços externos.

Exemplos:

- APIs de terceiros.
- Serviços de e-mail.
- Gateways de pagamento.
- Mensageria.

Responsabilidades:

- Comunicação com sistemas externos.
- Implementação de adaptadores e gateways.

---

# 8. Camada de Apresentação

Responsável pela comunicação HTTP.

---

## controllers/

Recebem requisições e executam casos de uso.

Responsabilidades:

- Receber dados da requisição.
- Chamar casos de uso.
- Converter respostas.

Não devem conter:

- Regras de negócio.
- Consultas ao banco.

---

## schemas/

Modelos Pydantic para entrada e saída da API.

Exemplos:

```python
class CreateUserRequest(BaseModel):
    name: str
    email: str
```

Responsabilidades:

- Validação de entrada.
- Serialização de saída.
- Documentação automática.

---

## routes/

Definição dos endpoints da API.

Exemplo:

```python
router.post("/users")
```

Responsabilidades:

- Definir rotas.
- Associar endpoints aos controllers.
- Organizar a API.

---

# 9. Fluxo de Execução

O fluxo padrão de uma requisição segue o seguinte caminho:

```text
HTTP Request
      ↓
Route
      ↓
Controller
      ↓
Use Case
      ↓
Domain
      ↓
Repository Interface
      ↓
Repository Implementation
      ↓
Database
```

O retorno segue o caminho inverso até a resposta HTTP.

---

# 10. Benefícios da Arquitetura

- Separação clara de responsabilidades.
- Baixo acoplamento entre camadas.
- Alta testabilidade.
- Facilidade para troca de tecnologias.
- Evolução sustentável do sistema.
- Regras de negócio protegidas de detalhes técnicos.
- Melhor organização para equipes e manutenção de longo prazo.

Essa arquitetura fornece uma base sólida para sistemas de pequeno, médio e grande porte, mantendo o domínio da aplicação como principal ativo do projeto.
