# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from ...error_data import ErrorData
from .user_debt_asset_pool import UserDebtAssetPool

__all__ = ["LendRetrieveLookupResponse"]


class LendRetrieveLookupResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[UserDebtAssetPool] = None
    """`UserDebtAssetPool`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
