# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..shared_params.function_definition import FunctionDefinition

__all__ = ["ChatCompletionToolParam"]


class ChatCompletionToolParam(TypedDict, total=False):
    type: Required[Literal["function", "browser_search", "code_interpreter"]]
    """The type of the tool. Currently, only `function` is supported."""

    function: FunctionDefinition
