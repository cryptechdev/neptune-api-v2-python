# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ......_models import BaseModel
from ....staking_pool_full import StakingPoolFull

__all__ = [
    "UserStakePool",
    "Content",
    "ContentExtra",
    "ContentExtraText",
    "ContentExtraValue",
    "ContentExtraValueExtra",
    "ContentExtraValueExtraText",
    "Extra",
    "ExtraText",
    "ExtraValue",
    "ExtraValueExtra",
    "ExtraValueExtraText",
]


class ContentExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    amount: str

    transition_at: str


class ContentExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    amount: str


class ContentExtraValueExtra(BaseModel):
    text: Optional[ContentExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class ContentExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    amount: str

    extra: ContentExtraValueExtra


class ContentExtra(BaseModel):
    text: Optional[ContentExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[ContentExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class Content(BaseModel):
    """`UserStakeBondingEntry`"""

    account_index: int
    """User account index"""

    amount: str
    """Bonding amount"""

    cascade: bool

    extra: ContentExtra

    last_stake_acc: str

    transition_at: Optional[datetime] = None


class ExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    amount_sum: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    amount_sum: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    amount_sum: str

    extra: ExtraValueExtra


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class UserStakePool(BaseModel):
    """`UserStakePool`"""

    amount_sum: str
    """Total staked of all entries

    **NOTE:** this value is affected by active filters, if any (e.g. filtering over
    account index)
    """

    common: StakingPoolFull
    """`StakingPoolFull`

    ---

    Merges `StakingPool` with both `StakingPoolWithParams` and `StakingPoolState`
    """

    contents: List[Content]
    """`UserStakeBondingEntry[]`

    ---

    Bonding/stake entries

    **NOTE:** entries that differ only in amount are merged upon creation
    """

    extra: Extra
