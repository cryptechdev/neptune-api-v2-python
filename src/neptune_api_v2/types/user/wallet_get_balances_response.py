# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..error_data import ErrorData
from .wallet_balance import WalletBalance

__all__ = ["WalletGetBalancesResponse", "Data"]


class Data(BaseModel):
    """Object data"""

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
    data: Optional[Data] = None
    """Object data"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""

    status: int
    """Request status"""

    status_text: str
    """Request status text"""
