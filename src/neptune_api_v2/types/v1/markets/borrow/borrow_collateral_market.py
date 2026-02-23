# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel
from ...asset_info import AssetInfo
from .borrow_collateral_state import BorrowCollateralState
from .borrow_collateral_config import BorrowCollateralConfig

__all__ = ["BorrowCollateralMarket"]


class BorrowCollateralMarket(BaseModel):
    """`BorrowCollateralMarket`"""

    asset_info: AssetInfo
    """`AssetInfo`"""

    config: BorrowCollateralConfig
    """`BorrowCollateralConfig`"""

    state: BorrowCollateralState
    """`BorrowCollateralState`"""
