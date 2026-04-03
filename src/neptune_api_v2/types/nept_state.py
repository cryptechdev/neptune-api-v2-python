# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .staking_pool_state import StakingPoolState

__all__ = [
    "NeptState",
    "Extra",
    "ExtraText",
    "ExtraValue",
    "ExtraValueExtra",
    "ExtraValueExtraText",
    "Staking",
    "StakingExtra",
    "StakingExtraText",
]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    total_claimed: str

    total_issued: str

    total_locked: str

    total_supply: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    price: str
    """Text representation of price"""

    total_claimed: str

    total_issued: str

    total_locked: str

    total_supply: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.

    ### Note

    This variant group contains an additional `price` field (set to the number used in value calculation).

    The embedded text group will contain the text variant if `with_text` was specified as well.
    """

    extra: ExtraValueExtra

    price: str
    """Price used in value calculations"""

    total_claimed: str

    total_issued: str

    total_locked: str

    total_supply: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.

    ### Note

    This variant group contains an additional `price` field (set to the number used
    in value calculation).

    The embedded text group will contain the text variant if `with_text` was
    specified as well.
    """


class StakingExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    duration: str

    index: str


class StakingExtra(BaseModel):
    text: Optional[StakingExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class Staking(BaseModel):
    """Staking pool contents along with associated pool state"""

    duration: int
    """The lockup duration for this pool in seconds"""

    extra: StakingExtra

    index: int
    """The ordered index (position) of this pool"""

    state: StakingPoolState
    """Current contract state of staking pool"""


class NeptState(BaseModel):
    extra: Extra

    staking: List[Staking]
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
