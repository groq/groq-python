# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BatchCreateParams"]


class BatchCreateParams(TypedDict, total=False):
    completion_window: Required[Literal["24h"]]
    """The time frame within which the batch should be processed.

    Currently only `24h` is supported.
    """

    endpoint: Required[Literal["/v1/chat/completions"]]
    """The endpoint to be used for all requests in the batch.

    Currently `/v1/chat/completions` is supported.
    """

    input_file_id: Required[str]
    """The ID of an uploaded file that contains requests for the new batch.

    See [upload file](/docs/api-reference#files-upload) for how to upload a file.

    Your input file must be formatted as a [JSONL file](/docs/batch), and must be
    uploaded with the purpose `batch`. The file can be up to 100 MB in size.
    """

    metadata: Optional[Dict[str, str]]
    """Optional custom metadata for the batch."""
