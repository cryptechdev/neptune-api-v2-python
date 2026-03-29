# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .lend_market import LendMarket

__all__ = ["LendListResponse"]


class LendListResponse(BaseModel):
    """List data success response"""

    count: int
    """Total number of objects irrespective of any pagination parameters."""

    data: List[LendMarket]
    """Primary response content (list)"""

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
