# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ......_models import BaseModel
from ....asset_info import AssetInfo
from ....error_data import ErrorData

__all__ = [
    "LookupRetrieveCollateralResponse",
    "Data",
    "DataAccount",
    "DataAccountExtra",
    "DataAccountExtraText",
    "DataAccountExtraValue",
    "DataAccountExtraValueExtra",
    "DataAccountExtraValueExtraText",
]


class DataAccountExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    amount: str


class DataAccountExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    amount: str


class DataAccountExtraValueExtra(BaseModel):
    text: Optional[DataAccountExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class DataAccountExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    amount: str

    extra: DataAccountExtraValueExtra


class DataAccountExtra(BaseModel):
    text: Optional[DataAccountExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[DataAccountExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class DataAccount(BaseModel):
    """`UserCollateralAccountPool`"""

    amount: str
    """Amount of this asset which is actively collateralized"""

    extra: DataAccountExtra

    index: int
    """Account index"""


class Data(BaseModel):
    """`UserCollateralLookup`"""

    accounts: List[DataAccount]
    """`UserMergedCollateralAccount[]`

    ---

    All collateral subaccounts for the associated asset type Collateral sub-accounts
    for the user
    """

    asset_info: AssetInfo
    """`AssetInfo`"""


class LookupRetrieveCollateralResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[Data] = None
    """`UserCollateralLookup`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
