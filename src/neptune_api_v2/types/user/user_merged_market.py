# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..asset_info import AssetInfo

__all__ = [
    "UserMergedMarket",
    "BorrowCollateral",
    "BorrowCollateralExtra",
    "BorrowCollateralExtraText",
    "BorrowCollateralExtraValue",
    "BorrowCollateralExtraValueExtra",
    "BorrowCollateralExtraValueExtraText",
    "BorrowDebt",
    "BorrowDebtExtra",
    "BorrowDebtExtraText",
    "BorrowDebtExtraValue",
    "BorrowDebtExtraValueExtra",
    "BorrowDebtExtraValueExtraText",
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


class BorrowCollateralExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    amount: str


class BorrowCollateralExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    amount: str


class BorrowCollateralExtraValueExtra(BaseModel):
    text: Optional[BorrowCollateralExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class BorrowCollateralExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    amount: str

    extra: BorrowCollateralExtraValueExtra


class BorrowCollateralExtra(BaseModel):
    text: Optional[BorrowCollateralExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[BorrowCollateralExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class BorrowCollateral(BaseModel):
    amount: str
    """Amount of this asset which is actively collateralized"""

    extra: BorrowCollateralExtra

    index: int
    """Account index"""


class BorrowDebtExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    debt: str

    interest: str

    principal: str


class BorrowDebtExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    debt: str

    interest: str

    principal: str


class BorrowDebtExtraValueExtra(BaseModel):
    text: Optional[BorrowDebtExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class BorrowDebtExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    debt: str

    extra: BorrowDebtExtraValueExtra

    interest: str

    principal: str


class BorrowDebtExtra(BaseModel):
    text: Optional[BorrowDebtExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[BorrowDebtExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class BorrowDebt(BaseModel):
    debt: str
    """Sum open debt amount (this is simply the principal + interest)"""

    extra: BorrowDebtExtra

    index: int
    """Account index"""

    interest: str
    """Sum of accrued interest for open debt position"""

    principal: str
    """Initial amount borrowed (of debts which have not yet been repaid)"""


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

    total: str


class LendReceiptAmountsExtraValueExtra(BaseModel):
    text: Optional[LendReceiptAmountsExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class LendReceiptAmountsExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    collateralized: str

    extra: LendReceiptAmountsExtraValueExtra

    held: str

    total: str


class LendReceiptAmountsExtra(BaseModel):
    text: Optional[LendReceiptAmountsExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[LendReceiptAmountsExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
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
    """User contirbution for asset's lending market, if one exists"""

    origin_equivalent: LendOriginEquivalent
    """
    The lending amounts converted into the equivalent for the receipt token's
    origin/source asset
    """

    receipt_amounts: LendReceiptAmounts
    """The lending amounts in the original receipt token amounts"""


class UserMergedMarket(BaseModel):
    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    borrow_collateral: List[BorrowCollateral]
    """User collateral contribution for asset in borrow market, listed by subaccount"""

    borrow_debt: List[BorrowDebt]
    """User debt contribution for asset in borrow market, listed by subaccount"""

    lend: Optional[Lend] = None
    """User contirbution for asset's lending market, if one exists"""
