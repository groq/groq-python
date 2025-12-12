# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .chat_completion_tool_param import ChatCompletionToolParam
from .chat_completion_message_param import ChatCompletionMessageParam
from ..shared_params.function_parameters import FunctionParameters
from .chat_completion_tool_choice_option_param import ChatCompletionToolChoiceOptionParam
from .chat_completion_function_call_option_param import ChatCompletionFunctionCallOptionParam

__all__ = [
    "CompletionCreateParams",
    "CompoundCustom",
    "CompoundCustomModels",
    "CompoundCustomTools",
    "CompoundCustomToolsWolframSettings",
    "Document",
    "DocumentSource",
    "DocumentSourceChatCompletionDocumentSourceText",
    "DocumentSourceChatCompletionDocumentSourceJson",
    "FunctionCall",
    "Function",
    "ResponseFormat",
    "ResponseFormatResponseFormatText",
    "ResponseFormatResponseFormatJsonSchema",
    "ResponseFormatResponseFormatJsonSchemaJsonSchema",
    "ResponseFormatResponseFormatJsonObject",
    "SearchSettings",
]


class CompletionCreateParams(TypedDict, total=False):
    messages: Required[Iterable[ChatCompletionMessageParam]]
    """A list of messages comprising the conversation so far."""

    model: Required[
        Union[
            str,
            Literal[
                "compound-beta",
                "compound-beta-mini",
                "gemma2-9b-it",
                "llama-3.1-8b-instant",
                "llama-3.3-70b-versatile",
                "meta-llama/llama-4-maverick-17b-128e-instruct",
                "meta-llama/llama-4-scout-17b-16e-instruct",
                "meta-llama/llama-guard-4-12b",
                "moonshotai/kimi-k2-instruct",
                "openai/gpt-oss-120b",
                "openai/gpt-oss-20b",
                "qwen/qwen3-32b",
            ],
        ]
    ]
    """ID of the model to use.

    For details on which models are compatible with the Chat API, see available
    [models](https://console.groq.com/docs/models)
    """

    citation_options: Optional[Literal["enabled", "disabled"]]
    """Whether to enable citations in the response.

    When enabled, the model will include citations for information retrieved from
    provided documents or web searches.
    """

    compound_custom: Optional[CompoundCustom]
    """Custom configuration of models and tools for Compound."""

    disable_tool_validation: bool
    """
    If set to true, groq will return called tools without validating that the tool
    is present in request.tools. tool_choice=required/none will still be enforced,
    but the request cannot require a specific tool be used.
    """

    documents: Optional[Iterable[Document]]
    """A list of documents to provide context for the conversation.

    Each document contains text that can be referenced by the model.
    """

    exclude_domains: Optional[SequenceNotStr[str]]
    """
    Deprecated: Use search_settings.exclude_domains instead. A list of domains to
    exclude from the search results when the model uses a web search tool.
    """

    frequency_penalty: Optional[float]
    """This is not yet supported by any of our models.

    Number between -2.0 and 2.0. Positive values penalize new tokens based on their
    existing frequency in the text so far, decreasing the model's likelihood to
    repeat the same line verbatim.
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

    include_domains: Optional[SequenceNotStr[str]]
    """
    Deprecated: Use search_settings.include_domains instead. A list of domains to
    include in the search results when the model uses a web search tool.
    """

    include_reasoning: Optional[bool]
    """Whether to include reasoning in the response.

    If true, the response will include a `reasoning` field. If false, the model's
    reasoning will not be included in the response. This field is mutually exclusive
    with `reasoning_format`.
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

    max_completion_tokens: Optional[int]
    """The maximum number of tokens that can be generated in the chat completion.

    The total length of input tokens and generated tokens is limited by the model's
    context length.
    """

    max_tokens: Optional[int]
    """
    Deprecated in favor of `max_completion_tokens`. The maximum number of tokens
    that can be generated in the chat completion. The total length of input tokens
    and generated tokens is limited by the model's context length.
    """

    metadata: Optional[Dict[str, str]]
    """This parameter is not currently supported."""

    n: Optional[int]
    """How many chat completion choices to generate for each input message.

    Note that the current moment, only n=1 is supported. Other values will result in
    a 400 response.
    """

    parallel_tool_calls: Optional[bool]
    """Whether to enable parallel function calling during tool use."""

    presence_penalty: Optional[float]
    """This is not yet supported by any of our models.

    Number between -2.0 and 2.0. Positive values penalize new tokens based on
    whether they appear in the text so far, increasing the model's likelihood to
    talk about new topics.
    """

    reasoning_effort: Optional[Literal["none", "default", "low", "medium", "high"]]
    """
    qwen3 models support the following values Set to 'none' to disable reasoning.
    Set to 'default' or null to let Qwen reason.

    openai/gpt-oss-20b and openai/gpt-oss-120b support 'low', 'medium', or 'high'.
    'medium' is the default value.
    """

    reasoning_format: Optional[Literal["hidden", "raw", "parsed"]]
    """
    Specifies how to output reasoning tokens This field is mutually exclusive with
    `include_reasoning`.
    """

    response_format: Optional[ResponseFormat]
    """An object specifying the format that the model must output.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
    Outputs which ensures the model will match your supplied JSON schema.
    `json_schema` response format is only available on
    [supported models](https://console.groq.com/docs/structured-outputs#supported-models).
    Setting to `{ "type": "json_object" }` enables the older JSON mode, which
    ensures the message the model generates is valid JSON. Using `json_schema` is
    preferred for models that support it.
    """

    search_settings: Optional[SearchSettings]
    """Settings for web search functionality when the model uses a web search tool."""

    seed: Optional[int]
    """
    If specified, our system will make a best effort to sample deterministically,
    such that repeated requests with the same `seed` and parameters should return
    the same result. Determinism is not guaranteed, and you should refer to the
    `system_fingerprint` response parameter to monitor changes in the backend.
    """

    service_tier: Optional[Literal["auto", "on_demand", "flex", "performance"]]
    """The service tier to use for the request. Defaults to `on_demand`.

    - `auto` will automatically select the highest tier available within the rate
      limits of your organization.
    - `flex` uses the flex tier, which will succeed or fail quickly.
    """

    stop: Union[Optional[str], SequenceNotStr[str], None]
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

    store: Optional[bool]
    """This parameter is not currently supported."""

    stream: Optional[bool]
    """If set, partial message deltas will be sent.

    Tokens will be sent as data-only
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
    as they become available, with the stream terminated by a `data: [DONE]`
    message. [Example code](/docs/text-chat#streaming-a-chat-completion).
    """

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. We generally recommend altering
    this or top_p but not both.
    """

    tool_choice: Optional[ChatCompletionToolChoiceOptionParam]
    """
    Controls which (if any) tool is called by the model. `none` means the model will
    not call any tool and instead generates a message. `auto` means the model can
    pick between generating a message or calling one or more tools. `required` means
    the model must call one or more tools. Specifying a particular tool via
    `{"type": "function", "function": {"name": "my_function"}}` forces the model to
    call that tool.

    `none` is the default when no tools are present. `auto` is the default if tools
    are present.
    """

    tools: Optional[Iterable[ChatCompletionToolParam]]
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


class CompoundCustomModels(TypedDict, total=False):
    answering_model: Optional[str]
    """Custom model to use for answering."""

    reasoning_model: Optional[str]
    """Custom model to use for reasoning."""


class CompoundCustomToolsWolframSettings(TypedDict, total=False):
    """Configuration for the Wolfram tool integration."""

    authorization: Optional[str]
    """API key used to authorize requests to Wolfram services."""


class CompoundCustomTools(TypedDict, total=False):
    """Configuration options for tools available to Compound."""

    enabled_tools: Optional[SequenceNotStr[str]]
    """A list of tool names that are enabled for the request."""

    wolfram_settings: Optional[CompoundCustomToolsWolframSettings]
    """Configuration for the Wolfram tool integration."""


class CompoundCustom(TypedDict, total=False):
    """Custom configuration of models and tools for Compound."""

    models: Optional[CompoundCustomModels]

    tools: Optional[CompoundCustomTools]
    """Configuration options for tools available to Compound."""


class DocumentSourceChatCompletionDocumentSourceText(TypedDict, total=False):
    """A document whose contents are provided inline as text."""

    text: Required[str]
    """The document contents."""

    type: Required[Literal["text"]]
    """Identifies this document source as inline text."""


class DocumentSourceChatCompletionDocumentSourceJson(TypedDict, total=False):
    """A document whose contents are provided inline as JSON data."""

    data: Required[Dict[str, object]]
    """The JSON payload associated with the document."""

    type: Required[Literal["json"]]
    """Identifies this document source as JSON data."""


DocumentSource: TypeAlias = Union[
    DocumentSourceChatCompletionDocumentSourceText, DocumentSourceChatCompletionDocumentSourceJson
]


class Document(TypedDict, total=False):
    """A document that can be referenced by the model while generating responses."""

    source: Required[DocumentSource]
    """The source of the document. Only text and JSON sources are currently supported."""

    id: Optional[str]
    """Optional unique identifier that can be used for citations in responses."""


FunctionCall: TypeAlias = Union[Literal["none", "auto", "required"], ChatCompletionFunctionCallOptionParam]


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

    parameters: FunctionParameters
    """Function parameters defined as a JSON Schema object.

    Refer to https://json-schema.org/understanding-json-schema/ for schema
    documentation.
    """


class ResponseFormatResponseFormatText(TypedDict, total=False):
    """Default response format. Used to generate text responses."""

    type: Required[Literal["text"]]
    """The type of response format being defined. Always `text`."""


class ResponseFormatResponseFormatJsonSchemaJsonSchema(TypedDict, total=False):
    """Structured Outputs configuration options, including a JSON Schema."""

    name: Required[str]
    """The name of the response format.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: str
    """
    A description of what the response format is for, used by the model to determine
    how to respond in the format.
    """

    schema: Dict[str, object]
    """
    The schema for the response format, described as a JSON Schema object. Learn how
    to build JSON schemas [here](https://json-schema.org/).
    """

    strict: Optional[bool]
    """Whether to enable strict schema adherence when generating the output.

    If set to true, the model will always follow the exact schema defined in the
    `schema` field. Only a subset of JSON Schema is supported when `strict` is
    `true`.
    """


class ResponseFormatResponseFormatJsonSchema(TypedDict, total=False):
    """JSON Schema response format. Used to generate structured JSON responses."""

    json_schema: Required[ResponseFormatResponseFormatJsonSchemaJsonSchema]
    """Structured Outputs configuration options, including a JSON Schema."""

    type: Required[Literal["json_schema"]]
    """The type of response format being defined. Always `json_schema`."""


class ResponseFormatResponseFormatJsonObject(TypedDict, total=False):
    """JSON object response format.

    An older method of generating JSON responses. Using `json_schema` is recommended for models that support it. Note that the model will not generate JSON without a system or user message instructing it to do so.
    """

    type: Required[Literal["json_object"]]
    """The type of response format being defined. Always `json_object`."""


ResponseFormat: TypeAlias = Union[
    ResponseFormatResponseFormatText, ResponseFormatResponseFormatJsonSchema, ResponseFormatResponseFormatJsonObject
]


class SearchSettings(TypedDict, total=False):
    """Settings for web search functionality when the model uses a web search tool."""

    country: Optional[str]
    """
    Name of country to prioritize search results from (e.g., "united states",
    "germany", "france").
    """

    exclude_domains: Optional[SequenceNotStr[str]]
    """A list of domains to exclude from the search results."""

    include_domains: Optional[SequenceNotStr[str]]
    """A list of domains to include in the search results."""

    include_images: Optional[bool]
    """Whether to include images in the search results."""
