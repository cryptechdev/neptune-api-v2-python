# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...error_data import ErrorData
from .borrow.user_collateral_asset_pool import UserCollateralAssetPool

__all__ = ["BorrowGetCollateralTotalsResponse"]


class BorrowGetCollateralTotalsResponse(BaseModel):
    count: Optional[int] = None
    """Total number of objects in all pages"""

    data: Optional[List[UserCollateralAssetPool]] = None
    """List contents"""

    error: Optional[ErrorData] = None
    """Error message, if any"""

    status: int
    """Request status"""

    status_text: str
    """Request status text"""
