# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .error_data import ErrorData
from .staking_pool_state import StakingPoolState

__all__ = [
    "NeptGetStateResponse",
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
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    total_claimed: str

    total_issued: str

    total_locked: str

    total_supply: str


class DataExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    total_claimed: str

    total_issued: str

    total_locked: str

    total_supply: str


class DataExtraValueExtra(BaseModel):
    text: Optional[DataExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class DataExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    extra: DataExtraValueExtra

    total_claimed: str

    total_issued: str

    total_locked: str

    total_supply: str


class DataExtra(BaseModel):
    text: Optional[DataExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[DataExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class DataStakingExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    duration: str

    index: str


class DataStakingExtra(BaseModel):
    text: Optional[DataStakingExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class DataStaking(BaseModel):
    """Merges `StakingPool` with `StakingPoolState`"""

    duration: int
    """The lockup duration for this pool in seconds"""

    extra: DataStakingExtra

    index: int
    """The ordered index (position) of this pool"""

    state: StakingPoolState
    """-- Current contract state of staking pool"""


class Data(BaseModel):
    """Object data"""

    extra: DataExtra

    staking: List[DataStaking]
    """Staking pools (current pool state is included)"""

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


class NeptGetStateResponse(BaseModel):
    data: Optional[Data] = None
    """Object data"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""

    status: int
    """Request status"""

    status_text: str
    """Request status text"""
