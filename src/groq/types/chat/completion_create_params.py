# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CompletionCreateParams",
    "Message",
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
    frequency_penalty: float

    logit_bias: Dict[str, int]

    logprobs: bool

    max_tokens: int

    messages: Iterable[Message]

    model: str

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


class MessageToolCallFunction(TypedDict, total=False):
    arguments: str

    name: str


class MessageToolCall(TypedDict, total=False):
    id: str

    function: MessageToolCallFunction

    type: str


class Message(TypedDict, total=False):
    content: str

    name: str

    role: str

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
