# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .user.user_market import UserMarket
from .user.nept.user_stake import UserStake
from .user.user_wallet_portfolio import UserWalletPortfolio
from .user.user_nept_unlock_overview import UserNeptUnlockOverview

__all__ = ["UserGetUserResponse", "Data", "DataNept"]


class DataNept(BaseModel):
    """User's NEPT associations (e.g. stake, unlocks)"""

    staking: UserStake
    """Overview of the user's staking contributions/activity"""

    unlocks: UserNeptUnlockOverview
    """Overview of the user's unlock arrangements and claim statistics"""


class Data(BaseModel):
    """Primary response content (object)"""

    markets: UserMarket
    """User's market contribution overview"""

    nept: DataNept
    """User's NEPT associations (e.g. stake, unlocks)"""

    wallets: UserWalletPortfolio
    """User's wallets and balances"""


class UserGetUserResponse(BaseModel):
    """Object data success response"""

    data: Data
    """Primary response content (object)"""

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
