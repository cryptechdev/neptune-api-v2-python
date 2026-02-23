# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .user_stake import UserStake
from ....._models import BaseModel
from ...error_data import ErrorData

__all__ = ["StakingListResponse"]


class StakingListResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[UserStake] = None
    """`UserStake`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
