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
from ...types import (
    market_get_merged_params,
    market_get_params_params,
    market_get_supply_params,
    market_get_overview_params,
    market_get_merged_by_asset_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
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
from ..._base_client import make_request_options
from ...types.market_get_merged_response import MarketGetMergedResponse
from ...types.market_get_params_response import MarketGetParamsResponse
from ...types.market_get_supply_response import MarketGetSupplyResponse
from ...types.market_get_overview_response import MarketGetOverviewResponse
from ...types.market_get_merged_by_asset_response import MarketGetMergedByAssetResponse

__all__ = ["MarketsResource", "AsyncMarketsResource"]


class MarketsResource(SyncAPIResource):
    @cached_property
    def lend(self) -> LendResource:
        return LendResource(self._client)

    @cached_property
    def borrow(self) -> BorrowResource:
        return BorrowResource(self._client)

    @cached_property
    def with_raw_response(self) -> MarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return MarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return MarketsResourceWithStreamingResponse(self)

    def get_merged(
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
    ) -> MarketGetMergedResponse:
        """
        Get lend/collateral/debt grouped by asset

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/markets/merged",
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
        Lookup merged market data by asset

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
            "/api/v1/markets/merged/lookup",
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

    def get_overview(
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
    ) -> MarketGetOverviewResponse:
        """
        Get market overview

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/markets",
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
                    market_get_overview_params.MarketGetOverviewParams,
                ),
            ),
            cast_to=MarketGetOverviewResponse,
        )

    def get_params(
        self,
        *,
        with_text: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGetParamsResponse:
        """
        Get market params

        Args:
          with_text: Include text variation fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/markets/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"with_text": with_text}, market_get_params_params.MarketGetParamsParams),
            ),
            cast_to=MarketGetParamsResponse,
        )

    def get_supply(
        self,
        *,
        with_text: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGetSupplyResponse:
        """
        Get market supply

        Args:
          with_text: Include text variation fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/markets/supply",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"with_text": with_text}, market_get_supply_params.MarketGetSupplyParams),
            ),
            cast_to=MarketGetSupplyResponse,
        )


class AsyncMarketsResource(AsyncAPIResource):
    @cached_property
    def lend(self) -> AsyncLendResource:
        return AsyncLendResource(self._client)

    @cached_property
    def borrow(self) -> AsyncBorrowResource:
        return AsyncBorrowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return AsyncMarketsResourceWithStreamingResponse(self)

    async def get_merged(
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
    ) -> MarketGetMergedResponse:
        """
        Get lend/collateral/debt grouped by asset

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/markets/merged",
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
        Lookup merged market data by asset

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
            "/api/v1/markets/merged/lookup",
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

    async def get_overview(
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
    ) -> MarketGetOverviewResponse:
        """
        Get market overview

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/markets",
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
                    market_get_overview_params.MarketGetOverviewParams,
                ),
            ),
            cast_to=MarketGetOverviewResponse,
        )

    async def get_params(
        self,
        *,
        with_text: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGetParamsResponse:
        """
        Get market params

        Args:
          with_text: Include text variation fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/markets/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"with_text": with_text}, market_get_params_params.MarketGetParamsParams
                ),
            ),
            cast_to=MarketGetParamsResponse,
        )

    async def get_supply(
        self,
        *,
        with_text: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketGetSupplyResponse:
        """
        Get market supply

        Args:
          with_text: Include text variation fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/markets/supply",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"with_text": with_text}, market_get_supply_params.MarketGetSupplyParams
                ),
            ),
            cast_to=MarketGetSupplyResponse,
        )


class MarketsResourceWithRawResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.get_merged = to_raw_response_wrapper(
            markets.get_merged,
        )
        self.get_merged_by_asset = to_raw_response_wrapper(
            markets.get_merged_by_asset,
        )
        self.get_overview = to_raw_response_wrapper(
            markets.get_overview,
        )
        self.get_params = to_raw_response_wrapper(
            markets.get_params,
        )
        self.get_supply = to_raw_response_wrapper(
            markets.get_supply,
        )

    @cached_property
    def lend(self) -> LendResourceWithRawResponse:
        return LendResourceWithRawResponse(self._markets.lend)

    @cached_property
    def borrow(self) -> BorrowResourceWithRawResponse:
        return BorrowResourceWithRawResponse(self._markets.borrow)


class AsyncMarketsResourceWithRawResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.get_merged = async_to_raw_response_wrapper(
            markets.get_merged,
        )
        self.get_merged_by_asset = async_to_raw_response_wrapper(
            markets.get_merged_by_asset,
        )
        self.get_overview = async_to_raw_response_wrapper(
            markets.get_overview,
        )
        self.get_params = async_to_raw_response_wrapper(
            markets.get_params,
        )
        self.get_supply = async_to_raw_response_wrapper(
            markets.get_supply,
        )

    @cached_property
    def lend(self) -> AsyncLendResourceWithRawResponse:
        return AsyncLendResourceWithRawResponse(self._markets.lend)

    @cached_property
    def borrow(self) -> AsyncBorrowResourceWithRawResponse:
        return AsyncBorrowResourceWithRawResponse(self._markets.borrow)


class MarketsResourceWithStreamingResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.get_merged = to_streamed_response_wrapper(
            markets.get_merged,
        )
        self.get_merged_by_asset = to_streamed_response_wrapper(
            markets.get_merged_by_asset,
        )
        self.get_overview = to_streamed_response_wrapper(
            markets.get_overview,
        )
        self.get_params = to_streamed_response_wrapper(
            markets.get_params,
        )
        self.get_supply = to_streamed_response_wrapper(
            markets.get_supply,
        )

    @cached_property
    def lend(self) -> LendResourceWithStreamingResponse:
        return LendResourceWithStreamingResponse(self._markets.lend)

    @cached_property
    def borrow(self) -> BorrowResourceWithStreamingResponse:
        return BorrowResourceWithStreamingResponse(self._markets.borrow)


class AsyncMarketsResourceWithStreamingResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.get_merged = async_to_streamed_response_wrapper(
            markets.get_merged,
        )
        self.get_merged_by_asset = async_to_streamed_response_wrapper(
            markets.get_merged_by_asset,
        )
        self.get_overview = async_to_streamed_response_wrapper(
            markets.get_overview,
        )
        self.get_params = async_to_streamed_response_wrapper(
            markets.get_params,
        )
        self.get_supply = async_to_streamed_response_wrapper(
            markets.get_supply,
        )

    @cached_property
    def lend(self) -> AsyncLendResourceWithStreamingResponse:
        return AsyncLendResourceWithStreamingResponse(self._markets.lend)

    @cached_property
    def borrow(self) -> AsyncBorrowResourceWithStreamingResponse:
        return AsyncBorrowResourceWithStreamingResponse(self._markets.borrow)
