# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .lend_market import LendMarket
from .lend_market_supply import LendMarketSupply

__all__ = ["LendOverview"]


class LendOverview(BaseModel):
    """Lending markets overview"""

    contents: List[LendMarket]
    """Lending markets"""

    supply: LendMarketSupply
    """Supply breakdown for lending markets"""
