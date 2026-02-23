# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .markets.user_debt_asset_pool import UserDebtAssetPool
from .markets.borrow.user_borrow_market_account import UserBorrowMarketAccount
from .markets.borrow.user_collateral_asset_pool import UserCollateralAssetPool

__all__ = ["UserMarket", "Borrow", "BorrowTotals", "Lend"]


class BorrowTotals(BaseModel):
    """
    `UserMarketTotalsData[]`
     ---
     Collateral/debt totals of all sub-accounts by asset
    """

    collaterals: List[UserCollateralAssetPool]
    """`UserCollateralAssetPool[]`

    ---

    Account collateral allocations
    """

    debts: List[UserDebtAssetPool]
    """`UserDebtAssetPool[]`

    ---

    Account debt allocations
    """


class Borrow(BaseModel):
    """`UserBorrowMarket`"""

    accounts: List[UserBorrowMarketAccount]
    """`UserBorrowMarketAccount[]`

    ---

    Market sub-accounts for the user
    """

    totals: BorrowTotals
    """`UserMarketTotalsData[]`

    ---

    Collateral/debt totals of all sub-accounts by asset
    """


class Lend(BaseModel):
    """`UserLendMarket`"""

    asset_pools: List[UserDebtAssetPool]
    """`UserLendAssetPool[]`

    ---

    User lending allocations
    """


class UserMarket(BaseModel):
    """`UserMarket`"""

    borrow: Borrow
    """`UserBorrowMarket`"""

    lend: Lend
    """`UserLendMarket`"""
