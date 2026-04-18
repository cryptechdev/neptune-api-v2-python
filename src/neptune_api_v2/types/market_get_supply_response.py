# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .tvl import Tvl
from .._models import BaseModel
from .market_supply_pool import MarketSupplyPool
from .markets.lend_market_supply import LendMarketSupply
from .markets.borrow.borrow_collateral_market_supply import BorrowCollateralMarketSupply

__all__ = ["MarketGetSupplyResponse", "Data"]


class Data(BaseModel):
    borrow_collateral: BorrowCollateralMarketSupply
    """Borrowing market supply - collaterals"""

    borrow_debt: MarketSupplyPool
    """Borrowing market supply - debts"""

    lend: LendMarketSupply
    """Lending market supply"""

    tvl: Tvl
    """Market TVL"""


class MarketGetSupplyResponse(BaseModel):
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
