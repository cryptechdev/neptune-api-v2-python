# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ....types.v1.markets import merged_get_merged_data_params, merged_lookup_by_asset_params
from ....types.v1.markets.merged_get_merged_data_response import MergedGetMergedDataResponse
from ....types.v1.markets.merged_lookup_by_asset_response import MergedLookupByAssetResponse

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

    def get_merged_data(
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
    ) -> MergedGetMergedDataResponse:
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
                    merged_get_merged_data_params.MergedGetMergedDataParams,
                ),
            ),
            cast_to=MergedGetMergedDataResponse,
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
    ) -> MergedLookupByAssetResponse:
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

    async def get_merged_data(
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
    ) -> MergedGetMergedDataResponse:
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
                    merged_get_merged_data_params.MergedGetMergedDataParams,
                ),
            ),
            cast_to=MergedGetMergedDataResponse,
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
    ) -> MergedLookupByAssetResponse:
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
                    merged_lookup_by_asset_params.MergedLookupByAssetParams,
                ),
            ),
            cast_to=MergedLookupByAssetResponse,
        )


class MergedResourceWithRawResponse:
    def __init__(self, merged: MergedResource) -> None:
        self._merged = merged

        self.get_merged_data = to_raw_response_wrapper(
            merged.get_merged_data,
        )
        self.lookup_by_asset = to_raw_response_wrapper(
            merged.lookup_by_asset,
        )


class AsyncMergedResourceWithRawResponse:
    def __init__(self, merged: AsyncMergedResource) -> None:
        self._merged = merged

        self.get_merged_data = async_to_raw_response_wrapper(
            merged.get_merged_data,
        )
        self.lookup_by_asset = async_to_raw_response_wrapper(
            merged.lookup_by_asset,
        )


class MergedResourceWithStreamingResponse:
    def __init__(self, merged: MergedResource) -> None:
        self._merged = merged

        self.get_merged_data = to_streamed_response_wrapper(
            merged.get_merged_data,
        )
        self.lookup_by_asset = to_streamed_response_wrapper(
            merged.lookup_by_asset,
        )


class AsyncMergedResourceWithStreamingResponse:
    def __init__(self, merged: AsyncMergedResource) -> None:
        self._merged = merged

        self.get_merged_data = async_to_streamed_response_wrapper(
            merged.get_merged_data,
        )
        self.lookup_by_asset = async_to_streamed_response_wrapper(
            merged.lookup_by_asset,
        )
