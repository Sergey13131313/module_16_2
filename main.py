from fastapi import FastAPI, Path
from typing import Annotated

from typing_extensions import deprecated

app = FastAPI()

@app.get("/")
async def read_root():
    return "Главная"

@app.get('/user/admin')
async def admin_page() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def id_page(user_id: Annotated[int, Path(ge=1, le=100, description='Номер пользователоя', example='50')]) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user/{username}/{age}')
async def user(username: Annotated[str, Path(min_length=5, max_length=20, description='Имя ползователя', example='Иван')],
               age: Annotated[int, Path(ge=18, le=120, description='Возраст пользователя', example='50')])->str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


if __name__ == "__main__":

    print(type(Path()))
    import uvicorn
    uvicorn.run(app, host="127.0.0.2", port=8000)