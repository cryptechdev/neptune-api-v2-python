# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ......_models import BaseModel

__all__ = ["UserAccountHealth", "Extra", "ExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    base: str

    boost: str

    result: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""


class UserAccountHealth(BaseModel):
    """`UserAccountHealth`"""

    base: str
    """`UserAccountHealthValue`

    ---

    Account health value, before any added health boosts
    """

    boost: str
    """`UserAccountHealthBoost`

    ---

    Account health boost to be applied
    """

    extra: Extra

    result: str
    """`UserAccountHealthValue`

    ---

    Account health, with boost
    """
