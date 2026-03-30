# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .nept_params import NeptParams

__all__ = ["NeptGetParamsResponse"]


class NeptGetParamsResponse(BaseModel):
    """Object data success response"""

    data: NeptParams

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
