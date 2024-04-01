from fastapi import APIRouter

from db import users, database


router = APIRouter()


@router.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(
            username=f"user{i}", email=f"mail{i}@mail.ru", password=f"password{i}"
        )
        await database.execute(query)
        return {"message": f"{count} fake users create"}
