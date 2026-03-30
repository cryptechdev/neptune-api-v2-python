# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .market.user_lend_market import UserLendMarket
from .market.user_borrow_market import UserBorrowMarket

__all__ = ["UserMarket"]


class UserMarket(BaseModel):
    borrow: UserBorrowMarket
    """Overview of user borrowing portfolio"""

    lend: UserLendMarket
    """Overview of user lending portfolio"""
