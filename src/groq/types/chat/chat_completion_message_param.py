# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

from .chat_completion_user_message_param import ChatCompletionUserMessageParam
from .chat_completion_system_message_param import ChatCompletionSystemMessageParam
from .chat_completion_function_message_param import ChatCompletionFunctionMessageParam
from .chat_completion_assistant_message_param import ChatCompletionAssistantMessageParam
from .chat_completion_message_tool_call_param import ChatCompletionMessageToolCallParam

__all__ = ["ChatCompletionMessageParam"]

ChatCompletionMessageParam = Union[
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
    ChatCompletionAssistantMessageParam,
    ChatCompletionMessageToolCallParam,
    ChatCompletionFunctionMessageParam,
]
