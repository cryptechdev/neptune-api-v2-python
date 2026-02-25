# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .lend import (
    LendResource,
    AsyncLendResource,
    LendResourceWithRawResponse,
    AsyncLendResourceWithRawResponse,
    LendResourceWithStreamingResponse,
    AsyncLendResourceWithStreamingResponse,
)
from .merged import (
    MergedResource,
    AsyncMergedResource,
    MergedResourceWithRawResponse,
    AsyncMergedResourceWithRawResponse,
    MergedResourceWithStreamingResponse,
    AsyncMergedResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .borrow.borrow import (
    BorrowResource,
    AsyncBorrowResource,
    BorrowResourceWithRawResponse,
    AsyncBorrowResourceWithRawResponse,
    BorrowResourceWithStreamingResponse,
    AsyncBorrowResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.v1.users import market_get_portfolio_params
from .....types.v1.users.market_get_portfolio_response import MarketGetPortfolioResponse

__all__ = ["MarketsResource", "AsyncMarketsResource"]


class MarketsResource(SyncAPIResource):
    @cached_property
    def lend(self) -> LendResource:
        return LendResource(self._client)

    @cached_property
    def borrow(self) -> BorrowResource:
        return BorrowResource(self._client)

    @cached_property
    def merged(self) -> MergedResource:
        return MergedResource(self._client)

    @cached_property
    def with_raw_response(self) -> MarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return MarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return MarketsResourceWithStreamingResponse(self)

    def get_portfolio(
        self,
        address: str,
        *,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGetPortfolioResponse:
        """
        Get user market portfolio

        Args:
          address: The user account address

          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return self._get(
            f"/api/v1/users/{address}/markets",
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
                    market_get_portfolio_params.MarketGetPortfolioParams,
                ),
            ),
            cast_to=MarketGetPortfolioResponse,
        )


class AsyncMarketsResource(AsyncAPIResource):
    @cached_property
    def lend(self) -> AsyncLendResource:
        return AsyncLendResource(self._client)

    @cached_property
    def borrow(self) -> AsyncBorrowResource:
        return AsyncBorrowResource(self._client)

    @cached_property
    def merged(self) -> AsyncMergedResource:
        return AsyncMergedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncMarketsResourceWithStreamingResponse(self)

    async def get_portfolio(
        self,
        address: str,
        *,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGetPortfolioResponse:
        """
        Get user market portfolio

        Args:
          address: The user account address

          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return await self._get(
            f"/api/v1/users/{address}/markets",
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
                    market_get_portfolio_params.MarketGetPortfolioParams,
                ),
            ),
            cast_to=MarketGetPortfolioResponse,
        )


class MarketsResourceWithRawResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.get_portfolio = to_raw_response_wrapper(
            markets.get_portfolio,
        )

    @cached_property
    def lend(self) -> LendResourceWithRawResponse:
        return LendResourceWithRawResponse(self._markets.lend)

    @cached_property
    def borrow(self) -> BorrowResourceWithRawResponse:
        return BorrowResourceWithRawResponse(self._markets.borrow)

    @cached_property
    def merged(self) -> MergedResourceWithRawResponse:
        return MergedResourceWithRawResponse(self._markets.merged)


class AsyncMarketsResourceWithRawResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.get_portfolio = async_to_raw_response_wrapper(
            markets.get_portfolio,
        )

    @cached_property
    def lend(self) -> AsyncLendResourceWithRawResponse:
        return AsyncLendResourceWithRawResponse(self._markets.lend)

    @cached_property
    def borrow(self) -> AsyncBorrowResourceWithRawResponse:
        return AsyncBorrowResourceWithRawResponse(self._markets.borrow)

    @cached_property
    def merged(self) -> AsyncMergedResourceWithRawResponse:
        return AsyncMergedResourceWithRawResponse(self._markets.merged)


class MarketsResourceWithStreamingResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.get_portfolio = to_streamed_response_wrapper(
            markets.get_portfolio,
        )

    @cached_property
    def lend(self) -> LendResourceWithStreamingResponse:
        return LendResourceWithStreamingResponse(self._markets.lend)

    @cached_property
    def borrow(self) -> BorrowResourceWithStreamingResponse:
        return BorrowResourceWithStreamingResponse(self._markets.borrow)

    @cached_property
    def merged(self) -> MergedResourceWithStreamingResponse:
        return MergedResourceWithStreamingResponse(self._markets.merged)


class AsyncMarketsResourceWithStreamingResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.get_portfolio = async_to_streamed_response_wrapper(
            markets.get_portfolio,
        )

    @cached_property
    def lend(self) -> AsyncLendResourceWithStreamingResponse:
        return AsyncLendResourceWithStreamingResponse(self._markets.lend)

    @cached_property
    def borrow(self) -> AsyncBorrowResourceWithStreamingResponse:
        return AsyncBorrowResourceWithStreamingResponse(self._markets.borrow)

    @cached_property
    def merged(self) -> AsyncMergedResourceWithStreamingResponse:
        return AsyncMergedResourceWithStreamingResponse(self._markets.merged)
