# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .asset_info import AssetInfo
from .staking_pool_full import StakingPoolFull

__all__ = [
    "NeptGetStakingOverviewResponse",
    "Data",
    "DataGlobalState",
    "DataGlobalStateExtra",
    "DataGlobalStateExtraText",
]


class DataGlobalStateExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    rewards_last_distributed: str


class DataGlobalStateExtra(BaseModel):
    text: Optional[DataGlobalStateExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class DataGlobalState(BaseModel):
    """Staking state values that are not directly associated to a pool"""

    extra: DataGlobalStateExtra

    rewards_last_distributed: datetime
    """When staking rewards were last distributed"""

    stake_acc: str
    """**! TODO:** rename, proper description, text/value?

    stake_acc = ∫ ( emission_rate / total_reward_weight ) dt
    """


class Data(BaseModel):
    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    global_state: DataGlobalState
    """Staking state values that are not directly associated to a pool"""

    pools: List[StakingPoolFull]
    """List of available staking pools"""


class NeptGetStakingOverviewResponse(BaseModel):
    data: Data

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
