# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .user_unlock_schedule_linear import UserUnlockScheduleLinear
from .user_unlock_schedule_lump_sum import UserUnlockScheduleLumpSum

__all__ = ["UserUnlockSchedule"]

UserUnlockSchedule: TypeAlias = Union[UserUnlockScheduleLinear, UserUnlockScheduleLumpSum]
