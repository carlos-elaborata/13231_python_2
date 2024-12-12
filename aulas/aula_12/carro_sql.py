from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from sqlalchemy import create_engine, text

if TYPE_CHECKING:
    from sqlalchemy import Engine, MappingResult, Result, RowMapping, TextClause


@dataclass
class Carro:
    id_: int | None
    marca: str
    modelo: str
    placa: str
    cor: str


def criar_tabela(engine: "Engine") -> None:
    drop_table_sql: TextClause = text(text="DROP TABLE IF EXISTS carro;")
    create_table_sql: TextClause = text(
        text="""CREATE TABLE IF NOT EXISTS carro (
                    id_ INTEGER PRIMARY KEY AUTOINCREMENT,
                    marca TEXT NOT NULL,
                    modelo TEXT NOT NULL,
                    placa TEXT NOT NULL UNIQUE,
                    cor TEXT NOT NULL
                );""",
    )
    with engine.connect() as conn:
        conn.execute(statement=drop_table_sql)
        conn.execute(statement=create_table_sql)


def inserir_carro(
    engine: "Engine",
    marca: str,
    modelo: str,
    placa: str,
    cor: str,
) -> Carro:
    insert_sql: TextClause = text(
        text="""INSERT INTO carro (marca, modelo, placa, cor)
                VALUES (:marca, :modelo, :placa, :cor);""",
    )

    with engine.connect() as conn:
        result: Result[Any] = conn.execute(
            statement=insert_sql,
            parameters={"marca": marca, "modelo": modelo, "placa": placa, "cor": cor},
        )
        inserted_id: int = result.lastrowid
        return Carro(id_=inserted_id, marca=marca, modelo=modelo, placa=placa, cor=cor)


def selecionar_todos_carros(engine: "Engine") -> list[Carro]:
    select_all_stmt: TextClause = text(text="SELECT * FROM carro;")

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
    select_by_id_sql: TextClause = text(
        text="""SELECT *
                FROM carro
                WHERE id_ = :id_""",
    )

    with engine.connect() as conn:
        result: RowMapping | None = (
            conn.execute(
                statement=select_by_id_sql,
                parameters={"id_": carro_id},
            )
            .mappings()
            .first()
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
    update_sql: TextClause = text(
        text="""UPDATE carro
                SET marca = :marca, modelo = :modelo, placa = :placa, cor = :cor
                WHERE id_ = :id_;""",
    )
    with engine.begin() as conn:
        result: Result[Any] = conn.execute(
            statement=update_sql,
            parameters={
                "id_": carro_id,
                "marca": marca,
                "modelo": modelo,
                "placa": placa,
                "cor": cor,
            },
        )
        return result.rowcount > 0


def deletar_carro(engine: "Engine", carro_id: int) -> bool:
    delete_sql: TextClause = text(text="DELETE FROM carro WHERE id_ = :id_")
    with engine.begin() as conn:
        result: Result[Any] = conn.execute(
            statement=delete_sql,
            parameters={"id_": carro_id},
        )
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
