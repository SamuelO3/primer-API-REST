from fastapi import FastAPI
from faker import Faker

app = FastAPI()
faker = Faker()

@app.get("/")
def read_root():
    return {"message": "Hello world"}

@app.get("/Saludar")
def get_saludo(nombre: str):
    return{"message": f"Hola, {nombre}!" }

#Ruta raiz
@app.get('/')
def read_root():
    return {'message': 'Hello World'}

#Metodo para generar una muestra falsa de usuarios y hacer la comprobacion del correcto funcionamiento del sistema
def generateUsers(n : int = 100):
    users = []
    for i in range(1, n+1):
        users.append({
            'id': i,
            'name': faker.name(),
            'email': faker.email,
            'city' : faker.city
        })
    return users

#Metodo para listar realizado con get
@app.get('/users')
def listUsers():
    return generateUsers()