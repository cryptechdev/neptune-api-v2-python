# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime

from ...._models import BaseModel

__all__ = ["HistoryGetLoansOriginatedResponse"]


class HistoryGetLoansOriginatedResponse(BaseModel):
    """Time + value pair representing a point in time for use with time series"""

    t: datetime

    v: Union[str, float, None] = None
