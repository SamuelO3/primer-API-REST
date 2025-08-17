from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello world"}

@app.get("/Saludar")
def get_saludo(nombre: str):
    return{"message": f"Hola, {nombre}!" }
