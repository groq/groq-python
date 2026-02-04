# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam
from .chat_completion_content_part_image_param import ChatCompletionContentPartImageParam

__all__ = [
    "ChatCompletionContentPartParam",
    "ChatCompletionRequestMessageContentPartDocument",
    "ChatCompletionRequestMessageContentPartDocumentDocument",
]


class ChatCompletionRequestMessageContentPartDocumentDocument(TypedDict, total=False):
    data: Required[Dict[str, object]]
    """The JSON document data."""

    id: Optional[str]
    """Optional unique identifier for the document."""


class ChatCompletionRequestMessageContentPartDocument(TypedDict, total=False):
    document: Required[ChatCompletionRequestMessageContentPartDocumentDocument]

    type: Required[Literal["document"]]
    """The type of the content part."""


ChatCompletionContentPartParam: TypeAlias = Union[
    ChatCompletionContentPartTextParam,
    ChatCompletionContentPartImageParam,
    ChatCompletionRequestMessageContentPartDocument,
]
