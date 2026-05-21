# Biblioteca Python da API Groq

**Idiomas / Languages:** [English](./README.md) · [中文](./README-ZH.md) · [Español](./README-ES.md) · [Français](./README-FR.md) · [Português](./README-PT.md) · [Русский](./README-RU.md) · [Deutsch](./README-DE.md)

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/groq.svg?label=pypi%20(stable))](https://pypi.org/project/groq/)

A biblioteca Python da Groq oferece acesso conveniente à API REST da Groq a partir de qualquer aplicação Python 3.10+. A biblioteca inclui definições de tipos para todos os parâmetros de requisição e campos de resposta, e oferece clientes síncronos e assíncronos baseados em [httpx](https://github.com/encode/httpx).

Ela é gerada com [Stainless](https://www.stainless.com/).

## Documentação

A documentação da API REST pode ser encontrada em [console.groq.com](https://console.groq.com/docs). A API completa desta biblioteca está em [api.md](api.md).

## Instalação

```sh
# install from PyPI
pip install groq
```

## Uso

A API completa desta biblioteca está em [api.md](api.md).

```python
import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    model="openai/gpt-oss-20b",
)
print(chat_completion.choices[0].message.content)
```

Embora seja possível fornecer um argumento de palavra-chave `api_key`, recomendamos usar [python-dotenv](https://pypi.org/project/python-dotenv/) para adicionar `GROQ_API_KEY="My API Key"` ao seu arquivo `.env`, de modo que sua chave de API não fique armazenada no controle de versão.

## Uso assíncrono

Basta importar `AsyncGroq` em vez de `Groq` e usar `await` em cada chamada à API:

```python
import os
import asyncio
from groq import AsyncGroq

client = AsyncGroq(
    api_key=os.environ.get("GROQ_API_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain the importance of low latency LLMs",
            }
        ],
        model="openai/gpt-oss-20b",
    )
    print(chat_completion.choices[0].message.content)


asyncio.run(main())
```

A funcionalidade entre os clientes síncrono e assíncrono é, de resto, idêntica.

### Com aiohttp

Por padrão, o cliente assíncrono usa `httpx` para requisições HTTP. No entanto, para melhor desempenho de concorrência, você também pode usar `aiohttp` como backend HTTP.

Você pode habilitar isso instalando `aiohttp`:

```sh
# install from PyPI
pip install groq[aiohttp]
```

Em seguida, habilite-o instanciando o cliente com `http_client=DefaultAioHttpClient()`:

```python
import os
import asyncio
from groq import DefaultAioHttpClient
from groq import AsyncGroq


async def main() -> None:
    async with AsyncGroq(
        api_key=os.environ.get("GROQ_API_KEY"),  # This is the default and can be omitted
        http_client=DefaultAioHttpClient(),
    ) as client:
        chat_completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Explain the importance of low latency LLMs",
                }
            ],
            model="openai/gpt-oss-20b",
        )
        print(chat_completion.id)


asyncio.run(main())
```

## Usando tipos

Parâmetros de requisição aninhados são [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). As respostas são [modelos Pydantic](https://docs.pydantic.dev), que também fornecem métodos auxiliares para coisas como:

- Serializar de volta para JSON, `model.to_json()`
- Converter para um dicionário, `model.to_dict()`

Requisições e respostas tipadas oferecem autocompletar e documentação no seu editor. Se quiser ver erros de tipo no VS Code para ajudar a detectar bugs mais cedo, defina `python.analysis.typeCheckingMode` como `basic`.

## Parâmetros aninhados

Parâmetros aninhados são dicionários, tipados com `TypedDict`, por exemplo:

```python
from groq import Groq

client = Groq()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "content": "string",
            "role": "system",
        }
    ],
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    compound_custom={},
)
print(chat_completion.compound_custom)
```

## Upload de arquivos

Parâmetros de requisição que correspondem a uploads de arquivos podem ser passados como `bytes`, uma instância de [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) ou uma tupla `(filename, contents, media type)`.

```python
from pathlib import Path
from groq import Groq

client = Groq()

client.audio.transcriptions.create(
    model="whisper-large-v3-turbo",
    file=Path("/path/to/file"),
)
```

O cliente assíncrono usa exatamente a mesma interface. Se você passar uma instância de [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike), o conteúdo do arquivo será lido de forma assíncrona automaticamente.

## Tratamento de erros

Quando a biblioteca não consegue se conectar à API (por exemplo, devido a problemas de conexão de rede ou timeout), uma subclasse de `groq.APIConnectionError` é lançada.

Quando a API retorna um código de status de falha (ou seja, resposta 4xx ou 5xx), uma subclasse de `groq.APIStatusError` é lançada, contendo as propriedades `status_code` e `response`.

Todos os erros herdam de `groq.APIError`.

```python
import groq
from groq import Groq

client = Groq()

try:
    client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Explain the importance of low latency LLMs",
            },
        ],
        model="openai/gpt-oss-20b",
    )
except groq.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except groq.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except groq.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Os códigos de erro são os seguintes:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Tentativas novas

Certos erros são automaticamente repetidos 2 vezes por padrão, com um backoff exponencial curto. Erros de conexão (por exemplo, devido a um problema de conectividade de rede), 408 Request Timeout, 409 Conflict, 429 Rate Limit e erros internos >=500 são todos repetidos por padrão.

Você pode usar a opção `max_retries` para configurar ou desabilitar as configurações de repetição:

```python
from groq import Groq

# Configure the default for all requests:
client = Groq(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        },
    ],
    model="openai/gpt-oss-20b",
)
```

### Timeouts

Por padrão, as requisições expiram após 1 minuto. Você pode configurar isso com a opção `timeout`, que aceita um float ou um objeto [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration):

```python
from groq import Groq

# Configure the default for all requests:
client = Groq(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = Groq(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        },
    ],
    model="openai/gpt-oss-20b",
)
```

Em caso de timeout, um `APITimeoutError` é lançado.

Observe que requisições que expiram são [repetidas duas vezes por padrão](#tentativas-novas).

## Avançado

### Logging

Usamos o módulo [`logging`](https://docs.python.org/3/library/logging.html) da biblioteca padrão.

Você pode habilitar o logging definindo a variável de ambiente `GROQ_LOG` como `info`.

```shell
$ export GROQ_LOG=info
```

Ou como `debug` para logging mais detalhado.

### Como saber se `None` significa `null` ou ausente

Em uma resposta da API, um campo pode ser explicitamente `null` ou estar totalmente ausente; em ambos os casos, seu valor é `None` nesta biblioteca. Você pode diferenciar os dois casos com `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Acessando dados brutos da resposta (ex.: cabeçalhos)

O objeto Response "bruto" pode ser acessado prefixando `.with_raw_response.` a qualquer chamada de método HTTP, por exemplo:

```py
from groq import Groq

client = Groq()
response = client.chat.completions.with_raw_response.create(
    messages=[{
        "role": "system",
        "content": "You are a helpful assistant.",
    }, {
        "role": "user",
        "content": "Explain the importance of low latency LLMs",
    }],
    model="openai/gpt-oss-20b",
)
print(response.headers.get('X-My-Header'))

completion = response.parse()  # get the object that `chat.completions.create()` would have returned
print(completion.id)
```

Esses métodos retornam um objeto [`APIResponse`](https://github.com/groq/groq-python/tree/main/src/groq/_response.py).

O cliente assíncrono retorna um [`AsyncAPIResponse`](https://github.com/groq/groq-python/tree/main/src/groq/_response.py) com a mesma estrutura; a única diferença são métodos `await` para ler o conteúdo da resposta.

#### `.with_streaming_response`

A interface acima lê ansiosamente o corpo completo da resposta quando você faz a requisição, o que nem sempre é o desejado.

Para transmitir o corpo da resposta, use `.with_streaming_response` em vez disso, o que requer um gerenciador de contexto e só lê o corpo da resposta quando você chama `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` ou `.parse()`. No cliente assíncrono, esses são métodos assíncronos.

```python
with client.chat.completions.with_streaming_response.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        },
    ],
    model="openai/gpt-oss-20b",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

O gerenciador de contexto é necessário para que a resposta seja fechada de forma confiável.

### Fazendo requisições personalizadas/não documentadas

Esta biblioteca é tipada para acesso conveniente à API documentada.

Se precisar acessar endpoints, parâmetros ou propriedades de resposta não documentados, a biblioteca ainda pode ser usada.

#### Endpoints não documentados

Para fazer requisições a endpoints não documentados, você pode usar `client.get`, `client.post` e outros verbos HTTP. As opções do cliente serão respeitadas (como tentativas novas) ao fazer essa requisição.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Parâmetros de requisição não documentados

Se quiser enviar explicitamente um parâmetro extra, você pode fazê-lo com as opções de requisição `extra_query`, `extra_body` e `extra_headers`.

#### Propriedades de resposta não documentadas

Para acessar propriedades de resposta não documentadas, você pode acessar os campos extras como `response.unknown_prop`. Você também pode obter todos os campos extras no modelo Pydantic como um dicionário com [`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configurando o cliente HTTP

Você pode substituir diretamente o [cliente httpx](https://www.python-httpx.org/api/#client) para personalizá-lo para o seu caso de uso, incluindo:

- Suporte a [proxies](https://www.python-httpx.org/advanced/proxies/)
- [Transports](https://www.python-httpx.org/advanced/transports/) personalizados
- Funcionalidades [avançadas](https://www.python-httpx.org/advanced/clients/) adicionais

```python
import httpx
from groq import Groq, DefaultHttpxClient

client = Groq(
    # Or use the `GROQ_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

Você também pode personalizar o cliente por requisição usando `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Gerenciando recursos HTTP

Por padrão, a biblioteca fecha as conexões HTTP subjacentes sempre que o cliente é [coletado pelo garbage collector](https://docs.python.org/3/reference/datamodel.html#object.__del__). Você pode fechar manualmente o cliente usando o método `.close()` se desejar, ou com um gerenciador de contexto que fecha ao sair.

```py
from groq import Groq

with Groq() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versionamento

Este pacote geralmente segue as convenções [SemVer](https://semver.org/spec/v2.0.0.html), embora certas alterações incompatíveis com versões anteriores possam ser lançadas como versões menores:

1. Alterações que afetam apenas tipos estáticos, sem quebrar o comportamento em tempo de execução.
2. Alterações em detalhes internos da biblioteca que são tecnicamente públicos, mas não destinados ou documentados para uso externo. _(Abra uma issue no GitHub para nos informar se você depende de tais detalhes internos.)_
3. Alterações que não esperamos impactar a grande maioria dos usuários na prática.

Levamos a compatibilidade com versões anteriores a sério e trabalhamos para garantir uma experiência de atualização tranquila.

Valorizamos seu feedback; abra uma [issue](https://www.github.com/groq/groq-python/issues) com dúvidas, bugs ou sugestões.

### Determinando a versão instalada

Se você atualizou para a versão mais recente, mas não está vendo os novos recursos que esperava, é provável que seu ambiente Python ainda esteja usando uma versão mais antiga.

Você pode determinar a versão usada em tempo de execução com:

```py
import groq
print(groq.__version__)
```

## Requisitos

Python 3.10 ou superior.

## Contribuindo

Consulte [a documentação de contribuição](./CONTRIBUTING.md).
