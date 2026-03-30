# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .borrow_debt_market import BorrowDebtMarket

__all__ = ["DebtListResponse"]


class DebtListResponse(BaseModel):
    """List data success response"""

    count: int
    """Total number of objects irrespective of any pagination parameters."""

    data: List[BorrowDebtMarket]

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
