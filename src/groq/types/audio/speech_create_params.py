# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpeechCreateParams"]


class SpeechCreateParams(TypedDict, total=False):
    input: Required[str]
    """The text to generate audio for."""

    model: Required[Union[str, Literal["playai-tts", "playai-tts-arabic"]]]
    """One of the [available TTS models](/docs/text-to-speech)."""

    voice: Required[str]
    """The voice to use when generating the audio.

    List of voices can be found [here](/docs/text-to-speech).
    """

    response_format: Literal["wav", "mp3"]
    """The format to audio in. Supported formats are `wav, mp3`."""

    speed: float
    """The speed of the generated audio. 1.0 is the only supported value."""
