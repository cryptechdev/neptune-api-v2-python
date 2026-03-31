# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .user_merged_market import UserMergedMarket

__all__ = ["MarketGetMergedByAssetResponse"]


class MarketGetMergedByAssetResponse(BaseModel):
    data: UserMergedMarket

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
