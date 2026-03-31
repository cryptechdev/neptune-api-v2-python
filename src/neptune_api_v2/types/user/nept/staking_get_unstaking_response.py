# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .user_stake_unbonding_entry import UserStakeUnbondingEntry

__all__ = ["StakingGetUnstakingResponse", "Data"]


class Data(BaseModel):
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


class StakingGetUnstakingResponse(BaseModel):
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
