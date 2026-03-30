# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .merged_market import MergedMarket

__all__ = ["MarketGetMergedByAssetResponse"]


class MarketGetMergedByAssetResponse(BaseModel):
    """Object data success response"""

    data: MergedMarket
    """Data for all of an assets markets"""

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
