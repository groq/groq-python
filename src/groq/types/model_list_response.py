# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .model import Model
from .._models import BaseModel

__all__ = ["ModelListResponse"]


class ModelListResponse(BaseModel):
    data: Optional[List[Model]] = None

    object: Optional[str] = None
