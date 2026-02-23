# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ..asset_info import AssetInfo
from .market_rate import MarketRate
from .lend_market_state import LendMarketState

__all__ = ["LendMarket"]


class LendMarket(BaseModel):
    """`LendMarket`"""

    asset_info: AssetInfo
    """`AssetInfo`"""

    state: LendMarketState
    """`LendMarketState`"""

    rate: Optional[MarketRate] = None
    """`MarketRate`"""
