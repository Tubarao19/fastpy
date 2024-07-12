from fastapi import FastAPI
from pydantic import BaseModel # type: ignore

app = FastAPI()

class Users(BaseModel):
	name: str
	surname: str
	url: str
	age: int

#entidad que se usa como base de datos de prueba
users_list = [Users(name= 'Brais', surname= 'moure', url= 'https://www.animefenix.tv/zerotwo', age= 35)]


@app.get("/usersjson")
async def usersjson():
    return [{'name': 'Brais', 'surname': 'moure', 'url': 'https://www.animefenix.tv/zerotwo', 'age': 35},
            {'name': 'Hakuna', 'surname': 'matata', 'url': 'https://www.animefenix.tv/zerotwo', 'age': 40}]

@app.get('/users')
async def users():
      return users_list