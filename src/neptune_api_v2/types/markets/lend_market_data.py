# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..market_rate import MarketRate
from .lend_market_state import LendMarketState

__all__ = ["LendMarketData"]


class LendMarketData(BaseModel):
    rate: MarketRate
    """Lending market rates"""

    state: LendMarketState
    """Current lending market state"""
