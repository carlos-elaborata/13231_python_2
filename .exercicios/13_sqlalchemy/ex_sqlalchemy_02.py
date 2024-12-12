"""Exercício 02.

Refaça o exerício 01 usando Core.
"""

from dataclasses import dataclass
from typing import Any

from sqlalchemy import (
    DECIMAL,
    Column,
    Engine,
    Insert,
    Integer,
    MappingResult,
    MetaData,
    Result,
    RowMapping,
    Select,
    String,
    Table,
    create_engine,
    insert,
    select,
)


@dataclass
class Cliente:
    id_: int | None
    nome: str
    cpf: str
    endereco: str
    renda: float


metadata = MetaData()

tabela_cliente = Table(
    "cliente",
    metadata,
    Column("id_", Integer, primary_key=True, autoincrement=True),
    Column("nome", String, nullable=False),
    Column("cpf", String, nullable=False, unique=True),
    Column("endereco", String, nullable=False),
    Column("renda", DECIMAL, nullable=False),
)


def criar_tabela(engine: "Engine") -> None:
    with engine.connect() as conn:
        tabela_cliente.drop(bind=conn, checkfirst=True)
        tabela_cliente.create(bind=conn, checkfirst=True)


def inserir_cliente(
    engine: "Engine",
    nome: str,
    cpf: str,
    endereco: str,
    renda: float,
) -> Cliente:
    insert_stmt: Insert = insert(table=tabela_cliente).values(
        nome=nome,
        cpf=cpf,
        endereco=endereco,
        renda=renda,
    )

    with engine.begin() as conn:
        result: Result[Any] = conn.execute(statement=insert_stmt)
        conn.commit()
        inserted_id: int = result.lastrowid

        return Cliente(
            id_=inserted_id,
            nome=nome,
            cpf=cpf,
            endereco=endereco,
            renda=renda,
        )


def selecionar_todos_clientes(engine: "Engine") -> list[Cliente]:
    select_all_stmt: Select[Any] = select(tabela_cliente)

    with engine.connect() as conn:
        result: MappingResult = conn.execute(statement=select_all_stmt).mappings()

        return [
            Cliente(
                id_=row["id_"],
                nome=row["nome"],
                cpf=row["cpf"],
                endereco=row["endereco"],
                renda=row["renda"],
            )
            for row in result
        ]


def selecionar_cliente_por_id(engine: "Engine", cliente_id: int) -> Cliente | None:
    select_by_id_stmt: Select[Any] = select(tabela_cliente).where(
        tabela_cliente.c.id_ == cliente_id,
    )

    with engine.connect() as conn:
        result: RowMapping | None = (
            conn.execute(statement=select_by_id_stmt).mappings().first()
        )
        if result is None:
            return None

        return Cliente(
            id_=result["id_"],
            nome=result["nome"],
            cpf=result["cpf"],
            endereco=result["endereco"],
            renda=result["renda"],
        )


def selecionar_clientes_por_renda(
    engine: "Engine",
    renda_min: float,
    renda_max: float,
) -> list[Cliente]:
    select_by_renda_stmt: Select[Any] = (
        select(tabela_cliente)
        .where(tabela_cliente.c.renda > renda_min)
        .where(tabela_cliente.c.renda <= renda_max)
    )

    with engine.connect() as conn:
        result: MappingResult = conn.execute(statement=select_by_renda_stmt).mappings()

        return [
            Cliente(
                id_=row["id_"],
                nome=row["nome"],
                cpf=row["cpf"],
                endereco=row["endereco"],
                renda=row["renda"],
            )
            for row in result
        ]


database_uri = "sqlite:///ex_02_cliente.db"

engine: "Engine" = create_engine(url=database_uri, echo=True)

criar_tabela(engine=engine)

cliente_1: Cliente = inserir_cliente(
    engine=engine,
    nome="João de Almeida",
    cpf="111.111.111-11",
    endereco="Rua A, 123",
    renda=1300,
)
cliente_2: Cliente = inserir_cliente(
    engine=engine,
    nome="Maria Helena",
    cpf="222.222.222-22",
    endereco="Rua B, 456",
    renda=1500,
)
cliente_3: Cliente = inserir_cliente(
    engine=engine,
    nome="Carlos Ulisses",
    cpf="333.333.333-33",
    endereco="Rua C, 789",
    renda=1000,
)

todos_clientes: list[Cliente] = selecionar_todos_clientes(engine=engine)
print("Todos os clientes:")
for cliente in todos_clientes:
    print(
        f"ID: {cliente.id_}"
        f"\n  Nome: {cliente.nome}"
        f"\n  CPF: {cliente.cpf}"
        f"\n  Endereço: {cliente.endereco}"
        f"\n  Renda: R$ {cliente.renda:.2f}\n",
    )


cliente_id: int = 1
cliente_especifico: Cliente | None = selecionar_cliente_por_id(
    engine=engine,
    cliente_id=cliente_id,
)

if cliente_especifico:
    print("Cliente com ID específico:")
    print(
        f"Cliente com ID: {cliente_id}"
        f"\n  Nome: {cliente_especifico.nome}"
        f"\n  CPF: {cliente_especifico.cpf}"
        f"\n  Endereço: {cliente_especifico.endereco}"
        f"\n  Renda: R$ {cliente_especifico.renda:.2f}\n",
    )


renda_min = 1200
renda_max = 1500
clientes_filtrados: list[Cliente] = selecionar_clientes_por_renda(
    engine=engine,
    renda_min=renda_min,
    renda_max=renda_max,
)
print(f"Clientes com renda entre R$ {renda_min:.2f} e R$ {renda_max:.2f}:")
for cliente in clientes_filtrados:
    print(
        f"ID: {cliente.id_}"
        f"\n  Nome: {cliente.nome}"
        f"\n  CPF: {cliente.cpf}"
        f"\n  Endereço: {cliente.endereco}"
        f"\n  Renda: R$ {cliente.renda:.2f}\n",
    )
