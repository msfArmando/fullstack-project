# Pytasks - Gerenciador de tarefas #
## Em desenvolvimento... ##

Projeto full-stack com React e FastAPI

## Comandos alembic ##

- poetry run alembic init migrations
- poetry run alembic revision --autogenerate -m "..."

No env.py, importar
- table_registry do model
- classe Settings, do base settings

Definir abaixo do config:
- config.set_main_option('sqlalchemy.url', Settings().database_url)

Atribuir o table_registry.metadata ao target_metadata

---

Aula atual: https://www.youtube.com/watch?v=XzRwKgdfUY0