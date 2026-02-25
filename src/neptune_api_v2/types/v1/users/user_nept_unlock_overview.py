# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..duration import Duration
from ...._models import BaseModel
from .user_nept_unlock_amounts import UserNeptUnlockAmounts

__all__ = [
    "UserNeptUnlockOverview",
    "Arrangement",
    "ArrangementExtra",
    "ArrangementExtraText",
    "ArrangementSchedule",
    "ArrangementScheduleLinear",
    "ArrangementScheduleLinearProperties",
    "ArrangementScheduleLinearPropertiesExtra",
    "ArrangementScheduleLinearPropertiesExtraText",
    "ArrangementScheduleLumpSum",
    "ArrangementAdmin",
    "Extra",
    "ExtraText",
]


class ArrangementExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    begins_at: str

    expires_at: str

    last_claimed_at: str


class ArrangementExtra(BaseModel):
    text: Optional[ArrangementExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""


class ArrangementScheduleLinearPropertiesExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    duration: str

    ends_at: str


class ArrangementScheduleLinearPropertiesExtra(BaseModel):
    text: Optional[ArrangementScheduleLinearPropertiesExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""


class ArrangementScheduleLinearProperties(BaseModel):
    duration: Duration
    """The duration of the unlock"""

    ends_at: datetime
    """
    The time at which the unlock has/was/would've completed. This is identical to
    `begins_at + duration`.

    This timestamp will remain valid even if the unlock has been reclaimed.
    Therefore, it should not be used as a validity check.
    """

    extra: ArrangementScheduleLinearPropertiesExtra


class ArrangementScheduleLinear(BaseModel):
    kind: Literal["linear"]

    properties: ArrangementScheduleLinearProperties


class ArrangementScheduleLumpSum(BaseModel):
    kind: Literal["lump_sum"]


ArrangementSchedule: TypeAlias = Union[ArrangementScheduleLinear, ArrangementScheduleLumpSum]


class ArrangementAdmin(BaseModel):
    """`UserNeptUnlockArrangementAdmin`"""

    address: str
    """The address of the unlock arrangement's admin"""

    issued_reclaim: bool
    """True if the admin his issued a reclaim on the unlock arrangement"""


class Arrangement(BaseModel):
    """`UserNeptUnlockArrangement`"""

    amounts: UserNeptUnlockAmounts
    """`UserNeptUnlockAmounts`"""

    begins_at: datetime
    """The time at which the unlock begins"""

    extra: ArrangementExtra

    schedule: ArrangementSchedule
    """`UserNeptUnlockSchedule`"""

    admin: Optional[ArrangementAdmin] = None
    """`UserNeptUnlockArrangementAdmin`"""

    expires_at: Optional[datetime] = None
    """The time at which the unlock expires, if any"""

    last_claimed_at: Optional[datetime] = None
    """The time at which the unlock was last claimed, if any"""


class ExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    last_claimed_at: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""


class UserNeptUnlockOverview(BaseModel):
    """`UserNeptUnlockOverview`"""

    arrangements: List[Arrangement]
    """
    `UserNeptUnlockArrangement[]` -- A list of the user's active unlock arrangements
    """

    extra: Extra

    totals: UserNeptUnlockAmounts
    """`UserNeptUnlockAmounts`"""

    last_claimed_at: Optional[datetime] = None
    """The time at which the most recent unlock claim occurred, if any"""
