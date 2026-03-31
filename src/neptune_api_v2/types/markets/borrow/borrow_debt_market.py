# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ...asset_info import AssetInfo
from ...market_rate import MarketRate
from .borrow_debt_state import BorrowDebtState
from .borrow_debt_config import BorrowDebtConfig

__all__ = ["BorrowDebtMarket"]


class BorrowDebtMarket(BaseModel):
    """Borrowing market, debt info"""

    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    config: BorrowDebtConfig
    """Debt market configuration parameters"""

    rate: Optional[MarketRate] = None
    """Market rates"""

    state: BorrowDebtState
    """Current debt market state"""
