from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from requests import Response

# resposta: "Response" = requests.get(url="https://httpbin.org/get", timeout=10)
# print(resposta.text)
# print(resposta.status_code)
# print(resposta.headers)
# for chave, valor in resposta.json().items():
#     print(f"{chave}: {valor}")

# payload: dict[str, str] = {"chave_1": "valor_1", "chave_2": "valor_2"}
# resposta: "Response" = requests.post(
#     url="https://google.com/",
#     data=payload,
#     timeout=10,
# )
# print(resposta.text)
# print(resposta.headers)
# print(resposta.status_code)


# payload: dict[str, str] = {"chave_1": "valor_1", "chave_2": "valor_2"}
# resposta: "Response" = requests.put(
#     url="https://httpbin.org/put",
#     data=payload,
#     timeout=10,
# )
# print(resposta.text)
# print(resposta.headers)
# print(resposta.status_code)


# payload: dict[str, str] = {"chave_1": "valor_1", "chave_2": "valor_2"}
# resposta: "Response" = requests.patch(
#     url="https://httpbin.org/patch",
#     data=payload,
#     timeout=10,
# )
# print(resposta.text)
# print(resposta.headers)
# print(resposta.status_code)


# resposta: "Response" = requests.delete(
#     url="https://httpbin.org/delete",
#     timeout=10,
# )
# print(resposta.text)
# print(resposta.headers)
# print(resposta.status_code)


# resposta: "Response" = requests.head(
#     url="https://httpbin.org/get",
#     timeout=10,
# )
# print(resposta.headers)
# print(resposta.status_code)


# resposta: "Response" = requests.options(
#     url="https://httpbin.org/get",
#     timeout=10,
# )
# print(resposta.headers)
# print(resposta.status_code)


# headers: dict[str, str] = {
#     "User-Agent": "MeuNavegador/1.0",
#     "Accept": "application/json",
#     "Authorization": "Bearer token_de_autenticacao",
# }
# resposta: "Response" = requests.get(
#     url="https://httpbin.org/get",
#     headers=headers,
#     timeout=10,
# )
# print(resposta.status_code)
# print(resposta.headers)
# print(resposta.text)


resposta: "Response" = requests.get(
    url="https://httpbin.org/basic-auth/usuario_batman/senha_abacate",
    auth=("usuario_batman", "senha_abacate"),
    timeout=10,
)

print(resposta.status_code)
print(resposta.headers)
print(resposta.text)
