# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["UserAccountHealth", "Extra", "ExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    base: str

    boost: str

    result: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class UserAccountHealth(BaseModel):
    base: str
    """Account health value, before any added health boosts"""

    boost: str
    """Account health boost to be applied"""

    extra: Extra

    result: str
    """Account health, with boost"""
