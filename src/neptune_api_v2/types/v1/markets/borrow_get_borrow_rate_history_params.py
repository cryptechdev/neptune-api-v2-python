# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..interval_unit import IntervalUnit

__all__ = ["BorrowGetBorrowRateHistoryParams"]


class BorrowGetBorrowRateHistoryParams(TypedDict, total=False):
    end: Required[int]
    """End timestamp for interval range (inclusive)

    Must be provided as unix timestamp (in seconds)
    """

    period: Required[IntervalUnit]
    """Interval period

    Values:

    - `h`: Hourly
    - `d`: Daily (accounts for offsets introduced by DST)
    - `w`: Weekly (provided for convenience, equivalent to 7d)
    - `m`: Monthly (accounts for varying # of days per month)
    - `y`: Yearly (accounts for varying # of days per year)

    E.g. for interval buckets of 2h `interval=2&period=h`
    """

    start: Required[int]
    """Start timestamp for interval range (inclusive)

    Must be provided as unix timestamp (in seconds)
    """

    asset_ids: str
    """Optional comma-separated list of asset IDs to filter for.

    If excluded, values will be returned for all assets.
    """

    interval: int
    """Interval value

    E.g. for interval buckets of 2h: `interval=2&period=h`
    """

    limit: int
    """Maximum number of time buckets/intervals to return.

    For responses with multiple series, this limit is applied to each series
    individually rather than accumulating across series. This is a limit of returned
    _interval sections_, it is **not** a limit of returned _points_. In other words,
    `limit=200` will provide 200 time points for a single series. For multi-series
    responses, each series will also see the exact same set of 200 time points.
    """

    offset: int
    """Time series bucket offset"""
