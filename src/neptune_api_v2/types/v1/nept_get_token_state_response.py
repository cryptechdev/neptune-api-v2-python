# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .duration import Duration
from ..._models import BaseModel
from .error_data import ErrorData
from .staking_pool_state import StakingPoolState

__all__ = [
    "NeptGetTokenStateResponse",
    "Data",
    "DataExtra",
    "DataExtraText",
    "DataExtraValue",
    "DataExtraValueExtra",
    "DataExtraValueExtraText",
    "DataStaking",
    "DataStakingExtra",
    "DataStakingExtraText",
]


class DataExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    total_claimed: str

    total_issued: str

    total_locked: str

    total_supply: str


class DataExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    total_claimed: str

    total_issued: str

    total_locked: str

    total_supply: str


class DataExtraValueExtra(BaseModel):
    text: Optional[DataExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class DataExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    extra: DataExtraValueExtra

    total_claimed: str

    total_issued: str

    total_locked: str

    total_supply: str


class DataExtra(BaseModel):
    text: Optional[DataExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[DataExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class DataStakingExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    duration: str

    index: str


class DataStakingExtra(BaseModel):
    text: Optional[DataStakingExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""


class DataStaking(BaseModel):
    """
    `StakingPoolWithState`
     ---
     Merges `StakingPool` with `StakingPoolState`
    """

    duration: Duration
    """The lockup duration for this pool"""

    extra: DataStakingExtra

    index: int
    """The ordered index (position) of this pool"""

    state: StakingPoolState
    """`StakingPoolState`"""


class Data(BaseModel):
    """`NeptState`"""

    extra: DataExtra

    staking: List[DataStaking]
    """`StakingPool[]`

    ---

    Staking pools (current pool state is included)
    """

    total_claimed: str
    """Total amount of NEPT claimed, either locked or unlocked

    Includes initial balances and claimed rewards but not unclaimed rewards
    """

    total_issued: str
    """Total amount of NEPT issued, either locked or unlocked

    Includes initial balances and all claimed or claimable rewards
    """

    total_locked: str
    """Total amount of NEPT locked

    Inlcudes unlocks which have not yet been claimed
    """

    total_supply: str
    """Total supply of NEPT

    Includes locked and unissued tokens
    """


class NeptGetTokenStateResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[Data] = None
    """`NeptState`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
