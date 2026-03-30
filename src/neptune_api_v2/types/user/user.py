# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .user_market import UserMarket
from .nept.user_stake import UserStake
from .user_unlock_overview import UserUnlockOverview
from .user_wallet_portfolio import UserWalletPortfolio

__all__ = ["User", "Nept"]


class Nept(BaseModel):
    """User's NEPT associations (e.g. stake, unlocks)"""

    staking: UserStake
    """Overview of the user's staking contributions/activity"""

    unlocks: UserUnlockOverview
    """Overview of the user's unlock arrangements and claim statistics"""


class User(BaseModel):
    markets: UserMarket
    """User's market contribution overview"""

    nept: Nept
    """User's NEPT associations (e.g. stake, unlocks)"""

    wallets: UserWalletPortfolio
    """User's wallets and balances"""
