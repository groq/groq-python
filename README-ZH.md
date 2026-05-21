# Groq Python API 库

**语言 / Languages:** [English](./README.md) · [中文](./README-ZH.md) · [Español](./README-ES.md) · [Français](./README-FR.md) · [Português](./README-PT.md) · [Русский](./README-RU.md) · [Deutsch](./README-DE.md)

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/groq.svg?label=pypi%20(stable))](https://pypi.org/project/groq/)

Groq Python 库为任何 Python 3.10+ 应用程序提供了便捷访问 Groq REST API 的方式。该库包含所有请求参数和响应字段的类型定义，并提供由 [httpx](https://github.com/encode/httpx) 驱动的同步与异步客户端。

本库由 [Stainless](https://www.stainless.com/) 生成。

## 文档

REST API 文档可在 [console.groq.com](https://console.groq.com/docs) 查看。本库的完整 API 说明见 [api.md](api.md)。

## 安装

```sh
# install from PyPI
pip install groq
```

## 用法

本库的完整 API 说明见 [api.md](api.md)。

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

虽然你可以通过 `api_key` 关键字参数传入 API 密钥，但我们建议使用 [python-dotenv](https://pypi.org/project/python-dotenv/) 将 `GROQ_API_KEY="My API Key"` 添加到 `.env` 文件中，这样 API 密钥就不会被提交到源代码管理中。

## 异步用法

只需导入 `AsyncGroq` 而不是 `Groq`，并在每次 API 调用时使用 `await`：

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

同步客户端与异步客户端的功能在其他方面完全相同。

### 使用 aiohttp

默认情况下，异步客户端使用 `httpx` 发起 HTTP 请求。不过，为提升并发性能，你也可以将 `aiohttp` 用作 HTTP 后端。

安装 `aiohttp` 即可启用：

```sh
# install from PyPI
pip install groq[aiohttp]
```

然后通过使用 `http_client=DefaultAioHttpClient()` 实例化客户端来启用：

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

## 使用类型

嵌套请求参数为 [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict)。响应为 [Pydantic 模型](https://docs.pydantic.dev)，并提供如下辅助方法：

- 序列化为 JSON：`model.to_json()`
- 转换为字典：`model.to_dict()`

类型化的请求与响应可在编辑器中提供自动补全和文档。若希望在 VS Code 中尽早通过类型错误发现 bug，可将 `python.analysis.typeCheckingMode` 设置为 `basic`。

## 嵌套参数

嵌套参数为字典，使用 `TypedDict` 进行类型标注，例如：

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

## 文件上传

对应文件上传的请求参数可传入 `bytes`、[`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) 实例，或 `(filename, contents, media type)` 元组。

```python
from pathlib import Path
from groq import Groq

client = Groq()

client.audio.transcriptions.create(
    model="whisper-large-v3-turbo",
    file=Path("/path/to/file"),
)
```

异步客户端使用完全相同的接口。若传入 [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) 实例，文件内容将自动异步读取。

## 错误处理

当库无法连接到 API（例如因网络连接问题或超时）时，会抛出 `groq.APIConnectionError` 的子类。

当 API 返回非成功状态码（即 4xx 或 5xx 响应）时，会抛出 `groq.APIStatusError` 的子类，其中包含 `status_code` 和 `response` 属性。

所有错误均继承自 `groq.APIError`。

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

错误代码对应关系如下：

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

### 重试

某些错误默认会自动重试 2 次，并采用简短的指数退避。连接错误（例如网络连通性问题）、408 Request Timeout、409 Conflict、429 Rate Limit 以及 >=500 内部错误默认都会重试。

可使用 `max_retries` 选项配置或禁用重试设置：

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

### 超时

默认情况下，请求在 1 分钟后超时。可通过 `timeout` 选项进行配置，该选项接受浮点数或 [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) 对象：

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

超时时会抛出 `APITimeoutError`。

请注意，超时的请求[默认会重试两次](#重试)。

## 高级用法

### 日志

我们使用标准库的 [`logging`](https://docs.python.org/3/library/logging.html) 模块。

将环境变量 `GROQ_LOG` 设置为 `info` 即可启用日志。

```shell
$ export GROQ_LOG=info
```

或设置为 `debug` 以获取更详细的日志。

### 如何判断 `None` 表示 `null` 还是缺失

在 API 响应中，字段可能显式为 `null`，或完全缺失；在这两种情况下，本库中的值均为 `None`。可通过 `.model_fields_set` 区分这两种情况：

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### 访问原始响应数据（例如 headers）

可在任何 HTTP 方法调用前加上 `.with_raw_response.` 前缀来访问“原始” Response 对象，例如：

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

这些方法返回 [`APIResponse`](https://github.com/groq/groq-python/tree/main/src/groq/_response.py) 对象。

异步客户端返回结构相同的 [`AsyncAPIResponse`](https://github.com/groq/groq-python/tree/main/src/groq/_response.py)，唯一区别是读取响应内容的方法需要 `await`。

#### `.with_streaming_response`

上述接口在发起请求时会立即读取完整响应体，这可能并不总是你想要的。

若要流式读取响应体，请改用 `.with_streaming_response`，它需要上下文管理器，且只有在你调用 `.read()`、`.text()`、`.json()`、`.iter_bytes()`、`.iter_text()`、`.iter_lines()` 或 `.parse()` 时才会读取响应体。在异步客户端中，这些为异步方法。

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

必须使用上下文管理器，以确保响应能被可靠关闭。

### 发起自定义/未文档化的请求

本库针对已文档化的 API 进行了类型标注，便于使用。

若需要访问未文档化的端点、参数或响应属性，仍可使用本库。

#### 未文档化的端点

要对未文档化的端点发起请求，可使用 `client.get`、`client.post` 及其他 HTTP 动词。发起请求时会尊重客户端上的选项（例如重试）。

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### 未文档化的请求参数

若要显式发送额外参数，可使用 `extra_query`、`extra_body` 和 `extra_headers` 请求选项。

#### 未文档化的响应属性

要访问未文档化的响应属性，可像 `response.unknown_prop` 一样访问额外字段。也可通过 [`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra) 将 Pydantic 模型上的所有额外字段获取为字典。

### 配置 HTTP 客户端

可直接覆盖 [httpx 客户端](https://www.python-httpx.org/api/#client) 以根据你的用例进行自定义，包括：

- 支持[代理](https://www.python-httpx.org/advanced/proxies/)
- 自定义[传输层](https://www.python-httpx.org/advanced/transports/)
- 其他[高级](https://www.python-httpx.org/advanced/clients/)功能

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

也可通过 `with_options()` 在每次请求时自定义客户端：

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### 管理 HTTP 资源

默认情况下，当客户端被[垃圾回收](https://docs.python.org/3/reference/datamodel.html#object.__del__)时，库会关闭底层 HTTP 连接。如需手动关闭，可使用 `.close()` 方法，或使用在退出时自动关闭的上下文管理器。

```py
from groq import Groq

with Groq() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## 版本管理

本包通常遵循 [SemVer](https://semver.org/spec/v2.0.0.html) 约定，但某些向后不兼容的变更可能作为次要版本发布：

1. 仅影响静态类型、不破坏运行时行为的变更。
2. 对库内部的技术上公开但未面向外部使用或文档化的变更。_（若你依赖此类内部实现，请提交 GitHub issue 告知我们。）_
3. 我们预计在实践中不会影响绝大多数用户的变更。

我们高度重视向后兼容性，并努力确保你能获得顺畅的升级体验。

我们欢迎你的反馈；如有问题、bug 或建议，请提交 [issue](https://www.github.com/groq/groq-python/issues)。

### 确定已安装版本

若你已升级到最新版本却看不到预期的新功能，可能是 Python 环境仍在使用旧版本。

可在运行时通过以下方式确定正在使用的版本：

```py
import groq
print(groq.__version__)
```

## 系统要求

Python 3.10 或更高版本。

## 贡献

请参阅[贡献文档](./CONTRIBUTING.md)。
