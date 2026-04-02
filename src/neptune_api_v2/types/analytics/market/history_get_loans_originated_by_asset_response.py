# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from ...._models import BaseModel
from ...interval import Interval
from ...asset_spec import AssetSpec

__all__ = [
    "HistoryGetLoansOriginatedByAssetResponse",
    "Data",
    "DataPagination",
    "DataRange",
    "DataSeries",
    "DataSeriesPoint",
]


class DataPagination(BaseModel):
    """Values used for paginating the time series data"""

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


class DataRange(BaseModel):
    """
    Provides values for the requested range in it's entire width, regardless of page/limit.
    """

    end: datetime

    interval: Interval
    """Interval period & size"""

    start: datetime


class DataSeriesPoint(BaseModel):
    """Time + value pair representing a point in time for use with time series"""

    t: datetime

    v: Union[str, float, None] = None


class DataSeries(BaseModel):
    """Item and associated points"""

    asset: AssetSpec
    """Provides a unique identifier for an asset for use throughout the Neptune API.

    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """

    points: List[DataSeriesPoint]


class Data(BaseModel):
    """Historical cumulative lend value for assets"""

    pagination: DataPagination
    """Values used for paginating the time series data"""

    range: DataRange
    """
    Provides values for the requested range in it's entire width, regardless of
    page/limit.
    """

    series: List[DataSeries]


class HistoryGetLoansOriginatedByAssetResponse(BaseModel):
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
