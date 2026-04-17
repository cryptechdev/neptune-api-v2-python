# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Tvl", "Extra", "ExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    net_tvl: str

    tvl: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class Tvl(BaseModel):
    extra: Extra

    net_tvl: str
    """Market net TVL in USD (equivalent to `tvl - borrow.debts.supply.balance`)"""

    tvl: str
    """
    Market TVL in USD (equivalent to
    `borrow.collaterals.supply.non_receipt.balance + lend.supply.principal`)
    """
