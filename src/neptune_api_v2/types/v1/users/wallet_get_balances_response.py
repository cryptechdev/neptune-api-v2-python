# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ..error_data import ErrorData
from .user_wallet_portfolio import UserWalletPortfolio

__all__ = ["WalletGetBalancesResponse"]


class WalletGetBalancesResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[UserWalletPortfolio] = None
    """`UserWalletPortfolio`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
