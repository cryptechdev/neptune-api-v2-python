# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .user_unlock_amounts import UserUnlockAmounts
from .user_unlock_schedule import UserUnlockSchedule

__all__ = [
    "UserUnlockOverview",
    "Arrangement",
    "ArrangementAdmin",
    "ArrangementExtra",
    "ArrangementExtraText",
    "Extra",
    "ExtraText",
]


class ArrangementAdmin(BaseModel):
    """The admin of the unlock, if any"""

    address: str
    """The address of the unlock arrangement's admin"""

    issued_reclaim: bool
    """True if the admin his issued a reclaim on the unlock arrangement"""


class ArrangementExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    begins_at: str

    expires_at: str

    last_claimed_at: str


class ArrangementExtra(BaseModel):
    text: Optional[ArrangementExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class Arrangement(BaseModel):
    admin: Optional[ArrangementAdmin] = None
    """The admin of the unlock, if any"""

    amounts: UserUnlockAmounts
    """Primary unlock amount and other pre-calculated/derived amounts"""

    begins_at: datetime
    """The time at which the unlock begins"""

    expires_at: Optional[datetime] = None
    """The time at which the unlock expires, if any"""

    extra: ArrangementExtra

    last_claimed_at: Optional[datetime] = None
    """The time at which the unlock was last claimed, if any"""

    schedule: UserUnlockSchedule
    """The schedule of the unlock"""


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    last_claimed_at: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class UserUnlockOverview(BaseModel):
    arrangements: List[Arrangement]
    """A list of the user's active unlock arrangements"""

    extra: Extra

    last_claimed_at: Optional[datetime] = None
    """The time at which the most recent unlock claim occurred, if any"""

    totals: UserUnlockAmounts
    """Contains pre-calculated total amounts for all unlock agreements"""
