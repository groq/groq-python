# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["TranslationCreateParams"]


class TranslationCreateParams(TypedDict, total=False):
    model: Required[Union[str, Literal["whisper-large-v3", "whisper-large-v3-turbo"]]]
    """ID of the model to use.

    `whisper-large-v3` and `whisper-large-v3-turbo` are currently available.
    """

    file: FileTypes
    """
    The audio file object (not file name) translate, in one of these formats: flac,
    mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.
    """

    prompt: str
    """An optional text to guide the model's style or continue a previous audio
    segment.

    The [prompt](/docs/guides/speech-to-text/prompting) should be in English.
    """

    response_format: Literal["json", "text", "verbose_json"]
    """
    The format of the transcript output, in one of these options: `json`, `text`, or
    `verbose_json`.
    """

    temperature: float
    """The sampling temperature, between 0 and 1.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. If set to 0, the model will use
    [log probability](https://en.wikipedia.org/wiki/Log_probability) to
    automatically increase the temperature until certain thresholds are hit.
    """

    url: str
    """The audio URL to translate/transcribe (supports Base64URL).

    Either file or url must be provided. When using the Batch API only url is
    supported.
    """
