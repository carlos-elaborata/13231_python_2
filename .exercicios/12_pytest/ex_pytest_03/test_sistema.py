# pyright: reportArgumentType=false

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


@pytest.mark.parametrize(
    ("estoque_inicial", "quantidade_remover", "estoque_final"),
    [
        (10, 5, 5),
        (10, 10, 0),
        (50, 25, 25),
        (1, 1, 0),
    ],
)
def test_remover_estoque(
    estoque_inicial: int,
    quantidade_remover: int,
    estoque_final: int,
) -> None:
    produto = Produto(nome="Laptop", preco=2500, estoque=estoque_inicial)
    produto.remover_estoque(quantidade=quantidade_remover)
    assert produto.estoque == estoque_final


@pytest.mark.parametrize(
    ("estoque", "quantidade_remover"),
    [
        (10, 15),
        (5, 10),
        (0, 1),
    ],
)
def test_remover_estoque_excecao(estoque: int, quantidade_remover: int) -> None:
    produto = Produto(nome="Laptop", preco=2500, estoque=estoque)
    with pytest.raises(
        expected_exception=ValueError,
        match="Quantidade solicitada maior que o estoque disponível.",
    ):
        produto.remover_estoque(quantidade=quantidade_remover)
    assert produto.estoque == estoque


@pytest.mark.parametrize(
    ("estoque_inicial", "quantidade_venda", "valor_total", "estoque_final"),
    [
        (10, 2, 5000, 8),
        (10, 10, 25000, 0),
        (20, 5, 12500, 15),
        (5, 1, 2500, 4),
    ],
)
def test_criar_venda(
    estoque_inicial: int,
    quantidade_venda: int,
    valor_total: float,
    estoque_final: int,
) -> None:
    produto = Produto(nome="Laptop", preco=2500, estoque=estoque_inicial)
    venda = Venda(produto=produto, quantidade=quantidade_venda)
    assert venda.produto == produto
    assert venda.quantidade == quantidade_venda
    assert venda.valor_total == valor_total
    assert produto.estoque == estoque_final


@pytest.mark.parametrize(
    ("estoque", "quantidade", "erro", "msg"),
    [
        (2, 3, ValueError, "Estoque insuficiente para a venda."),
        (5, 10, ValueError, "Estoque insuficiente para a venda."),
        (1, 2, ValueError, "Estoque insuficiente para a venda."),
        (1, -1, ValueError, "A quantidade de venda deve ser positiva."),
        (10, 0, ValueError, "A quantidade de venda deve ser positiva."),
        (10, None, TypeError, "Quantidade não pode ser None."),
        (None, 1, TypeError, "Produto não pode ser None."),
    ],
)
def test_venda_excecao(
    estoque: int,
    quantidade: int,
    erro: type[Exception],
    msg: str,
) -> None:
    produto: Produto | None = (
        Produto(nome="Laptop", preco=2500, estoque=estoque)
        if estoque is not None
        else None
    )
    with pytest.raises(expected_exception=erro, match=msg):
        Venda(produto=produto, quantidade=quantidade)

    if produto:
        assert produto.estoque == estoque
