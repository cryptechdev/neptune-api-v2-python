# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from ...error_data import ErrorData
from .borrow_debt_market import BorrowDebtMarket

__all__ = ["DebtListResponse"]


class DebtListResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    count: Optional[int] = None
    """Total number of objects in all pages"""

    data: Optional[List[BorrowDebtMarket]] = None
    """List contents"""

    error: Optional[ErrorData] = None
    """Error message, if any"""
