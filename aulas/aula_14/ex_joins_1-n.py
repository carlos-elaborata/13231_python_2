from sqlalchemy import Engine, ForeignKey, ScalarResult, Select, create_engine, select
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    joinedload,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    pass


class Departamento(Base):
    __tablename__: str = "departamento"

    id_: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)

    funcionarios: Mapped[list["Funcionario"]] = relationship(
        back_populates="departamento",
        cascade="all, delete-orphan",
    )


class Funcionario(Base):
    __tablename__: str = "funcionario"

    id_: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    departamento_fk: Mapped[int] = mapped_column(ForeignKey(column="departamento.id_"))

    departamento: Mapped[Departamento] = relationship(back_populates="funcionarios")


engine: Engine = create_engine(url="sqlite:///ex_1_n.db", echo=False)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session, session.begin():
    departamento_rh = Departamento(nome="RH")
    departamento_ti = Departamento(nome="TI")

    funcionario_1 = Funcionario(nome="Pedro", departamento=departamento_rh)
    funcionario_2 = Funcionario(nome="André", departamento=departamento_ti)
    funcionario_3 = Funcionario(nome="Gustavo", departamento=departamento_rh)

    session.add_all(
        instances=[
            departamento_rh,
            departamento_ti,
            funcionario_1,
            funcionario_2,
            funcionario_3,
        ],
    )


with Session(bind=engine) as session:
    select_stmt: Select[tuple[Funcionario]] = select(Funcionario).options(
        joinedload(Funcionario.departamento),
    )

    result: ScalarResult[Funcionario] = session.scalars(statement=select_stmt)
    for funcionario in result:
        print(
            f"Nome: {funcionario.nome}, Departamento: {funcionario.departamento.nome}",
        )
