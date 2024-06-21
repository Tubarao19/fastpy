from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return 'Hola fastapi'

@app.get("/url")
async def root():
    return { "url_curso":"https://www.udemy.com/" }

