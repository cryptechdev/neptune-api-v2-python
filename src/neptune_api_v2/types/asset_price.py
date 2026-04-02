# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AssetPrice", "Extra", "ExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    last_updated_at: str

    price: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class AssetPrice(BaseModel):
    """> **Note**: Prices are sourced from Neptune's Price Oracle"""

    extra: Extra

    last_updated_at: datetime
    """Asset price value, as per Neptune Price Oracle"""

    price: str
    """Asset price"""
