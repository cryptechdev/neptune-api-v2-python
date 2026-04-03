# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..asset_info import AssetInfo
from .market.user_lend_origin_amounts import UserLendOriginAmounts
from .market.user_lend_receipt_amounts import UserLendReceiptAmounts
from .market.borrow.user_debt_account_pool import UserDebtAccountPool
from .market.borrow.user_collateral_account_pool import UserCollateralAccountPool

__all__ = ["UserMergedMarket", "Lend"]


class Lend(BaseModel):
    """User contribution for asset's lending market, if one exists"""

    origin_equivalent: UserLendOriginAmounts
    """
    The lending amounts converted into the equivalent for the receipt token's
    origin/source asset
    """

    receipt_amounts: UserLendReceiptAmounts
    """The lending amounts in the original receipt token amounts"""


class UserMergedMarket(BaseModel):
    """User market allocations grouped by asset.

    **Note**: because of the inverted structure of merged market accounts, account
    health cannot be represented and is excluded in the merged structures.
    """

    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    borrow_collateral: List[UserCollateralAccountPool]
    """User collateral contribution for asset in borrow market, listed by subaccount"""

    borrow_debt: List[UserDebtAccountPool]
    """User debt contribution for asset in borrow market, listed by subaccount"""

    lend: Optional[Lend] = None
    """User contribution for asset's lending market, if one exists"""
