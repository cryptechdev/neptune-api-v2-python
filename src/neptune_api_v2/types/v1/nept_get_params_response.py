# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .duration import Duration
from ..._models import BaseModel
from .error_data import ErrorData
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
    """Human-readable field variants. Must provide `?with-text=true`"""

    emission_rate: str


class DataExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    emission_rate: str


class DataExtraValueExtra(BaseModel):
    text: Optional[DataExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class DataExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    emission_rate: str

    extra: DataExtraValueExtra


class DataExtra(BaseModel):
    text: Optional[DataExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[DataExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class DataStakingPoolExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    duration: str

    index: str


class DataStakingPoolExtra(BaseModel):
    text: Optional[DataStakingPoolExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""


class DataStakingPool(BaseModel):
    """
    `StakingPoolWithParams`
     ---
     Merges `StakingPool` with `StakingPoolParams`
    """

    duration: Duration
    """The lockup duration for this pool"""

    extra: DataStakingPoolExtra

    index: int
    """The ordered index (position) of this pool"""

    params: StakingPoolParams
    """`StakingPoolParams`"""


class Data(BaseModel):
    """`NeptParams`"""

    emission_rate: str
    """The emission rate of NEPT in tokens per year"""

    extra: DataExtra

    staking_pools: List[DataStakingPool]
    """`StakingPool[]`

    ---

    Staking pools (pool params are included)
    """

    tokens_per_weight: int
    """Weight:token scaling factor

    This is defined in the contract spec to mitigate library type restrictions
    """


class NeptGetParamsResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[Data] = None
    """`NeptParams`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
