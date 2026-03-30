# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .borrow_collateral_state import BorrowCollateralState
from .borrow_collateral_config import BorrowCollateralConfig

__all__ = ["BorrowCollateralMarketData"]


class BorrowCollateralMarketData(BaseModel):
    config: BorrowCollateralConfig
    """Collateral configuration parameters"""

    state: BorrowCollateralState
    """Current collateral state"""
