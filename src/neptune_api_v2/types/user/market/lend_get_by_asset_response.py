# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .user_lend_asset_pool import UserLendAssetPool

__all__ = ["LendGetByAssetResponse"]


class LendGetByAssetResponse(BaseModel):
    data: UserLendAssetPool

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
