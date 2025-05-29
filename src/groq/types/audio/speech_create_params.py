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

    response_format: Literal["flac", "mp3", "mulaw", "ogg", "wav"]
    """The format of the generated audio.

    Supported formats are `flac, mp3, mulaw, ogg, wav`.
    """

    sample_rate: Literal[8000, 16000, 22050, 24000, 32000, 44100, 48000]
    """The sample rate for generated audio"""

    speed: float
    """The speed of the generated audio."""
