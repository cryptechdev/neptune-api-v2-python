# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..nept_unlock_distribution_group import NeptUnlockDistributionGroup

__all__ = ["NeptUnlocksDistributionResponse", "Data"]


class Data(BaseModel):
    groups: List[NeptUnlockDistributionGroup]


class NeptUnlocksDistributionResponse(BaseModel):
    """Object data success response"""

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
