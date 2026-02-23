# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import IntervalUnit
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.markets import (
    lend_lookup_by_asset_params,
    lend_get_rate_history_params,
    lend_get_lending_markets_params,
)
from ....types.v1.interval_unit import IntervalUnit
from ....types.v1.markets.lend_lookup_by_asset_response import LendLookupByAssetResponse
from ....types.v1.markets.lend_get_rate_history_response import LendGetRateHistoryResponse
from ....types.v1.markets.lend_get_lending_markets_response import LendGetLendingMarketsResponse

__all__ = ["LendResource", "AsyncLendResource"]


class LendResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return LendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return LendResourceWithStreamingResponse(self)

    def get_lending_markets(
        self,
        *,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LendGetLendingMarketsResponse:
        """
        Get lending markets

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/markets/lend",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "with_text": with_text,
                        "with_value": with_value,
                    },
                    lend_get_lending_markets_params.LendGetLendingMarketsParams,
                ),
            ),
            cast_to=LendGetLendingMarketsResponse,
        )

    def get_rate_history(
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
    ) -> LendGetRateHistoryResponse:
        """
        Get historical lending rates for assets

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
            "/api/v1/markets/lend/rate-history",
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
                    lend_get_rate_history_params.LendGetRateHistoryParams,
                ),
            ),
            cast_to=LendGetRateHistoryResponse,
        )

    def lookup_by_asset(
        self,
        *,
        asset_id: str,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LendLookupByAssetResponse:
        """
        Lookup lending market by asset

        Args:
          asset_id: Asset ID for lookup

          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/markets/lend/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_id": asset_id,
                        "with_text": with_text,
                        "with_value": with_value,
                    },
                    lend_lookup_by_asset_params.LendLookupByAssetParams,
                ),
            ),
            cast_to=LendLookupByAssetResponse,
        )


class AsyncLendResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncLendResourceWithStreamingResponse(self)

    async def get_lending_markets(
        self,
        *,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LendGetLendingMarketsResponse:
        """
        Get lending markets

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/markets/lend",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "with_text": with_text,
                        "with_value": with_value,
                    },
                    lend_get_lending_markets_params.LendGetLendingMarketsParams,
                ),
            ),
            cast_to=LendGetLendingMarketsResponse,
        )

    async def get_rate_history(
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
    ) -> LendGetRateHistoryResponse:
        """
        Get historical lending rates for assets

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
            "/api/v1/markets/lend/rate-history",
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
                    lend_get_rate_history_params.LendGetRateHistoryParams,
                ),
            ),
            cast_to=LendGetRateHistoryResponse,
        )

    async def lookup_by_asset(
        self,
        *,
        asset_id: str,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LendLookupByAssetResponse:
        """
        Lookup lending market by asset

        Args:
          asset_id: Asset ID for lookup

          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/markets/lend/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asset_id": asset_id,
                        "with_text": with_text,
                        "with_value": with_value,
                    },
                    lend_lookup_by_asset_params.LendLookupByAssetParams,
                ),
            ),
            cast_to=LendLookupByAssetResponse,
        )


class LendResourceWithRawResponse:
    def __init__(self, lend: LendResource) -> None:
        self._lend = lend

        self.get_lending_markets = to_raw_response_wrapper(
            lend.get_lending_markets,
        )
        self.get_rate_history = to_raw_response_wrapper(
            lend.get_rate_history,
        )
        self.lookup_by_asset = to_raw_response_wrapper(
            lend.lookup_by_asset,
        )


class AsyncLendResourceWithRawResponse:
    def __init__(self, lend: AsyncLendResource) -> None:
        self._lend = lend

        self.get_lending_markets = async_to_raw_response_wrapper(
            lend.get_lending_markets,
        )
        self.get_rate_history = async_to_raw_response_wrapper(
            lend.get_rate_history,
        )
        self.lookup_by_asset = async_to_raw_response_wrapper(
            lend.lookup_by_asset,
        )


class LendResourceWithStreamingResponse:
    def __init__(self, lend: LendResource) -> None:
        self._lend = lend

        self.get_lending_markets = to_streamed_response_wrapper(
            lend.get_lending_markets,
        )
        self.get_rate_history = to_streamed_response_wrapper(
            lend.get_rate_history,
        )
        self.lookup_by_asset = to_streamed_response_wrapper(
            lend.lookup_by_asset,
        )


class AsyncLendResourceWithStreamingResponse:
    def __init__(self, lend: AsyncLendResource) -> None:
        self._lend = lend

        self.get_lending_markets = async_to_streamed_response_wrapper(
            lend.get_lending_markets,
        )
        self.get_rate_history = async_to_streamed_response_wrapper(
            lend.get_rate_history,
        )
        self.lookup_by_asset = async_to_streamed_response_wrapper(
            lend.lookup_by_asset,
        )
