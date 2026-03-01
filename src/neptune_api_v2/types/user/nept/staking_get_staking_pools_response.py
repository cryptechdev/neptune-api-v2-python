# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...error_data import ErrorData
from .user_stake_pool import UserStakePool

__all__ = ["StakingGetStakingPoolsResponse"]


class StakingGetStakingPoolsResponse(BaseModel):
    count: Optional[int] = None
    """Total number of objects in all pages"""

    data: Optional[List[UserStakePool]] = None
    """List contents"""

    error: Optional[ErrorData] = None
    """Error message, if any"""

    status: int
    """Request status"""

    status_text: str
    """Request status text"""
