# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from ...asset_info import AssetInfo
from .borrow_collateral_state import BorrowCollateralState
from .borrow_collateral_config import BorrowCollateralConfig

__all__ = ["BorrowCollateralMarket"]


class BorrowCollateralMarket(BaseModel):
    """Borrowing market, collateral info"""

    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    config: BorrowCollateralConfig
    """Collateral configuration parameters"""

    state: BorrowCollateralState
    """Current collateral state"""
