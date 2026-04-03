# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...asset_info import AssetInfo
from .user_stake_pool import UserStakePool
from .user_stake_unbonding import UserStakeUnbonding

__all__ = ["UserStake", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


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

    price: str
    """Text representation of price"""

    unclaimed: str


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

    bonding_sum: str

    claimable_rewards: str

    claimable_unbonding: str

    extra: ExtraValueExtra

    price: str
    """Price used in value calculations"""

    unclaimed: str


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

    unbonding: UserStakeUnbonding
    """User unstake/unbonding data"""

    unclaimed: str
