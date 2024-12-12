from typing import TYPE_CHECKING

from sqlalchemy import ScalarResult, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

if TYPE_CHECKING:
    from sqlalchemy import Engine, Select


class Base(DeclarativeBase):
    pass


class Carro(Base):
    __tablename__: str = "carro"

    id_: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    marca: Mapped[str] = mapped_column(nullable=False)
    modelo: Mapped[str] = mapped_column(nullable=False)
    placa: Mapped[str] = mapped_column(nullable=False, unique=True)
    cor: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"Carro(id_={self.id_}, marca={self.marca!r}, modelo={self.modelo!r}, "
            f"placa={self.placa!r}, cor={self.cor!r})"
        )


def criar_tabela(engine: "Engine") -> None:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def inserir_carro(
    engine: "Engine",
    marca: str,
    modelo: str,
    placa: str,
    cor: str,
) -> Carro:
    with Session(bind=engine, expire_on_commit=False) as session, session.begin():
        novo_carro = Carro(marca=marca, modelo=modelo, placa=placa, cor=cor)
        session.add(instance=novo_carro)
        return novo_carro


def selecionar_todos_carros(engine: "Engine") -> list[Carro]:
    select_all_stmt: Select[tuple[Carro]] = select(Carro)

    with Session(bind=engine) as session:
        result: ScalarResult[Carro] = session.scalars(statement=select_all_stmt)
        return list(result)


def selecionar_carro_por_id(engine: "Engine", carro_id: int) -> Carro | None:
    with Session(bind=engine) as session:
        return session.get(entity=Carro, ident=carro_id)


def atualizar_carro(
    engine: "Engine",
    carro_id: int,
    marca: str,
    modelo: str,
    placa: str,
    cor: str,
) -> bool:
    with Session(bind=engine) as session, session.begin():
        carro: Carro | None = session.get(entity=Carro, ident=carro_id)
        if carro is None:
            return False
        carro.marca = marca
        carro.modelo = modelo
        carro.placa = placa
        carro.cor = cor
        return True


def deletar_carro(engine: "Engine", carro_id: int) -> bool:
    with Session(bind=engine) as session, session.begin():
        carro: Carro | None = session.get(entity=Carro, ident=carro_id)
        if carro is None:
            return False
        session.delete(instance=carro)
        return True


engine: "Engine" = create_engine(url="sqlite:///carro_orm.db", echo=False)

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
    placa="AAA-1112",
    cor="Preto",
):
    print("Carro atualizado com sucesso.")

if deletar_carro(engine=engine, carro_id=2):
    print("Carro removido com sucesso.")
