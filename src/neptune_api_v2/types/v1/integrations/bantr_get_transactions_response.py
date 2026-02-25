# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["BantrGetTransactionsResponse", "Data", "Error"]


class Data(BaseModel):
    action: str
    """The type of action (e.g., lend, borrow)."""

    block: int
    """The block number where the transaction was"""

    tokens_amount_in_usd: str
    """Value of tokens sent into the transaction in USD."""

    tokens_amount_out_usd: str
    """Value of tokens received from the transaction in USD."""

    txn_hash: str
    """The transaction hash."""

    unique_foreign_txn_id: str
    """A unique identifier for the transaction from your system"""

    user_address: str
    """The wallet address of the user."""

    volume_usd: str
    """Total transaction volume in USD."""


class Error(BaseModel):
    code: str

    message: str


class BantrGetTransactionsResponse(BaseModel):
    success: bool

    data: Optional[List[Data]] = None

    error: Optional[Error] = None
