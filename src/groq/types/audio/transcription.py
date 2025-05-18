# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from typing import List, Union

__all__ = ["Transcription"]

class Word(BaseModel):
    word: str
    """The transcribed word"""
    start: float
    """The start of the word (in milliseconds)"""
    end: float
    """The end of the word (in milliseconds)"""

class Transcription(BaseModel):
    text: str
    """The transcribed text."""
    words: Union[List[Word], None]
    """The words in the transcription depending on the granularity setting."""
