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
from ....types.markets.borrow import collateral_list_params, collateral_get_by_asset_params
from ....types.markets.borrow.collateral_list_response import CollateralListResponse
from ....types.markets.borrow.collateral_get_by_asset_response import CollateralGetByAssetResponse

__all__ = ["CollateralsResource", "AsyncCollateralsResource"]


class CollateralsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CollateralsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/stainless-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return CollateralsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollateralsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/stainless-api-v2-python#with_streaming_response
        """
        return CollateralsResourceWithStreamingResponse(self)

    def list(
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
    ) -> CollateralListResponse:
        """
        Get borrowing collateral markets

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/markets/borrow/collaterals",
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
                    collateral_list_params.CollateralListParams,
                ),
            ),
            cast_to=CollateralListResponse,
        )

    def get_by_asset(
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
    ) -> CollateralGetByAssetResponse:
        """
        Lookup borrowing market collateral by asset

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
            "/api/v1/markets/borrow/collaterals/lookup",
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
                    collateral_get_by_asset_params.CollateralGetByAssetParams,
                ),
            ),
            cast_to=CollateralGetByAssetResponse,
        )


class AsyncCollateralsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCollateralsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/stainless-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCollateralsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollateralsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/stainless-api-v2-python#with_streaming_response
        """
        return AsyncCollateralsResourceWithStreamingResponse(self)

    async def list(
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
    ) -> CollateralListResponse:
        """
        Get borrowing collateral markets

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/markets/borrow/collaterals",
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
                    collateral_list_params.CollateralListParams,
                ),
            ),
            cast_to=CollateralListResponse,
        )

    async def get_by_asset(
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
    ) -> CollateralGetByAssetResponse:
        """
        Lookup borrowing market collateral by asset

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
            "/api/v1/markets/borrow/collaterals/lookup",
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
                    collateral_get_by_asset_params.CollateralGetByAssetParams,
                ),
            ),
            cast_to=CollateralGetByAssetResponse,
        )


class CollateralsResourceWithRawResponse:
    def __init__(self, collaterals: CollateralsResource) -> None:
        self._collaterals = collaterals

        self.list = to_raw_response_wrapper(
            collaterals.list,
        )
        self.get_by_asset = to_raw_response_wrapper(
            collaterals.get_by_asset,
        )


class AsyncCollateralsResourceWithRawResponse:
    def __init__(self, collaterals: AsyncCollateralsResource) -> None:
        self._collaterals = collaterals

        self.list = async_to_raw_response_wrapper(
            collaterals.list,
        )
        self.get_by_asset = async_to_raw_response_wrapper(
            collaterals.get_by_asset,
        )


class CollateralsResourceWithStreamingResponse:
    def __init__(self, collaterals: CollateralsResource) -> None:
        self._collaterals = collaterals

        self.list = to_streamed_response_wrapper(
            collaterals.list,
        )
        self.get_by_asset = to_streamed_response_wrapper(
            collaterals.get_by_asset,
        )


class AsyncCollateralsResourceWithStreamingResponse:
    def __init__(self, collaterals: AsyncCollateralsResource) -> None:
        self._collaterals = collaterals

        self.list = async_to_streamed_response_wrapper(
            collaterals.list,
        )
        self.get_by_asset = async_to_streamed_response_wrapper(
            collaterals.get_by_asset,
        )
