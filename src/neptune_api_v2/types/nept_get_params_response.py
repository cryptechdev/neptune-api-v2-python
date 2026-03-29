# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .staking_pool_params import StakingPoolParams

__all__ = [
    "NeptGetParamsResponse",
    "Data",
    "DataExtra",
    "DataExtraText",
    "DataExtraValue",
    "DataExtraValueExtra",
    "DataExtraValueExtraText",
    "DataStakingPool",
    "DataStakingPoolExtra",
    "DataStakingPoolExtraText",
]


class DataExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    emission_rate: str


class DataExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    emission_rate: str


class DataExtraValueExtra(BaseModel):
    text: Optional[DataExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class DataExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    emission_rate: str

    extra: DataExtraValueExtra


class DataExtra(BaseModel):
    text: Optional[DataExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[DataExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class DataStakingPoolExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    duration: str

    index: str


class DataStakingPoolExtra(BaseModel):
    text: Optional[DataStakingPoolExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class DataStakingPool(BaseModel):
    """Merges `StakingPool` with `StakingPoolParams`"""

    duration: int
    """The lockup duration for this pool in seconds"""

    extra: DataStakingPoolExtra

    index: int
    """The ordered index (position) of this pool"""

    params: StakingPoolParams
    """Staking pool contract parameters"""


class Data(BaseModel):
    """Primary response content (object)"""

    emission_rate: str
    """The emission rate of NEPT in tokens per year"""

    extra: DataExtra

    staking_pools: List[DataStakingPool]
    """Staking pools (pool params are included)"""

    tokens_per_weight: int
    """Weight:token scaling factor

    This is defined in the contract spec to mitigate library type restrictions
    """


class NeptGetParamsResponse(BaseModel):
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
