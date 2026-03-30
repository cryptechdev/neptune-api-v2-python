# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .user_borrow_market_pools import UserBorrowMarketPools
from .borrow.user_borrow_market_account import UserBorrowMarketAccount

__all__ = ["UserBorrowMarket"]


class UserBorrowMarket(BaseModel):
    accounts: List[UserBorrowMarketAccount]
    """Market sub-accounts for the user"""

    totals: UserBorrowMarketPools
    """Collateral/debt totals of all sub-accounts by asset"""
