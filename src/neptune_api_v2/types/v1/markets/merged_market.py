# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ..asset_info import AssetInfo
from .market_rate import MarketRate
from .lend_market_state import LendMarketState
from .borrow.borrow_debt_state import BorrowDebtState
from .borrow.borrow_debt_config import BorrowDebtConfig
from .borrow.borrow_collateral_state import BorrowCollateralState
from .borrow.borrow_collateral_config import BorrowCollateralConfig

__all__ = ["MergedMarket", "BorrowCollateral", "BorrowDebt", "Lend"]


class BorrowCollateral(BaseModel):
    """Info for asset as collateral for borrow market, if one exists"""

    config: BorrowCollateralConfig
    """`BorrowCollateralConfig`"""

    state: BorrowCollateralState
    """`BorrowCollateralState`"""


class BorrowDebt(BaseModel):
    """Info for asset as debt for borrow market, if one exists"""

    config: BorrowDebtConfig
    """`BorrowDebtConfig`"""

    state: BorrowDebtState
    """`BorrowDebtState`"""

    rate: Optional[MarketRate] = None
    """`MarketRate`"""


class Lend(BaseModel):
    """Info for asset's lending market, if one exists"""

    state: LendMarketState
    """`LendMarketState`"""

    rate: Optional[MarketRate] = None
    """`MarketRate`"""


class MergedMarket(BaseModel):
    """
    `MergedMarket`
     ---
     Data for all of an assets  markets
    """

    asset_info: AssetInfo
    """`AssetInfo`"""

    borrow_collateral: Optional[BorrowCollateral] = None
    """Info for asset as collateral for borrow market, if one exists"""

    borrow_debt: Optional[BorrowDebt] = None
    """Info for asset as debt for borrow market, if one exists"""

    lend: Optional[Lend] = None
    """Info for asset's lending market, if one exists"""
