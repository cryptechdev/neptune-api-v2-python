# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["UserStakeBondingEntry", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    amount: str

    transition_at: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    amount: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    amount: str

    extra: ExtraValueExtra


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class UserStakeBondingEntry(BaseModel):
    account_index: int
    """User account index"""

    amount: str
    """Bonding amount"""

    cascade: bool

    extra: Extra

    last_stake_acc: str

    transition_at: Optional[datetime] = None
