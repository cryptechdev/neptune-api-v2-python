# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from ...._models import BaseModel
from ...interval import Interval

__all__ = ["HistoryGetLoansOriginatedResponse", "Data", "DataPagination", "DataPoint", "DataRange"]


class DataPagination(BaseModel):
    """Pagination parameters for the interval response"""

    interval_count: int
    """
    The total number of intervals/buckets for the provided interval parameters
    (size, period, start, end)
    """

    next_offset: Optional[int] = None
    """
    The offset a client should use to fetch the next page of intervals (so long as
    limit remains unchanged)
    """


class DataPoint(BaseModel):
    """Time + value pair representing a point in time for use with time series"""

    t: datetime

    v: Union[str, float, None] = None


class DataRange(BaseModel):
    """Interval window parameters"""

    end: datetime

    interval: Interval
    """Interval period & size"""

    start: datetime


class Data(BaseModel):
    """Historical cumulative lend value for assets"""

    pagination: DataPagination
    """Pagination parameters for the interval response"""

    points: List[DataPoint]

    range: DataRange
    """Interval window parameters"""


class HistoryGetLoansOriginatedResponse(BaseModel):
    data: Data
    """Historical cumulative lend value for assets"""

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
