# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .staking_pool_state import StakingPoolState
from .staking_pool_params import StakingPoolParams

__all__ = ["StakingPoolFull", "Extra", "ExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    duration: str

    index: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class StakingPoolFull(BaseModel):
    """Merges `StakingPool` with both `StakingPoolWithParams` and `StakingPoolState`"""

    duration: int
    """The lockup duration for this pool in seconds"""

    extra: Extra

    index: int
    """The ordered index (position) of this pool"""

    params: StakingPoolParams
    """-- Staking pool contract parameters"""

    state: StakingPoolState
    """-- Current contract state of staking pool"""
