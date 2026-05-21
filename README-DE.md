# Groq Python-API-Bibliothek

**Sprachen / Languages:** [English](./README.md) · [中文](./README-ZH.md) · [Español](./README-ES.md) · [Français](./README-FR.md) · [Português](./README-PT.md) · [Русский](./README-RU.md) · [Deutsch](./README-DE.md)

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/groq.svg?label=pypi%20(stable))](https://pypi.org/project/groq/)

Die Groq Python-Bibliothek bietet bequemen Zugriff auf die Groq REST API aus jeder Python-3.10+-Anwendung. Die Bibliothek enthält Typdefinitionen für alle Anfrageparameter und Antwortfelder und bietet sowohl synchrone als auch asynchrone Clients auf Basis von [httpx](https://github.com/encode/httpx).

Sie wird mit [Stainless](https://www.stainless.com/) generiert.

## Dokumentation

Die REST-API-Dokumentation finden Sie auf [console.groq.com](https://console.groq.com/docs). Die vollständige API dieser Bibliothek ist in [api.md](api.md) dokumentiert.

## Installation

```sh
# install from PyPI
pip install groq
```

## Verwendung

Die vollständige API dieser Bibliothek ist in [api.md](api.md) dokumentiert.

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

Obwohl Sie ein `api_key`-Schlüsselwortargument übergeben können, empfehlen wir die Verwendung von [python-dotenv](https://pypi.org/project/python-dotenv/), um `GROQ_API_KEY="My API Key"` zu Ihrer `.env`-Datei hinzuzufügen, damit Ihr API-Schlüssel nicht in der Versionskontrolle gespeichert wird.

## Asynchrone Verwendung

Importieren Sie einfach `AsyncGroq` anstelle von `Groq` und verwenden Sie `await` bei jedem API-Aufruf:

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

Die Funktionalität zwischen dem synchronen und dem asynchronen Client ist ansonsten identisch.

### Mit aiohttp

Standardmäßig verwendet der asynchrone Client `httpx` für HTTP-Anfragen. Für eine bessere Nebenläufigkeitsleistung können Sie jedoch auch `aiohttp` als HTTP-Backend verwenden.

Sie können dies aktivieren, indem Sie `aiohttp` installieren:

```sh
# install from PyPI
pip install groq[aiohttp]
```

Aktivieren Sie es dann, indem Sie den Client mit `http_client=DefaultAioHttpClient()` instanziieren:

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

## Typen verwenden

Verschachtelte Anfrageparameter sind [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Antworten sind [Pydantic-Modelle](https://docs.pydantic.dev), die auch Hilfsmethoden für folgende Aufgaben bereitstellen:

- Zurückserialisieren in JSON, `model.to_json()`
- Umwandeln in ein Dictionary, `model.to_dict()`

Typisierte Anfragen und Antworten bieten Autovervollständigung und Dokumentation in Ihrem Editor. Wenn Sie Typfehler in VS Code sehen möchten, um Fehler früher zu erkennen, setzen Sie `python.analysis.typeCheckingMode` auf `basic`.

## Verschachtelte Parameter

Verschachtelte Parameter sind Dictionaries, die mit `TypedDict` typisiert sind, zum Beispiel:

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

## Datei-Uploads

Anfrageparameter, die Datei-Uploads entsprechen, können als `bytes`, als [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike)-Instanz oder als Tupel `(filename, contents, media type)` übergeben werden.

```python
from pathlib import Path
from groq import Groq

client = Groq()

client.audio.transcriptions.create(
    model="whisper-large-v3-turbo",
    file=Path("/path/to/file"),
)
```

Der asynchrone Client verwendet exakt dieselbe Schnittstelle. Wenn Sie eine [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike)-Instanz übergeben, wird der Dateiinhalt automatisch asynchron gelesen.

## Fehlerbehandlung

Wenn die Bibliothek keine Verbindung zur API herstellen kann (z. B. aufgrund von Netzwerkverbindungsproblemen oder einem Timeout), wird eine Unterklasse von `groq.APIConnectionError` ausgelöst.

Wenn die API einen Nicht-Erfolgs-Statuscode zurückgibt (d. h. 4xx- oder 5xx-Antwort), wird eine Unterklasse von `groq.APIStatusError` ausgelöst, die die Eigenschaften `status_code` und `response` enthält.

Alle Fehler erben von `groq.APIError`.

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

Die Fehlercodes sind wie folgt:

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

### Wiederholungsversuche

Bestimmte Fehler werden standardmäßig automatisch 2-mal wiederholt, mit einem kurzen exponentiellen Backoff. Verbindungsfehler (z. B. aufgrund eines Netzwerkverbindungsproblems), 408 Request Timeout, 409 Conflict, 429 Rate Limit und >=500 Internal Errors werden alle standardmäßig wiederholt.

Sie können die Option `max_retries` verwenden, um Wiederholungseinstellungen zu konfigurieren oder zu deaktivieren:

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

Standardmäßig laufen Anfragen nach 1 Minute ab. Sie können dies mit der Option `timeout` konfigurieren, die einen Float oder ein [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration)-Objekt akzeptiert:

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

Bei einem Timeout wird ein `APITimeoutError` ausgelöst.

Beachten Sie, dass Anfragen, die ablaufen, [standardmäßig zweimal wiederholt werden](#wiederholungsversuche).

## Erweitert

### Logging

Wir verwenden das Modul [`logging`](https://docs.python.org/3/library/logging.html) der Standardbibliothek.

Sie können Logging aktivieren, indem Sie die Umgebungsvariable `GROQ_LOG` auf `info` setzen.

```shell
$ export GROQ_LOG=info
```

Oder auf `debug` für ausführlicheres Logging.

### Wie man erkennt, ob `None` `null` oder fehlend bedeutet

In einer API-Antwort kann ein Feld explizit `null` sein oder vollständig fehlen; in beiden Fällen ist sein Wert in dieser Bibliothek `None`. Sie können die beiden Fälle mit `.model_fields_set` unterscheiden:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Zugriff auf Rohdaten der Antwort (z. B. Header)

Auf das „rohe“ Response-Objekt kann zugegriffen werden, indem `.with_raw_response.` vor jeden HTTP-Methodenaufruf gesetzt wird, z. B.:

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

Diese Methoden geben ein [`APIResponse`](https://github.com/groq/groq-python/tree/main/src/groq/_response.py)-Objekt zurück.

Der asynchrone Client gibt ein [`AsyncAPIResponse`](https://github.com/groq/groq-python/tree/main/src/groq/_response.py) mit derselben Struktur zurück; der einzige Unterschied sind `await`-fähige Methoden zum Lesen des Antwortinhalts.

#### `.with_streaming_response`

Die obige Schnittstelle liest den vollständigen Antwortbody beim Senden der Anfrage sofort ein, was nicht immer gewünscht ist.

Um den Antwortbody zu streamen, verwenden Sie stattdessen `.with_streaming_response`, was einen Kontextmanager erfordert und den Antwortbody erst liest, wenn Sie `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` oder `.parse()` aufrufen. Im asynchronen Client sind dies asynchrone Methoden.

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

Der Kontextmanager ist erforderlich, damit die Antwort zuverlässig geschlossen wird.

### Benutzerdefinierte/undokumentierte Anfragen

Diese Bibliothek ist für den bequemen Zugriff auf die dokumentierte API typisiert.

Wenn Sie auf undokumentierte Endpunkte, Parameter oder Antworteigenschaften zugreifen müssen, kann die Bibliothek dennoch verwendet werden.

#### Undokumentierte Endpunkte

Um Anfragen an undokumentierte Endpunkte zu senden, können Sie `client.get`, `client.post` und andere HTTP-Verben verwenden. Client-Optionen (wie Wiederholungsversuche) werden bei dieser Anfrage berücksichtigt.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undokumentierte Anfrageparameter

Wenn Sie explizit einen zusätzlichen Parameter senden möchten, können Sie dies mit den Anfrageoptionen `extra_query`, `extra_body` und `extra_headers` tun.

#### Undokumentierte Antworteigenschaften

Um auf undokumentierte Antworteigenschaften zuzugreifen, können Sie auf die zusätzlichen Felder wie `response.unknown_prop` zugreifen. Sie können auch alle zusätzlichen Felder im Pydantic-Modell als Dictionary mit [`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra) abrufen.

### Konfiguration des HTTP-Clients

Sie können den [httpx-Client](https://www.python-httpx.org/api/#client) direkt überschreiben, um ihn für Ihren Anwendungsfall anzupassen, einschließlich:

- Unterstützung für [Proxies](https://www.python-httpx.org/advanced/proxies/)
- Benutzerdefinierte [Transports](https://www.python-httpx.org/advanced/transports/)
- Zusätzliche [erweiterte](https://www.python-httpx.org/advanced/clients/) Funktionalität

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

Sie können den Client auch pro Anfrage mit `with_options()` anpassen:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Verwaltung von HTTP-Ressourcen

Standardmäßig schließt die Bibliothek die zugrunde liegenden HTTP-Verbindungen, wenn der Client [vom Garbage Collector freigegeben](https://docs.python.org/3/reference/datamodel.html#object.__del__) wird. Sie können den Client bei Bedarf manuell mit der Methode `.close()` schließen oder mit einem Kontextmanager, der beim Verlassen schließt.

```py
from groq import Groq

with Groq() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versionierung

Dieses Paket folgt im Allgemeinen den [SemVer](https://semver.org/spec/v2.0.0.html)-Konventionen, obwohl bestimmte rückwärtsinkompatible Änderungen als Minor-Versionen veröffentlicht werden können:

1. Änderungen, die nur statische Typen betreffen, ohne das Laufzeitverhalten zu beeinträchtigen.
2. Änderungen an Bibliotheksinterna, die technisch öffentlich sind, aber nicht für die externe Nutzung vorgesehen oder dokumentiert sind. _(Bitte öffnen Sie ein GitHub-Issue, wenn Sie auf solche Interna angewiesen sind.)_
3. Änderungen, von denen wir nicht erwarten, dass sie die überwiegende Mehrheit der Benutzer in der Praxis betreffen.

Wir nehmen Rückwärtskompatibilität ernst und arbeiten daran, Ihnen ein reibungsloses Upgrade-Erlebnis zu bieten.

Wir freuen uns über Ihr Feedback; öffnen Sie bitte ein [Issue](https://www.github.com/groq/groq-python/issues) mit Fragen, Fehlern oder Vorschlägen.

### Ermittlung der installierten Version

Wenn Sie auf die neueste Version aktualisiert haben, aber keine neuen Funktionen sehen, die Sie erwartet haben, verwendet Ihre Python-Umgebung wahrscheinlich noch eine ältere Version.

Sie können die zur Laufzeit verwendete Version wie folgt ermitteln:

```py
import groq
print(groq.__version__)
```

## Anforderungen

Python 3.10 oder höher.

## Mitwirken

Siehe [die Mitwirkungsdokumentation](./CONTRIBUTING.md).
