from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from requests import Response

resposta: "Response" = requests.get(url="http://127.0.0.1:8000/teste", timeout=10)

print(resposta.json())
