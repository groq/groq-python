# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..shared_params.function_definition import FunctionDefinition

__all__ = ["ChatCompletionToolParam", "UnionMember0", "UnionMember1"]


class UnionMember0(TypedDict, total=False):
    function: Required[FunctionDefinition]

    server_url: str
    """The URL of the MCP server to connect to (required for MCP tools)."""

    type: Literal["function"]


class UnionMember1(TypedDict, total=False):
    server_url: Required[str]
    """The URL of the MCP server to connect to (required for MCP tools)."""

    function: FunctionDefinition

    type: Literal["mcp"]


ChatCompletionToolParam: TypeAlias = Union[UnionMember0, UnionMember1]
