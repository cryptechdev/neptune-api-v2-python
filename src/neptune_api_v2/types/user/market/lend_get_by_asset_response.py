# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ...asset_info import AssetInfo

__all__ = [
    "LendGetByAssetResponse",
    "Data",
    "DataOriginEquivalent",
    "DataOriginEquivalentExtra",
    "DataOriginEquivalentExtraText",
    "DataReceiptAmounts",
    "DataReceiptAmountsExtra",
    "DataReceiptAmountsExtraText",
    "DataReceiptAmountsExtraValue",
    "DataReceiptAmountsExtraValueExtra",
    "DataReceiptAmountsExtraValueExtraText",
]


class DataOriginEquivalentExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    collateralized: str

    held: str

    total: str


class DataOriginEquivalentExtra(BaseModel):
    text: Optional[DataOriginEquivalentExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class DataOriginEquivalent(BaseModel):
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

    extra: DataOriginEquivalentExtra

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


class DataReceiptAmountsExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    collateralized: str

    held: str

    total: str


class DataReceiptAmountsExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    collateralized: str

    held: str

    total: str


class DataReceiptAmountsExtraValueExtra(BaseModel):
    text: Optional[DataReceiptAmountsExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class DataReceiptAmountsExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    collateralized: str

    extra: DataReceiptAmountsExtraValueExtra

    held: str

    total: str


class DataReceiptAmountsExtra(BaseModel):
    text: Optional[DataReceiptAmountsExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[DataReceiptAmountsExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class DataReceiptAmounts(BaseModel):
    """The lending amounts in the original receipt token amounts"""

    collateralized: str
    """
    Total amount of receipt token collateralized across this user's borrowing
    portfolio
    """

    extra: DataReceiptAmountsExtra

    held: str
    """Total amount of receipt token held in address balance"""

    total: str
    """Sum of receipt amount held and receipt amount collateralized"""


class Data(BaseModel):
    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    origin_equivalent: DataOriginEquivalent
    """
    The lending amounts converted into the equivalent for the receipt token's
    origin/source asset
    """

    receipt_amounts: DataReceiptAmounts
    """The lending amounts in the original receipt token amounts"""


class LendGetByAssetResponse(BaseModel):
    data: Data

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
