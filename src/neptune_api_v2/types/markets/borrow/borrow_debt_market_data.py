# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ...market_rate import MarketRate
from .borrow_debt_state import BorrowDebtState
from .borrow_debt_config import BorrowDebtConfig

__all__ = ["BorrowDebtMarketData"]


class BorrowDebtMarketData(BaseModel):
    config: BorrowDebtConfig
    """Debt market configuration parameters"""

    rate: Optional[MarketRate] = None
    """Market rates"""

    state: BorrowDebtState
    """Current debt market state"""
