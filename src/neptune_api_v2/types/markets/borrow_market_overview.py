# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .borrow.borrow_debt_overview import BorrowDebtOverview
from .borrow.borrow_collateral_overview import BorrowCollateralOverview

__all__ = ["BorrowMarketOverview"]


class BorrowMarketOverview(BaseModel):
    collaterals: BorrowCollateralOverview
    """Borrowing market collaterals overview"""

    debts: BorrowDebtOverview
    """Borrowing market debts overview"""
