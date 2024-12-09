def soma(a: float, b: float) -> float:
    try:
        resultado: float = float(a) + float(b)
    except TypeError as e:
        msg: str = "Os argumentos devem ser números inteiros ou decimais."
        raise TypeError(msg) from e
    except ValueError as e:
        msg: str = "Ocorreu um erro ao somar os argumentos."
        raise ValueError(msg) from e

    return resultado
