# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["SwapRouteTargetSet"]


class SwapRouteTargetSet(BaseModel):
    source: str
    """Source denom for swap routes"""

    targets: List[str]
    """List of target denoms for available swap routes"""
