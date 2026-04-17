# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .borrow_collateral_market import BorrowCollateralMarket

__all__ = [
    "CollateralListResponse",
    "Data",
    "DataSupply",
    "DataSupplyNonReceipt",
    "DataSupplyNonReceiptExtra",
    "DataSupplyNonReceiptExtraText",
    "DataSupplyReceipt",
    "DataSupplyReceiptExtra",
    "DataSupplyReceiptExtraText",
    "DataSupplyTotal",
    "DataSupplyTotalExtra",
    "DataSupplyTotalExtraText",
]


class DataSupplyNonReceiptExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    balance: str

    shares: str


class DataSupplyNonReceiptExtra(BaseModel):
    text: Optional[DataSupplyNonReceiptExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class DataSupplyNonReceipt(BaseModel):
    """Supply of all collaterals (excluding receipt tokens)"""

    balance: str
    """Sum USD value of market balance"""

    extra: DataSupplyNonReceiptExtra

    shares: str
    """Sum USD value of market shares"""


class DataSupplyReceiptExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    balance: str

    shares: str


class DataSupplyReceiptExtra(BaseModel):
    text: Optional[DataSupplyReceiptExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class DataSupplyReceipt(BaseModel):
    """Supply of receipt token collaterals"""

    balance: str
    """Sum USD value of market balance"""

    extra: DataSupplyReceiptExtra

    shares: str
    """Sum USD value of market shares"""


class DataSupplyTotalExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    balance: str

    shares: str


class DataSupplyTotalExtra(BaseModel):
    text: Optional[DataSupplyTotalExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class DataSupplyTotal(BaseModel):
    """Total supply for collaterals, regardless of type.

    Equivalent to `non_receipt + receipt`
    """

    balance: str
    """Sum USD value of market balance"""

    extra: DataSupplyTotalExtra

    shares: str
    """Sum USD value of market shares"""


class DataSupply(BaseModel):
    """Supply breakdown for collaterals"""

    non_receipt: DataSupplyNonReceipt
    """Supply of all collaterals (excluding receipt tokens)"""

    receipt: DataSupplyReceipt
    """Supply of receipt token collaterals"""

    total: DataSupplyTotal
    """Total supply for collaterals, regardless of type.

    Equivalent to `non_receipt + receipt`
    """


class Data(BaseModel):
    """Borrowing market collaterals overview"""

    contents: List[BorrowCollateralMarket]
    """Borrowing collateral markets"""

    supply: DataSupply
    """Supply breakdown for collaterals"""


class CollateralListResponse(BaseModel):
    data: Data
    """Borrowing market collaterals overview"""

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
