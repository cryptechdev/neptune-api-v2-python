# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .borrow.user_debt_asset_pool import UserDebtAssetPool

__all__ = ["UserLendMarket"]


class UserLendMarket(BaseModel):
    asset_pools: List[UserDebtAssetPool]
    """User lending allocations"""
