# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .error_data import ErrorData
from .global_market_config import GlobalMarketConfig

__all__ = ["MarketGetParamsResponse"]


class MarketGetParamsResponse(BaseModel):
    status: int
    """Request status"""

    status_text: str
    """Request status text"""

    data: Optional[GlobalMarketConfig] = None
    """`GlobalMarketConfig`"""

    error: Optional[ErrorData] = None
    """Error content, only set if an error occurs"""
