# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from ...asset_info import AssetInfo
from ..market_rate import MarketRate
from .borrow_debt_state import BorrowDebtState
from .borrow_debt_config import BorrowDebtConfig

__all__ = ["BorrowDebtMarket"]


class BorrowDebtMarket(BaseModel):
    """`BorrowDebtMarket`"""

    asset_info: AssetInfo
    """`AssetInfo`"""

    config: BorrowDebtConfig
    """`BorrowDebtConfig`"""

    state: BorrowDebtState
    """`BorrowDebtState`"""

    rate: Optional[MarketRate] = None
    """`MarketRate`"""
