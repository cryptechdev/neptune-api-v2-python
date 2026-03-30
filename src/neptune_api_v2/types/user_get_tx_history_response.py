# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .user_tx import UserTx
from .._models import BaseModel

__all__ = ["UserGetTxHistoryResponse"]


class UserGetTxHistoryResponse(BaseModel):
    """List data success response"""

    count: int
    """Total number of objects irrespective of any pagination parameters."""

    data: List[UserTx]

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
