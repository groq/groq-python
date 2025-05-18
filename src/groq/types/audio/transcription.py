# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from typing import List, Union

__all__ = ["Transcription"]

class Transcription(BaseModel):
    text: str
    """The transcribed text."""
    words: Union[List[dict], None]
    """The words in the transcription depending on the granularity setting."""
