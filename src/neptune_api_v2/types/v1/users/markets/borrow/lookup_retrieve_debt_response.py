# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ......_models import BaseModel
from ....asset_info import AssetInfo
from ....error_data import ErrorData

__all__ = [
    "LookupRetrieveDebtResponse",
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

    debt: str

    interest: str

    principal: str


class DataAccountExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    debt: str

    interest: str

    principal: str


class DataAccountExtraValueExtra(BaseModel):
    text: Optional[DataAccountExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class DataAccountExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    debt: str

    extra: DataAccountExtraValueExtra

    interest: str

    principal: str


class DataAccountExtra(BaseModel):
    text: Optional[DataAccountExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[DataAccountExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class DataAccount(BaseModel):
    """`UserCollateralAccountPool`"""

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
    """`UserDebtLookup`"""

    accounts: List[DataAccount]
    """`UserDebtAccountPool[]`

    ---

    All debt subaccounts for the associated asset type
    """

    asset_info: AssetInfo
    """`AssetInfo`"""


class LookupRetrieveDebtResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[Data] = None
    """`UserDebtLookup`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
