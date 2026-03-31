# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from ...asset_info import AssetInfo
from .borrow.user_debt_account_pool import UserDebtAccountPool

__all__ = ["BorrowGetDebtAccountsByAssetResponse", "Data"]


class Data(BaseModel):
    accounts: List[UserDebtAccountPool]
    """All debt subaccounts for the associated asset type"""

    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""


class BorrowGetDebtAccountsByAssetResponse(BaseModel):
    data: Data

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
