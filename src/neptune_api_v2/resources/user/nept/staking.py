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
from ....types.user.nept import (
    staking_get_overview_params,
    staking_get_unstaking_params,
    staking_get_staking_pool_params,
    staking_get_staking_pools_params,
)
from ....types.user.nept.staking_get_overview_response import StakingGetOverviewResponse
from ....types.user.nept.staking_get_unstaking_response import StakingGetUnstakingResponse
from ....types.user.nept.staking_get_staking_pool_response import StakingGetStakingPoolResponse
from ....types.user.nept.staking_get_staking_pools_response import StakingGetStakingPoolsResponse

__all__ = ["StakingResource", "AsyncStakingResource"]


class StakingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StakingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/stainless-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return StakingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StakingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/stainless-api-v2-python#with_streaming_response
        """
        return StakingResourceWithStreamingResponse(self)

    def get_overview(
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
    ) -> StakingGetOverviewResponse:
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
                    staking_get_overview_params.StakingGetOverviewParams,
                ),
            ),
            cast_to=StakingGetOverviewResponse,
        )

    def get_staking_pool(
        self,
        address: str,
        *,
        duration: int | Omit = omit,
        index: int | Omit = omit,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StakingGetStakingPoolResponse:
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
                    staking_get_staking_pool_params.StakingGetStakingPoolParams,
                ),
            ),
            cast_to=StakingGetStakingPoolResponse,
        )

    def get_staking_pools(
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
    ) -> StakingGetStakingPoolsResponse:
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
                    staking_get_staking_pools_params.StakingGetStakingPoolsParams,
                ),
            ),
            cast_to=StakingGetStakingPoolsResponse,
        )

    def get_unstaking(
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
    ) -> StakingGetUnstakingResponse:
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
                    staking_get_unstaking_params.StakingGetUnstakingParams,
                ),
            ),
            cast_to=StakingGetUnstakingResponse,
        )


class AsyncStakingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStakingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/stainless-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStakingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStakingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/stainless-api-v2-python#with_streaming_response
        """
        return AsyncStakingResourceWithStreamingResponse(self)

    async def get_overview(
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
    ) -> StakingGetOverviewResponse:
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
                    staking_get_overview_params.StakingGetOverviewParams,
                ),
            ),
            cast_to=StakingGetOverviewResponse,
        )

    async def get_staking_pool(
        self,
        address: str,
        *,
        duration: int | Omit = omit,
        index: int | Omit = omit,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StakingGetStakingPoolResponse:
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
                    staking_get_staking_pool_params.StakingGetStakingPoolParams,
                ),
            ),
            cast_to=StakingGetStakingPoolResponse,
        )

    async def get_staking_pools(
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
    ) -> StakingGetStakingPoolsResponse:
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
                    staking_get_staking_pools_params.StakingGetStakingPoolsParams,
                ),
            ),
            cast_to=StakingGetStakingPoolsResponse,
        )

    async def get_unstaking(
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
    ) -> StakingGetUnstakingResponse:
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
                    staking_get_unstaking_params.StakingGetUnstakingParams,
                ),
            ),
            cast_to=StakingGetUnstakingResponse,
        )


class StakingResourceWithRawResponse:
    def __init__(self, staking: StakingResource) -> None:
        self._staking = staking

        self.get_overview = to_raw_response_wrapper(
            staking.get_overview,
        )
        self.get_staking_pool = to_raw_response_wrapper(
            staking.get_staking_pool,
        )
        self.get_staking_pools = to_raw_response_wrapper(
            staking.get_staking_pools,
        )
        self.get_unstaking = to_raw_response_wrapper(
            staking.get_unstaking,
        )


class AsyncStakingResourceWithRawResponse:
    def __init__(self, staking: AsyncStakingResource) -> None:
        self._staking = staking

        self.get_overview = async_to_raw_response_wrapper(
            staking.get_overview,
        )
        self.get_staking_pool = async_to_raw_response_wrapper(
            staking.get_staking_pool,
        )
        self.get_staking_pools = async_to_raw_response_wrapper(
            staking.get_staking_pools,
        )
        self.get_unstaking = async_to_raw_response_wrapper(
            staking.get_unstaking,
        )


class StakingResourceWithStreamingResponse:
    def __init__(self, staking: StakingResource) -> None:
        self._staking = staking

        self.get_overview = to_streamed_response_wrapper(
            staking.get_overview,
        )
        self.get_staking_pool = to_streamed_response_wrapper(
            staking.get_staking_pool,
        )
        self.get_staking_pools = to_streamed_response_wrapper(
            staking.get_staking_pools,
        )
        self.get_unstaking = to_streamed_response_wrapper(
            staking.get_unstaking,
        )


class AsyncStakingResourceWithStreamingResponse:
    def __init__(self, staking: AsyncStakingResource) -> None:
        self._staking = staking

        self.get_overview = async_to_streamed_response_wrapper(
            staking.get_overview,
        )
        self.get_staking_pool = async_to_streamed_response_wrapper(
            staking.get_staking_pool,
        )
        self.get_staking_pools = async_to_streamed_response_wrapper(
            staking.get_staking_pools,
        )
        self.get_unstaking = async_to_streamed_response_wrapper(
            staking.get_unstaking,
        )
