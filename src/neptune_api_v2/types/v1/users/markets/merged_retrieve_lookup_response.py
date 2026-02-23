# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from ...error_data import ErrorData
from .user_merged_market import UserMergedMarket

__all__ = ["MergedRetrieveLookupResponse"]


class MergedRetrieveLookupResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[UserMergedMarket] = None
    """`UserMergedMarket`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
