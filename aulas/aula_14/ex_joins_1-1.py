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


class Pessoa(Base):
    __tablename__: str = "pessoa"

    id_: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)

    passaporte: Mapped["Passaporte"] = relationship(
        back_populates="pessoa",
        uselist=False,
    )


class Passaporte(Base):
    __tablename__: str = "passaporte"

    id_: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    numero: Mapped[str] = mapped_column(nullable=False, unique=True)
    pessoa_fk: Mapped[int] = mapped_column(ForeignKey(column="pessoa.id_"))

    pessoa: Mapped[Pessoa] = relationship(back_populates="passaporte")


engine: Engine = create_engine(url="sqlite:///ex_1_1.db", echo=False)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    pessoa_1 = Pessoa(nome="Alice")
    passaporte_1 = Passaporte(numero="ABC1234", pessoa=pessoa_1)
    pessoa_2 = Pessoa(nome="Lucas")
    session.add_all(instances=[pessoa_1, passaporte_1, pessoa_2])
    session.commit()

with Session(bind=engine) as session:
    select_stmt: Select[tuple[Pessoa]] = select(Pessoa).options(
        joinedload(Pessoa.passaporte),
    )
    pessoas: ScalarResult[Pessoa] = session.scalars(statement=select_stmt).all()

    for pessoa in pessoas:
        if pessoa.passaporte:
            print(f"{pessoa.nome} possuí o passaporte {pessoa.passaporte.numero}.")
        else:
            print(f"{pessoa.nome} não possuí passaporte.")
