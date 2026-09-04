# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..completion_usage import CompletionUsage
from .chat_completion_token_logprob import ChatCompletionTokenLogprob

__all__ = [
    "ChatCompletionChunk",
    "Choice",
    "ChoiceDelta",
    "ChoiceDeltaAnnotation",
    "ChoiceDeltaAnnotationDocumentCitation",
    "ChoiceDeltaAnnotationFunctionCitation",
    "ChoiceDeltaExecutedTool",
    "ChoiceDeltaExecutedToolBrowserResult",
    "ChoiceDeltaExecutedToolCodeResult",
    "ChoiceDeltaExecutedToolCodeResultChart",
    "ChoiceDeltaExecutedToolCodeResultChartElement",
    "ChoiceDeltaExecutedToolSearchResults",
    "ChoiceDeltaExecutedToolSearchResultsResult",
    "ChoiceDeltaFunctionCall",
    "ChoiceDeltaToolCall",
    "ChoiceDeltaToolCallFunction",
    "ChoiceLogprobs",
    "XGroq",
    "XGroqDebug",
    "XGroqUsageBreakdown",
    "XGroqUsageBreakdownModel",
]


class ChoiceDeltaAnnotationDocumentCitation(BaseModel):
    """A citation referencing a specific document that was provided in the request."""

    document_id: str
    """
    The ID of the document being cited, corresponding to a document provided in the
    request.
    """

    end_index: int
    """The character index in the message content where this citation ends."""

    start_index: int
    """The character index in the message content where this citation begins."""


class ChoiceDeltaAnnotationFunctionCitation(BaseModel):
    """A citation referencing the result of a function or tool call."""

    end_index: int
    """The character index in the message content where this citation ends."""

    start_index: int
    """The character index in the message content where this citation begins."""

    tool_call_id: str
    """
    The ID of the tool call being cited, corresponding to a tool call made during
    the conversation.
    """


class ChoiceDeltaAnnotation(BaseModel):
    """An annotation that provides citations or references for content in a message."""

    type: Literal["document_citation", "function_citation"]
    """The type of annotation."""

    document_citation: Optional[ChoiceDeltaAnnotationDocumentCitation] = None
    """A citation referencing a specific document that was provided in the request."""

    function_citation: Optional[ChoiceDeltaAnnotationFunctionCitation] = None
    """A citation referencing the result of a function or tool call."""


class ChoiceDeltaExecutedToolBrowserResult(BaseModel):
    title: str
    """The title of the browser window"""

    url: str
    """The URL of the browser window"""

    content: Optional[str] = None
    """The content of the browser result"""

    live_view_url: Optional[str] = None
    """The live view URL for the browser window"""


class ChoiceDeltaExecutedToolCodeResultChartElement(BaseModel):
    label: str
    """The label for this chart element"""

    angle: Optional[float] = None
    """The angle for this element"""

    first_quartile: Optional[float] = None
    """The first quartile value for this element"""

    group: Optional[str] = None
    """The group this element belongs to"""

    max: Optional[float] = None

    median: Optional[float] = None
    """The median value for this element"""

    min: Optional[float] = None
    """The minimum value for this element"""

    outliers: Optional[List[float]] = None
    """The outliers for this element"""

    points: Optional[List[List[float]]] = None
    """The points for this element"""

    radius: Optional[float] = None
    """The radius for this element"""

    third_quartile: Optional[float] = None
    """The third quartile value for this element"""

    value: Optional[float] = None
    """The value for this element"""


class ChoiceDeltaExecutedToolCodeResultChart(BaseModel):
    elements: List[ChoiceDeltaExecutedToolCodeResultChartElement]
    """The chart elements (data series, points, etc.)"""

    type: Literal["bar", "box_and_whisker", "line", "pie", "scatter", "superchart", "unknown"]
    """The type of chart"""

    title: Optional[str] = None
    """The title of the chart"""

    x_label: Optional[str] = None
    """The label for the x-axis"""

    x_scale: Optional[str] = None
    """The scale type for the x-axis"""

    x_tick_labels: Optional[List[str]] = None
    """The labels for the x-axis ticks"""

    x_ticks: Optional[List[float]] = None
    """The tick values for the x-axis"""

    x_unit: Optional[str] = None
    """The unit for the x-axis"""

    y_label: Optional[str] = None
    """The label for the y-axis"""

    y_scale: Optional[str] = None
    """The scale type for the y-axis"""

    y_tick_labels: Optional[List[str]] = None
    """The labels for the y-axis ticks"""

    y_ticks: Optional[List[float]] = None
    """The tick values for the y-axis"""

    y_unit: Optional[str] = None
    """The unit for the y-axis"""


class ChoiceDeltaExecutedToolCodeResult(BaseModel):
    chart: Optional[ChoiceDeltaExecutedToolCodeResultChart] = None

    charts: Optional[List[ChoiceDeltaExecutedToolCodeResultChart]] = None
    """Array of charts from a superchart"""

    png: Optional[str] = None
    """Base64 encoded PNG image output from code execution"""

    text: Optional[str] = None
    """The text version of the code execution result"""


class ChoiceDeltaExecutedToolSearchResultsResult(BaseModel):
    content: Optional[str] = None
    """The content of the search result"""

    score: Optional[float] = None
    """The relevance score of the search result"""

    title: Optional[str] = None
    """The title of the search result"""

    url: Optional[str] = None
    """The URL of the search result"""


class ChoiceDeltaExecutedToolSearchResults(BaseModel):
    """The search results returned by the tool, if applicable."""

    images: Optional[List[str]] = None
    """List of image URLs returned by the search"""

    results: Optional[List[ChoiceDeltaExecutedToolSearchResultsResult]] = None
    """List of search results"""


class ChoiceDeltaExecutedTool(BaseModel):
    arguments: str
    """The arguments passed to the tool in JSON format."""

    index: int
    """The index of the executed tool."""

    type: str
    """The type of tool that was executed."""

    browser_results: Optional[List[ChoiceDeltaExecutedToolBrowserResult]] = None
    """Array of browser results"""

    code_results: Optional[List[ChoiceDeltaExecutedToolCodeResult]] = None
    """Array of code execution results"""

    output: Optional[str] = None
    """The output returned by the tool."""

    search_results: Optional[ChoiceDeltaExecutedToolSearchResults] = None
    """The search results returned by the tool, if applicable."""


class ChoiceDeltaFunctionCall(BaseModel):
    """Deprecated and replaced by `tool_calls`.

    The name and arguments of a function that should be called, as generated by the model.
    """

    arguments: Optional[str] = None
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Optional[str] = None
    """The name of the function to call."""


class ChoiceDeltaToolCallFunction(BaseModel):
    arguments: Optional[str] = None
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Optional[str] = None
    """The name of the function to call."""


class ChoiceDeltaToolCall(BaseModel):
    index: int

    id: Optional[str] = None
    """The ID of the tool call."""

    function: Optional[ChoiceDeltaToolCallFunction] = None

    type: Optional[Literal["function"]] = None
    """The type of the tool. Currently, only `function` is supported."""


class ChoiceDelta(BaseModel):
    """A chat completion delta generated by streamed model responses."""

    annotations: Optional[List[ChoiceDeltaAnnotation]] = None
    """
    A list of annotations providing citations and references for the content in the
    message.
    """

    content: Optional[str] = None
    """The contents of the chunk message."""

    executed_tools: Optional[List[ChoiceDeltaExecutedTool]] = None
    """
    A list of tools that were executed during the chat completion for compound AI
    systems.
    """

    function_call: Optional[ChoiceDeltaFunctionCall] = None
    """Deprecated and replaced by `tool_calls`.

    The name and arguments of a function that should be called, as generated by the
    model.
    """

    reasoning: Optional[str] = None
    """The model's reasoning for a response.

    Only available for
    [models that support reasoning](https://console.groq.com/docs/reasoning) when
    request parameter reasoning_format has value `parsed`.
    """

    refusal: Optional[str] = None
    """A safety refusal the model generated instead of content."""

    role: Optional[Literal["system", "user", "assistant", "tool"]] = None
    """The role of the author of this message."""

    tool_calls: Optional[List[ChoiceDeltaToolCall]] = None


class ChoiceLogprobs(BaseModel):
    """Log probability information for the choice."""

    content: Optional[List[ChatCompletionTokenLogprob]] = None
    """A list of message content tokens with log probability information."""


class Choice(BaseModel):
    delta: ChoiceDelta
    """A chat completion delta generated by streamed model responses."""

    finish_reason: Optional[Literal["stop", "length", "tool_calls", "function_call"]] = None
    """The reason the model stopped generating tokens.

    This will be `stop` if the model hit a natural stop point or a provided stop
    sequence, `length` if the maximum number of tokens specified in the request was
    reached, `tool_calls` if the model called a tool, or `function_call`
    (deprecated) if the model called a function.
    """

    index: int
    """The index of the choice in the list of choices."""

    logprobs: Optional[ChoiceLogprobs] = None
    """Log probability information for the choice."""


class XGroqDebug(BaseModel):
    """Debug information including input and output token IDs and strings.

    Only present when debug=true in the request.
    """

    input_token_ids: Optional[List[int]] = None
    """Token IDs for the input."""

    input_tokens: Optional[List[str]] = None
    """Token strings for the input."""

    output_token_ids: Optional[List[int]] = None
    """Token IDs for the output."""

    output_tokens: Optional[List[str]] = None
    """Token strings for the output."""


class XGroqUsageBreakdownModel(BaseModel):
    model: str
    """The name/identifier of the model used"""

    usage: CompletionUsage
    """Usage statistics for the completion request."""


class XGroqUsageBreakdown(BaseModel):
    """Usage statistics for compound AI completion requests."""

    models: List[XGroqUsageBreakdownModel]
    """List of models used in the request and their individual usage statistics"""


class XGroq(BaseModel):
    """Groq-specific metadata for streaming responses.

    Different fields appear in different chunks.
    """

    id: Optional[str] = None
    """
    A groq request ID which can be used to refer to a specific request to groq
    support. Sent only in the first and final chunk.
    """

    debug: Optional[XGroqDebug] = None
    """Debug information including input and output token IDs and strings.

    Only present when debug=true in the request.
    """

    error: Optional[str] = None
    """An error string indicating why a stream was stopped early."""

    seed: Optional[int] = None
    """The seed used for the request. Sent in the final chunk."""

    usage: Optional[CompletionUsage] = None
    """Usage statistics for the completion request."""

    usage_breakdown: Optional[XGroqUsageBreakdown] = None
    """Usage statistics for compound AI completion requests."""


class ChatCompletionChunk(BaseModel):
    """
    Represents a streamed chunk of a chat completion response returned by model, based on the provided input.
    """

    id: str
    """A unique identifier for the chat completion. Each chunk has the same ID."""

    choices: List[Choice]
    """A list of chat completion choices.

    Can contain more than one elements if `n` is greater than 1.
    """

    created: int
    """The Unix timestamp (in seconds) of when the chat completion was created.

    Each chunk has the same timestamp.
    """

    model: str
    """The model to generate the completion."""

    object: Literal["chat.completion.chunk"]
    """The object type, which is always `chat.completion.chunk`."""

    obfuscation: Optional[str] = None
    """
    Random padding that normalizes chunk sizes as a mitigation against side-channel
    attacks. Present on deployments that stream obfuscation unless
    `stream_options.include_obfuscation` is false.
    """

    service_tier: Optional[Literal["auto", "on_demand", "flex", "performance", "default"]] = None
    """The service tier used for the request.

    Deployments running in strict OpenAI compatibility report Groq-specific tiers as
    `default`.
    """

    system_fingerprint: Optional[str] = None
    """
    This fingerprint represents the backend configuration that the model runs with.
    Can be used in conjunction with the `seed` request parameter to understand when
    backend changes have been made that might impact determinism.
    """

    usage: Optional[CompletionUsage] = None
    """Usage statistics for the completion request."""

    x_groq: Optional[XGroq] = None
    """Groq-specific metadata for streaming responses.

    Different fields appear in different chunks.
    """
