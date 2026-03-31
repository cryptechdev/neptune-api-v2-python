# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...asset_info import AssetInfo

__all__ = [
    "UserLendMarket",
    "AssetPool",
    "AssetPoolOriginEquivalent",
    "AssetPoolOriginEquivalentExtra",
    "AssetPoolOriginEquivalentExtraText",
    "AssetPoolReceiptAmounts",
    "AssetPoolReceiptAmountsExtra",
    "AssetPoolReceiptAmountsExtraText",
    "AssetPoolReceiptAmountsExtraValue",
    "AssetPoolReceiptAmountsExtraValueExtra",
    "AssetPoolReceiptAmountsExtraValueExtraText",
]


class AssetPoolOriginEquivalentExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    collateralized: str

    held: str

    total: str


class AssetPoolOriginEquivalentExtra(BaseModel):
    text: Optional[AssetPoolOriginEquivalentExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class AssetPoolOriginEquivalent(BaseModel):
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

    extra: AssetPoolOriginEquivalentExtra

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


class AssetPoolReceiptAmountsExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    collateralized: str

    held: str

    total: str


class AssetPoolReceiptAmountsExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    collateralized: str

    held: str

    total: str


class AssetPoolReceiptAmountsExtraValueExtra(BaseModel):
    text: Optional[AssetPoolReceiptAmountsExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class AssetPoolReceiptAmountsExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    collateralized: str

    extra: AssetPoolReceiptAmountsExtraValueExtra

    held: str

    total: str


class AssetPoolReceiptAmountsExtra(BaseModel):
    text: Optional[AssetPoolReceiptAmountsExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[AssetPoolReceiptAmountsExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class AssetPoolReceiptAmounts(BaseModel):
    """The lending amounts in the original receipt token amounts"""

    collateralized: str
    """
    Total amount of receipt token collateralized across this user's borrowing
    portfolio
    """

    extra: AssetPoolReceiptAmountsExtra

    held: str
    """Total amount of receipt token held in address balance"""

    total: str
    """Sum of receipt amount held and receipt amount collateralized"""


class AssetPool(BaseModel):
    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    origin_equivalent: AssetPoolOriginEquivalent
    """
    The lending amounts converted into the equivalent for the receipt token's
    origin/source asset
    """

    receipt_amounts: AssetPoolReceiptAmounts
    """The lending amounts in the original receipt token amounts"""


class UserLendMarket(BaseModel):
    asset_pools: List[AssetPool]
    """User lending allocations"""
