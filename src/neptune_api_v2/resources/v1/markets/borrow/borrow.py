# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .debts import (
    DebtsResource,
    AsyncDebtsResource,
    DebtsResourceWithRawResponse,
    AsyncDebtsResourceWithRawResponse,
    DebtsResourceWithStreamingResponse,
    AsyncDebtsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from .collaterals import (
    CollateralsResource,
    AsyncCollateralsResource,
    CollateralsResourceWithRawResponse,
    AsyncCollateralsResourceWithRawResponse,
    CollateralsResourceWithStreamingResponse,
    AsyncCollateralsResourceWithStreamingResponse,
)
from .....types.v1 import IntervalUnit
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.v1.markets import borrow_overview_params, borrow_get_borrow_rate_history_params
from .....types.v1.interval_unit import IntervalUnit
from .....types.v1.markets.borrow_overview_response import BorrowOverviewResponse
from .....types.v1.markets.borrow_get_borrow_rate_history_response import BorrowGetBorrowRateHistoryResponse

__all__ = ["BorrowResource", "AsyncBorrowResource"]


class BorrowResource(SyncAPIResource):
    @cached_property
    def collaterals(self) -> CollateralsResource:
        return CollateralsResource(self._client)

    @cached_property
    def debts(self) -> DebtsResource:
        return DebtsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BorrowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return BorrowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BorrowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return BorrowResourceWithStreamingResponse(self)

    def get_borrow_rate_history(
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
    ) -> BorrowGetBorrowRateHistoryResponse:
        """
        Get historical borrowing rates for assets

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
            "/api/v1/markets/borrow/rate-history",
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
                    borrow_get_borrow_rate_history_params.BorrowGetBorrowRateHistoryParams,
                ),
            ),
            cast_to=BorrowGetBorrowRateHistoryResponse,
        )

    def overview(
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
    ) -> BorrowOverviewResponse:
        """
        Get borrowing market overview

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/markets/borrow",
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
                    borrow_overview_params.BorrowOverviewParams,
                ),
            ),
            cast_to=BorrowOverviewResponse,
        )


class AsyncBorrowResource(AsyncAPIResource):
    @cached_property
    def collaterals(self) -> AsyncCollateralsResource:
        return AsyncCollateralsResource(self._client)

    @cached_property
    def debts(self) -> AsyncDebtsResource:
        return AsyncDebtsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBorrowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBorrowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBorrowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncBorrowResourceWithStreamingResponse(self)

    async def get_borrow_rate_history(
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
    ) -> BorrowGetBorrowRateHistoryResponse:
        """
        Get historical borrowing rates for assets

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
            "/api/v1/markets/borrow/rate-history",
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
                    borrow_get_borrow_rate_history_params.BorrowGetBorrowRateHistoryParams,
                ),
            ),
            cast_to=BorrowGetBorrowRateHistoryResponse,
        )

    async def overview(
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
    ) -> BorrowOverviewResponse:
        """
        Get borrowing market overview

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/markets/borrow",
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
                    borrow_overview_params.BorrowOverviewParams,
                ),
            ),
            cast_to=BorrowOverviewResponse,
        )


class BorrowResourceWithRawResponse:
    def __init__(self, borrow: BorrowResource) -> None:
        self._borrow = borrow

        self.get_borrow_rate_history = to_raw_response_wrapper(
            borrow.get_borrow_rate_history,
        )
        self.overview = to_raw_response_wrapper(
            borrow.overview,
        )

    @cached_property
    def collaterals(self) -> CollateralsResourceWithRawResponse:
        return CollateralsResourceWithRawResponse(self._borrow.collaterals)

    @cached_property
    def debts(self) -> DebtsResourceWithRawResponse:
        return DebtsResourceWithRawResponse(self._borrow.debts)


class AsyncBorrowResourceWithRawResponse:
    def __init__(self, borrow: AsyncBorrowResource) -> None:
        self._borrow = borrow

        self.get_borrow_rate_history = async_to_raw_response_wrapper(
            borrow.get_borrow_rate_history,
        )
        self.overview = async_to_raw_response_wrapper(
            borrow.overview,
        )

    @cached_property
    def collaterals(self) -> AsyncCollateralsResourceWithRawResponse:
        return AsyncCollateralsResourceWithRawResponse(self._borrow.collaterals)

    @cached_property
    def debts(self) -> AsyncDebtsResourceWithRawResponse:
        return AsyncDebtsResourceWithRawResponse(self._borrow.debts)


class BorrowResourceWithStreamingResponse:
    def __init__(self, borrow: BorrowResource) -> None:
        self._borrow = borrow

        self.get_borrow_rate_history = to_streamed_response_wrapper(
            borrow.get_borrow_rate_history,
        )
        self.overview = to_streamed_response_wrapper(
            borrow.overview,
        )

    @cached_property
    def collaterals(self) -> CollateralsResourceWithStreamingResponse:
        return CollateralsResourceWithStreamingResponse(self._borrow.collaterals)

    @cached_property
    def debts(self) -> DebtsResourceWithStreamingResponse:
        return DebtsResourceWithStreamingResponse(self._borrow.debts)


class AsyncBorrowResourceWithStreamingResponse:
    def __init__(self, borrow: AsyncBorrowResource) -> None:
        self._borrow = borrow

        self.get_borrow_rate_history = async_to_streamed_response_wrapper(
            borrow.get_borrow_rate_history,
        )
        self.overview = async_to_streamed_response_wrapper(
            borrow.overview,
        )

    @cached_property
    def collaterals(self) -> AsyncCollateralsResourceWithStreamingResponse:
        return AsyncCollateralsResourceWithStreamingResponse(self._borrow.collaterals)

    @cached_property
    def debts(self) -> AsyncDebtsResourceWithStreamingResponse:
        return AsyncDebtsResourceWithStreamingResponse(self._borrow.debts)
