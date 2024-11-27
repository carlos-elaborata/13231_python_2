from quartos import Quarto

quarto_101 = Quarto(numero=101, tipo="simples")
quarto_201 = Quarto(numero=201, tipo="duplo")
quarto_301 = Quarto(numero=301, tipo="suíte")

print(quarto_101.verificar_disponibilidade())
print(quarto_201.verificar_disponibilidade())
print(quarto_301.verificar_disponibilidade(), "\n")

print(quarto_101.reservar_quarto())
print(quarto_201.reservar_quarto())
print(quarto_301.reservar_quarto(), "\n")

print(quarto_101.reservar_quarto(), "\n")

print(quarto_101.liberar_quarto())
print(quarto_201.liberar_quarto(), "\n")

print(quarto_201.liberar_quarto(), "\n")

print(quarto_101.verificar_disponibilidade())
print(quarto_201.verificar_disponibilidade())
print(quarto_301.verificar_disponibilidade())
