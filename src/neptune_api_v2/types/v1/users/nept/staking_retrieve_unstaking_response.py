# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from ...error_data import ErrorData
from .user_stake_unbonding_entry import UserStakeUnbondingEntry

__all__ = ["StakingRetrieveUnstakingResponse", "Data"]


class Data(BaseModel):
    """Object data"""

    amount_sum: str
    """Total amount of all unbond entries

    **NOTE:** this value is affected by active filters, if any (e.g. filtering over
    account index)
    """

    contents: List[UserStakeUnbondingEntry]
    """`UserStakeUnbondingEntry[]`

    ---

    Unbonding/unstake entries

    **NOTE:** cascade unbondings from pool >= 2 are contained in the bondings list
    of the lower adjacent pool from which the unbond occurred.
    """


class StakingRetrieveUnstakingResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[Data] = None
    """Object data"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
