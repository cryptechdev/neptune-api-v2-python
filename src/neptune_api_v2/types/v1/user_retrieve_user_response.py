# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .error_data import ErrorData
from .users.user_market import UserMarket
from .users.nept.user_stake import UserStake
from .users.user_wallet_portfolio import UserWalletPortfolio
from .users.user_nept_unlock_overview import UserNeptUnlockOverview

__all__ = ["UserRetrieveUserResponse", "Data", "DataNept"]


class DataNept(BaseModel):
    """`UserNeptOverview`"""

    staking: UserStake
    """`UserStake`"""

    unlocks: UserNeptUnlockOverview
    """`UserNeptUnlockOverview`"""


class Data(BaseModel):
    """`User`"""

    markets: UserMarket
    """`UserMarket`"""

    nept: DataNept
    """`UserNeptOverview`"""

    wallets: UserWalletPortfolio
    """`UserWalletPortfolio`"""


class UserRetrieveUserResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[Data] = None
    """`User`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
