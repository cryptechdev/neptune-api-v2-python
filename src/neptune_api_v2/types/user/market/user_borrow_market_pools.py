# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .borrow.user_debt_asset_pool import UserDebtAssetPool
from .borrow.user_collateral_asset_pool import UserCollateralAssetPool

__all__ = ["UserBorrowMarketPools"]


class UserBorrowMarketPools(BaseModel):
    collaterals: List[UserCollateralAssetPool]
    """Account collateral allocations"""

    debts: List[UserDebtAssetPool]
    """Account debt allocations"""
