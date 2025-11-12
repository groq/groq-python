# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .chat_completion_message_tool_call import ChatCompletionMessageToolCall

__all__ = [
    "ChatCompletionMessage",
    "Annotation",
    "AnnotationDocumentCitation",
    "AnnotationFunctionCitation",
    "ExecutedTool",
    "ExecutedToolBrowserResult",
    "ExecutedToolCodeResult",
    "ExecutedToolCodeResultChart",
    "ExecutedToolCodeResultChartElement",
    "ExecutedToolSearchResults",
    "ExecutedToolSearchResultsResult",
    "FunctionCall",
]


class AnnotationDocumentCitation(BaseModel):
    document_id: str
    """
    The ID of the document being cited, corresponding to a document provided in the
    request.
    """

    end_index: int
    """The character index in the message content where this citation ends."""

    start_index: int
    """The character index in the message content where this citation begins."""


class AnnotationFunctionCitation(BaseModel):
    end_index: int
    """The character index in the message content where this citation ends."""

    start_index: int
    """The character index in the message content where this citation begins."""

    tool_call_id: str
    """
    The ID of the tool call being cited, corresponding to a tool call made during
    the conversation.
    """


class Annotation(BaseModel):
    type: Literal["document_citation", "function_citation"]
    """The type of annotation."""

    document_citation: Optional[AnnotationDocumentCitation] = None
    """A citation referencing a specific document that was provided in the request."""

    function_citation: Optional[AnnotationFunctionCitation] = None
    """A citation referencing the result of a function or tool call."""


class ExecutedToolBrowserResult(BaseModel):
    title: str
    """The title of the browser window"""

    url: str
    """The URL of the browser window"""

    content: Optional[str] = None
    """The content of the browser result"""

    live_view_url: Optional[str] = None
    """The live view URL for the browser window"""


class ExecutedToolCodeResultChartElement(BaseModel):
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


class ExecutedToolCodeResultChart(BaseModel):
    elements: List[ExecutedToolCodeResultChartElement]
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


class ExecutedToolCodeResult(BaseModel):
    chart: Optional[ExecutedToolCodeResultChart] = None

    charts: Optional[List[ExecutedToolCodeResultChart]] = None
    """Array of charts from a superchart"""

    png: Optional[str] = None
    """Base64 encoded PNG image output from code execution"""

    text: Optional[str] = None
    """The text version of the code execution result"""


class ExecutedToolSearchResultsResult(BaseModel):
    content: Optional[str] = None
    """The content of the search result"""

    score: Optional[float] = None
    """The relevance score of the search result"""

    title: Optional[str] = None
    """The title of the search result"""

    url: Optional[str] = None
    """The URL of the search result"""


class ExecutedToolSearchResults(BaseModel):
    images: Optional[List[str]] = None
    """List of image URLs returned by the search"""

    results: Optional[List[ExecutedToolSearchResultsResult]] = None
    """List of search results"""


class ExecutedTool(BaseModel):
    arguments: str
    """The arguments passed to the tool in JSON format."""

    index: int
    """The index of the executed tool."""

    type: str
    """The type of tool that was executed."""

    browser_results: Optional[List[ExecutedToolBrowserResult]] = None
    """Array of browser results"""

    code_results: Optional[List[ExecutedToolCodeResult]] = None
    """Array of code execution results"""

    output: Optional[str] = None
    """The output returned by the tool."""

    search_results: Optional[ExecutedToolSearchResults] = None
    """The search results returned by the tool, if applicable."""


class FunctionCall(BaseModel):
    arguments: str
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: str
    """The name of the function to call."""


class ChatCompletionMessage(BaseModel):
    content: Optional[str] = None
    """The contents of the message."""

    role: Literal["assistant"]
    """The role of the author of this message."""

    annotations: Optional[List[Annotation]] = None
    """
    A list of annotations providing citations and references for the content in the
    message.
    """

    executed_tools: Optional[List[ExecutedTool]] = None
    """
    A list of tools that were executed during the chat completion for compound AI
    systems.
    """

    function_call: Optional[FunctionCall] = None
    """Deprecated and replaced by `tool_calls`.

    The name and arguments of a function that should be called, as generated by the
    model.
    """

    reasoning: Optional[str] = None
    """The model's reasoning for a response.

    Only available for reasoning models when requests parameter reasoning_format has
    value `parsed.
    """

    tool_calls: Optional[List[ChatCompletionMessageToolCall]] = None
    """The tool calls generated by the model, such as function calls."""
