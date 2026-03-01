# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .market.user_borrow_market import UserBorrowMarket
from .market.user_debt_asset_pool import UserDebtAssetPool

__all__ = ["UserMarket", "Lend"]


class Lend(BaseModel):
    """Overview of user lending portfolio"""

    asset_pools: List[UserDebtAssetPool]
    """User lending allocations"""


class UserMarket(BaseModel):
    borrow: UserBorrowMarket
    """Overview of user borrowing portfolio"""

    lend: Lend
    """Overview of user lending portfolio"""
