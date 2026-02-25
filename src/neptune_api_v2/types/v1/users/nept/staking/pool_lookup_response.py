# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ......_models import BaseModel
from ....error_data import ErrorData
from .user_stake_pool import UserStakePool

__all__ = ["PoolLookupResponse"]


class PoolLookupResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[UserStakePool] = None
    """`UserStakePool`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
