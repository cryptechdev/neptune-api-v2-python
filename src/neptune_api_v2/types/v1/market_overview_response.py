# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .error_data import ErrorData
from .markets.lend_market import LendMarket
from .global_market_config import GlobalMarketConfig
from .markets.borrow_market_overview import BorrowMarketOverview

__all__ = ["MarketOverviewResponse", "Data"]


class Data(BaseModel):
    """`MarketOverview`"""

    borrow: BorrowMarketOverview
    """`BorrowMarketOverview`"""

    global_config: GlobalMarketConfig
    """`GlobalMarketConfig`"""

    lend: List[LendMarket]
    """`LendMarket[]`

    ---

    Current lending markets
    """


class MarketOverviewResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[Data] = None
    """`MarketOverview`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
