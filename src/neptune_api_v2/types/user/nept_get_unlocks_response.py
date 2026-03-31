# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .user_unlock_overview import UserUnlockOverview

__all__ = ["NeptGetUnlocksResponse"]


class NeptGetUnlocksResponse(BaseModel):
    data: UserUnlockOverview

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
