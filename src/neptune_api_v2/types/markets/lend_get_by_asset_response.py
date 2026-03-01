# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..error_data import ErrorData
from .lend_market import LendMarket

__all__ = ["LendGetByAssetResponse"]


class LendGetByAssetResponse(BaseModel):
    data: Optional[LendMarket] = None
    """Object data"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""

    status: int
    """Request status"""

    status_text: str
    """Request status text"""
