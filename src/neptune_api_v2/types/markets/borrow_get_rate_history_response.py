# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..asset_rate_history import AssetRateHistory

__all__ = ["BorrowGetRateHistoryResponse"]


class BorrowGetRateHistoryResponse(BaseModel):
    """Object data success response"""

    data: AssetRateHistory
    """Historical rates for assets"""

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
