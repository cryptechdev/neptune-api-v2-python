# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ...._models import BaseModel
from ..asset_spec import AssetSpec
from ..error_data import ErrorData

__all__ = ["MarketGetCurrentStateResponse", "Data", "DataAsset", "DataLoansOriginated", "DataLoansOriginatedBreakdown"]


class DataAsset(BaseModel):
    """Provides a generic type for associating an `AssetSpec` with some arbitrary data

    Fields from `T` are flattened into the `WithAsset` struct, rendering data inline with the `asset` field.
    """

    asset: AssetSpec
    """`AssetSpec`

    Provides a unique identifier for an asset for use throughout the Neptune API.
    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """

    lend_interest_paid: str


class DataLoansOriginatedBreakdown(BaseModel):
    asset: AssetSpec
    """`AssetSpec`

    Provides a unique identifier for an asset for use throughout the Neptune API.
    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """

    value: Union[str, float]


class DataLoansOriginated(BaseModel):
    """
    `MarketStateLoanValue`
     ---
     Analytics for accumulated value of originated loans
    """

    breakdown: List[DataLoansOriginatedBreakdown]

    total_value: Union[str, float]


class Data(BaseModel):
    """Object data"""

    assets: List[DataAsset]

    borrower_account_active: int

    borrower_active: int

    flash_loan_volume_total: str

    lender_active: int

    loans_originated: DataLoansOriginated
    """`MarketStateLoanValue`

    ---

    Analytics for accumulated value of originated loans
    """


class MarketGetCurrentStateResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[Data] = None
    """Object data"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
