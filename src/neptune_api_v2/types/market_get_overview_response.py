# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .tvl import Tvl
from .._models import BaseModel
from .markets.lend_market import LendMarket
from .global_market_config import GlobalMarketConfig
from .markets.borrow_market_overview import BorrowMarketOverview

__all__ = [
    "MarketGetOverviewResponse",
    "Data",
    "DataLend",
    "DataLendSupply",
    "DataLendSupplyExtra",
    "DataLendSupplyExtraText",
]


class DataLendSupplyExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    principal: str


class DataLendSupplyExtra(BaseModel):
    text: Optional[DataLendSupplyExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class DataLendSupply(BaseModel):
    """Supply breakdown for lending markets"""

    extra: DataLendSupplyExtra

    principal: str
    """Sum USD value of lending principal"""


class DataLend(BaseModel):
    """Lending markets overview"""

    contents: List[LendMarket]
    """Lending markets"""

    supply: DataLendSupply
    """Supply breakdown for lending markets"""


class Data(BaseModel):
    borrow: BorrowMarketOverview
    """Borrow market overview"""

    global_config: GlobalMarketConfig
    """Market runtime parameters"""

    lend: DataLend
    """Lending markets overview"""

    tvl: Tvl
    """Oveerall market TVL"""


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
