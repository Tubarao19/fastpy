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

#entidad que se usa como base de datos de prueba, construccion de los datos con base en la clase
users_list = [User(id= 1, name= 'Brais', surname= 'moure', url= 'https://www.animefenix.tv/zerotwo', age= 35),
              User(id= 2, name= 'Hakuna', surname= 'matata', url= 'https://www.animefenix.tv/zerotwo', age= 40),
              User(id= 3, name= 'Brais2', surname= 'moure2', url= 'https://www.animefenix.tv/zerotwo', age= 38)]

#paginas a las que se podra ingresar

#construccion de los datos a mano
@app.get("/usersjson")
async def usersjson():
    return [{'name': 'Brais', 'surname': 'moure', 'url': 'https://www.animefenix.tv/zerotwo', 'age': 35},
            {'name': 'Hakuna', 'surname': 'matata', 'url': 'https://www.animefenix.tv/zerotwo', 'age': 40}]

@app.get('/users')
async def users():
    return users_list

#funcion que externa para realizar un tipo de busqueda desde cualquier otra funcion 
#todo esto con el fin de que se puede repetir esto mismo es mejor solo realizarlo una vez 
#y hacer su respectivo llamado    
def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)#filter puede devolver varios objetos
    try:
        return list(users)[0] #devuelve mas de un usuario
        #el 0 es para que aparezca el primer resultado de la busqueda
    except:
        return {"error":"No se a encontrado el usuario"}

#se le pueden añadir parametros a la ruta los cuales se van a capturar
#en este caso el id el cual es el mismo nombre que usaremos de identificacion
#mostrado en el modelo de la clase USER lo cual cambia la ruta y la funcion 
#de users a user para tener sentido al llamar a un unico usuario
@app.get('/user/{id}')
async def user(id: int): #se lee id dentro de la funcion como un parametro tipado
    return search_user(id)#llamado de la funcion que realiza algo especifico usado multiples veces

#llamado de datos por query osea /user/1
@app.get('/user/')
async def user(id: int):
    return search_user(id)
    
