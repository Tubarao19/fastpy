from fastapi import FastAPI
from pydantic import BaseModel # type: ignore

app = FastAPI()

#entidad usuario

class User(BaseModel):
	name: str
	surname: str
	url: str
	age: int

#entidad que se usa como base de datos de prueba, construccion de los datos con base en la clase
users_list = [User(name= 'Brais', surname= 'moure', url= 'https://www.animefenix.tv/zerotwo', age= 35),
              User(name= 'Hakuna', surname= 'matata', url= 'https://www.animefenix.tv/zerotwo', age= 40),
              User(name= 'Brais2', surname= 'moure2', url= 'https://www.animefenix.tv/zerotwo', age= 38)]

#paginas a las que se podra ingresar

#construccion de los datos a mano
@app.get("/usersjson")
async def usersjson():
    return [{'name': 'Brais', 'surname': 'moure', 'url': 'https://www.animefenix.tv/zerotwo', 'age': 35},
            {'name': 'Hakuna', 'surname': 'matata', 'url': 'https://www.animefenix.tv/zerotwo', 'age': 40}]

@app.get('/users')
async def users():
      return users_list