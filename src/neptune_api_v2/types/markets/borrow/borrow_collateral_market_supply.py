# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from ...market_supply_pool import MarketSupplyPool

__all__ = ["BorrowCollateralMarketSupply"]


class BorrowCollateralMarketSupply(BaseModel):
    non_receipt: MarketSupplyPool
    """Supply of all collaterals (excluding receipt tokens)"""

    receipt: MarketSupplyPool
    """Supply of receipt token collaterals"""

    total: MarketSupplyPool
    """Total supply for collaterals, regardless of type.

    Equivalent to `non_receipt + receipt`
    """
