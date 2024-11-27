class Quarto:
    def __init__(self, numero: int, tipo: str) -> None:
        self.numero: int = numero
        self.tipo: str = tipo
        self.disponivel: bool = True

    def reservar_quarto(self) -> str:
        if self.disponivel:
            self.disponivel = False

            return f"Quarto {self.numero} reservado com sucesso."

        return f"Quanto {self.numero} não está disponível para reserva."

    def liberar_quarto(self) -> str:
        if not self.disponivel:
            self.disponivel = True

            return f"Quarto {self.numero} liberado com sucesso."

        return f"Quarto {self.numero} já está disponível."

    def verificar_disponibilidade(self) -> str:
        if self.disponivel:
            return f"Quarto {self.numero} está disponível para reserva."
        return f"Quarto {self.numero} não está disponível para reserva."
