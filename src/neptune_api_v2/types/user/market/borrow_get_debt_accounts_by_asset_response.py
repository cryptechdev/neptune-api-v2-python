# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...asset_info import AssetInfo
from ...error_data import ErrorData

__all__ = [
    "BorrowGetDebtAccountsByAssetResponse",
    "Data",
    "DataAccount",
    "DataAccountExtra",
    "DataAccountExtraText",
    "DataAccountExtraValue",
    "DataAccountExtraValueExtra",
    "DataAccountExtraValueExtraText",
]


class DataAccountExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    debt: str

    interest: str

    principal: str


class DataAccountExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    debt: str

    interest: str

    principal: str


class DataAccountExtraValueExtra(BaseModel):
    text: Optional[DataAccountExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class DataAccountExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    debt: str

    extra: DataAccountExtraValueExtra

    interest: str

    principal: str


class DataAccountExtra(BaseModel):
    text: Optional[DataAccountExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[DataAccountExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class DataAccount(BaseModel):
    debt: str
    """Sum open debt amount (this is simply the principal + interest)"""

    extra: DataAccountExtra

    index: int
    """Account index"""

    interest: str
    """Sum of accrued interest for open debt position"""

    principal: str
    """Initial amount borrowed (of debts which have not yet been repaid)"""


class Data(BaseModel):
    """Object data"""

    accounts: List[DataAccount]
    """All debt subaccounts for the associated asset type"""

    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""


class BorrowGetDebtAccountsByAssetResponse(BaseModel):
    data: Optional[Data] = None
    """Object data"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""

    status: int
    """Request status"""

    status_text: str
    """Request status text"""
