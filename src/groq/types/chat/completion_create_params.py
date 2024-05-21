# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CompletionCreateParams",
    "Message",
    "MessageChatCompletionRequestSystemMessage",
    "MessageChatCompletionRequestUserMessage",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPart",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartText",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartImage",
    "MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartImageImageURL",
    "MessageChatCompletionRequestAssistantMessage",
    "MessageChatCompletionRequestAssistantMessageFunctionCall",
    "MessageChatCompletionRequestAssistantMessageToolCall",
    "MessageChatCompletionRequestAssistantMessageToolCallFunction",
    "MessageChatCompletionRequestToolMessage",
    "MessageChatCompletionRequestFunctionMessage",
    "FunctionCall",
    "FunctionCallChatCompletionFunctionCallOption",
    "Function",
    "ResponseFormat",
    "ToolChoice",
    "ToolChoiceChatToolChoice",
    "ToolChoiceChatToolChoiceFunction",
    "Tool",
    "ToolFunction",
]


class CompletionCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """A list of messages comprising the conversation so far."""

    model: Required[str]
    """ID of the model to use.

    For details on which models are compatible with the Chat API, see available
    [models](/docs/models)
    """

    frequency_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on their existing frequency in the
    text so far, decreasing the model's likelihood to repeat the same line verbatim.
    """

    function_call: Optional[FunctionCall]
    """Deprecated in favor of `tool_choice`.

    Controls which (if any) function is called by the model. `none` means the model
    will not call a function and instead generates a message. `auto` means the model
    can pick between generating a message or calling a function. Specifying a
    particular function via `{"name": "my_function"}` forces the model to call that
    function.

    `none` is the default when no functions are present. `auto` is the default if
    functions are present.
    """

    functions: Optional[Iterable[Function]]
    """Deprecated in favor of `tools`.

    A list of functions the model may generate JSON inputs for.
    """

    logit_bias: Optional[Dict[str, int]]
    """
    This is not yet supported by any of our models. Modify the likelihood of
    specified tokens appearing in the completion.
    """

    logprobs: Optional[bool]
    """
    This is not yet supported by any of our models. Whether to return log
    probabilities of the output tokens or not. If true, returns the log
    probabilities of each output token returned in the `content` of `message`.
    """

    max_tokens: Optional[int]
    """The maximum number of tokens that can be generated in the chat completion.

    The total length of input tokens and generated tokens is limited by the model's
    context length.
    """

    n: Optional[int]
    """How many chat completion choices to generate for each input message.

    Note that you will be charged based on the number of generated tokens across all
    of the choices. Keep `n` as `1` to minimize costs.
    """

    presence_penalty: Optional[float]
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far, increasing the model's likelihood to talk about new topics.
    """

    response_format: Optional[ResponseFormat]
    """An object specifying the format that the model must output.

    Setting to `{ "type": "json" }` enables JSON mode, which guarantees the message
    the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce
    JSON yourself via a system or user message. Without this, the model may generate
    an unending stream of whitespace until the generation reaches the token limit,
    resulting in a long-running and seemingly "stuck" request. Also note that the
    message content may be partially cut off if finish_reason="length", which
    indicates the generation exceeded max_tokens or the conversation exceeded the
    max context length.
    """

    seed: Optional[int]
    """
    If specified, our system will sample deterministically, such that repeated
    requests with the same seed and parameters will return the same result.
    """

    stop: Union[Optional[str], List[str], None]
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

    stream: Optional[bool]
    """If set, partial message deltas will be sent.

    Tokens will be sent as data-only server-sent events as they become available,
    with the stream terminated by a data: [DONE].
    [Example code](/docs/text-chat#streaming-a-chat-completion).
    """

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. We generally recommend altering
    this or top_p but not both
    """

    tool_choice: Optional[ToolChoice]
    """Controls which (if any) function is called by the model.

    Specifying a particular function via a structured object like
    `{"type": "function", "function": {"name": "my_function"}}` forces the model to
    call that function.
    """

    tools: Optional[Iterable[Tool]]
    """A list of tools the model may call.

    Currently, only functions are supported as a tool. Use this to provide a list of
    functions the model may generate JSON inputs for. A max of 128 functions are
    supported.
    """

    top_logprobs: Optional[int]
    """
    This is not yet supported by any of our models. An integer between 0 and 20
    specifying the number of most likely tokens to return at each token position,
    each with an associated log probability. `logprobs` must be set to `true` if
    this parameter is used.
    """

    top_p: Optional[float]
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered. We
    generally recommend altering this or temperature but not both.
    """

    user: Optional[str]
    """
    A unique identifier representing your end-user, which can help us monitor and
    detect abuse.
    """


class MessageChatCompletionRequestSystemMessage(TypedDict, total=False):
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


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartText(
    TypedDict, total=False
):
    text: Required[str]
    """The text content."""

    type: Required[Literal["text"]]
    """The type of the content part."""


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartImageImageURL(
    TypedDict, total=False
):
    url: Required[str]
    """Either a URL of the image or the base64 encoded image data."""

    detail: Literal["auto", "low", "high"]
    """Specifies the detail level of the image."""


class MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartImage(
    TypedDict, total=False
):
    image_url: Required[
        MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartImageImageURL
    ]

    type: Required[Literal["image_url"]]
    """The type of the content part."""


MessageChatCompletionRequestUserMessageContentArrayOfContentPart = Union[
    MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartText,
    MessageChatCompletionRequestUserMessageContentArrayOfContentPartChatCompletionRequestMessageContentPartImage,
]


class MessageChatCompletionRequestUserMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageChatCompletionRequestUserMessageContentArrayOfContentPart]]]
    """The contents of the user message."""

    role: Required[Literal["user"]]
    """The role of the messages author, in this case `user`."""

    name: Optional[str]
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """

    tool_call_id: Optional[str]


class MessageChatCompletionRequestAssistantMessageFunctionCall(TypedDict, total=False):
    arguments: Required[str]
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Required[str]
    """The name of the function to call."""


class MessageChatCompletionRequestAssistantMessageToolCallFunction(TypedDict, total=False):
    arguments: Required[str]
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Required[str]
    """The name of the function to call."""


class MessageChatCompletionRequestAssistantMessageToolCall(TypedDict, total=False):
    id: Required[str]
    """The ID of the tool call."""

    function: Required[MessageChatCompletionRequestAssistantMessageToolCallFunction]
    """The function that the model called."""

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class MessageChatCompletionRequestAssistantMessage(TypedDict, total=False):
    role: Required[Literal["assistant"]]
    """The role of the messages author, in this case `assistant`."""

    content: Optional[str]
    """The contents of the assistant message.

    Required unless `tool_calls` or `function_call` is specified.
    """

    function_call: MessageChatCompletionRequestAssistantMessageFunctionCall
    """Deprecated and replaced by `tool_calls`.

    The name and arguments of a function that should be called, as generated by the
    model.
    """

    name: str
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """

    tool_call_id: Optional[str]

    tool_calls: Iterable[MessageChatCompletionRequestAssistantMessageToolCall]
    """The tool calls generated by the model, such as function calls."""


class MessageChatCompletionRequestToolMessage(TypedDict, total=False):
    content: Required[str]
    """The contents of the tool message."""

    role: Required[Literal["tool"]]
    """The role of the messages author, in this case `tool`."""

    tool_call_id: Required[str]
    """Tool call that this message is responding to."""

    name: Optional[str]


class MessageChatCompletionRequestFunctionMessage(TypedDict, total=False):
    content: Required[Optional[str]]
    """The contents of the function message."""

    name: Required[str]
    """The name of the function to call."""

    role: Required[Literal["function"]]
    """The role of the messages author, in this case `function`."""

    tool_call_id: Optional[str]


Message = Union[
    MessageChatCompletionRequestSystemMessage,
    MessageChatCompletionRequestUserMessage,
    MessageChatCompletionRequestAssistantMessage,
    MessageChatCompletionRequestToolMessage,
    MessageChatCompletionRequestFunctionMessage,
]


class FunctionCallChatCompletionFunctionCallOption(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""


FunctionCall = Union[Literal["none", "auto"], FunctionCallChatCompletionFunctionCallOption]


class Function(TypedDict, total=False):
    name: Required[str]
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: str
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: Dict[str, object]
    """The parameters the functions accepts, described as a JSON Schema object.

    See the [guide](/docs/guides/text-generation/function-calling) for examples, and
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema/)
    for documentation about the format.

    Omitting `parameters` defines a function with an empty parameter list.
    """


class ResponseFormat(TypedDict, total=False):
    type: str


class ToolChoiceChatToolChoiceFunction(TypedDict, total=False):
    name: Required[str]
    """The name of the function to call."""


class ToolChoiceChatToolChoice(TypedDict, total=False):
    function: Required[ToolChoiceChatToolChoiceFunction]

    type: Required[Literal["function"]]


ToolChoice = Union[Literal["none", "auto"], ToolChoiceChatToolChoice]


class ToolFunction(TypedDict, total=False):
    name: Required[str]

    description: str

    parameters: Dict[str, object]


class Tool(TypedDict, total=False):
    function: Required[ToolFunction]

    type: Required[Literal["function"]]
