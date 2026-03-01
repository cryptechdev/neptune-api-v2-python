# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .asset_info import AssetInfo
from .markets.market_rate import MarketRate
from .markets.lend_market_state import LendMarketState
from .markets.borrow.borrow_debt_state import BorrowDebtState
from .markets.borrow.borrow_debt_config import BorrowDebtConfig
from .markets.borrow.borrow_collateral_state import BorrowCollateralState
from .markets.borrow.borrow_collateral_config import BorrowCollateralConfig

__all__ = ["MergedMarket", "BorrowCollateral", "BorrowDebt", "Lend"]


class BorrowCollateral(BaseModel):
    """Info for asset as collateral for borrow market, if one exists"""

    config: BorrowCollateralConfig
    """Collateral configuration parameters"""

    state: BorrowCollateralState
    """Current collateral state"""


class BorrowDebt(BaseModel):
    """Info for asset as debt for borrow market, if one exists"""

    config: BorrowDebtConfig
    """Debt market configuration parameters"""

    rate: Optional[MarketRate] = None
    """Market rates"""

    state: BorrowDebtState
    """Current debt market state"""


class Lend(BaseModel):
    """Info for asset's lending market, if one exists"""

    rate: Optional[MarketRate] = None
    """Lending market rates"""

    state: LendMarketState
    """Current lending market state"""


class MergedMarket(BaseModel):
    """Data for all of an assets  markets"""

    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    borrow_collateral: Optional[BorrowCollateral] = None
    """Info for asset as collateral for borrow market, if one exists"""

    borrow_debt: Optional[BorrowDebt] = None
    """Info for asset as debt for borrow market, if one exists"""

    lend: Optional[Lend] = None
    """Info for asset's lending market, if one exists"""
