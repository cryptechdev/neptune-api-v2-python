# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..error_data import ErrorData
from .user_merged_market import UserMergedMarket

__all__ = ["MarketGetMergedByAssetResponse"]


class MarketGetMergedByAssetResponse(BaseModel):
    data: Optional[UserMergedMarket] = None
    """Object data"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""

    status: int
    """Request status"""

    status_text: str
    """Request status text"""
