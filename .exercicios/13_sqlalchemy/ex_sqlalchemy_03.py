"""Exercício 03.

Refaça o exerício 01 usando ORM.
"""

from sqlalchemy import Engine, ScalarResult, Select, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Cliente(Base):
    __tablename__: str = "cliente"

    id_: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    cpf: Mapped[str] = mapped_column(nullable=False, unique=True)
    endereco: Mapped[str] = mapped_column(nullable=False)
    renda: Mapped[float] = mapped_column(nullable=False)


def criar_tabela(engine: "Engine") -> None:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def inserir_cliente(
    engine: "Engine",
    nome: str,
    cpf: str,
    endereco: str,
    renda: float,
) -> Cliente:
    with Session(bind=engine, expire_on_commit=False) as session, session.begin():
        novo_cliente = Cliente(nome=nome, cpf=cpf, endereco=endereco, renda=renda)
        session.add(instance=novo_cliente)
        return novo_cliente


def selecionar_todos_clientes(engine: "Engine") -> list[Cliente]:
    select_all_stmt: Select[tuple[Cliente]] = select(Cliente)

    with Session(bind=engine) as session:
        result: ScalarResult[Cliente] = session.scalars(statement=select_all_stmt)
        return list(result)


def selecionar_cliente_por_id(engine: "Engine", cliente_id: int) -> Cliente | None:
    with Session(bind=engine) as session:
        return session.get(entity=Cliente, ident=cliente_id)


def selecionar_clientes_por_renda(
    engine: "Engine",
    renda_min: float,
    renda_max: float,
) -> list[Cliente]:
    select_by_renda_stmt: Select[tuple[Cliente]] = (
        select(Cliente)
        .where(Cliente.renda > renda_min)
        .where(Cliente.renda <= renda_max)
    )

    with Session(bind=engine) as session:
        result: ScalarResult[Cliente] = session.scalars(statement=select_by_renda_stmt)
        return list(result)


database_uri = "sqlite:///ex_03_cliente.db"

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
