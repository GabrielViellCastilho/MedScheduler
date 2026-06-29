## Alembic

### Criar uma migration

Gera uma nova migration comparando os modelos da aplicação com o estado atual do banco.

```bash
alembic revision --autogenerate -m "nome_da_migration"
```

Exemplo:

```bash
alembic revision --autogenerate -m "create_users_table"
```

---

### Executar as migrations

Aplica todas as migrations pendentes no banco de dados.

```bash
alembic upgrade head
```
