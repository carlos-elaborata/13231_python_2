class Pato:
    def emitir_som(self) -> None:
        print("Quack!")

    def mover(self) -> None:
        print("O pato está nadando.")


class Galinha:
    def emitir_som(self) -> None:
        print("Cócóró!")

    def mover(self) -> None:
        print("A galinha está ciscando.")


class Cachorro:
    def emitir_som(self) -> None:
        print("Au au!")

    def mover(self) -> None:
        print("O cachorro está correndo.")


class Gato:
    def emitir_som(self) -> None:
        print("Miau!")

    def mover(self) -> None:
        print("O gato está andando silenciosamente.")


def interagir_com_animal(animal: Pato | Galinha | Cachorro | Gato) -> None:
    animal.emitir_som()
    animal.mover()
    print("-" * 30)


animais: list[Pato | Galinha | Cachorro | Gato] = [
    Pato(),
    Galinha(),
    Cachorro(),
    Gato(),
]

for animal in animais:
    interagir_com_animal(animal=animal)
