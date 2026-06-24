# 1. Elicitação de Requisitos

## Desafio de Negócio

Clínicas de saúde enfrentam alto índice de no-show (faltas sem aviso), gerando:
- ociosidade de consultórios
- baixa eficiência da agenda médica
- perda financeira e operacional

Além disso, o sistema deve garantir:
- segurança de dados sensíveis (LGPD)
- controle de acesso a informações clínicas
- rastreabilidade de ações no sistema

## Objetivo do Sistema
Desenvolver uma plataforma de gestão de clínicas e agendamentos inteligentes, com foco em:
- redução de no-show
- automação de lembretes
- políticas de cancelamento
- controle seguro de dados clínicos

## Atores do Sistema
- Paciente
- Médico
- Administrador do sistema

---

# 2. Histórias de Usuário

## EPIC 1 - Acesso e Segurança

### US01: Autenticação e acesso ao sistema
Como usuário do sistema\
Quero me autenticar com e-mail e senha\
Para acessar minhas funcionalidades de acordo com meu perfil

### US02: Controle de acesso por perfil
Como sistema\
Quero restringir funcionalidades por perfil de usuário\
Para garantir segurança e conformidade com LGPD

## EPIC 2 - Consultas e Agenda

### US03: Gerenciar disponibilidade médica
Como médico\
Quero definir e bloquear meus horários de atendimento\
Para controlar minha disponibilidade de consultas

### US04: Agendar consulta
Como paciente\
Quero agendar uma consulta em um horário disponível\
Para receber atendimento médico

### US05: Gerenciar minhas consultas
Como paciente ou médico\
Quero visualizar, reagendar ou cancelar consultas\
Para manter controle da agenda

## EPIC 3 - Redução de No-Show

### US06: Lembrete automático de consulta
Como sistema\
Quero enviar lembretes automáticos antes da consulta\
Para reduzir faltas (no-show)

### US07: Confirmação de presença
Como paciente\
Quero confirmar minha presença na consulta\
Para ajudar a clínica a organizar a agenda

### US08: Registro de no-show
Como sistema\
Quero registrar quando um paciente não comparece\
Para gerar histórico de comportamento e métricas

---

# 3. Requisitos Funcionais

## Autenticação

### RF001 - Autenticação de usuários

O sistema deve permitir autenticação por e-mail e senha.

### RF002 - Autorização

O sistema deve controlar acesso com base no perfil do usuário (paciente, médico, administrador).

### RF003 - Renovação de sessão

O sistema deve permitir renovação de tokens de acesso.

## Gestão de Pacientes

### RF004 - Cadastro de pacientes

O sistema deve permitir cadastro de pacientes.

### RF005 - Consulta de pacientes

O sistema deve permitir consulta de pacientes cadastrados.

### RF006 - Atualização de pacientes

O sistema deve permitir atualização de dados de pacientes.

### RF007 - Inativação de pacientes

O sistema deve permitir inativar pacientes sem remoção física.

## Gestão de Médicos

### RF008 - Cadastro de médicos

O sistema deve permitir cadastro de médicos.

### RF009 - Consulta de médicos

O sistema deve permitir consulta de médicos.

### RF010 - Atualização de médicos

O sistema deve permitir atualização de médicos.

### RF011 - Inativação de médicos

O sistema deve permitir inativar médicos sem remoção física.

## Agenda Médica

### RF012 - Configuração de disponibilidade médica

O sistema deve permitir que médicos configurem seus horários disponíveis.

### RF013 - Bloqueio de agenda

O sistema deve permitir bloqueio de períodos indisponíveis.

### RF014 - Consulta de disponibilidade

O sistema deve retornar horários disponíveis para agendamento considerando regras e bloqueios.

## Consultas

### RF015 - Agendamento de consultas

O sistema deve permitir que pacientes agendem consultas com médicos disponíveis.

### RF016 - Reagendamento de consultas

O sistema deve permitir alteração de data e horário de consultas.

### RF017 - Cancelamento de consultas

O sistema deve permitir cancelamento de consultas respeitando políticas de prazo.

### RF018 - Consulta de consultas

O sistema deve permitir consulta de consultas por paciente ou médico.

### RF019 - Atualização de status da consulta

O sistema deve permitir atualização de status da consulta.

Status:
- Agendada
- Confirmada
- Realizada
- Cancelada
- Não Compareceu

## Redução de No-Show

### RF020 - Envio de lembretes automáticos

O sistema deve enviar lembretes automáticos antes da consulta.

### RF021 - Confirmação de consulta

O sistema deve permitir que pacientes confirmem presença na consulta.

### RF022 - Registro de no-show

O sistema deve registrar automaticamente quando um paciente não comparece.

## Relatórios e Métricas

### RF023 - Relatório de consultas

O sistema deve fornecer dados sobre consultas realizadas, canceladas e faltas.

### RF024 - Relatório de ocupação

O sistema deve fornecer dados sobre ocupação da agenda médica.

### RF025 - Relatório de no-show

O sistema deve fornecer dados sobre taxa de faltas dos pacientes.

---

# 4. Requisitos Não Funcionais

### RNF001
A API deve seguir o padrão REST.

### RNF002
A API deve retornar respostas no formato JSON.

### RNF003
A API deve utilizar autenticação baseada em JWT.

### RNF004
A API deve registrar logs de auditoria para operações críticas, incluindo acesso e alteração de dados sensíveis.

### RNF005
A API deve possuir documentação no padrão OpenAPI/Swagger.

### RNF006
A API deve utilizar paginação em todas as listagens que possam retornar grandes volumes de dados.

### RNF007
A API deve validar todos os dados recebidos antes do processamento.

### RNF008
A API deve armazenar senhas utilizando algoritmos de hash seguro (ex: bcrypt ou equivalente).

### RNF009
A API deve utilizar migrações para versionamento e controle de evolução do banco de dados.

### RNF010
A API deve garantir controle de acesso baseado em perfis (RBAC), restringindo acesso a dados de acordo com o tipo de usuário (paciente, médico, administrador).

---

# 5. Regras De Negócio

## Regras de Conflito de Agenda

### RN001
Um médico não pode ter duas consultas no mesmo horário.

### RN002
Um paciente não pode ter duas consultas no mesmo horário.

### RN003
Consultas só podem ser criadas em horários disponíveis.

### RN004
Consultas não podem ser criadas em períodos bloqueados.

## Regras de Estado de Entidades

### RN005
Consultas só podem ser criadas para médicos ativos.

### RN006
Consultas só podem ser criadas para pacientes ativos.

## Regras de Ciclo de Vida da Consulta

### RN007
Consultas realizadas não podem ser reagendadas.

### RN008
Consultas realizadas não podem ser canceladas.

### RN009
Consultas canceladas não podem ser marcadas como realizadas.

## Regras de Tempo e Duração

### RN010
A duração padrão de uma consulta é de 30 minutos.

### RN011
Cancelamentos devem respeitar política de antecedência mínima definida pela clínica.

## Regras de Acesso Funcional (LGPD)

### RN012
Um paciente só pode visualizar e gerenciar suas próprias consultas.

### RN013
Um médico só pode visualizar sua própria agenda e suas consultas.

## Regras de No-Show

### RN014
Uma consulta é marcada como "Não Compareceu" se o paciente não confirmar ou não comparecer.

###  RN015
Lembretes devem ser enviados automaticamente antes da consulta.

---

# 6. Entidades

### User

```text
    id: UUID
    name: string
    email: string
    password: string
    role: enum (ADMIN | RECEPTIONIST | PATIENT | DOCTOR)

    createdAt: datetime
    updatedAt: datetime
```

### Patient

```text
    id: UUID
    userId: UUID | null

    name: string
    cpf: string
    birthDate: date
    phone: string
    email: string
    active: boolean

    createdAt: datetime
    updatedAt: datetime
```

### Doctor

```text
    id: UUID
    userId: UUID | null

    name: string
    crm: string
    specialtyId: UUID
    active: boolean

    createdAt: datetime
    updatedAt: datetime
```

### Specialty

```text
    id: UUID
    name: string
    description: string

    createdAt: datetime
    updatedAt: datetime
```

### Schedule

```text
    id: UUID
    doctorId: UUID

    weekday: enum (MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY)
    startTime: time
    endTime: time

    createdAt: datetime
    updatedAt: datetime
```

### ScheduleBlock

```text
    id: UUID
    doctorId: UUID

    startDateTime: datetime
    endDateTime: datetime
    reason: string

    createdAt: datetime
    updatedAt: datetime
```

### Appointment

```text
    id: UUID

    patientId: UUID
    doctorId: UUID

    startDateTime: datetime
    endDateTime: datetime

    status: enum ( SCHEDULED | CONFIRMED | COMPLETED | CANCELLED | NO_SHOW )

    confirmationStatus: enum ( PENDING | CONFIRMED | DECLINED )

    notes: string | null

    reminderSentAt: datetime | null
    confirmedAt: datetime | null
    cancelledAt: datetime | null
    noShowAt: datetime | null

    createdAt: datetime
    updatedAt: datetime
```

### Notification

```text
    id: UUID

    userId: UUID
    appointmentId: UUID | null

    type: enum (EMAIL | SMS | WHATSAPP)
    status: enum (PENDING | SENT | FAILED)

    message: string

    sentAt: datetime | null

    createdAt: datetime
    updatedAt: datetime
```

### AuditLog
```text
    id: UUID

    userId: UUID

    action: string
    entity: string
    entityId: UUID

    timestamp: datetime

    ipAddress: string | null
    userAgent: string | null

    metadata: string | json

    createdAt: datetime
```

---

# 7. Relações
```text
    User → Patient (1:0..1)
    User → Doctor (1:0..1)

    Doctor → Specialty (N:1)

    Doctor → Schedule (1:N)
    Doctor → ScheduleBlock (1:N)
    Doctor → Appointment (1:N)

    Patient → Appointment (1:N)

    Appointment → Notification (1:N)
    User → AuditLog (1:N)
```

---

# 8. Endpoints

### Auth
```html
    POST /auth/login
    POST /auth/refresh
    GET  /auth/me
```

### Patients
```html
    GET    /patients
    POST   /patients
    GET    /patients/:id
    PUT    /patients/:id
    DELETE /patients/:id
```

### Doctors
```html
    GET    /doctors
    POST   /doctors
    GET    /doctors/:id
    PUT    /doctors/:id
    DELETE /doctors/:id
```

### Specialties
```html
    GET    /specialties
    POST   /specialties
    PUT    /specialties/:id
    DELETE /specialties/:id
```

### Availability
```html
    GET /doctors/:id/availability
    GET /doctors/:id/schedule
    POST /schedule-blocks
    GET /schedule-blocks
```

### Appointments
Criação e consulta
```html
    POST /appointments
    GET  /appointments
    GET  /appointments/:id
```
Fluxo de negócio
```html
    PATCH /appointments/:id/confirm
    PATCH /appointments/:id/cancel
    PATCH /appointments/:id/reschedule
    PATCH /appointments/:id/no-show
```

### Notifications
```html
    POST /notifications/send
    GET  /notifications
    GET  /notifications/:id
```

### Reports
```html
    GET /reports/no-show
    GET /reports/appointments
    GET /reports/occupancy
```