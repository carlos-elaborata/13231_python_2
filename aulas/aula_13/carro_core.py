from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    delete,
    insert,
    select,
    update,
)

if TYPE_CHECKING:
    from sqlalchemy import (
        Delete,
        Engine,
        Insert,
        MappingResult,
        Result,
        RowMapping,
        Select,
        Update,
    )


@dataclass
class Carro:
    id_: int | None
    marca: str
    modelo: str
    placa: str
    cor: str


metadata = MetaData()


tabela_carro = Table(
    "carro",
    metadata,
    Column("id_", Integer, primary_key=True, autoincrement=True),
    Column("marca", String, nullable=False),
    Column("modelo", String, nullable=False),
    Column("placa", String, nullable=False, unique=True),
    Column("cor", String, nullable=False),
)


def criar_tabela(engine: "Engine") -> None:
    with engine.connect() as conn:
        tabela_carro.drop(bind=conn, checkfirst=True)
        tabela_carro.create(bind=conn, checkfirst=True)


def inserir_carro(
    engine: "Engine",
    marca: str,
    modelo: str,
    placa: str,
    cor: str,
) -> Carro:
    insert_stmt: Insert = insert(table=tabela_carro).values(
        marca=marca,
        modelo=modelo,
        placa=placa,
        cor=cor,
    )

    with engine.begin() as conn:
        result: Result[Any] = conn.execute(statement=insert_stmt)
        inserted_id: int = result.lastrowid
        return Carro(id_=inserted_id, marca=marca, modelo=modelo, placa=placa, cor=cor)


def selecionar_todos_carros(engine: "Engine") -> list[Carro]:
    select_all_stmt: Select[Any] = select(tabela_carro)

    with engine.connect() as conn:
        result: MappingResult = conn.execute(statement=select_all_stmt).mappings()

        return [
            Carro(
                id_=row["id_"],
                marca=row["marca"],
                modelo=row["modelo"],
                placa=row["placa"],
                cor=row["cor"],
            )
            for row in result
        ]


def selecionar_carro_por_id(engine: "Engine", carro_id: int) -> Carro | None:
    select_by_id_stmt: Select[Any] = select(tabela_carro).where(
        tabela_carro.c.id_ == carro_id,
    )

    with engine.connect() as conn:
        result: RowMapping | None = (
            conn.execute(statement=select_by_id_stmt).mappings().first()
        )
        if result:
            return Carro(
                id_=result["id_"],
                marca=result["marca"],
                modelo=result["modelo"],
                placa=result["placa"],
                cor=result["cor"],
            )
        return None


def atualizar_carro(
    engine: "Engine",
    carro_id: int,
    marca: str,
    modelo: str,
    placa: str,
    cor: str,
) -> bool:
    update_stmt: Update = (
        update(table=tabela_carro)
        .where(tabela_carro.c.id_ == carro_id)
        .values(marca=marca, modelo=modelo, placa=placa, cor=cor)
    )

    with engine.begin() as conn:
        result: Result[Any] = conn.execute(statement=update_stmt)
        return result.rowcount > 0


def deletar_carro(engine: "Engine", carro_id: int) -> bool:
    delete_stmt: Delete = delete(table=tabela_carro).where(
        tabela_carro.c.id_ == carro_id,
    )

    with engine.begin() as conn:
        result: Result[Any] = conn.execute(statement=delete_stmt)
        return result.rowcount > 0


engine: "Engine" = create_engine(url="sqlite:///carro_core.db", echo=False)

criar_tabela(engine=engine)

carro_1: Carro = inserir_carro(
    engine=engine,
    marca="Toyota",
    modelo="Corolla",
    placa="AAA-1111",
    cor="Azul",
)

carro_2: Carro = inserir_carro(
    engine=engine,
    marca="Chevrolet",
    modelo="Onix",
    placa="BBB-2222",
    cor="Branco",
)

todos_carros: list[Carro] = selecionar_todos_carros(engine=engine)
print("Todos os carros:")
for carro in todos_carros:
    print(carro)

carro_especifico: Carro | None = selecionar_carro_por_id(
    engine=engine,
    carro_id=1,
)
if carro_especifico:
    print("Carro com ID específico:")
    print(carro_especifico)

if atualizar_carro(
    engine=engine,
    carro_id=1,
    marca="Honda",
    modelo="Civic",
    placa="AAA-1111",
    cor="Preto",
):
    print("Carro atualizado com sucesso.")

if deletar_carro(engine=engine, carro_id=2):
    print("Carro removido com sucesso.")
