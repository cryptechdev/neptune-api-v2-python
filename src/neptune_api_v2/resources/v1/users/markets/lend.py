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
from .....types.v1.users.markets import lend_list_params, lend_retrieve_lookup_params
from .....types.v1.users.markets.lend_list_response import LendListResponse
from .....types.v1.users.markets.lend_retrieve_lookup_response import LendRetrieveLookupResponse

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
            f"/api/v1/users/{address}/markets/lend",
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

    def retrieve_lookup(
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
    ) -> LendRetrieveLookupResponse:
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
            f"/api/v1/users/{address}/markets/lend/lookup",
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
                    lend_retrieve_lookup_params.LendRetrieveLookupParams,
                ),
            ),
            cast_to=LendRetrieveLookupResponse,
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
            f"/api/v1/users/{address}/markets/lend",
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

    async def retrieve_lookup(
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
    ) -> LendRetrieveLookupResponse:
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
            f"/api/v1/users/{address}/markets/lend/lookup",
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
                    lend_retrieve_lookup_params.LendRetrieveLookupParams,
                ),
            ),
            cast_to=LendRetrieveLookupResponse,
        )


class LendResourceWithRawResponse:
    def __init__(self, lend: LendResource) -> None:
        self._lend = lend

        self.list = to_raw_response_wrapper(
            lend.list,
        )
        self.retrieve_lookup = to_raw_response_wrapper(
            lend.retrieve_lookup,
        )


class AsyncLendResourceWithRawResponse:
    def __init__(self, lend: AsyncLendResource) -> None:
        self._lend = lend

        self.list = async_to_raw_response_wrapper(
            lend.list,
        )
        self.retrieve_lookup = async_to_raw_response_wrapper(
            lend.retrieve_lookup,
        )


class LendResourceWithStreamingResponse:
    def __init__(self, lend: LendResource) -> None:
        self._lend = lend

        self.list = to_streamed_response_wrapper(
            lend.list,
        )
        self.retrieve_lookup = to_streamed_response_wrapper(
            lend.retrieve_lookup,
        )


class AsyncLendResourceWithStreamingResponse:
    def __init__(self, lend: AsyncLendResource) -> None:
        self._lend = lend

        self.list = async_to_streamed_response_wrapper(
            lend.list,
        )
        self.retrieve_lookup = async_to_streamed_response_wrapper(
            lend.retrieve_lookup,
        )
