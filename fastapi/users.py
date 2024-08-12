from fastapi import FastAPI
from pydantic import BaseModel # type: ignore

app = FastAPI()

#entidad usuario

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id= 1, name= 'Brais', surname= 'moure', url= 'https://www.animefenix.tv/zerotwo', age= 35),
              User(id= 2, name= 'Hakuna', surname= 'matata', url= 'https://www.animefenix.tv/zerotwo', age= 40),
              User(id= 3, name= 'Brais2', surname= 'moure2', url= 'https://www.animefenix.tv/zerotwo', age= 38)]

#paginas a las que se podra ingresar

#construccion de los datos a mano
@app.get("/usersjson")
async def usersjson():
    return [{"id": 1,'name': 'Brais', 'surname': 'moure', 'url': 'https://www.animefenix.tv/zerotwo', 'age': 35},
            {"id": 2,'name': 'Hakuna', 'surname': 'matata', 'url': 'https://www.animefenix.tv/zerotwo', 'age': 40}]

@app.get('/users')
async def users():
    return users_list


def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0] 
        
    except:
        return {"error":"No se a encontrado el usuario"}


@app.get('/user/{id}')
async def user(id: int): 
    return search_user(id)

#llamado de datos por query osea /user/1
@app.get('/user/')
async def user(id: int):
    return search_user(id)
    
#para añadir un nuevo usuario
@app.post('/user/')
async def user(user:User):
    if type(search_user(user.id)) == User:
        return {'error':'El usuario ya existe'}
    else:
        users_list.append(user)
        return user

@app.put("/user/")
async def user(user:User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user 
            found = True

    if not found:
        return {'error':'El usuario no se ha actualizado'}
    else:
        return user