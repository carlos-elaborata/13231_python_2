from collections.abc import Sequence

from sqlalchemy import Engine, ForeignKey, Select, create_engine, select
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


class AlunoCurso(Base):
    __tablename__: str = "aluno_curso"

    aluno_id: Mapped[int] = mapped_column(
        ForeignKey(column="aluno.id_"),
        primary_key=True,
    )
    curso_id: Mapped[int] = mapped_column(
        ForeignKey(column="curso.id_"),
        primary_key=True,
    )


class Aluno(Base):
    __tablename__: str = "aluno"

    id_: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)

    cursos: Mapped[list["Curso"]] = relationship(
        secondary="aluno_curso",
        back_populates="alunos",
    )


class Curso(Base):
    __tablename__: str = "curso"

    id_: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(nullable=False)

    alunos: Mapped[list[Aluno]] = relationship(
        secondary="aluno_curso",
        back_populates="cursos",
    )


engine: Engine = create_engine(url="sqlite:///ex_m_n.db", echo=False)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session, session.begin():
    curso_1 = Curso(titulo="Matemática")
    curso_2 = Curso(titulo="História")
    curso_3 = Curso(titulo="Geografia")

    aluno_1 = Aluno(nome="Ana")
    aluno_2 = Aluno(nome="Bruno")

    aluno_1.cursos.append(curso_1)
    aluno_1.cursos.append(curso_2)
    aluno_2.cursos.append(curso_2)
    aluno_2.cursos.append(curso_3)

    session.add_all(instances=[aluno_1, aluno_2, curso_1, curso_2, curso_3])

with Session(bind=engine) as session:
    select_stmt: Select[tuple[Aluno]] = select(Aluno).options(joinedload(Aluno.cursos))
    alunos: Sequence[Aluno] = (
        session.execute(statement=select_stmt).unique().scalars().all()
    )

for aluno in alunos:
    cursos_titulos: str = ", ".join(curso.titulo for curso in aluno.cursos)
    print(f"Aluno: {aluno.nome}, Cursos: {cursos_titulos}")
