# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.
from enum import Enum
from typing import Optional

import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
movies = []


class Genre(Enum):
    BOEVIK = "боевик"
    FANTASTICA = "фантастика"
    COMEDIA = "комедия"


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: Genre


class MovieIn(BaseModel):
    title: str
    description: str
    genre: Genre


@app.post("/movie/", response_model=Movie)
async def create_movie(new_movie: MovieIn):
    movies.append(
        Movie(
            id=len(movies) + 1,
            title=new_movie.title,
            description=new_movie.description,
            genre=new_movie.genre,
        )
    )
    return movies[-1]


@app.get("/movies/{genre}", response_model=list[Movie])
async def get_movies(genre: Genre):
    result = []
    for movie in movies:
        if movie.genre == genre:
            result.append(movie)
        return result


if __name__ == "__main__":
    uvicorn.run("task_2:app", host="127.0.0.1", port=8000, reload=True)
