# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .asset_info import AssetInfo
from .error_data import ErrorData
from .staking_pool_full import StakingPoolFull

__all__ = [
    "NeptGetStakingOverviewResponse",
    "Data",
    "DataGlobalState",
    "DataGlobalStateExtra",
    "DataGlobalStateExtraText",
]


class DataGlobalStateExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    rewards_last_distributed: str


class DataGlobalStateExtra(BaseModel):
    text: Optional[DataGlobalStateExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""


class DataGlobalState(BaseModel):
    """
    `StakingGlobalState`
    /// --
    /// Staking state values that are not directly associated to a pool
    """

    extra: DataGlobalStateExtra

    rewards_last_distributed: datetime
    """When staking rewards were last distributed"""

    stake_acc: str
    """**TODO:** rename, proper description

    stake_acc = ∫ ( emission_rate / total_reward_weight ) dt
    """


class Data(BaseModel):
    """`StakingOverview`"""

    asset_info: AssetInfo
    """`AssetInfo`"""

    global_state: DataGlobalState
    """
    `StakingGlobalState` /// -- /// Staking state values that are not directly
    associated to a pool
    """

    pools: List[StakingPoolFull]
    """`StakingPool[]` -- Staking pool contract parameter.

    List of available staking pools
    """


class NeptGetStakingOverviewResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[Data] = None
    """`StakingOverview`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
