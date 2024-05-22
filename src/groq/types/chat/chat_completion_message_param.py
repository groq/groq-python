# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .chat_completion_content_part_param import ChatCompletionContentPartParam
from .chat_completion_function_message_param import ChatCompletionFunctionMessageParam
from .chat_completion_assistant_message_param import ChatCompletionAssistantMessageParam

__all__ = [
    "ChatCompletionMessageParam",
    "ChatCompletionRequestSystemMessage",
    "ChatCompletionRequestUserMessage",
    "ChatCompletionRequestToolMessage",
]


class ChatCompletionRequestSystemMessage(TypedDict, total=False):
    content: Required[str]
    """The contents of the system message."""

    role: Required[Literal["system"]]
    """The role of the messages author, in this case `system`."""

    name: str
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """

    tool_call_id: Optional[str]


class ChatCompletionRequestUserMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[ChatCompletionContentPartParam]]]
    """The contents of the user message."""

    role: Required[Literal["user"]]
    """The role of the messages author, in this case `user`."""

    name: Optional[str]
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """

    tool_call_id: Optional[str]


class ChatCompletionRequestToolMessage(TypedDict, total=False):
    content: Required[str]
    """The contents of the tool message."""

    role: Required[Literal["tool"]]
    """The role of the messages author, in this case `tool`."""

    tool_call_id: Required[str]
    """Tool call that this message is responding to."""

    name: Optional[str]


ChatCompletionMessageParam = Union[
    ChatCompletionRequestSystemMessage,
    ChatCompletionRequestUserMessage,
    ChatCompletionAssistantMessageParam,
    ChatCompletionRequestToolMessage,
    ChatCompletionFunctionMessageParam,
]
