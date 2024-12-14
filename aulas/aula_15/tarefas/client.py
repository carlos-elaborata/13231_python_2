import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT_TAREFAS = "tarefas/"


def criar_tarefa(nome: str, descricao: str) -> dict[str, str | int]:
    url: str = f"{BASE_URL}{ENDPOINT_TAREFAS}"
    data: dict[str, str] = {"nome": nome, "descricao": descricao}
    resposta = requests.post(url=url, json=data, timeout=10)
    return resposta.json()


def obter_todas_tarefas() -> list[dict[str, str | int]]:
    url: str = f"{BASE_URL}{ENDPOINT_TAREFAS}"
    resposta = requests.get(url=url, timeout=10)
    return resposta.json()


print("Tarefas criadas:")
nova_tarefa_1: dict[str, str | int] = criar_tarefa(
    nome="Comprar pão",
    descricao="Ir à padaria e comprar pão",
)
print(
    f"{nova_tarefa_1['id_']}.\n  Nome: {nova_tarefa_1['nome']}\n  Descrição: "
    f"{nova_tarefa_1['descricao']}",
)

nova_tarefa_2: dict[str, str | int] = criar_tarefa(
    nome="Ir à farmácia",
    descricao="Ir à farmácia e retirar os medicamentos",
)
print(
    f"\n{nova_tarefa_2['id_']}.\n  Nome: {nova_tarefa_2['nome']}\n  Descrição: "
    f"{nova_tarefa_2['descricao']}",
)

tarefas: list[dict[str, str | int]] = obter_todas_tarefas()
print("\nTodas as tarefas:")
for tarefa in tarefas:
    print(
        f"{tarefa['id_']}.\n  Nome: {tarefa['nome']}\n  Descrição: "
        f"{tarefa['descricao']}",
    )
