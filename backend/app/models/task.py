from sqlalchemy.orm import registry, mapped_column, Mapped

table_registry = registry()

@table_registry.mapped_as_dataclass()
class Task:
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)