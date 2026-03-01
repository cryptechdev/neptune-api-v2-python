# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .user_nept_unlock_amounts import UserNeptUnlockAmounts

__all__ = [
    "UserNeptUnlockOverview",
    "Arrangement",
    "ArrangementAdmin",
    "ArrangementExtra",
    "ArrangementExtraText",
    "ArrangementSchedule",
    "ArrangementScheduleUnlockScheduleLinear",
    "ArrangementScheduleUnlockScheduleLinearExtra",
    "ArrangementScheduleUnlockScheduleLinearExtraText",
    "ArrangementScheduleUnlockScheduleLumpSum",
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


class ArrangementScheduleUnlockScheduleLinearExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    duration: str

    ends_at: str


class ArrangementScheduleUnlockScheduleLinearExtra(BaseModel):
    text: Optional[ArrangementScheduleUnlockScheduleLinearExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class ArrangementScheduleUnlockScheduleLinear(BaseModel):
    duration: int
    """The duration of the unlock in seconds"""

    ends_at: datetime
    """
    The time at which the unlock has/was/would've completed. This is identical to
    `begins_at + duration`.

    This timestamp will remain valid even if the unlock has been reclaimed.
    Therefore, it should not be used as a validity check.
    """

    extra: ArrangementScheduleUnlockScheduleLinearExtra

    kind: Literal["linear"]


class ArrangementScheduleUnlockScheduleLumpSum(BaseModel):
    kind: Literal["lump_sum"]


ArrangementSchedule: TypeAlias = Union[
    ArrangementScheduleUnlockScheduleLinear, ArrangementScheduleUnlockScheduleLumpSum
]


class Arrangement(BaseModel):
    admin: Optional[ArrangementAdmin] = None
    """The admin of the unlock, if any"""

    amounts: UserNeptUnlockAmounts
    """Primary unlock amount and other pre-calculated/derived amounts"""

    begins_at: datetime
    """The time at which the unlock begins"""

    expires_at: Optional[datetime] = None
    """The time at which the unlock expires, if any"""

    extra: ArrangementExtra

    last_claimed_at: Optional[datetime] = None
    """The time at which the unlock was last claimed, if any"""

    schedule: ArrangementSchedule
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


class UserNeptUnlockOverview(BaseModel):
    arrangements: List[Arrangement]
    """-- A list of the user's active unlock arrangements"""

    extra: Extra

    last_claimed_at: Optional[datetime] = None
    """The time at which the most recent unlock claim occurred, if any"""

    totals: UserNeptUnlockAmounts
    """-- Contains pre-calculated total amounts for all unlock agreements"""
