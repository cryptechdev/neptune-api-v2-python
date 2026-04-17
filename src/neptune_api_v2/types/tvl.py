# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Tvl", "Extra", "ExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    collateral_value: str

    lend_value: str

    total_value: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class Tvl(BaseModel):
    collateral_value: str
    """Market TVL in USD - collateral portion"""

    extra: Extra

    lend_value: str
    """Market TVL in USD - lend portion"""

    total_value: str
    """Market TVL in USD"""
