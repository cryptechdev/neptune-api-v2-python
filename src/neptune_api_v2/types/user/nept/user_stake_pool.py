# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...staking_pool_full import StakingPoolFull
from .user_stake_bonding_entry import UserStakeBondingEntry

__all__ = ["UserStakePool", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    amount_sum: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    amount_sum: str

    price: str
    """Text representation of price"""


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

    amount_sum: str

    extra: ExtraValueExtra

    price: str
    """Price used in value calculations"""


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


class UserStakePool(BaseModel):
    amount_sum: str
    """Total staked of all entries

    **NOTE:** this value is affected by active filters, if any (e.g. filtering over
    account index)
    """

    common: StakingPoolFull
    """Staking pool contents along with associated pool state and pool params"""

    contents: List[UserStakeBondingEntry]
    """Bonding/stake entries

    **NOTE:** entries that differ only in amount are merged upon creation
    """

    extra: Extra
