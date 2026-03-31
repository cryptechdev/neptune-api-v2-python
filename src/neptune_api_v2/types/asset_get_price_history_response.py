# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .asset_price_history import AssetPriceHistory

__all__ = ["AssetGetPriceHistoryResponse"]


class AssetGetPriceHistoryResponse(BaseModel):
    data: AssetPriceHistory
    """Historical prices for assets"""

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
