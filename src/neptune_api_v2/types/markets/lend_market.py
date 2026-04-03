# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..asset_info import AssetInfo
from ..market_rate import MarketRate
from .lend_market_state import LendMarketState

__all__ = ["LendMarket"]


class LendMarket(BaseModel):
    """Lending market overview"""

    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    rate: MarketRate
    """Lending market rates"""

    state: LendMarketState
    """Current lending market state"""
