# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..asset_info import AssetInfo
from .market.borrow.user_debt_account_pool import UserDebtAccountPool
from .market.borrow.user_collateral_account_pool import UserCollateralAccountPool

__all__ = [
    "UserMergedMarket",
    "Lend",
    "LendOriginEquivalent",
    "LendOriginEquivalentExtra",
    "LendOriginEquivalentExtraText",
    "LendReceiptAmounts",
    "LendReceiptAmountsExtra",
    "LendReceiptAmountsExtraText",
    "LendReceiptAmountsExtraValue",
    "LendReceiptAmountsExtraValueExtra",
    "LendReceiptAmountsExtraValueExtraText",
]


class LendOriginEquivalentExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    collateralized: str

    held: str

    total: str


class LendOriginEquivalentExtra(BaseModel):
    text: Optional[LendOriginEquivalentExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class LendOriginEquivalent(BaseModel):
    """
    The lending amounts converted into the equivalent for the receipt token's origin/source asset
    """

    collateralized: str
    """
    Total equivalent amount of origin token collateralized across this user's
    borrowing portfolio

    **NOTE:** This is **not** the amount of the origin asset that the user holds,
    but the amount held in the receipt token rendered as the equivalent amount in
    the origin asset.

    Or, more formally:
    `origin_equivalent_collateralized = receipt_collateralized / receipt_redemption_ratio`
    """

    extra: LendOriginEquivalentExtra

    held: str
    """Total equivalent amount of origin token held in address balance

    **NOTE:** This is **not** the amount of the origin asset that the user holds,
    but the amount held in the receipt token rendered as the equivalent amount in
    the origin asset.

    Or, more formally:
    `origin_equivalent_held = receipt_held / receipt_redemption_ratio`
    """

    total: str
    """Total of held and collateralized equivalent for origin asset

    Or, more formally:
    `origin_equivalent_total = receipt_lent_total / receipt_redemption_ratio`
    """


class LendReceiptAmountsExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    collateralized: str

    held: str

    total: str


class LendReceiptAmountsExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    collateralized: str

    held: str

    price: str
    """Text representation of price"""

    total: str


class LendReceiptAmountsExtraValueExtra(BaseModel):
    text: Optional[LendReceiptAmountsExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class LendReceiptAmountsExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.

    ### Note

    This variant group contains an additional `price` field (set to the number used in value calculation).

    The embedded text group will contain the text variant if `with_text` was specified as well.
    """

    collateralized: str

    extra: LendReceiptAmountsExtraValueExtra

    held: str

    price: str
    """Price used in value calculations"""

    total: str


class LendReceiptAmountsExtra(BaseModel):
    text: Optional[LendReceiptAmountsExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[LendReceiptAmountsExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.

    ### Note

    This variant group contains an additional `price` field (set to the number used
    in value calculation).

    The embedded text group will contain the text variant if `with_text` was
    specified as well.
    """


class LendReceiptAmounts(BaseModel):
    """The lending amounts in the original receipt token amounts"""

    collateralized: str
    """
    Total amount of receipt token collateralized across this user's borrowing
    portfolio
    """

    extra: LendReceiptAmountsExtra

    held: str
    """Total amount of receipt token held in address balance"""

    total: str
    """Sum of receipt amount held and receipt amount collateralized"""


class Lend(BaseModel):
    """User contribution for asset's lending market, if one exists"""

    origin_equivalent: LendOriginEquivalent
    """
    The lending amounts converted into the equivalent for the receipt token's
    origin/source asset
    """

    receipt_amounts: LendReceiptAmounts
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
