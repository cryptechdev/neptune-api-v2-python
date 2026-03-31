# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .wallet_balance import WalletBalance

__all__ = ["WalletGetBalancesResponse", "Data"]


class Data(BaseModel):
    balances: List[WalletBalance]
    """Array of each wallet balance"""

    total_value: Optional[str] = None
    """
    Sum value in USD. Guaranteed null if value calculation is disabled / guaranteed
    non-null if calculation is enabled.

    **NOTE:** this only accounts for assets which are internally known & tracked.
    See the `/assets` endpoint for a list of supported assets.
    """


class WalletGetBalancesResponse(BaseModel):
    data: Data

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
