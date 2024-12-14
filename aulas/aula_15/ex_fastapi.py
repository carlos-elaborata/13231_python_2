from fastapi import FastAPI

app = FastAPI()


@app.get(path="/teste")
def teste() -> dict[str, str]:
    return {"mensagem": "Olá, Mundo!"}


@app.get(path="/")
def root() -> str:
    return "Página inicial"
