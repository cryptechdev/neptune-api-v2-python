# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ......_models import BaseModel
from .user_account_health import UserAccountHealth
from ..user_debt_asset_pool import UserDebtAssetPool
from .user_collateral_asset_pool import UserCollateralAssetPool

__all__ = ["UserBorrowMarketAccount"]


class UserBorrowMarketAccount(BaseModel):
    """`UserBorrowMarketAccount`"""

    collaterals: List[UserCollateralAssetPool]
    """`UserCollateralAssetPool[]`

    ---

    Account collateral allocations
    """

    debts: List[UserDebtAssetPool]
    """`UserDebtAssetPool[]`

    ---

    Account debt allocations
    """

    index: int
    """Account index"""

    health: Optional[UserAccountHealth] = None
    """`UserAccountHealth`"""
