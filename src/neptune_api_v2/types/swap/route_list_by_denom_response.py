# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .swap_route_target_set import SwapRouteTargetSet

__all__ = ["RouteListByDenomResponse"]


class RouteListByDenomResponse(BaseModel):
    data: SwapRouteTargetSet

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
