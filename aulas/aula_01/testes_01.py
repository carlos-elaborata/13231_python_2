class Carro:
    def __init__(self, modelo: str, cor: str, ano: int = 2025) -> None:
        self.modelo: str = modelo
        self.cor: str = cor
        self.ano: int = ano
        self.ligado: bool = False

    def ligar(self) -> None:
        if not self.ligado:
            print(f"{self.modelo} {self.cor} foi ligado.")
            self.ligado = True
        else:
            print(f"{self.modelo} {self.cor} já está ligado.")

    def desligar(self) -> None:
        if self.ligado:
            print(f"{self.modelo} {self.cor} foi desligado.")
            self.ligado = False
        else:
            print(f"{self.modelo} {self.cor} já está desligado.")


honda_fit = Carro(modelo="Honda Fit", cor="Laranja", ano=2017)
ferrari_296 = Carro(modelo="Ferrari 296", cor="Amarelo", ano=2024)
novo_carro = Carro(modelo="X", cor="Verde")

honda_fit.ligar()
honda_fit.ligar()
ferrari_296.ligar()

print(honda_fit.cor)
print(honda_fit.ano)
print(honda_fit.ligado)
honda_fit.desligar()
print(honda_fit.ligado)

honda_fit.cor = "Azul"
honda_fit.ligar()
