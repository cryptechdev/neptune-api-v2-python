# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...asset_info import AssetInfo

__all__ = [
    "BorrowGetCollateralAccountsByAssetResponse",
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

    amount: str


class DataAccountExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    amount: str


class DataAccountExtraValueExtra(BaseModel):
    text: Optional[DataAccountExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class DataAccountExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    amount: str

    extra: DataAccountExtraValueExtra


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
    amount: str
    """Amount of this asset which is actively collateralized"""

    extra: DataAccountExtra

    index: int
    """Account index"""


class Data(BaseModel):
    """Primary response content (object)"""

    accounts: List[DataAccount]
    """All collateral subaccounts for the associated asset type"""

    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""


class BorrowGetCollateralAccountsByAssetResponse(BaseModel):
    """Object data success response"""

    data: Data
    """Primary response content (object)"""

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
