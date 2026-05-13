# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MarketSupplyPool", "Extra", "ExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    balance: str

    shares: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class MarketSupplyPool(BaseModel):
    balance: str
    """Sum USD value of market balance"""

    extra: Extra

    shares: str
    """Sum USD value of market shares"""
