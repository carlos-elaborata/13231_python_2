from minha_classe import MinhaClasse


def test_dobrar() -> None:
    obj = MinhaClasse(valor=5)
    assert obj.dobrar() == 10
