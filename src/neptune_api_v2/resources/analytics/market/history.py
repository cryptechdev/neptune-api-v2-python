# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ....types import IntervalUnit
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.interval_unit import IntervalUnit
from ....types.analytics.market import history_get_loans_originated_params, history_get_loans_originated_by_asset_params
from ....types.analytics.market.history_get_loans_originated_response import HistoryGetLoansOriginatedResponse
from ....types.analytics.market.history_get_loans_originated_by_asset_response import (
    HistoryGetLoansOriginatedByAssetResponse,
)

__all__ = ["HistoryResource", "AsyncHistoryResource"]


class HistoryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return HistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return HistoryResourceWithStreamingResponse(self)

    def get_loans_originated(
        self,
        *,
        end: int,
        period: IntervalUnit,
        start: int,
        interval: int | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HistoryGetLoansOriginatedResponse:
        """
        Get cumulative lending value history independent of assets

        Args:
          end: End timestamp for interval range (inclusive)

              Must be provided as unix timestamp (in seconds)

          period: Interval period

              Values:

              - `h`: Hourly
              - `d`: Daily (accounts for offsets introduced by DST)
              - `w`: Weekly (provided for convenience, equivalent to 7d)
              - `m`: Monthly (accounts for varying # of days per month)
              - `y`: Yearly (accounts for varying # of days per year)

              E.g. for interval buckets of 2h `interval=2&period=h`

          start: Start timestamp for interval range (inclusive)

              Must be provided as unix timestamp (in seconds)

          interval: Interval value

              E.g. for interval buckets of 2h: `interval=2&period=h`

          limit: Maximum number of time buckets/intervals to return.

              For responses with multiple series, this limit is applied to each series
              individually rather than accumulating across series. This is a limit of returned
              _interval sections_, it is **not** a limit of returned _points_. In other words,
              `limit=200` will provide 200 time points for a single series. For multi-series
              responses, each series will also see the exact same set of 200 time points.

          offset: Time series bucket offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/analytics/market/history/loans-originated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "period": period,
                        "start": start,
                        "interval": interval,
                        "limit": limit,
                        "offset": offset,
                    },
                    history_get_loans_originated_params.HistoryGetLoansOriginatedParams,
                ),
            ),
            cast_to=HistoryGetLoansOriginatedResponse,
        )

    def get_loans_originated_by_asset(
        self,
        *,
        end: int,
        period: IntervalUnit,
        start: int,
        asset_ids: Optional[str] | Omit = omit,
        interval: int | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HistoryGetLoansOriginatedByAssetResponse:
        """
        Get cumulative lending value history assets

        Args:
          end: End timestamp for interval range (inclusive)

              Must be provided as unix timestamp (in seconds)

          period: Interval period

              Values:

              - `h`: Hourly
              - `d`: Daily (accounts for offsets introduced by DST)
              - `w`: Weekly (provided for convenience, equivalent to 7d)
              - `m`: Monthly (accounts for varying # of days per month)
              - `y`: Yearly (accounts for varying # of days per year)

              E.g. for interval buckets of 2h `interval=2&period=h`

          start: Start timestamp for interval range (inclusive)

              Must be provided as unix timestamp (in seconds)

          asset_ids: Optional comma-separated list of asset IDs to filter for. If excluded, values
              will be returned for all assets.

          interval: Interval value

              E.g. for interval buckets of 2h: `interval=2&period=h`

          limit: Maximum number of time buckets/intervals to return.

              For responses with multiple series, this limit is applied to each series
              individually rather than accumulating across series. This is a limit of returned
              _interval sections_, it is **not** a limit of returned _points_. In other words,
              `limit=200` will provide 200 time points for a single series. For multi-series
              responses, each series will also see the exact same set of 200 time points.

          offset: Time series bucket offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/analytics/market/history/loans-originated/by-asset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "period": period,
                        "start": start,
                        "asset_ids": asset_ids,
                        "interval": interval,
                        "limit": limit,
                        "offset": offset,
                    },
                    history_get_loans_originated_by_asset_params.HistoryGetLoansOriginatedByAssetParams,
                ),
            ),
            cast_to=HistoryGetLoansOriginatedByAssetResponse,
        )


class AsyncHistoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return AsyncHistoryResourceWithStreamingResponse(self)

    async def get_loans_originated(
        self,
        *,
        end: int,
        period: IntervalUnit,
        start: int,
        interval: int | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HistoryGetLoansOriginatedResponse:
        """
        Get cumulative lending value history independent of assets

        Args:
          end: End timestamp for interval range (inclusive)

              Must be provided as unix timestamp (in seconds)

          period: Interval period

              Values:

              - `h`: Hourly
              - `d`: Daily (accounts for offsets introduced by DST)
              - `w`: Weekly (provided for convenience, equivalent to 7d)
              - `m`: Monthly (accounts for varying # of days per month)
              - `y`: Yearly (accounts for varying # of days per year)

              E.g. for interval buckets of 2h `interval=2&period=h`

          start: Start timestamp for interval range (inclusive)

              Must be provided as unix timestamp (in seconds)

          interval: Interval value

              E.g. for interval buckets of 2h: `interval=2&period=h`

          limit: Maximum number of time buckets/intervals to return.

              For responses with multiple series, this limit is applied to each series
              individually rather than accumulating across series. This is a limit of returned
              _interval sections_, it is **not** a limit of returned _points_. In other words,
              `limit=200` will provide 200 time points for a single series. For multi-series
              responses, each series will also see the exact same set of 200 time points.

          offset: Time series bucket offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/analytics/market/history/loans-originated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "period": period,
                        "start": start,
                        "interval": interval,
                        "limit": limit,
                        "offset": offset,
                    },
                    history_get_loans_originated_params.HistoryGetLoansOriginatedParams,
                ),
            ),
            cast_to=HistoryGetLoansOriginatedResponse,
        )

    async def get_loans_originated_by_asset(
        self,
        *,
        end: int,
        period: IntervalUnit,
        start: int,
        asset_ids: Optional[str] | Omit = omit,
        interval: int | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HistoryGetLoansOriginatedByAssetResponse:
        """
        Get cumulative lending value history assets

        Args:
          end: End timestamp for interval range (inclusive)

              Must be provided as unix timestamp (in seconds)

          period: Interval period

              Values:

              - `h`: Hourly
              - `d`: Daily (accounts for offsets introduced by DST)
              - `w`: Weekly (provided for convenience, equivalent to 7d)
              - `m`: Monthly (accounts for varying # of days per month)
              - `y`: Yearly (accounts for varying # of days per year)

              E.g. for interval buckets of 2h `interval=2&period=h`

          start: Start timestamp for interval range (inclusive)

              Must be provided as unix timestamp (in seconds)

          asset_ids: Optional comma-separated list of asset IDs to filter for. If excluded, values
              will be returned for all assets.

          interval: Interval value

              E.g. for interval buckets of 2h: `interval=2&period=h`

          limit: Maximum number of time buckets/intervals to return.

              For responses with multiple series, this limit is applied to each series
              individually rather than accumulating across series. This is a limit of returned
              _interval sections_, it is **not** a limit of returned _points_. In other words,
              `limit=200` will provide 200 time points for a single series. For multi-series
              responses, each series will also see the exact same set of 200 time points.

          offset: Time series bucket offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/analytics/market/history/loans-originated/by-asset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "period": period,
                        "start": start,
                        "asset_ids": asset_ids,
                        "interval": interval,
                        "limit": limit,
                        "offset": offset,
                    },
                    history_get_loans_originated_by_asset_params.HistoryGetLoansOriginatedByAssetParams,
                ),
            ),
            cast_to=HistoryGetLoansOriginatedByAssetResponse,
        )


class HistoryResourceWithRawResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.get_loans_originated = to_raw_response_wrapper(
            history.get_loans_originated,
        )
        self.get_loans_originated_by_asset = to_raw_response_wrapper(
            history.get_loans_originated_by_asset,
        )


class AsyncHistoryResourceWithRawResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.get_loans_originated = async_to_raw_response_wrapper(
            history.get_loans_originated,
        )
        self.get_loans_originated_by_asset = async_to_raw_response_wrapper(
            history.get_loans_originated_by_asset,
        )


class HistoryResourceWithStreamingResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.get_loans_originated = to_streamed_response_wrapper(
            history.get_loans_originated,
        )
        self.get_loans_originated_by_asset = to_streamed_response_wrapper(
            history.get_loans_originated_by_asset,
        )


class AsyncHistoryResourceWithStreamingResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.get_loans_originated = async_to_streamed_response_wrapper(
            history.get_loans_originated,
        )
        self.get_loans_originated_by_asset = async_to_streamed_response_wrapper(
            history.get_loans_originated_by_asset,
        )
