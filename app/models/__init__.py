from app.backend.db import Base, engine
from app.models.user import User
from app.models.task import Task
from sqlalchemy.schema import CreateTable

# Создаем все таблицы
Base.metadata.create_all(bind=engine)

# Печатаем SQL запросы для создания таблиц
print(CreateTable(User.__table__).compile(engine))
print(CreateTable(Task.__table__).compile(engine))
