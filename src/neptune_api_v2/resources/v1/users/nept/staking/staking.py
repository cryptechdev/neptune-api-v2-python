# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .pools import (
    PoolsResource,
    AsyncPoolsResource,
    PoolsResourceWithRawResponse,
    AsyncPoolsResourceWithRawResponse,
    PoolsResourceWithStreamingResponse,
    AsyncPoolsResourceWithStreamingResponse,
)
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
from ......types.v1.users.nept import staking_list_params, staking_retrieve_unstaking_params
from ......types.v1.users.nept.staking_list_response import StakingListResponse
from ......types.v1.users.nept.staking_retrieve_unstaking_response import StakingRetrieveUnstakingResponse

__all__ = ["StakingResource", "AsyncStakingResource"]


class StakingResource(SyncAPIResource):
    @cached_property
    def pools(self) -> PoolsResource:
        return PoolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> StakingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return StakingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StakingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return StakingResourceWithStreamingResponse(self)

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
    ) -> StakingListResponse:
        """
        Get user staking overview

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
            f"/api/v1/users/{address}/nept/staking",
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
                    staking_list_params.StakingListParams,
                ),
            ),
            cast_to=StakingListResponse,
        )

    def retrieve_unstaking(
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
    ) -> StakingRetrieveUnstakingResponse:
        """
        Get user unstaking pool

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
            f"/api/v1/users/{address}/nept/staking/unstaking",
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
                    staking_retrieve_unstaking_params.StakingRetrieveUnstakingParams,
                ),
            ),
            cast_to=StakingRetrieveUnstakingResponse,
        )


class AsyncStakingResource(AsyncAPIResource):
    @cached_property
    def pools(self) -> AsyncPoolsResource:
        return AsyncPoolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStakingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStakingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStakingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncStakingResourceWithStreamingResponse(self)

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
    ) -> StakingListResponse:
        """
        Get user staking overview

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
            f"/api/v1/users/{address}/nept/staking",
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
                    staking_list_params.StakingListParams,
                ),
            ),
            cast_to=StakingListResponse,
        )

    async def retrieve_unstaking(
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
    ) -> StakingRetrieveUnstakingResponse:
        """
        Get user unstaking pool

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
            f"/api/v1/users/{address}/nept/staking/unstaking",
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
                    staking_retrieve_unstaking_params.StakingRetrieveUnstakingParams,
                ),
            ),
            cast_to=StakingRetrieveUnstakingResponse,
        )


class StakingResourceWithRawResponse:
    def __init__(self, staking: StakingResource) -> None:
        self._staking = staking

        self.list = to_raw_response_wrapper(
            staking.list,
        )
        self.retrieve_unstaking = to_raw_response_wrapper(
            staking.retrieve_unstaking,
        )

    @cached_property
    def pools(self) -> PoolsResourceWithRawResponse:
        return PoolsResourceWithRawResponse(self._staking.pools)


class AsyncStakingResourceWithRawResponse:
    def __init__(self, staking: AsyncStakingResource) -> None:
        self._staking = staking

        self.list = async_to_raw_response_wrapper(
            staking.list,
        )
        self.retrieve_unstaking = async_to_raw_response_wrapper(
            staking.retrieve_unstaking,
        )

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithRawResponse:
        return AsyncPoolsResourceWithRawResponse(self._staking.pools)


class StakingResourceWithStreamingResponse:
    def __init__(self, staking: StakingResource) -> None:
        self._staking = staking

        self.list = to_streamed_response_wrapper(
            staking.list,
        )
        self.retrieve_unstaking = to_streamed_response_wrapper(
            staking.retrieve_unstaking,
        )

    @cached_property
    def pools(self) -> PoolsResourceWithStreamingResponse:
        return PoolsResourceWithStreamingResponse(self._staking.pools)


class AsyncStakingResourceWithStreamingResponse:
    def __init__(self, staking: AsyncStakingResource) -> None:
        self._staking = staking

        self.list = async_to_streamed_response_wrapper(
            staking.list,
        )
        self.retrieve_unstaking = async_to_streamed_response_wrapper(
            staking.retrieve_unstaking,
        )

    @cached_property
    def pools(self) -> AsyncPoolsResourceWithStreamingResponse:
        return AsyncPoolsResourceWithStreamingResponse(self._staking.pools)
