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
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.user import market_get_merged_params, market_get_portfolio_params, market_get_merged_by_asset_params
from .borrow.borrow import (
    BorrowResource,
    AsyncBorrowResource,
    BorrowResourceWithRawResponse,
    AsyncBorrowResourceWithRawResponse,
    BorrowResourceWithStreamingResponse,
    AsyncBorrowResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.user.market_get_merged_response import MarketGetMergedResponse
from ....types.user.market_get_portfolio_response import MarketGetPortfolioResponse
from ....types.user.market_get_merged_by_asset_response import MarketGetMergedByAssetResponse

__all__ = ["MarketResource", "AsyncMarketResource"]


class MarketResource(SyncAPIResource):
    @cached_property
    def lend(self) -> LendResource:
        return LendResource(self._client)

    @cached_property
    def borrow(self) -> BorrowResource:
        return BorrowResource(self._client)

    @cached_property
    def with_raw_response(self) -> MarketResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return MarketResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return MarketResourceWithStreamingResponse(self)

    def get_merged(
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
    ) -> MarketGetMergedResponse:
        """
        Get user markets for all kinds (lend + borrow debt/collateral), grouped together
        by asset

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
            path_template("/api/v1/users/{address}/markets/merged", address=address),
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
                    market_get_merged_params.MarketGetMergedParams,
                ),
            ),
            cast_to=MarketGetMergedResponse,
        )

    def get_merged_by_asset(
        self,
        address: str,
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
    ) -> MarketGetMergedByAssetResponse:
        """
        Get user's markets (lend + borrow debt/collateral) for a specific asset

        Args:
          address: The user account address

          asset_id: Asset ID for lookup

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
            path_template("/api/v1/users/{address}/markets/merged/lookup", address=address),
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
                    market_get_merged_by_asset_params.MarketGetMergedByAssetParams,
                ),
            ),
            cast_to=MarketGetMergedByAssetResponse,
        )

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
            path_template("/api/v1/users/{address}/markets", address=address),
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


class AsyncMarketResource(AsyncAPIResource):
    @cached_property
    def lend(self) -> AsyncLendResource:
        return AsyncLendResource(self._client)

    @cached_property
    def borrow(self) -> AsyncBorrowResource:
        return AsyncBorrowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMarketResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return AsyncMarketResourceWithStreamingResponse(self)

    async def get_merged(
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
    ) -> MarketGetMergedResponse:
        """
        Get user markets for all kinds (lend + borrow debt/collateral), grouped together
        by asset

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
            path_template("/api/v1/users/{address}/markets/merged", address=address),
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
                    market_get_merged_params.MarketGetMergedParams,
                ),
            ),
            cast_to=MarketGetMergedResponse,
        )

    async def get_merged_by_asset(
        self,
        address: str,
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
    ) -> MarketGetMergedByAssetResponse:
        """
        Get user's markets (lend + borrow debt/collateral) for a specific asset

        Args:
          address: The user account address

          asset_id: Asset ID for lookup

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
            path_template("/api/v1/users/{address}/markets/merged/lookup", address=address),
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
                    market_get_merged_by_asset_params.MarketGetMergedByAssetParams,
                ),
            ),
            cast_to=MarketGetMergedByAssetResponse,
        )

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
            path_template("/api/v1/users/{address}/markets", address=address),
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


class MarketResourceWithRawResponse:
    def __init__(self, market: MarketResource) -> None:
        self._market = market

        self.get_merged = to_raw_response_wrapper(
            market.get_merged,
        )
        self.get_merged_by_asset = to_raw_response_wrapper(
            market.get_merged_by_asset,
        )
        self.get_portfolio = to_raw_response_wrapper(
            market.get_portfolio,
        )

    @cached_property
    def lend(self) -> LendResourceWithRawResponse:
        return LendResourceWithRawResponse(self._market.lend)

    @cached_property
    def borrow(self) -> BorrowResourceWithRawResponse:
        return BorrowResourceWithRawResponse(self._market.borrow)


class AsyncMarketResourceWithRawResponse:
    def __init__(self, market: AsyncMarketResource) -> None:
        self._market = market

        self.get_merged = async_to_raw_response_wrapper(
            market.get_merged,
        )
        self.get_merged_by_asset = async_to_raw_response_wrapper(
            market.get_merged_by_asset,
        )
        self.get_portfolio = async_to_raw_response_wrapper(
            market.get_portfolio,
        )

    @cached_property
    def lend(self) -> AsyncLendResourceWithRawResponse:
        return AsyncLendResourceWithRawResponse(self._market.lend)

    @cached_property
    def borrow(self) -> AsyncBorrowResourceWithRawResponse:
        return AsyncBorrowResourceWithRawResponse(self._market.borrow)


class MarketResourceWithStreamingResponse:
    def __init__(self, market: MarketResource) -> None:
        self._market = market

        self.get_merged = to_streamed_response_wrapper(
            market.get_merged,
        )
        self.get_merged_by_asset = to_streamed_response_wrapper(
            market.get_merged_by_asset,
        )
        self.get_portfolio = to_streamed_response_wrapper(
            market.get_portfolio,
        )

    @cached_property
    def lend(self) -> LendResourceWithStreamingResponse:
        return LendResourceWithStreamingResponse(self._market.lend)

    @cached_property
    def borrow(self) -> BorrowResourceWithStreamingResponse:
        return BorrowResourceWithStreamingResponse(self._market.borrow)


class AsyncMarketResourceWithStreamingResponse:
    def __init__(self, market: AsyncMarketResource) -> None:
        self._market = market

        self.get_merged = async_to_streamed_response_wrapper(
            market.get_merged,
        )
        self.get_merged_by_asset = async_to_streamed_response_wrapper(
            market.get_merged_by_asset,
        )
        self.get_portfolio = async_to_streamed_response_wrapper(
            market.get_portfolio,
        )

    @cached_property
    def lend(self) -> AsyncLendResourceWithStreamingResponse:
        return AsyncLendResourceWithStreamingResponse(self._market.lend)

    @cached_property
    def borrow(self) -> AsyncBorrowResourceWithStreamingResponse:
        return AsyncBorrowResourceWithStreamingResponse(self._market.borrow)
