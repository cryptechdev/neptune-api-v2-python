# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .interval import Interval
from .asset_spec import AssetSpec

__all__ = ["AssetRateHistory", "Pagination", "Range", "Series", "SeriesPoint"]


class Pagination(BaseModel):
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


class Range(BaseModel):
    """
    Provides values for the requested range in it's entire width, regardless of page/limit.
    """

    end: datetime

    interval: Interval
    """Interval period & size"""

    start: datetime


class SeriesPoint(BaseModel):
    """Time + value pair representing a point in time for use with time series"""

    t: datetime

    v: Optional[str] = None


class Series(BaseModel):
    asset: AssetSpec
    """Provides a unique identifier for an asset for use throughout the Neptune API.

    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """

    points: List[SeriesPoint]


class AssetRateHistory(BaseModel):
    """Historical rates for assets"""

    pagination: Pagination
    """Values used for paginating the time series data"""

    range: Range
    """
    Provides values for the requested range in it's entire width, regardless of
    page/limit.
    """

    series: List[Series]
    """Pairs of items and their associated points"""
