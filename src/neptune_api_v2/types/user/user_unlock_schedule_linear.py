# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["UserUnlockScheduleLinear", "Extra", "ExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    duration: str

    ends_at: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class UserUnlockScheduleLinear(BaseModel):
    duration: int
    """The duration of the unlock in seconds"""

    ends_at: datetime
    """
    The time at which the unlock has/was/would've completed. This is identical to
    `begins_at + duration`.

    This timestamp will remain valid even if the unlock has been reclaimed.
    Therefore, it should not be used as a validity check.
    """

    extra: Extra

    kind: Literal["linear"]
