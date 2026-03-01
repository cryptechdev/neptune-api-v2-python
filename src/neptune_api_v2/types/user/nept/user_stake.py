# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...asset_info import AssetInfo
from .user_stake_pool import UserStakePool
from .user_stake_unbonding_entry import UserStakeUnbondingEntry

__all__ = [
    "UserStake",
    "Extra",
    "ExtraText",
    "ExtraValue",
    "ExtraValueExtra",
    "ExtraValueExtraText",
    "Unbonding",
    "UnbondingExtra",
    "UnbondingExtraText",
    "UnbondingExtraValue",
    "UnbondingExtraValueExtra",
    "UnbondingExtraValueExtraText",
]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    bonding_sum: str

    claimable_rewards: str

    claimable_unbonding: str

    unclaimed: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    bonding_sum: str

    claimable_rewards: str

    claimable_unbonding: str

    unclaimed: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    bonding_sum: str

    claimable_rewards: str

    claimable_unbonding: str

    extra: ExtraValueExtra

    unclaimed: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class UnbondingExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    amount_sum: str


class UnbondingExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    amount_sum: str


class UnbondingExtraValueExtra(BaseModel):
    text: Optional[UnbondingExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class UnbondingExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    amount_sum: str

    extra: UnbondingExtraValueExtra


class UnbondingExtra(BaseModel):
    text: Optional[UnbondingExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[UnbondingExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class Unbonding(BaseModel):
    """User unstake/unbonding data"""

    amount_sum: str
    """Total amount of all unbond entries

    **NOTE:** this value is affected by active filters, if any (e.g. filtering over
    account index)
    """

    contents: List[UserStakeUnbondingEntry]
    """Unbonding/unstake entries

    **NOTE:** cascade unbondings from pool >= 2 are contained in the bondings list
    of the lower adjacent pool from which the unbond occurred.
    """

    extra: UnbondingExtra


class UserStake(BaseModel):
    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    bonding_sum: str
    """Total staked of all entries across all listed pools

    **NOTE:** this value is affected by active filters, if any (e.g. filtering over
    account index)
    """

    claimable_rewards: str
    """NEPT rewarded from staking that is available yet not claimed by the user"""

    claimable_unbonding: str
    """
    Sum of all unbond/unstake amounts that have completed their lockup period and
    are ready to be claimed.
    """

    extra: Extra

    pools: List[UserStakePool]
    """User allocations for each staking pool"""

    unbonding: Unbonding
    """User unstake/unbonding data"""

    unclaimed: str
