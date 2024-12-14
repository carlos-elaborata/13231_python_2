from pydantic import BaseModel, ValidationError


class Pessoa(BaseModel):
    nome: str
    idade: int
    altura: float


try:
    pessoa = Pessoa(nome="João", idade=30, altura=1.75)
    pessoa = Pessoa(nome="João", idade="trinta", altura=1.75)
except ValidationError as e:
    print(f"Erro de validação: {e}")
