# Shared Types

```python
from groq.types import ErrorObject, FunctionDefinition, FunctionParameters
```

# Embeddings

Types:

```python
from groq.types import CreateEmbeddingResponse, Embedding
```

Methods:

- <code title="post /openai/v1/embeddings">client.embeddings.<a href="./src/groq/resources/embeddings.py">create</a>(\*\*<a href="src/groq/types/embedding_create_params.py">params</a>) -> <a href="./src/groq/types/create_embedding_response.py">CreateEmbeddingResponse</a></code>

# Chat

## Completions

Types:

```python
from groq.types.chat import (
    ChatCompletionAssistantMessageParam,
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
    ChatCompletionToolChoiceOption,
    ChatCompletionToolMessageParam,
    ChatCompletionUserMessageParam,
    CompletionCreateResponse,
)
```

Methods:

- <code title="post /openai/v1/chat/completions">client.chat.completions.<a href="./src/groq/resources/chat/completions.py">create</a>(\*\*<a href="src/groq/types/chat/completion_create_params.py">params</a>) -> <a href="./src/groq/types/chat/completion_create_response.py">CompletionCreateResponse</a></code>

# Audio

## Transcriptions

Types:

```python
from groq.types.audio import Transcription, TranscriptionCreateResponse
```

Methods:

- <code title="post /openai/v1/audio/transcriptions">client.audio.transcriptions.<a href="./src/groq/resources/audio/transcriptions.py">create</a>(\*\*<a href="src/groq/types/audio/transcription_create_params.py">params</a>) -> <a href="./src/groq/types/audio/transcription_create_response.py">TranscriptionCreateResponse</a></code>

## Translations

Types:

```python
from groq.types.audio import Translation, TranslationCreateResponse
```

Methods:

- <code title="post /openai/v1/audio/translations">client.audio.translations.<a href="./src/groq/resources/audio/translations.py">create</a>(\*\*<a href="src/groq/types/audio/translation_create_params.py">params</a>) -> <a href="./src/groq/types/audio/translation_create_response.py">TranslationCreateResponse</a></code>

# Models

Types:

```python
from groq.types import Model, ModelListResponse, ModelDeleteResponse
```

Methods:

- <code title="get /openai/v1/models/{model}">client.models.<a href="./src/groq/resources/models.py">retrieve</a>(model) -> <a href="./src/groq/types/model.py">Model</a></code>
- <code title="get /openai/v1/models">client.models.<a href="./src/groq/resources/models.py">list</a>() -> <a href="./src/groq/types/model_list_response.py">ModelListResponse</a></code>
- <code title="delete /openai/v1/models/{model}">client.models.<a href="./src/groq/resources/models.py">delete</a>(model) -> <a href="./src/groq/types/model_delete_response.py">ModelDeleteResponse</a></code>
