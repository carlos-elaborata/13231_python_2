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

payload: dict[str, str] = {"chave_1": "valor_1", "chave_2": "valor_2"}
resposta: "Response" = requests.post(
    url="https://httpbin.org/post",
    data=payload,
    timeout=10,
)
print(resposta.text)
print(resposta.headers)
print(resposta.status_code)
