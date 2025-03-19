# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpeechCreateParams"]


class SpeechCreateParams(TypedDict, total=False):
    input: Required[str]
    """The text to generate audio for."""

    model: Required[str]
    """One of the available TTS models"""

    voice: Required[str]
    """The voice to use when generating the audio."""

    response_format: Literal["wav"]
    """The format to audio in. Supported formats are `wav`."""

    speed: float
    """The speed of the generated audio. 1.0 is the only supported value."""
