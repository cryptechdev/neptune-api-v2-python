# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...._base_client import make_request_options
from ....types.user.market import lend_list_params, lend_get_by_asset_params
from ....types.user.market.lend_list_response import LendListResponse
from ....types.user.market.lend_get_by_asset_response import LendGetByAssetResponse

__all__ = ["LendResource", "AsyncLendResource"]


class LendResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return LendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return LendResourceWithStreamingResponse(self)

    def list(
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
    ) -> LendListResponse:
        """
        Get user lending portfolio

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
            path_template("/api/v1/users/{address}/markets/lend", address=address),
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
                    lend_list_params.LendListParams,
                ),
            ),
            cast_to=LendListResponse,
        )

    def get_by_asset(
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
    ) -> LendGetByAssetResponse:
        """
        Lookup user lending distribution by asset

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
            path_template("/api/v1/users/{address}/markets/lend/lookup", address=address),
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
                    lend_get_by_asset_params.LendGetByAssetParams,
                ),
            ),
            cast_to=LendGetByAssetResponse,
        )


class AsyncLendResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return AsyncLendResourceWithStreamingResponse(self)

    async def list(
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
    ) -> LendListResponse:
        """
        Get user lending portfolio

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
            path_template("/api/v1/users/{address}/markets/lend", address=address),
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
                    lend_list_params.LendListParams,
                ),
            ),
            cast_to=LendListResponse,
        )

    async def get_by_asset(
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
    ) -> LendGetByAssetResponse:
        """
        Lookup user lending distribution by asset

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
            path_template("/api/v1/users/{address}/markets/lend/lookup", address=address),
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
                    lend_get_by_asset_params.LendGetByAssetParams,
                ),
            ),
            cast_to=LendGetByAssetResponse,
        )


class LendResourceWithRawResponse:
    def __init__(self, lend: LendResource) -> None:
        self._lend = lend

        self.list = to_raw_response_wrapper(
            lend.list,
        )
        self.get_by_asset = to_raw_response_wrapper(
            lend.get_by_asset,
        )


class AsyncLendResourceWithRawResponse:
    def __init__(self, lend: AsyncLendResource) -> None:
        self._lend = lend

        self.list = async_to_raw_response_wrapper(
            lend.list,
        )
        self.get_by_asset = async_to_raw_response_wrapper(
            lend.get_by_asset,
        )


class LendResourceWithStreamingResponse:
    def __init__(self, lend: LendResource) -> None:
        self._lend = lend

        self.list = to_streamed_response_wrapper(
            lend.list,
        )
        self.get_by_asset = to_streamed_response_wrapper(
            lend.get_by_asset,
        )


class AsyncLendResourceWithStreamingResponse:
    def __init__(self, lend: AsyncLendResource) -> None:
        self._lend = lend

        self.list = async_to_streamed_response_wrapper(
            lend.list,
        )
        self.get_by_asset = async_to_streamed_response_wrapper(
            lend.get_by_asset,
        )
