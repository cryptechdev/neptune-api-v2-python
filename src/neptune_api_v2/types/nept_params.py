# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .staking_pool_params import StakingPoolParams

__all__ = [
    "NeptParams",
    "Extra",
    "ExtraText",
    "ExtraValue",
    "ExtraValueExtra",
    "ExtraValueExtraText",
    "StakingPool",
    "StakingPoolExtra",
    "StakingPoolExtraText",
]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    emission_rate: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    emission_rate: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    emission_rate: str

    extra: ExtraValueExtra


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class StakingPoolExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    duration: str

    index: str


class StakingPoolExtra(BaseModel):
    text: Optional[StakingPoolExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class StakingPool(BaseModel):
    """Merges `StakingPool` with `StakingPoolParams`"""

    duration: int
    """The lockup duration for this pool in seconds"""

    extra: StakingPoolExtra

    index: int
    """The ordered index (position) of this pool"""

    params: StakingPoolParams
    """Staking pool contract parameters"""


class NeptParams(BaseModel):
    emission_rate: str
    """The emission rate of NEPT in tokens per year"""

    extra: Extra

    staking_pools: List[StakingPool]
    """Staking pools (pool params are included)"""

    tokens_per_weight: int
    """Weight:token scaling factor

    This is defined in the contract spec to mitigate library type restrictions
    """
