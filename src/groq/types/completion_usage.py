# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CompletionUsage", "CompletionTokensDetails", "PromptTokensDetails"]


class CompletionTokensDetails(BaseModel):
    reasoning_tokens: int
    """Number of tokens used for reasoning (for reasoning models)."""


class PromptTokensDetails(BaseModel):
    cached_tokens: int
    """Number of tokens that were cached and reused."""


class CompletionUsage(BaseModel):
    completion_tokens: int
    """Number of tokens in the generated completion."""

    prompt_tokens: int
    """Number of tokens in the prompt."""

    total_tokens: int
    """Total number of tokens used in the request (prompt + completion)."""

    completion_time: Optional[float] = None
    """Time spent generating tokens"""

    completion_tokens_details: Optional[CompletionTokensDetails] = None
    """Breakdown of tokens in the completion."""

    prompt_time: Optional[float] = None
    """Time spent processing input tokens"""

    prompt_tokens_details: Optional[PromptTokensDetails] = None
    """Breakdown of tokens in the prompt."""

    queue_time: Optional[float] = None
    """Time the requests was spent queued"""

    total_time: Optional[float] = None
    """completion time and prompt time combined"""
