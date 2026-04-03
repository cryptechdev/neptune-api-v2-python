# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from ...market_rate import MarketRate
from .user_lend_asset_pool import UserLendAssetPool

__all__ = ["UserLendMarket"]


class UserLendMarket(BaseModel):
    asset_pools: List[UserLendAssetPool]
    """User lending allocations"""

    net_rate: MarketRate
    """Account debt net rate"""
