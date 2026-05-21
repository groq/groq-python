# Python-библиотека API Groq

**Языки / Languages:** [English](./README.md) · [中文](./README-ZH.md) · [Español](./README-ES.md) · [Français](./README-FR.md) · [Português](./README-PT.md) · [Русский](./README-RU.md) · [Deutsch](./README-DE.md)

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/groq.svg?label=pypi%20(stable))](https://pypi.org/project/groq/)

Python-библиотека Groq обеспечивает удобный доступ к REST API Groq из любого приложения на Python 3.10+. Библиотека включает определения типов для всех параметров запросов и полей ответов, а также предоставляет синхронные и асинхронные клиенты на базе [httpx](https://github.com/encode/httpx).

Она сгенерирована с помощью [Stainless](https://www.stainless.com/).

## Документация

Документация REST API доступна на [console.groq.com](https://console.groq.com/docs). Полный API этой библиотеки описан в [api.md](api.md).

## Установка

```sh
# install from PyPI
pip install groq
```

## Использование

Полный API этой библиотеки описан в [api.md](api.md).

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

Хотя вы можете передать ключевой аргумент `api_key`, мы рекомендуем использовать [python-dotenv](https://pypi.org/project/python-dotenv/) для добавления `GROQ_API_KEY="My API Key"` в ваш файл `.env`, чтобы API-ключ не хранился в системе контроля версий.

## Асинхронное использование

Просто импортируйте `AsyncGroq` вместо `Groq` и используйте `await` с каждым вызовом API:

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

Функциональность синхронного и асинхронного клиентов в остальном идентична.

### С aiohttp

По умолчанию асинхронный клиент использует `httpx` для HTTP-запросов. Однако для улучшения производительности при конкурентном доступе вы также можете использовать `aiohttp` в качестве HTTP-бэкенда.

Вы можете включить это, установив `aiohttp`:

```sh
# install from PyPI
pip install groq[aiohttp]
```

Затем включите его, создав экземпляр клиента с `http_client=DefaultAioHttpClient()`:

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

## Использование типов

Вложенные параметры запросов — это [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Ответы — это [модели Pydantic](https://docs.pydantic.dev), которые также предоставляют вспомогательные методы для таких операций, как:

- Сериализация обратно в JSON, `model.to_json()`
- Преобразование в словарь, `model.to_dict()`

Типизированные запросы и ответы обеспечивают автодополнение и документацию в вашем редакторе. Если вы хотите видеть ошибки типов в VS Code для раннего обнаружения ошибок, установите `python.analysis.typeCheckingMode` в значение `basic`.

## Вложенные параметры

Вложенные параметры — это словари, типизированные с помощью `TypedDict`, например:

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

## Загрузка файлов

Параметры запросов, соответствующие загрузке файлов, могут быть переданы как `bytes`, экземпляр [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) или кортеж `(filename, contents, media type)`.

```python
from pathlib import Path
from groq import Groq

client = Groq()

client.audio.transcriptions.create(
    model="whisper-large-v3-turbo",
    file=Path("/path/to/file"),
)
```

Асинхронный клиент использует точно такой же интерфейс. Если вы передаёте экземпляр [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike), содержимое файла будет прочитано асинхронно автоматически.

## Обработка ошибок

Когда библиотека не может подключиться к API (например, из-за проблем с сетевым соединением или таймаута), выбрасывается подкласс `groq.APIConnectionError`.

Когда API возвращает код статуса, отличный от успешного (то есть ответ 4xx или 5xx), выбрасывается подкласс `groq.APIStatusError`, содержащий свойства `status_code` и `response`.

Все ошибки наследуются от `groq.APIError`.

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

Коды ошибок следующие:

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

### Повторные попытки

Некоторые ошибки автоматически повторяются 2 раза по умолчанию с короткой экспоненциальной задержкой. Ошибки соединения (например, из-за проблем с сетевым подключением), 408 Request Timeout, 409 Conflict, 429 Rate Limit и внутренние ошибки >=500 по умолчанию повторяются.

Вы можете использовать опцию `max_retries` для настройки или отключения параметров повторных попыток:

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

### Таймауты

По умолчанию запросы завершаются по таймауту через 1 минуту. Вы можете настроить это с помощью опции `timeout`, которая принимает float или объект [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration):

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

При таймауте выбрасывается `APITimeoutError`.

Обратите внимание, что запросы, завершившиеся по таймауту, [повторяются дважды по умолчанию](#повторные-попытки).

## Расширенные возможности

### Логирование

Мы используем модуль [`logging`](https://docs.python.org/3/library/logging.html) стандартной библиотеки.

Вы можете включить логирование, установив переменную окружения `GROQ_LOG` в значение `info`.

```shell
$ export GROQ_LOG=info
```

Или в значение `debug` для более подробного логирования.

### Как определить, означает ли `None` значение `null` или отсутствие поля

В ответе API поле может быть явно `null` или полностью отсутствовать; в обоих случаях его значение в этой библиотеке равно `None`. Вы можете различить эти два случая с помощью `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Доступ к необработанным данным ответа (например, заголовкам)

«Необработанный» объект Response можно получить, добавив префикс `.with_raw_response.` к любому вызову HTTP-метода, например:

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

Эти методы возвращают объект [`APIResponse`](https://github.com/groq/groq-python/tree/main/src/groq/_response.py).

Асинхронный клиент возвращает [`AsyncAPIResponse`](https://github.com/groq/groq-python/tree/main/src/groq/_response.py) с той же структурой; единственное отличие — методы с `await` для чтения содержимого ответа.

#### `.with_streaming_response`

Описанный выше интерфейс жадно считывает всё тело ответа при выполнении запроса, что не всегда желательно.

Для потоковой передачи тела ответа используйте `.with_streaming_response`, что требует менеджера контекста и считывает тело ответа только после вызова `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` или `.parse()`. В асинхронном клиенте это асинхронные методы.

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

Менеджер контекста необходим для надёжного закрытия ответа.

### Выполнение пользовательских/недокументированных запросов

Эта библиотека типизирована для удобного доступа к документированному API.

Если вам нужен доступ к недокументированным эндпоинтам, параметрам или свойствам ответов, библиотекой всё равно можно пользоваться.

#### Недокументированные эндпоинты

Для выполнения запросов к недокументированным эндпоинтам вы можете использовать `client.get`, `client.post` и другие HTTP-глаголы. Параметры клиента (например, повторные попытки) будут учитываться при выполнении такого запроса.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Недокументированные параметры запросов

Если вы хотите явно отправить дополнительный параметр, вы можете сделать это с помощью опций запроса `extra_query`, `extra_body` и `extra_headers`.

#### Недокументированные свойства ответов

Для доступа к недокументированным свойствам ответов вы можете обращаться к дополнительным полям, например `response.unknown_prop`. Вы также можете получить все дополнительные поля модели Pydantic в виде словаря с помощью [`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Настройка HTTP-клиента

Вы можете напрямую переопределить [клиент httpx](https://www.python-httpx.org/api/#client) для настройки под ваш случай использования, включая:

- Поддержку [прокси](https://www.python-httpx.org/advanced/proxies/)
- Пользовательские [транспорты](https://www.python-httpx.org/advanced/transports/)
- Дополнительные [расширенные](https://www.python-httpx.org/advanced/clients/) возможности

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

Вы также можете настраивать клиент для отдельных запросов с помощью `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Управление HTTP-ресурсами

По умолчанию библиотека закрывает базовые HTTP-соединения при [сборке мусора](https://docs.python.org/3/reference/datamodel.html#object.__del__) клиента. При необходимости вы можете вручную закрыть клиент с помощью метода `.close()` или использовать менеджер контекста, который закрывает соединение при выходе.

```py
from groq import Groq

with Groq() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Версионирование

Этот пакет в целом следует соглашениям [SemVer](https://semver.org/spec/v2.0.0.html), хотя некоторые обратно несовместимые изменения могут выпускаться как минорные версии:

1. Изменения, затрагивающие только статические типы, без нарушения поведения во время выполнения.
2. Изменения во внутренних компонентах библиотеки, которые технически являются публичными, но не предназначены или не документированы для внешнего использования. _(Пожалуйста, откройте issue на GitHub, если вы полагаетесь на такие внутренние компоненты.)_
3. Изменения, которые, как мы ожидаем, не повлияют на подавляющее большинство пользователей на практике.

Мы серьёзно относимся к обратной совместимости и стремимся обеспечить плавный процесс обновления.

Мы будем рады вашей обратной связи; откройте [issue](https://www.github.com/groq/groq-python/issues) с вопросами, сообщениями об ошибках или предложениями.

### Определение установленной версии

Если вы обновились до последней версии, но не видите ожидаемых новых функций, вероятно, ваша среда Python всё ещё использует более старую версию.

Вы можете определить версию, используемую во время выполнения, с помощью:

```py
import groq
print(groq.__version__)
```

## Требования

Python 3.10 или выше.

## Участие в разработке

См. [документацию по участию в разработке](./CONTRIBUTING.md).
