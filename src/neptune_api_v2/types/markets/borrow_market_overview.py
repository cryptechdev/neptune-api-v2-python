# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .borrow.borrow_debt_market import BorrowDebtMarket
from .borrow.borrow_collateral_market import BorrowCollateralMarket

__all__ = [
    "BorrowMarketOverview",
    "Collaterals",
    "CollateralsSupply",
    "CollateralsSupplyNonReceipt",
    "CollateralsSupplyNonReceiptExtra",
    "CollateralsSupplyNonReceiptExtraText",
    "CollateralsSupplyReceipt",
    "CollateralsSupplyReceiptExtra",
    "CollateralsSupplyReceiptExtraText",
    "CollateralsSupplyTotal",
    "CollateralsSupplyTotalExtra",
    "CollateralsSupplyTotalExtraText",
    "Debts",
    "DebtsSupply",
    "DebtsSupplyExtra",
    "DebtsSupplyExtraText",
]


class CollateralsSupplyNonReceiptExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    balance: str

    shares: str


class CollateralsSupplyNonReceiptExtra(BaseModel):
    text: Optional[CollateralsSupplyNonReceiptExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class CollateralsSupplyNonReceipt(BaseModel):
    """Supply of all collaterals (excluding receipt tokens)"""

    balance: str
    """Sum USD value of market balance"""

    extra: CollateralsSupplyNonReceiptExtra

    shares: str
    """Sum USD value of market shares"""


class CollateralsSupplyReceiptExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    balance: str

    shares: str


class CollateralsSupplyReceiptExtra(BaseModel):
    text: Optional[CollateralsSupplyReceiptExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class CollateralsSupplyReceipt(BaseModel):
    """Supply of receipt token collaterals"""

    balance: str
    """Sum USD value of market balance"""

    extra: CollateralsSupplyReceiptExtra

    shares: str
    """Sum USD value of market shares"""


class CollateralsSupplyTotalExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    balance: str

    shares: str


class CollateralsSupplyTotalExtra(BaseModel):
    text: Optional[CollateralsSupplyTotalExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class CollateralsSupplyTotal(BaseModel):
    """Total supply for collaterals, regardless of type.

    Equivalent to `non_receipt + receipt`
    """

    balance: str
    """Sum USD value of market balance"""

    extra: CollateralsSupplyTotalExtra

    shares: str
    """Sum USD value of market shares"""


class CollateralsSupply(BaseModel):
    """Supply breakdown for collaterals"""

    non_receipt: CollateralsSupplyNonReceipt
    """Supply of all collaterals (excluding receipt tokens)"""

    receipt: CollateralsSupplyReceipt
    """Supply of receipt token collaterals"""

    total: CollateralsSupplyTotal
    """Total supply for collaterals, regardless of type.

    Equivalent to `non_receipt + receipt`
    """


class Collaterals(BaseModel):
    """Borrowing market collaterals overview"""

    contents: List[BorrowCollateralMarket]
    """Borrowing collateral markets"""

    supply: CollateralsSupply
    """Supply breakdown for collaterals"""


class DebtsSupplyExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    balance: str

    shares: str


class DebtsSupplyExtra(BaseModel):
    text: Optional[DebtsSupplyExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class DebtsSupply(BaseModel):
    """Supply breakdown for debt markets"""

    balance: str
    """Sum USD value of market balance"""

    extra: DebtsSupplyExtra

    shares: str
    """Sum USD value of market shares"""


class Debts(BaseModel):
    """Borrowing market debts overview"""

    contents: List[BorrowDebtMarket]
    """Borrowing debt markets"""

    supply: DebtsSupply
    """Supply breakdown for debt markets"""


class BorrowMarketOverview(BaseModel):
    collaterals: Collaterals
    """Borrowing market collaterals overview"""

    debts: Debts
    """Borrowing market debts overview"""
