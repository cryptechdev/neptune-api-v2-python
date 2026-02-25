# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......types.v1 import IntervalUnit
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.v1.interval_unit import IntervalUnit
from ......types.v1.analytics.market.history import (
    loans_originated_get_all_params,
    loans_originated_get_by_asset_params,
)
from ......types.v1.analytics.market.history.loans_originated_get_all_response import LoansOriginatedGetAllResponse
from ......types.v1.analytics.market.history.loans_originated_get_by_asset_response import (
    LoansOriginatedGetByAssetResponse,
)

__all__ = ["LoansOriginatedResource", "AsyncLoansOriginatedResource"]


class LoansOriginatedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoansOriginatedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return LoansOriginatedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoansOriginatedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return LoansOriginatedResourceWithStreamingResponse(self)

    def get_all(
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
    ) -> LoansOriginatedGetAllResponse:
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
                    loans_originated_get_all_params.LoansOriginatedGetAllParams,
                ),
            ),
            cast_to=LoansOriginatedGetAllResponse,
        )

    def get_by_asset(
        self,
        *,
        end: int,
        period: IntervalUnit,
        start: int,
        asset_ids: str | Omit = omit,
        interval: int | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoansOriginatedGetByAssetResponse:
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
                    loans_originated_get_by_asset_params.LoansOriginatedGetByAssetParams,
                ),
            ),
            cast_to=LoansOriginatedGetByAssetResponse,
        )


class AsyncLoansOriginatedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoansOriginatedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoansOriginatedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoansOriginatedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncLoansOriginatedResourceWithStreamingResponse(self)

    async def get_all(
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
    ) -> LoansOriginatedGetAllResponse:
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
                    loans_originated_get_all_params.LoansOriginatedGetAllParams,
                ),
            ),
            cast_to=LoansOriginatedGetAllResponse,
        )

    async def get_by_asset(
        self,
        *,
        end: int,
        period: IntervalUnit,
        start: int,
        asset_ids: str | Omit = omit,
        interval: int | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoansOriginatedGetByAssetResponse:
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
                    loans_originated_get_by_asset_params.LoansOriginatedGetByAssetParams,
                ),
            ),
            cast_to=LoansOriginatedGetByAssetResponse,
        )


class LoansOriginatedResourceWithRawResponse:
    def __init__(self, loans_originated: LoansOriginatedResource) -> None:
        self._loans_originated = loans_originated

        self.get_all = to_raw_response_wrapper(
            loans_originated.get_all,
        )
        self.get_by_asset = to_raw_response_wrapper(
            loans_originated.get_by_asset,
        )


class AsyncLoansOriginatedResourceWithRawResponse:
    def __init__(self, loans_originated: AsyncLoansOriginatedResource) -> None:
        self._loans_originated = loans_originated

        self.get_all = async_to_raw_response_wrapper(
            loans_originated.get_all,
        )
        self.get_by_asset = async_to_raw_response_wrapper(
            loans_originated.get_by_asset,
        )


class LoansOriginatedResourceWithStreamingResponse:
    def __init__(self, loans_originated: LoansOriginatedResource) -> None:
        self._loans_originated = loans_originated

        self.get_all = to_streamed_response_wrapper(
            loans_originated.get_all,
        )
        self.get_by_asset = to_streamed_response_wrapper(
            loans_originated.get_by_asset,
        )


class AsyncLoansOriginatedResourceWithStreamingResponse:
    def __init__(self, loans_originated: AsyncLoansOriginatedResource) -> None:
        self._loans_originated = loans_originated

        self.get_all = async_to_streamed_response_wrapper(
            loans_originated.get_all,
        )
        self.get_by_asset = async_to_streamed_response_wrapper(
            loans_originated.get_by_asset,
        )
