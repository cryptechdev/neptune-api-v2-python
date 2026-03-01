# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .error_data import ErrorData
from .merged_market import MergedMarket

__all__ = ["MarketGetMergedByAssetResponse"]


class MarketGetMergedByAssetResponse(BaseModel):
    data: Optional[MergedMarket] = None
    """Data for all of an assets markets"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""

    status: int
    """Request status"""

    status_text: str
    """Request status text"""
