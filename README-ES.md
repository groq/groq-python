# Biblioteca Python de la API de Groq

**Idiomas / Languages:** [English](./README.md) · [中文](./README-ZH.md) · [Español](./README-ES.md) · [Français](./README-FR.md) · [Português](./README-PT.md) · [Русский](./README-RU.md) · [Deutsch](./README-DE.md)

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/groq.svg?label=pypi%20(stable))](https://pypi.org/project/groq/)

La biblioteca Python de Groq ofrece un acceso conveniente a la API REST de Groq desde cualquier aplicación Python 3.10 o superior. La biblioteca incluye definiciones de tipos para todos los parámetros de solicitud y campos de respuesta, y ofrece clientes síncronos y asíncronos impulsados por [httpx](https://github.com/encode/httpx).

Está generada con [Stainless](https://www.stainless.com/).

## Documentación

La documentación de la API REST se encuentra en [console.groq.com](https://console.groq.com/docs). La API completa de esta biblioteca está en [api.md](api.md).

## Instalación

```sh
# install from PyPI
pip install groq
```

## Uso

La API completa de esta biblioteca está en [api.md](api.md).

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

Aunque puedes proporcionar un argumento de palabra clave `api_key`,
recomendamos usar [python-dotenv](https://pypi.org/project/python-dotenv/)
para añadir `GROQ_API_KEY="My API Key"` a tu archivo `.env`
de modo que tu clave de API no quede almacenada en el control de versiones.

## Uso asíncrono

Simplemente importa `AsyncGroq` en lugar de `Groq` y usa `await` en cada llamada a la API:

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

La funcionalidad entre los clientes síncrono y asíncrono es idéntica en lo demás.

### Con aiohttp

Por defecto, el cliente asíncrono usa `httpx` para las solicitudes HTTP. Sin embargo, para mejorar el rendimiento de concurrencia también puedes usar `aiohttp` como backend HTTP.

Puedes habilitarlo instalando `aiohttp`:

```sh
# install from PyPI
pip install groq[aiohttp]
```

Luego puedes habilitarlo instanciando el cliente con `http_client=DefaultAioHttpClient()`:

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

## Uso de tipos

Los parámetros de solicitud anidados son [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Las respuestas son [modelos Pydantic](https://docs.pydantic.dev) que también ofrecen métodos auxiliares para cosas como:

- Serializar de nuevo a JSON, `model.to_json()`
- Convertir a un diccionario, `model.to_dict()`

Las solicitudes y respuestas tipadas proporcionan autocompletado y documentación en tu editor. Si deseas ver errores de tipo en VS Code para detectar errores antes, establece `python.analysis.typeCheckingMode` en `basic`.

## Parámetros anidados

Los parámetros anidados son diccionarios, tipados con `TypedDict`, por ejemplo:

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

## Carga de archivos

Los parámetros de solicitud que corresponden a cargas de archivos pueden pasarse como `bytes`, una instancia de [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) o una tupla de `(filename, contents, media type)`.

```python
from pathlib import Path
from groq import Groq

client = Groq()

client.audio.transcriptions.create(
    model="whisper-large-v3-turbo",
    file=Path("/path/to/file"),
)
```

El cliente asíncrono usa exactamente la misma interfaz. Si pasas una instancia de [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike), el contenido del archivo se leerá de forma asíncrona automáticamente.

## Manejo de errores

Cuando la biblioteca no puede conectarse a la API (por ejemplo, debido a problemas de conexión de red o un tiempo de espera), se lanza una subclase de `groq.APIConnectionError`.

Cuando la API devuelve un código de estado que no indica éxito (es decir, respuesta 4xx o 5xx), se lanza una subclase de `groq.APIStatusError`, que contiene las propiedades `status_code` y `response`.

Todos los errores heredan de `groq.APIError`.

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

Los códigos de error son los siguientes:

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

### Reintentos

Ciertos errores se reintentan automáticamente 2 veces por defecto, con un breve retroceso exponencial.
Los errores de conexión (por ejemplo, debido a un problema de conectividad de red), 408 Request Timeout, 409 Conflict,
429 Rate Limit y errores internos >=500 se reintentan por defecto.

Puedes usar la opción `max_retries` para configurar o deshabilitar los ajustes de reintento:

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

### Tiempos de espera

Por defecto, las solicitudes agotan el tiempo de espera tras 1 minuto. Puedes configurarlo con la opción `timeout`,
que acepta un float o un objeto [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration):

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

En caso de tiempo de espera, se lanza un `APITimeoutError`.

Ten en cuenta que las solicitudes que agotan el tiempo de espera [se reintentan dos veces por defecto](#reintentos).

## Avanzado

### Registro

Usamos el módulo estándar [`logging`](https://docs.python.org/3/library/logging.html).

Puedes habilitar el registro estableciendo la variable de entorno `GROQ_LOG` en `info`.

```shell
$ export GROQ_LOG=info
```

O en `debug` para un registro más detallado.

### Cómo saber si `None` significa `null` o ausente

En una respuesta de la API, un campo puede ser explícitamente `null` o estar completamente ausente; en cualquier caso, su valor es `None` en esta biblioteca. Puedes diferenciar los dos casos con `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Acceso a datos de respuesta sin procesar (p. ej. headers)

Se puede acceder al objeto Response «sin procesar» anteponiendo `.with_raw_response.` a cualquier llamada de método HTTP, p. ej.:

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

Estos métodos devuelven un objeto [`APIResponse`](https://github.com/groq/groq-python/tree/main/src/groq/_response.py).

El cliente asíncrono devuelve un [`AsyncAPIResponse`](https://github.com/groq/groq-python/tree/main/src/groq/_response.py) con la misma estructura; la única diferencia son los métodos que requieren `await` para leer el contenido de la respuesta.

#### `.with_streaming_response`

La interfaz anterior lee con avidez el cuerpo completo de la respuesta al hacer la solicitud, lo cual puede no ser siempre lo que deseas.

Para transmitir el cuerpo de la respuesta, usa `.with_streaming_response` en su lugar, que requiere un administrador de contexto y solo lee el cuerpo de la respuesta cuando llamas a `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` o `.parse()`. En el cliente asíncrono, estos son métodos asíncronos.

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

El administrador de contexto es necesario para que la respuesta se cierre de forma fiable.

### Realizar solicitudes personalizadas/no documentadas

Esta biblioteca está tipada para un acceso conveniente a la API documentada.

Si necesitas acceder a endpoints, parámetros o propiedades de respuesta no documentados, la biblioteca sigue siendo utilizable.

#### Endpoints no documentados

Para hacer solicitudes a endpoints no documentados, puedes usar `client.get`, `client.post` y otros
verbos http. Las opciones del cliente se respetarán (como los reintentos) al hacer esta solicitud.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Parámetros de solicitud no documentados

Si deseas enviar explícitamente un parámetro adicional, puedes hacerlo con las opciones de solicitud `extra_query`, `extra_body` y `extra_headers`.

#### Propiedades de respuesta no documentadas

Para acceder a propiedades de respuesta no documentadas, puedes acceder a los campos adicionales como `response.unknown_prop`. También
puedes obtener todos los campos adicionales del modelo Pydantic como un diccionario con
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuración del cliente HTTP

Puedes sobrescribir directamente el [cliente httpx](https://www.python-httpx.org/api/#client) para personalizarlo según tu caso de uso, incluyendo:

- Soporte para [proxies](https://www.python-httpx.org/advanced/proxies/)
- [Transportes](https://www.python-httpx.org/advanced/transports/) personalizados
- Funcionalidad [avanzada](https://www.python-httpx.org/advanced/clients/) adicional

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

También puedes personalizar el cliente por solicitud usando `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Gestión de recursos HTTP

Por defecto, la biblioteca cierra las conexiones HTTP subyacentes cuando el cliente es [recolectado por el recolector de basura](https://docs.python.org/3/reference/datamodel.html#object.__del__). Puedes cerrar el cliente manualmente con el método `.close()` si lo deseas, o con un administrador de contexto que se cierra al salir.

```py
from groq import Groq

with Groq() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versionado

Este paquete generalmente sigue las convenciones de [SemVer](https://semver.org/spec/v2.0.0.html), aunque ciertos cambios incompatibles con versiones anteriores pueden publicarse como versiones menores:

1. Cambios que solo afectan a tipos estáticos, sin romper el comportamiento en tiempo de ejecución.
2. Cambios en los internos de la biblioteca que son técnicamente públicos pero no están destinados ni documentados para uso externo. _(Abre un issue en GitHub para informarnos si dependes de dichos internos.)_
3. Cambios que no esperamos que afecten a la gran mayoría de usuarios en la práctica.

Nos tomamos en serio la compatibilidad hacia atrás y trabajamos para que puedas contar con una experiencia de actualización fluida.

Agradecemos tus comentarios; abre un [issue](https://www.github.com/groq/groq-python/issues) con preguntas, errores o sugerencias.

### Determinar la versión instalada

Si has actualizado a la última versión pero no ves las nuevas funciones que esperabas, es probable que tu entorno de Python siga usando una versión anterior.

Puedes determinar la versión que se usa en tiempo de ejecución con:

```py
import groq
print(groq.__version__)
```

## Requisitos

Python 3.10 o superior.

## Contribuir

Consulta [la documentación de contribución](./CONTRIBUTING.md).
