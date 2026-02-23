# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .borrow.borrow_debt_market import BorrowDebtMarket
from .borrow.borrow_collateral_market import BorrowCollateralMarket

__all__ = ["BorrowMarketOverview"]


class BorrowMarketOverview(BaseModel):
    """`BorrowMarketOverview`"""

    collaterals: List[BorrowCollateralMarket]
    """Borrowing collateral markets"""

    debts: List[BorrowDebtMarket]
    """Borrowing debt markets"""
