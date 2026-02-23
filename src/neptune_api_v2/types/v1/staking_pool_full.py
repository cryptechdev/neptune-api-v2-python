# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .duration import Duration
from ..._models import BaseModel
from .staking_pool_state import StakingPoolState
from .staking_pool_params import StakingPoolParams

__all__ = ["StakingPoolFull", "Extra", "ExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    duration: str

    index: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""


class StakingPoolFull(BaseModel):
    """
    `StakingPoolFull`
     ---
     Merges `StakingPool` with both `StakingPoolWithParams` and `StakingPoolState`
    """

    duration: Duration
    """The lockup duration for this pool"""

    extra: Extra

    index: int
    """The ordered index (position) of this pool"""

    params: StakingPoolParams
    """`StakingPoolParams`"""

    state: StakingPoolState
    """`StakingPoolState`"""
