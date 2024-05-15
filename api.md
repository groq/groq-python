# Embeddings

Types:

```python
from groq.types import Embeddings
```

Methods:

- <code title="post /openai/v1/embeddings">client.embeddings.<a href="./src/groq/resources/embeddings.py">create</a>(\*\*<a href="src/groq/types/embedding_create_params.py">params</a>) -> <a href="./src/groq/types/embeddings.py">Embeddings</a></code>

# Chat

## Completions

Types:

```python
from groq.types.chat import ChatCompletion
```

Methods:

- <code title="post /openai/v1/chat/completions">client.chat.completions.<a href="./src/groq/resources/chat/completions.py">create</a>(\*\*<a href="src/groq/types/chat/completion_create_params.py">params</a>) -> <a href="./src/groq/types/chat/chat_completion.py">ChatCompletion</a></code>

# Audio

Types:

```python
from groq.types import Translation
```

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
from groq.types.audio import TranslationCreateResponse
```

Methods:

- <code title="post /openai/v1/audio/translations">client.audio.translations.<a href="./src/groq/resources/audio/translations.py">create</a>(\*\*<a href="src/groq/types/audio/translation_create_params.py">params</a>) -> <a href="./src/groq/types/audio/translation_create_response.py">TranslationCreateResponse</a></code>

# Models

Types:

```python
from groq.types import Model, ModelList
```

Methods:

- <code title="get /openai/v1/models/{model}">client.models.<a href="./src/groq/resources/models.py">retrieve</a>(model) -> <a href="./src/groq/types/model.py">Model</a></code>
- <code title="get /openai/v1/models">client.models.<a href="./src/groq/resources/models.py">list</a>() -> <a href="./src/groq/types/model_list.py">ModelList</a></code>
- <code title="delete /openai/v1/models/{model}">client.models.<a href="./src/groq/resources/models.py">delete</a>(model) -> None</code>
