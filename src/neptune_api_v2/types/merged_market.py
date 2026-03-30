# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .asset_info import AssetInfo
from .markets.lend_market_data import LendMarketData
from .markets.borrow.borrow_debt_market_data import BorrowDebtMarketData
from .markets.borrow.borrow_collateral_market_data import BorrowCollateralMarketData

__all__ = ["MergedMarket"]


class MergedMarket(BaseModel):
    """Data for all of an assets  markets"""

    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    borrow_collateral: Optional[BorrowCollateralMarketData] = None
    """Info for asset as collateral for borrow market, if one exists"""

    borrow_debt: Optional[BorrowDebtMarketData] = None
    """Info for asset as debt for borrow market, if one exists"""

    lend: Optional[LendMarketData] = None
    """Info for asset's lending market, if one exists"""
