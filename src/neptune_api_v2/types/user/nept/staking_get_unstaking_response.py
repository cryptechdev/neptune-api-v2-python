# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .user_stake_unbonding import UserStakeUnbonding

__all__ = ["StakingGetUnstakingResponse"]


class StakingGetUnstakingResponse(BaseModel):
    data: UserStakeUnbonding

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
