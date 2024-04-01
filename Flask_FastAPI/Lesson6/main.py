# Перечень принимаемых функцией Field параметров
#
# ● default: значение по умолчанию для поля
# ● alias: альтернативное имя для поля (используется при сериализации и десериализации)
# ● title: заголовок поля для генерации документации API
# ● description: описание поля для генерации документации API
# ● gt: ограничение на значение поля (больше указанного значения)
# ● ge: ограничение на значение поля (больше или равно указанному значению)
# ● lt: ограничение на значение поля (меньше указанного значения)
# ● le: ограничение на значение поля (меньше или равно указанному значению)
# ● multiple_of: ограничение на значение поля (должно быть кратно указанному значению)
# ● max_length: ограничение на максимальную длину значения поля
# ● min_length: ограничение на минимальную длину значения поля
# ● regex: регулярное выражение, которому должно соответствовать значение поля
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

#
# app = FastAPI()
#
#
# class Item(BaseModel):
#     name: str = Field(title="Name", max_length=50)
#     price: float = Field(title="Price", gt=0, le=100000)
#     description: str = Field(default=None, title="Description", max_length=1000)
#     tax: float = Field(0, title="Tax", ge=0, le=10)
#
#
# class User(BaseModel):
#     username: str = Field(title="Username", max_length=50)
#     full_name: str = Field(None, title="Full Name", max_length=100)
#
#
# @app.post("/items/")
# async def create_item(item: Item):
#     return {"item": item}

# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


# Операции CRUD — это основные функции, которые используются в любом
# приложении, управляемом базой данных. Они используются для создания, чтения,
# обновления и удаления данных из базы данных. В FastAPI с SQLAlchemy ORM мы
# можем создавать эти операции, используя функции и методы Python.
# ● CREATE, Создать: добавление новых записей в базу данных.
# ● READ, Чтение: получение записей из базы данных.
# ● UPDATE, Обновление: изменение существующих записей в базе данных.
# ● DELETE, Удалить: удаление записей из базы данных.

import databases
import sqlalchemy
from fastapi import FastAPI

DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


app = FastAPI


# @app.get("/fake_users/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(name=f"user{i}", email=f"mail{i}@mail.ru")
#         await database.execute(query)
#     return {"message": f"{count} fake users create"}


# ➢Создание пользователя в БД, create
@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


# ➢Чтение пользователей из БД, read
@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


# ➢Чтение одного пользователя из БД, read
@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


# ➢Обновление пользователя в БД, update
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


# ➢Удаление пользователя из БД, delete
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"message": "User deleted"}
