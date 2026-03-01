# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .error_data import ErrorData
from .user.user_market import UserMarket
from .user.nept.user_stake import UserStake
from .user.user_wallet_portfolio import UserWalletPortfolio
from .user.user_nept_unlock_overview import UserNeptUnlockOverview

__all__ = ["UserGetUserResponse", "Data", "DataNept"]


class DataNept(BaseModel):
    """User's NEPT associations (e.g. stake, unlocks)"""

    staking: UserStake
    """-- Overview of the user's staking contributions/activity"""

    unlocks: UserNeptUnlockOverview
    """-- Overview of the user's unlock arrangements and claim statistics"""


class Data(BaseModel):
    """Object data"""

    markets: UserMarket
    """User's market contribution overview"""

    nept: DataNept
    """User's NEPT associations (e.g. stake, unlocks)"""

    wallets: UserWalletPortfolio
    """User's wallets and balances"""


class UserGetUserResponse(BaseModel):
    data: Optional[Data] = None
    """Object data"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""

    status: int
    """Request status"""

    status_text: str
    """Request status text"""
