# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ......_models import BaseModel
from ....error_data import ErrorData
from .user_account_health import UserAccountHealth

__all__ = ["AccountGetHealthResponse"]


class AccountGetHealthResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[UserAccountHealth] = None
    """`UserAccountHealth`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
