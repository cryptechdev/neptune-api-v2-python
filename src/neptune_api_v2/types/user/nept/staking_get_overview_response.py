# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .user_stake import UserStake
from ...error_data import ErrorData

__all__ = ["StakingGetOverviewResponse"]


class StakingGetOverviewResponse(BaseModel):
    data: Optional[UserStake] = None
    """Object data"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""

    status: int
    """Request status"""

    status_text: str
    """Request status text"""
