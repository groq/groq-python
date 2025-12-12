# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ErrorObject", "Debug"]


class Debug(BaseModel):
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


class ErrorObject(BaseModel):
    message: str

    type: str

    code: Optional[str] = None

    debug: Optional[Debug] = None
    """Debug information including input and output token IDs and strings.

    Only present when debug=true in the request.
    """

    failed_generation: Optional[str] = None

    param: Optional[str] = None

    schema_code: Optional[str] = None

    schema_kind: Optional[str] = None

    schema_path: Optional[str] = None

    schema_path_segments: Optional[List[str]] = None
    """Segments of the schema path relevant to validation errors."""
