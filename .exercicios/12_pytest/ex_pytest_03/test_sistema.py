import pytest
from produto import Produto
from venda import Venda


@pytest.mark.parametrize(
    ("nome", "preco", "estoque"),
    [
        ("Laptop", 2500, 10),
        ("Mouse", 25, 50),
        ("Teclado", 100, 20),
        ("Monitor", 700, 15),
        ("Impressora", 450, 5),
    ],
)
def test_criar_produto(nome: str, preco: float, estoque: int) -> None:
    produto = Produto(nome=nome, preco=preco, estoque=estoque)
    assert produto.nome == nome
    assert produto.preco == preco
    assert produto.estoque == estoque


@pytest.mark.parametrize(
    ("estoque_inicial", "quantidade_adicionar", "estoque_final"),
    [
        (10, 5, 15),
        (10, -5, 10),
        (10, 0, 10),
        (1, 1, 2),
    ],
)
def test_adicionar_estoque(
    estoque_inicial: int,
    quantidade_adicionar: int,
    estoque_final: int,
) -> None:
    produto = Produto(nome="Laptop", preco=2500, estoque=estoque_inicial)
    produto.adicionar_estoque(quantidade=quantidade_adicionar)
    assert produto.estoque == estoque_final


def test_remover_estoque(
    estoque_inicial: int,
    quantidade_remover: int,
    estoque_final: int,
) -> None:
    pass


def test_remover_estoque_excecao(estoque: int, quantidade_remover: int) -> None:
    pass


def test_criar_venda(
    estoque_inicial: int,
    quantidade_venda: int,
    estoque_final: int,
    valor_total: float,
) -> None:
    pass


def test_venda_excecao(
    estoque: int,
    quantidade: int,
    erro: type[Exception],
    msg: str,
) -> None:
    pass
