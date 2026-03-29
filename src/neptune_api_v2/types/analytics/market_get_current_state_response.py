# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from ..._models import BaseModel
from ..asset_spec import AssetSpec

__all__ = ["MarketGetCurrentStateResponse", "Data", "DataAsset", "DataLoansOriginated", "DataLoansOriginatedBreakdown"]


class DataAsset(BaseModel):
    """Provides a generic type for associating an `AssetSpec` with some arbitrary data

    Fields from `T` are flattened into the `WithAsset` struct, rendering data inline with the `asset` field.
    """

    asset: AssetSpec
    """Provides a unique identifier for an asset for use throughout the Neptune API.

    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """

    lend_interest_paid: str


class DataLoansOriginatedBreakdown(BaseModel):
    asset: AssetSpec
    """Provides a unique identifier for an asset for use throughout the Neptune API.

    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """

    value: Union[str, float]


class DataLoansOriginated(BaseModel):
    """Analytics for accumulated value of originated loans"""

    breakdown: List[DataLoansOriginatedBreakdown]

    total_value: Union[str, float]


class Data(BaseModel):
    """Primary response content (object)"""

    assets: List[DataAsset]

    borrower_account_active: int

    borrower_active: int

    flash_loan_volume_total: str

    lender_active: int

    loans_originated: DataLoansOriginated
    """Analytics for accumulated value of originated loans"""


class MarketGetCurrentStateResponse(BaseModel):
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
