# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Transcription"]


class Transcription(BaseModel):
    """
    Represents a transcription response returned by model, based on the provided input.
    """

    text: str
    """The transcribed text."""
