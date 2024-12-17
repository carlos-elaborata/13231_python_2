from abc import ABC
from typing import Generic, TypeVar

from database import SessionDep
from fastapi import HTTPException, status
from sqlmodel import SQLModel, select

# Define uma variável genérica para tipos concretos, restringindo para subtipos de
# SQLModel
T = TypeVar("T", bound=SQLModel)

# Define uma variável genérica para tipos de leitura, também para subtipos de SQLModel
R = TypeVar("R", bound=SQLModel)


class CRUDBase(ABC, Generic[T, R]):
    """Classe base genérica para operações CRUD.

    Attributes:
        model (type[T]): O modelo principal da entidade.
        read_model (type[R]): O modelo utilizado para leitura da entidade.
    """

    def __init__(self, model: type[T], read_model: type[R]) -> None:
        """Inicializa a classe CRUDBase.

        Args:
            model (type[T]): Modelo principal da entidade.
            read_model (type[R]): Modelo utilizado para leitura.
        """
        # Armazena o modelo principal da entidade
        self.model: type[T] = model

        # Armazena o modelo utilizado para leitura
        self.read_model: type[R] = read_model

    def create(self, session: SessionDep, obj_model: SQLModel) -> R:
        """Cria um novo registro no banco de dados.

        Args:
            session (SessionDep): Sessão de banco de dados.
            obj_model (SQLModel): Dados do registro a ser criado.

        Returns:
            R: Objeto criado no formato do modelo de leitura.
        """
        # Valida os dados fornecidos pelo usuário usando o modelo
        validated_data: SQLModel = obj_model.model_validate(obj=obj_model)

        # Cria uma instância do modelo validado
        obj: T = self.model.model_validate(obj=validated_data)

        # Adiciona o objeto à sessão do banco de dados
        session.add(instance=obj)

        # Persiste o objeto no banco de dados
        session.commit()

        # Atualiza o objeto com informações do banco, como IDs gerados
        session.refresh(instance=obj)

        # Retorna o objeto criado no formato do modelo de leitura
        return self.read_model.model_validate(obj=obj)

    def read_by_id(self, session: SessionDep, obj_id: int) -> T:
        """Lê um registro do banco de dados pelo ID.

        Args:
            session (SessionDep): Sessão de banco de dados.
            obj_id (int): ID do registro a ser lido.

        Raises:
            HTTPException: Caso o registro não seja encontrado.

        Returns:
            T: Objeto encontrado no banco de dados.
        """
        # Busca o objeto pelo ID no banco de dados
        obj: T | None = session.get(entity=self.model, ident=obj_id)

        # Verifica se o objeto não foi encontrado
        if not obj:
            # Lança uma exceção HTTP 404 indicando que o registro não foi encontrado
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.model.__name__} não encontrado.",
            )

        # Retorna o objeto encontrado
        return obj

    def read_all(self, session: SessionDep) -> list[T]:
        """Lê todos os registros da entidade.

        Args:
            session (SessionDep): Sessão de banco de dados.

        Returns:
            list[T]: Lista de todos os registros encontrados.
        """
        # Executa uma consulta para buscar todos os registros do modelo e retorna a
        # lista dos registros.
        return list(session.exec(statement=select(self.model)))

    def update(
        self,
        session: SessionDep,
        obj_id: int,
        obj_model: SQLModel,
        partial: bool = False,
    ) -> T:
        """Atualiza um registro no banco de dados, total ou parcialmente.

        Args:
            session (SessionDep): Sessão de banco de dados.
            obj_id (int): ID do registro a ser atualizado.
            obj_model (SQLModel): Dados atualizados do registro.
            partial (bool, optional): Indica se a atualização será parcial (True) ou
            total (False).

        Raises:
            HTTPException: Caso o registro não seja encontrado.

        Returns:
            T: Objeto atualizado.
        """
        # Busca o objeto no banco de dados pelo ID
        obj: T | None = session.get(entity=self.model, ident=obj_id)

        # Verifica se o objeto não foi encontrado no banco
        if not obj:
            # Lança uma exceção HTTP 404 indicando que o registro não foi encontrado
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.model.__name__} não encontrado.",
            )

        # Valida e extrai os dados fornecidos no modelo de entrada
        # - `exclude_unset=partial`: Se `partial` for True, somente os campos definidos
        #   no modelo serão validados e usados
        validated_date: dict[str, str | int] = obj_model.model_dump(
            exclude_unset=partial,
        )

        # Itera sobre os dados validados para aplicar as mudanças no objeto do banco
        for key, value in validated_date.items():
            # Atualiza o atributo correspondente no objeto com o novo valor
            setattr(obj, key, value)

        # Salva as alterações no banco
        session.commit()

        # Atualiza o objeto com os dados mais recentes salvos no banco
        session.refresh(instance=obj)

        # Retorna o objeto atualizado
        return obj

    def delete(self, session: SessionDep, obj_id: int) -> None:
        """Remove um registro do banco de dados.

        Args:
            session (SessionDep): Sessão de banco de dados.
            obj_id (int): ID do registro a ser removido.

        Raises:
            HTTPException: Caso o registro não seja encontrado.
        """
        # Busca o objeto no banco de dados pelo ID
        obj: T | None = session.get(entity=self.model, ident=obj_id)

        # Verifica se o objeto não foi encontrado no banco
        if not obj:
            # Lança uma exceção HTTP 404 indicando que o registro não foi encontrado
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.model.__name__} não encontrado.",
            )

        # Remove o objeto do banco de dados
        session.delete(instance=obj)

        # Persiste a exclusão no banco de dados
        session.commit()
