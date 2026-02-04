# Shared Types

```python
from groq.types import ErrorObject, FunctionDefinition, FunctionParameters
```

# Completions

Types:

```python
from groq.types import CompletionUsage
```

# Chat

## Completions

Types:

```python
from groq.types.chat import (
    ChatCompletion,
    ChatCompletionAssistantMessageParam,
    ChatCompletionChunk,
    ChatCompletionContentPart,
    ChatCompletionContentPartImage,
    ChatCompletionContentPartText,
    ChatCompletionFunctionCallOption,
    ChatCompletionFunctionMessageParam,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionMessageToolCall,
    ChatCompletionNamedToolChoice,
    ChatCompletionRole,
    ChatCompletionSystemMessageParam,
    ChatCompletionTokenLogprob,
    ChatCompletionTool,
    ChatCompletionToolChoiceOption,
    ChatCompletionToolMessageParam,
    ChatCompletionUserMessageParam,
)
```

Methods:

- <code title="post /openai/v1/chat/completions">client.chat.completions.<a href="./src/groq/resources/chat/completions.py">create</a>(\*\*<a href="src/groq/types/chat/completion_create_params.py">params</a>) -> <a href="./src/groq/types/chat/chat_completion.py">ChatCompletion</a></code>

# Embeddings

Types:

```python
from groq.types import CreateEmbeddingResponse, Embedding
```

Methods:

- <code title="post /openai/v1/embeddings">client.embeddings.<a href="./src/groq/resources/embeddings.py">create</a>(\*\*<a href="src/groq/types/embedding_create_params.py">params</a>) -> <a href="./src/groq/types/create_embedding_response.py">CreateEmbeddingResponse</a></code>

# Audio

## Speech

Methods:

- <code title="post /openai/v1/audio/speech">client.audio.speech.<a href="./src/groq/resources/audio/speech.py">create</a>(\*\*<a href="src/groq/types/audio/speech_create_params.py">params</a>) -> BinaryAPIResponse</code>

## Transcriptions

Types:

```python
from groq.types.audio import Transcription
```

Methods:

- <code title="post /openai/v1/audio/transcriptions">client.audio.transcriptions.<a href="./src/groq/resources/audio/transcriptions.py">create</a>(\*\*<a href="src/groq/types/audio/transcription_create_params.py">params</a>) -> <a href="./src/groq/types/audio/transcription.py">Transcription</a></code>

## Translations

Types:

```python
from groq.types.audio import Translation
```

Methods:

- <code title="post /openai/v1/audio/translations">client.audio.translations.<a href="./src/groq/resources/audio/translations.py">create</a>(\*\*<a href="src/groq/types/audio/translation_create_params.py">params</a>) -> <a href="./src/groq/types/audio/translation.py">Translation</a></code>

# Models

Types:

```python
from groq.types import Model, ModelDeleted, ModelListResponse
```

Methods:

- <code title="get /openai/v1/models/{model}">client.models.<a href="./src/groq/resources/models.py">retrieve</a>(model) -> <a href="./src/groq/types/model.py">Model</a></code>
- <code title="get /openai/v1/models">client.models.<a href="./src/groq/resources/models.py">list</a>() -> <a href="./src/groq/types/model_list_response.py">ModelListResponse</a></code>
- <code title="delete /openai/v1/models/{model}">client.models.<a href="./src/groq/resources/models.py">delete</a>(model) -> <a href="./src/groq/types/model_deleted.py">ModelDeleted</a></code>

# Batches

Types:

```python
from groq.types import (
    BatchCreateResponse,
    BatchRetrieveResponse,
    BatchListResponse,
    BatchCancelResponse,
)
```

Methods:

- <code title="post /openai/v1/batches">client.batches.<a href="./src/groq/resources/batches.py">create</a>(\*\*<a href="src/groq/types/batch_create_params.py">params</a>) -> <a href="./src/groq/types/batch_create_response.py">BatchCreateResponse</a></code>
- <code title="get /openai/v1/batches/{batch_id}">client.batches.<a href="./src/groq/resources/batches.py">retrieve</a>(batch_id) -> <a href="./src/groq/types/batch_retrieve_response.py">BatchRetrieveResponse</a></code>
- <code title="get /openai/v1/batches">client.batches.<a href="./src/groq/resources/batches.py">list</a>() -> <a href="./src/groq/types/batch_list_response.py">BatchListResponse</a></code>
- <code title="post /openai/v1/batches/{batch_id}/cancel">client.batches.<a href="./src/groq/resources/batches.py">cancel</a>(batch_id) -> <a href="./src/groq/types/batch_cancel_response.py">BatchCancelResponse</a></code>

# Files

Types:

```python
from groq.types import FileCreateResponse, FileListResponse, FileDeleteResponse, FileInfoResponse
```

Methods:

- <code title="post /openai/v1/files">client.files.<a href="./src/groq/resources/files.py">create</a>(\*\*<a href="src/groq/types/file_create_params.py">params</a>) -> <a href="./src/groq/types/file_create_response.py">FileCreateResponse</a></code>
- <code title="get /openai/v1/files">client.files.<a href="./src/groq/resources/files.py">list</a>() -> <a href="./src/groq/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /openai/v1/files/{file_id}">client.files.<a href="./src/groq/resources/files.py">delete</a>(file_id) -> <a href="./src/groq/types/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /openai/v1/files/{file_id}/content">client.files.<a href="./src/groq/resources/files.py">content</a>(file_id) -> BinaryAPIResponse</code>
- <code title="get /openai/v1/files/{file_id}">client.files.<a href="./src/groq/resources/files.py">info</a>(file_id) -> <a href="./src/groq/types/file_info_response.py">FileInfoResponse</a></code>
