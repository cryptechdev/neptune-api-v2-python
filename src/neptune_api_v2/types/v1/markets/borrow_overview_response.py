# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ..error_data import ErrorData
from .borrow_market_overview import BorrowMarketOverview

__all__ = ["BorrowOverviewResponse"]


class BorrowOverviewResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[BorrowMarketOverview] = None
    """`BorrowMarketOverview`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
