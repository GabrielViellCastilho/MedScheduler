# Escopo do Sistema de Agendamento Médico (Backend)

## Objetivo

Desenvolver uma API REST para gerenciamento de médicos, pacientes, agendas e consultas médicas.

---

# Requisitos Funcionais

## Autenticação

### RF001 - Autenticação de usuários

O sistema deve permitir autenticação por e-mail e senha.

### RF002 - Autorização

O sistema deve controlar acesso aos recursos conforme o perfil do usuário.

### RF003 - Renovação de sessão

O sistema deve permitir renovação de tokens de acesso.

---

## Pacientes

### RF004 - Cadastro de pacientes

O sistema deve permitir cadastrar pacientes.

### RF005 - Consulta de pacientes

O sistema deve permitir consultar pacientes cadastrados.

### RF006 - Atualização de pacientes

O sistema deve permitir atualizar dados de pacientes.

### RF007 - Exclusão lógica de pacientes

O sistema deve permitir inativar pacientes.

---

## Médicos

### RF008 - Cadastro de médicos

O sistema deve permitir cadastrar médicos.

### RF009 - Consulta de médicos

O sistema deve permitir consultar médicos.

### RF010 - Atualização de médicos

O sistema deve permitir atualizar médicos.

### RF011 - Exclusão lógica de médicos

O sistema deve permitir inativar médicos.

---

## Especialidades

### RF012 - Cadastro de especialidades

O sistema deve permitir cadastrar especialidades.

### RF013 - Consulta de especialidades

O sistema deve permitir listar especialidades.

### RF014 - Atualização de especialidades

O sistema deve permitir atualizar especialidades.

### RF015 - Exclusão lógica de especialidades

O sistema deve permitir inativar especialidades.

---

## Agenda Médica

### RF016 - Configuração de agenda

O sistema deve permitir configurar horários de atendimento dos médicos.

### RF017 - Bloqueio de agenda

O sistema deve permitir registrar períodos de indisponibilidade.

### RF018 - Consulta de horários disponíveis

O sistema deve retornar horários disponíveis para agendamento.

---

## Consultas

### RF019 - Agendamento de consultas

O sistema deve permitir criar consultas.

### RF020 - Reagendamento de consultas

O sistema deve permitir alterar data e horário de consultas.

### RF021 - Cancelamento de consultas

O sistema deve permitir cancelar consultas.

### RF022 - Consulta de agendamentos

O sistema deve permitir consultar consultas agendadas.

### RF023 - Histórico de consultas

O sistema deve permitir consultar histórico de consultas de um paciente.

### RF024 - Atualização de status

O sistema deve permitir atualizar o status de uma consulta.

Status possíveis:

- Agendada
- Confirmada
- Realizada
- Cancelada
- Não Compareceu

---

## Relatórios

### RF025 - Relatório de consultas

O sistema deve fornecer dados para relatórios de consultas.

### RF026 - Relatório de ocupação

O sistema deve fornecer dados sobre utilização das agendas médicas.

### RF027 - Relatório de faltas

O sistema deve fornecer dados sobre pacientes ausentes.

---

# Regras de Negócio

### RN001

Um médico não pode possuir duas consultas no mesmo horário.

### RN002

Um paciente não pode possuir duas consultas no mesmo horário.

### RN003

Consultas somente podem ser criadas em horários disponíveis.

### RN004

Consultas somente podem ser criadas para médicos ativos.

### RN005

Consultas somente podem ser criadas para pacientes ativos.

### RN006

Consultas canceladas não podem ser marcadas como realizadas.

### RN007

Consultas realizadas não podem ser reagendadas.

### RN008

Consultas realizadas não podem ser canceladas.

### RN009

A duração padrão da consulta será de 30 minutos.

### RN010

Horários bloqueados não podem receber agendamentos.

### RN011

Especialidades vinculadas a médicos não podem ser removidas enquanto existirem consultas futuras associadas.

---

# Requisitos Não Funcionais

### RNF001

A API deve seguir o padrão REST.

### RNF002

A API deve retornar respostas no formato JSON.

### RNF003

A API deve utilizar autenticação JWT.

### RNF004

A API deve registrar logs de operações críticas.

### RNF005

A API deve possuir documentação OpenAPI/Swagger.

### RNF006

A API deve utilizar paginação em listagens.

### RNF007

A API deve validar todos os dados recebidos.

### RNF008

A API deve armazenar senhas utilizando hash seguro.

### RNF009

A API deve utilizar migrações para versionamento do banco de dados.

---

# Principais Entidades

### User

```text
id
name
email
password
role
createdAt
updatedAt
```

### Patient

```text
id
name
cpf
birthDate
phone
email
active
createdAt
updatedAt
```

### Specialty

```text
id
name
description
createdAt
updatedAt
```

### Doctor

```text
id
name
crm
specialtyId
active
createdAt
updatedAt
```

### Schedule

```text
id
doctorId
weekday
startTime
endTime
createdAt
updatedAt
```

### ScheduleBlock

```text
id
doctorId
startDateTime
endDateTime
reason
createdAt
updatedAt
```

### Appointment

```text
id
patientId
doctorId
startDateTime
endDateTime
status
notes
createdAt
updatedAt
```

# Endpoints Principais

```http
POST   /auth/login

GET    /patients
POST   /patients
PUT    /patients/:id
DELETE /patients/:id

GET    /doctors
POST   /doctors
PUT    /doctors/:id
DELETE /doctors/:id

GET    /specialties
POST   /specialties

GET    /appointments
POST   /appointments
PATCH  /appointments/:id/reschedule
PATCH  /appointments/:id/cancel
PATCH  /appointments/:id/status

GET    /doctors/:id/availability

POST   /schedule-blocks
GET    /schedule-blocks
```
