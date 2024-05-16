# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CompletionCreateParams",
    "Message",
    "MessageContentUnionMember1",
    "MessageContentUnionMember1TypesChatCompletionRequestMessageContentPartText",
    "MessageContentUnionMember1TypesChatCompletionRequestMessageContentPartImage",
    "MessageContentUnionMember1TypesChatCompletionRequestMessageContentPartImageImageURL",
    "MessageToolCall",
    "MessageToolCallFunction",
    "ResponseFormat",
    "ToolChoice",
    "ToolChoiceToolChoice",
    "ToolChoiceToolChoiceFunction",
    "Tool",
    "ToolFunction",
]


class CompletionCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    model: Required[str]

    frequency_penalty: float

    logit_bias: Dict[str, int]

    logprobs: bool

    max_tokens: int

    n: int

    presence_penalty: float

    response_format: ResponseFormat

    seed: int

    stop: Union[Optional[str], List[str], None]
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

    stream: bool

    temperature: float

    tool_choice: ToolChoice

    tools: Iterable[Tool]

    top_logprobs: int

    top_p: float

    user: str


class MessageContentUnionMember1TypesChatCompletionRequestMessageContentPartText(TypedDict, total=False):
    text: Required[str]
    """The text content."""

    type: Required[Literal["text"]]
    """The type of the content part."""


class MessageContentUnionMember1TypesChatCompletionRequestMessageContentPartImageImageURL(TypedDict, total=False):
    url: Required[str]
    """Either a URL of the image or the base64 encoded image data."""

    detail: Literal["auto", "low", "high"]
    """Specifies the detail level of the image."""


class MessageContentUnionMember1TypesChatCompletionRequestMessageContentPartImage(TypedDict, total=False):
    image_url: Required[MessageContentUnionMember1TypesChatCompletionRequestMessageContentPartImageImageURL]

    type: Required[Literal["image_url"]]
    """The type of the content part."""


MessageContentUnionMember1 = Union[
    MessageContentUnionMember1TypesChatCompletionRequestMessageContentPartText,
    MessageContentUnionMember1TypesChatCompletionRequestMessageContentPartImage,
]


class MessageToolCallFunction(TypedDict, total=False):
    arguments: str

    name: str


class MessageToolCall(TypedDict, total=False):
    id: str

    function: MessageToolCallFunction

    type: str


class Message(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageContentUnionMember1]]]

    role: Required[str]

    name: str

    tool_call_id: str
    """ToolMessage Fields"""

    tool_calls: Iterable[MessageToolCall]
    """AssistantMessage Fields"""


class ResponseFormat(TypedDict, total=False):
    type: str


class ToolChoiceToolChoiceFunction(TypedDict, total=False):
    name: str


class ToolChoiceToolChoice(TypedDict, total=False):
    function: ToolChoiceToolChoiceFunction

    type: str


class ToolChoice(TypedDict, total=False):
    string: str

    tool_choice: Annotated[ToolChoiceToolChoice, PropertyInfo(alias="toolChoice")]


class ToolFunction(TypedDict, total=False):
    description: str

    name: str

    parameters: Dict[str, object]


class Tool(TypedDict, total=False):
    function: ToolFunction

    type: str
