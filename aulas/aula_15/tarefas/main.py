from collections.abc import Generator, Sequence
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import Engine
from sqlmodel import Field, Session, SQLModel, create_engine, select


class TaferaBase(SQLModel):
    nome: str
    descricao: str


class Tarefa(TaferaBase, table=True):
    id_: int | None = Field(default=None, primary_key=True)


class TarefaCreate(TaferaBase):
    pass


class TarefaRead(TaferaBase):
    id_: int


class TarefaUpdate(SQLModel):
    nome: str | None
    descricao: str | None


engine: Engine = create_engine(url="sqlite:///tarefas.db", echo=False)


def get_session() -> Generator[Session]:
    with Session(bind=engine) as session:
        yield session


def create_db_and_tables() -> None:
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)


SessionDep = Annotated[Session, Depends(dependency=get_session)]
app = FastAPI(lifespan=create_db_and_tables())


@app.post(path="/tarefas", status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: TarefaCreate, session: SessionDep) -> TarefaRead:
    nova_tarefa = Tarefa(nome=tarefa.nome, descricao=tarefa.descricao)
    session.add(instance=nova_tarefa)
    session.commit()
    session.refresh(instance=nova_tarefa)
    return TarefaRead.model_validate(obj=nova_tarefa)


@app.get(path="/tarefas")
def ler_tarefas(session: SessionDep) -> list[TarefaRead]:
    tarefas: Sequence[Tarefa] = session.exec(statement=select(Tarefa)).all()
    return [TarefaRead.model_validate(obj=tarefa) for tarefa in tarefas]


@app.get(path="/tarefas/{id_}")
def ler_tarefa(id_: int, session: SessionDep) -> TarefaRead:
    tarefa: Tarefa | None = session.get(entity=Tarefa, ident=id_)
    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada",
        )
    return TarefaRead.model_validate(obj=tarefa)


@app.patch(path="/tarefas/{id_}")
def atualizar_tarefa(
    id_: int,
    tarefa_atualizada: TarefaUpdate,
    session: SessionDep,
) -> TarefaRead:
    tarefa: Tarefa | None = session.get(entity=Tarefa, ident=id_)
    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada",
        )
    tarefa_data: dict[str, str | int] = tarefa_atualizada.model_dump(exclude_unset=True)
    for key, value in tarefa_data.items():
        setattr(tarefa, key, value)
    session.merge(instance=tarefa)
    session.commit()
    session.refresh(instance=tarefa)
    return TarefaRead.model_validate(tarefa)


@app.delete(path="/tarefas/{id_}")
def remover_tarefa(id_: int, session: SessionDep) -> dict[str, str]:
    tarefa: Tarefa | None = session.get(entity=Tarefa, ident=id_)
    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada",
        )
    session.delete(instance=tarefa)
    session.commit()
    return {"detail": "Tarefa removida com sucesso"}
