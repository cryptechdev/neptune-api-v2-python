# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ....._base_client import make_request_options
from .....types.v1.users.markets import merged_get_all_markets_params, merged_lookup_by_asset_params
from .....types.v1.users.markets.merged_get_all_markets_response import MergedGetAllMarketsResponse
from .....types.v1.users.markets.merged_lookup_by_asset_response import MergedLookupByAssetResponse

__all__ = ["MergedResource", "AsyncMergedResource"]


class MergedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MergedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return MergedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MergedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return MergedResourceWithStreamingResponse(self)

    def get_all_markets(
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
    ) -> MergedGetAllMarketsResponse:
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
            f"/api/v1/users/{address}/markets/merged",
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
                    merged_get_all_markets_params.MergedGetAllMarketsParams,
                ),
            ),
            cast_to=MergedGetAllMarketsResponse,
        )

    def lookup_by_asset(
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
    ) -> MergedLookupByAssetResponse:
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
            f"/api/v1/users/{address}/markets/merged/lookup",
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
                    merged_lookup_by_asset_params.MergedLookupByAssetParams,
                ),
            ),
            cast_to=MergedLookupByAssetResponse,
        )


class AsyncMergedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMergedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMergedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMergedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncMergedResourceWithStreamingResponse(self)

    async def get_all_markets(
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
    ) -> MergedGetAllMarketsResponse:
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
            f"/api/v1/users/{address}/markets/merged",
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
                    merged_get_all_markets_params.MergedGetAllMarketsParams,
                ),
            ),
            cast_to=MergedGetAllMarketsResponse,
        )

    async def lookup_by_asset(
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
    ) -> MergedLookupByAssetResponse:
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
            f"/api/v1/users/{address}/markets/merged/lookup",
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
                    merged_lookup_by_asset_params.MergedLookupByAssetParams,
                ),
            ),
            cast_to=MergedLookupByAssetResponse,
        )


class MergedResourceWithRawResponse:
    def __init__(self, merged: MergedResource) -> None:
        self._merged = merged

        self.get_all_markets = to_raw_response_wrapper(
            merged.get_all_markets,
        )
        self.lookup_by_asset = to_raw_response_wrapper(
            merged.lookup_by_asset,
        )


class AsyncMergedResourceWithRawResponse:
    def __init__(self, merged: AsyncMergedResource) -> None:
        self._merged = merged

        self.get_all_markets = async_to_raw_response_wrapper(
            merged.get_all_markets,
        )
        self.lookup_by_asset = async_to_raw_response_wrapper(
            merged.lookup_by_asset,
        )


class MergedResourceWithStreamingResponse:
    def __init__(self, merged: MergedResource) -> None:
        self._merged = merged

        self.get_all_markets = to_streamed_response_wrapper(
            merged.get_all_markets,
        )
        self.lookup_by_asset = to_streamed_response_wrapper(
            merged.lookup_by_asset,
        )


class AsyncMergedResourceWithStreamingResponse:
    def __init__(self, merged: AsyncMergedResource) -> None:
        self._merged = merged

        self.get_all_markets = async_to_streamed_response_wrapper(
            merged.get_all_markets,
        )
        self.lookup_by_asset = async_to_streamed_response_wrapper(
            merged.lookup_by_asset,
        )
