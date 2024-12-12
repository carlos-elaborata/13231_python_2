"""Exercício 01.

Crie uma estrutura de classes para a entidade Cliente.
    a. A entidade Cliente possui os atributos: nome, cpf, endereço e renda;
    b. Utilizando SQLAlchemy, criar a estrutura de uma tabela cliente;
    c. Inserir novos clientes no banco de dados;
    d. Selecionar todos os clientes;
    e. Selecionar um cliente específico pelo ID;
    f. Selecionar clientes cuja renda seja maior que R$ 1200 e menor ou igual a R$ 1500.
"""

from dataclasses import dataclass
from typing import Any

from sqlalchemy import (
    Engine,
    MappingResult,
    Result,
    RowMapping,
    TextClause,
    create_engine,
    text,
)


@dataclass
class Cliente:
    id_: int | None
    nome: str
    cpf: str
    endereco: str
    renda: float


def criar_tabela(engine: "Engine") -> None:
    drop_table_sql: TextClause = text(text="DROP TABLE IF EXISTS cliente;")
    create_table_sql: TextClause = text(
        text="""CREATE TABLE IF NOT EXISTS cliente (
                    id_ INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf TEXT NOT NULL UNIQUE,
                    endereco TEXT NOT NULL,
                    renda REAL NOT NULL
        );""",
    )
    with engine.connect() as conn:
        conn.execute(statement=drop_table_sql)
        conn.execute(statement=create_table_sql)


def inserir_cliente(
    engine: "Engine",
    nome: str,
    cpf: str,
    endereco: str,
    renda: float,
) -> Cliente:
    insert_sql: TextClause = text(
        text="""INSERT INTO cliente (nome, cpf, endereco, renda)
                VALUES (:nome, :cpf, :endereco, :renda)""",
    )

    with engine.connect() as conn:
        result: Result[Any] = conn.execute(
            statement=insert_sql,
            parameters={
                "nome": nome,
                "cpf": cpf,
                "endereco": endereco,
                "renda": renda,
            },
        )
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
    select_all_sql: TextClause = text(text="SELECT * FROM cliente;")

    with engine.connect() as conn:
        result: MappingResult = conn.execute(statement=select_all_sql).mappings()

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
    select_by_id_sql: TextClause = text(
        text="""SELECT *
                FROM cliente
                WHERE id_ = :id_;""",
    )

    with engine.connect() as conn:
        result: RowMapping | None = (
            conn.execute(
                statement=select_by_id_sql,
                parameters={"id_": cliente_id},
            )
            .mappings()
            .first()
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
    select_by_renda_sql: TextClause = text(
        text="""SELECT *
                FROM cliente
                WHERE renda > :renda_min
                    AND renda <= :renda_max;""",
    )

    with engine.connect() as conn:
        result: MappingResult = conn.execute(
            statement=select_by_renda_sql,
            parameters={"renda_min": renda_min, "renda_max": renda_max},
        ).mappings()

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


database_uri = "sqlite:///ex_01_cliente.db"

engine: "Engine" = create_engine(url=database_uri, echo=False)

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
