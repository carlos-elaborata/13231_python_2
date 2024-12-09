# pyright: reportArgumentType=false

import pytest
from ex_pytest_01 import adicionar_tarefa, lista_tarefas

MSG_TYPE_ERROR = "A tarefa deve ser uma string."


def inicializar_lista() -> None:
    lista_tarefas.clear()


def test_adicionar_tarefa() -> None:
    inicializar_lista()
    adicionar_tarefa(nova_tarefa="Tarefa 1")
    assert lista_tarefas == ["Tarefa 1"]
    assert len(lista_tarefas) == 1


def test_adicionar_tarefas_multiplas() -> None:
    inicializar_lista()
    adicionar_tarefa(nova_tarefa="Tarefa 1")
    adicionar_tarefa(nova_tarefa="Tarefa 2")
    assert lista_tarefas == ["Tarefa 1", "Tarefa 2"]
    assert len(lista_tarefas) == 2


def test_adicionar_tarefa_com_espacos() -> None:
    inicializar_lista()
    adicionar_tarefa(nova_tarefa="   Tarefa 1   ")
    assert lista_tarefas == ["   Tarefa 1   "]
    assert len(lista_tarefas) == 1


def test_adicionar_tarefa_vazia() -> None:
    inicializar_lista()
    adicionar_tarefa(nova_tarefa="")
    assert lista_tarefas == [""]
    assert len(lista_tarefas) == 1


def test_lista_vazia() -> None:
    inicializar_lista()
    assert lista_tarefas == []
    assert len(lista_tarefas) == 0


def test_adicionar_tarefa_com_caracteres_especiais() -> None:
    inicializar_lista()
    adicionar_tarefa(nova_tarefa="!@#$% Tarefa 1 %$#@!")
    assert lista_tarefas == ["!@#$% Tarefa 1 %$#@!"]
    assert len(lista_tarefas) == 1


def test_adicionar_tarefa_com_unicode() -> None:
    inicializar_lista()
    adicionar_tarefa(nova_tarefa="タスク")
    assert lista_tarefas == ["タスク"]
    assert len(lista_tarefas) == 1


def test_adicionar_varias_tarefas() -> None:
    inicializar_lista()
    for i in range(10):
        adicionar_tarefa(nova_tarefa=f"Tarefa {i + 1}")
    assert lista_tarefas == [f"Tarefa {i + 1}" for i in range(10)]
    assert len(lista_tarefas) == 10


def test_adicionar_tarefas_em_alta_frequencia() -> None:
    inicializar_lista()
    for i in range(1000):
        adicionar_tarefa(nova_tarefa=f"Tarefa {i + 1}")
    assert lista_tarefas == [f"Tarefa {i + 1}" for i in range(1000)]
    assert len(lista_tarefas) == 1000


def test_adicionar_tarefa_string_longa() -> None:
    inicializar_lista()
    tarefa_longa: str = "a" * 10000
    adicionar_tarefa(nova_tarefa=tarefa_longa)
    assert lista_tarefas == [tarefa_longa]
    assert len(lista_tarefas) == 1


def test_adicionar_tarefa_duplicada() -> None:
    inicializar_lista()
    adicionar_tarefa(nova_tarefa="Tarefa 1")
    adicionar_tarefa(nova_tarefa="Tarefa 1")
    assert lista_tarefas == ["Tarefa 1", "Tarefa 1"]
    assert len(lista_tarefas) == 2


def test_adicionar_tarefa_com_nova_linha() -> None:
    inicializar_lista()
    adicionar_tarefa(nova_tarefa="Tarefa\n1")
    assert lista_tarefas == ["Tarefa\n1"]
    assert len(lista_tarefas) == 1


def test_adicionar_tarefa_com_tabulacao() -> None:
    inicializar_lista()
    adicionar_tarefa(nova_tarefa="Tarefa\t1")
    assert lista_tarefas == ["Tarefa\t1"]
    assert len(lista_tarefas) == 1


def test_adicionar_tarefa_com_caracteres_de_escape() -> None:
    inicializar_lista()
    adicionar_tarefa(nova_tarefa="Tarefa\n\t1")
    assert lista_tarefas == ["Tarefa\n\t1"]
    assert len(lista_tarefas) == 1


def test_adicionar_tarefa_none() -> None:
    inicializar_lista()
    with pytest.raises(expected_exception=TypeError, match=MSG_TYPE_ERROR):
        adicionar_tarefa(nova_tarefa=None)


def test_adicionar_tarefa_inteiro() -> None:
    inicializar_lista()
    with pytest.raises(expected_exception=TypeError, match=MSG_TYPE_ERROR):
        adicionar_tarefa(nova_tarefa=123)


def test_adicionar_tarefa_lista() -> None:
    inicializar_lista()
    with pytest.raises(expected_exception=TypeError, match=MSG_TYPE_ERROR):
        adicionar_tarefa(nova_tarefa=["Tarefa"])


def test_adicionar_tarefa_dicionario() -> None:
    inicializar_lista()
    with pytest.raises(expected_exception=TypeError, match=MSG_TYPE_ERROR):
        adicionar_tarefa(nova_tarefa={"tarefa": "Tarefa 1"})


def test_adicionar_tarefa_float() -> None:
    inicializar_lista()
    with pytest.raises(expected_exception=TypeError, match=MSG_TYPE_ERROR):
        adicionar_tarefa(nova_tarefa=12.34)


def test_adicionar_tarefa_booleano() -> None:
    inicializar_lista()
    with pytest.raises(expected_exception=TypeError, match=MSG_TYPE_ERROR):
        adicionar_tarefa(nova_tarefa=False)
