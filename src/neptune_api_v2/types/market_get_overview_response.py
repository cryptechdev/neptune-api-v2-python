# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .markets.lend_market import LendMarket
from .global_market_config import GlobalMarketConfig
from .markets.borrow_market_overview import BorrowMarketOverview

__all__ = ["MarketGetOverviewResponse", "Data"]


class Data(BaseModel):
    borrow: BorrowMarketOverview
    """Borrow market overview"""

    global_config: GlobalMarketConfig
    """Market runtime parameters"""

    lend: List[LendMarket]
    """Current lending markets"""


class MarketGetOverviewResponse(BaseModel):
    data: Data

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
