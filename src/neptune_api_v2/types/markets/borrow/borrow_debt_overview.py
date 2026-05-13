# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .borrow_debt_market import BorrowDebtMarket
from ...market_supply_pool import MarketSupplyPool

__all__ = ["BorrowDebtOverview"]


class BorrowDebtOverview(BaseModel):
    """Borrowing market debts overview"""

    contents: List[BorrowDebtMarket]
    """Borrowing debt markets"""

    supply: MarketSupplyPool
    """Supply breakdown for debt markets"""
