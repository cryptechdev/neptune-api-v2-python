# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .error_data import ErrorData
from .markets.lend_market import LendMarket
from .global_market_config import GlobalMarketConfig
from .markets.borrow_market_overview import BorrowMarketOverview

__all__ = ["MarketGetOverviewResponse", "Data"]


class Data(BaseModel):
    """Object data"""

    borrow: BorrowMarketOverview
    """Borrow market overview"""

    global_config: GlobalMarketConfig
    """Market runtime parameters"""

    lend: List[LendMarket]
    """Current lending markets"""


class MarketGetOverviewResponse(BaseModel):
    data: Optional[Data] = None
    """Object data"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""

    status: int
    """Request status"""

    status_text: str
    """Request status text"""
