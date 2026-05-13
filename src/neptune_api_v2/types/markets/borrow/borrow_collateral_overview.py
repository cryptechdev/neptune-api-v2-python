# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .borrow_collateral_market import BorrowCollateralMarket
from .borrow_collateral_market_supply import BorrowCollateralMarketSupply

__all__ = ["BorrowCollateralOverview"]


class BorrowCollateralOverview(BaseModel):
    """Borrowing market collaterals overview"""

    contents: List[BorrowCollateralMarket]
    """Borrowing collateral markets"""

    supply: BorrowCollateralMarketSupply
    """Supply breakdown for collaterals"""
