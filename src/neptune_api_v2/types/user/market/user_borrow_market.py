# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .user_debt_asset_pool import UserDebtAssetPool
from .borrow.user_borrow_market_account import UserBorrowMarketAccount
from .borrow.user_collateral_asset_pool import UserCollateralAssetPool

__all__ = ["UserBorrowMarket", "Totals"]


class Totals(BaseModel):
    """Collateral/debt totals of all sub-accounts by asset"""

    collaterals: List[UserCollateralAssetPool]
    """Account collateral allocations"""

    debts: List[UserDebtAssetPool]
    """Account debt allocations"""


class UserBorrowMarket(BaseModel):
    accounts: List[UserBorrowMarketAccount]
    """Market sub-accounts for the user"""

    totals: Totals
    """Collateral/debt totals of all sub-accounts by asset"""
