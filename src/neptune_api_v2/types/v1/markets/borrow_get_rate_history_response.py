# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ..error_data import ErrorData
from .asset_rate_history import AssetRateHistory

__all__ = ["BorrowGetRateHistoryResponse"]


class BorrowGetRateHistoryResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[AssetRateHistory] = None
    """`AssetRateHistory`

    ---

    Historical rates for assets
    """

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
