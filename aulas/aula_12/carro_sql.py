from dataclasses import dataclass

from sqlalchemy import Engine, Row, create_engine, text

engine: Engine = create_engine(url="sqlite:///carro_sql.db")


@dataclass
class Carro:
    marca: str
    modelo: str
    placa: str
    cor: str
    id_: int | None = None


with engine.connect() as conn:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS carro (
        id_ INTEGER PRIMARY KEY,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        placa TEXT NOT NULL,
        cor TEXT NOT NULL
    )
    """
    conn.execute(statement=text(text="DROP TABLE IF EXISTS carro"))
    conn.execute(statement=text(text=create_table_query))


def create_carro(marca: str, modelo: str, placa: str, cor: str) -> Carro:
    with engine.begin() as conn:
        create_carro_query: str = """
        INSERT INTO carro (marca, modelo, placa, cor)
        VALUES (:marca, :modelo, :placa, :cor)
        """
        conn.execute(
            statement=text(text=create_carro_query),
            parameters={
                "marca": marca,
                "modelo": modelo,
                "placa": placa,
                "cor": cor,
            },
        )
        last_id_query = "SELECT last_insert_rowid()"
        carro_id: int | None = conn.execute(statement=text(text=last_id_query)).scalar()

    return Carro(marca=marca, modelo=modelo, placa=placa, cor=cor, id_=carro_id)


def read_carro(id_: int) -> Carro | None:
    with engine.connect() as conn:
        read_carro_query: str = "SELECT * FROM carro WHERE id_ = :id_"
        result: Row | None = conn.execute(
            statement=text(text=read_carro_query),
            parameters={"id_": id_},
        ).first()
        if result:
            return Carro(
                id_=result.id_,
                marca=result.marca,
                modelo=result.modelo,
                placa=result.placa,
                cor=result.cor,
            )
        return None


def update_carro(carro: Carro) -> None:
    with engine.begin() as conn:
        update_carro_query: str = """
        UPDATE carro
        SET marca = :marca, modelo = :modelo, placa = :placa, cor = :cor
        WHERE id_ = :id_
        """
        conn.execute(
            statement=text(text=update_carro_query),
            parameters={
                "marca": carro.marca,
                "modelo": carro.modelo,
                "placa": carro.placa,
                "cor": carro.cor,
                "id_": carro.id_,
            },
        )


def delete_carro(id_: int) -> None:
    with engine.begin() as conn:
        delete_carro_query: str = "DELETE FROM carro WHERE id_ = :id_"
        conn.execute(statement=text(text=delete_carro_query), parameters={"id_": id_})


carro: Carro | None = create_carro(
    marca="Toyota",
    modelo="Corolla",
    placa="ABC1234",
    cor="Azul",
)
print(carro)
carro = read_carro(id_=1)
if carro:
    print(f"Carro original: {carro}")
    carro.cor = "Vermelho"
    update_carro(carro=carro)
    carro = read_carro(id_=1)
    if carro:
        print(f"Carro atualizado: {carro}")
delete_carro(id_=1)
