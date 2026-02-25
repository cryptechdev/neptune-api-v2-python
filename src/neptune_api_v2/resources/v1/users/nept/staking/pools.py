# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.v1.users.nept.staking import pool_lookup_params, pool_get_all_params
from ......types.v1.users.nept.staking.pool_lookup_response import PoolLookupResponse
from ......types.v1.users.nept.staking.pool_get_all_response import PoolGetAllResponse

__all__ = ["PoolsResource", "AsyncPoolsResource"]


class PoolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return PoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return PoolsResourceWithStreamingResponse(self)

    def get_all(
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
    ) -> PoolGetAllResponse:
        """
        Get user staking pools

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
            f"/api/v1/users/{address}/nept/staking/pools",
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
                    pool_get_all_params.PoolGetAllParams,
                ),
            ),
            cast_to=PoolGetAllResponse,
        )

    def lookup(
        self,
        address: str,
        *,
        duration: str | Omit = omit,
        index: str | Omit = omit,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PoolLookupResponse:
        """
        Get user staking pool by duration/index

        Args:
          address: The user account address

          duration: Duration of pool to lookup (**in nanoseconds**)

              **NOTE:** Either index or duration must be provided. Cannot specify both.

          index: Index of pool to lookup

              **NOTE:** Either index or duration must be provided. Cannot specify both.

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
            f"/api/v1/users/{address}/nept/staking/pools/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "duration": duration,
                        "index": index,
                        "with_text": with_text,
                        "with_value": with_value,
                    },
                    pool_lookup_params.PoolLookupParams,
                ),
            ),
            cast_to=PoolLookupResponse,
        )


class AsyncPoolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncPoolsResourceWithStreamingResponse(self)

    async def get_all(
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
    ) -> PoolGetAllResponse:
        """
        Get user staking pools

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
            f"/api/v1/users/{address}/nept/staking/pools",
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
                    pool_get_all_params.PoolGetAllParams,
                ),
            ),
            cast_to=PoolGetAllResponse,
        )

    async def lookup(
        self,
        address: str,
        *,
        duration: str | Omit = omit,
        index: str | Omit = omit,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PoolLookupResponse:
        """
        Get user staking pool by duration/index

        Args:
          address: The user account address

          duration: Duration of pool to lookup (**in nanoseconds**)

              **NOTE:** Either index or duration must be provided. Cannot specify both.

          index: Index of pool to lookup

              **NOTE:** Either index or duration must be provided. Cannot specify both.

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
            f"/api/v1/users/{address}/nept/staking/pools/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "duration": duration,
                        "index": index,
                        "with_text": with_text,
                        "with_value": with_value,
                    },
                    pool_lookup_params.PoolLookupParams,
                ),
            ),
            cast_to=PoolLookupResponse,
        )


class PoolsResourceWithRawResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

        self.get_all = to_raw_response_wrapper(
            pools.get_all,
        )
        self.lookup = to_raw_response_wrapper(
            pools.lookup,
        )


class AsyncPoolsResourceWithRawResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

        self.get_all = async_to_raw_response_wrapper(
            pools.get_all,
        )
        self.lookup = async_to_raw_response_wrapper(
            pools.lookup,
        )


class PoolsResourceWithStreamingResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

        self.get_all = to_streamed_response_wrapper(
            pools.get_all,
        )
        self.lookup = to_streamed_response_wrapper(
            pools.lookup,
        )


class AsyncPoolsResourceWithStreamingResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

        self.get_all = async_to_streamed_response_wrapper(
            pools.get_all,
        )
        self.lookup = async_to_streamed_response_wrapper(
            pools.lookup,
        )
