class ListaPersonalizada:
    def __init__(self, elementos: list[str]) -> None:
        self.elementos: list[str] = elementos

    def __getitem__(self, indice: int) -> str:
        return self.elementos[indice].capitalize()

    def __setitem__(self, indice: int, valor: str) -> None:
        self.elementos[indice] = valor.lower()

    def __delitem__(self, indice: int) -> None:
        # del self.elementos[0]
        self.elementos[indice] = "removido"

    def __str__(self) -> str:
        return f"[{', '.join(self.elementos)}]"


minha_lista = ListaPersonalizada(elementos=["banana", "maça", "laranja", "abaxaxi"])
print(minha_lista[1])
minha_lista[2] = "UVA"
print(minha_lista)

del minha_lista[0]
print(minha_lista)
