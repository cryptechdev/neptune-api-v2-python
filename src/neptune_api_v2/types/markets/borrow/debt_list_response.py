# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .borrow_debt_market import BorrowDebtMarket

__all__ = ["DebtListResponse", "Data", "DataSupply", "DataSupplyExtra", "DataSupplyExtraText"]


class DataSupplyExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    balance: str

    shares: str


class DataSupplyExtra(BaseModel):
    text: Optional[DataSupplyExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class DataSupply(BaseModel):
    """Supply breakdown for debt markets"""

    balance: str
    """Sum USD value of market balance"""

    extra: DataSupplyExtra

    shares: str
    """Sum USD value of market shares"""


class Data(BaseModel):
    """Borrowing market debts overview"""

    contents: List[BorrowDebtMarket]
    """Borrowing debt markets"""

    supply: DataSupply
    """Supply breakdown for debt markets"""


class DebtListResponse(BaseModel):
    data: Data
    """Borrowing market debts overview"""

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
