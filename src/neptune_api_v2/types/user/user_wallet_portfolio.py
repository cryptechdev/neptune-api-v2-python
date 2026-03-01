# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .wallet_balance import WalletBalance

__all__ = ["UserWalletPortfolio", "Extra", "ExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    total_value: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class UserWalletPortfolio(BaseModel):
    balances: List[WalletBalance]
    """Array of each wallet balance"""

    extra: Extra

    total_value: Optional[str] = None
    """
    Sum value in USD. Guaranteed null if value calculation is disabled / guaranteed
    non-null if calculation is enabled.

    **NOTE:** this only accounts for assets which are internally known & tracked.
    See the `/assets` endpoint for a list of supported assets.
    """
