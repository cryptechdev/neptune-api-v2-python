# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MarketRate", "Extra", "ExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    apr: str

    apy: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class MarketRate(BaseModel):
    apr: str
    """Market rate in APR standard as a decimal percentage"""

    apy: str
    """Market rate in APY standard as a decimal percentage"""

    extra: Extra
