# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .staking import (
    StakingResource,
    AsyncStakingResource,
    StakingResourceWithRawResponse,
    AsyncStakingResourceWithRawResponse,
    StakingResourceWithStreamingResponse,
    AsyncStakingResourceWithStreamingResponse,
)
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
from ....types.user import nept_get_unlocks_params
from ...._base_client import make_request_options
from ....types.user.nept_get_unlocks_response import NeptGetUnlocksResponse

__all__ = ["NeptResource", "AsyncNeptResource"]


class NeptResource(SyncAPIResource):
    @cached_property
    def staking(self) -> StakingResource:
        return StakingResource(self._client)

    @cached_property
    def with_raw_response(self) -> NeptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/stainless-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return NeptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NeptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/stainless-api-v2-python#with_streaming_response
        """
        return NeptResourceWithStreamingResponse(self)

    def get_unlocks(
        self,
        address: str,
        *,
        with_percent: bool | Omit = omit,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NeptGetUnlocksResponse:
        """
        Get user NEPT unlocks

        Args:
          address: The user account address

          with_percent: Calculate and include proportional percentages, where applicable

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
            f"/api/v1/users/{address}/nept/unlocks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "with_percent": with_percent,
                        "with_text": with_text,
                        "with_value": with_value,
                    },
                    nept_get_unlocks_params.NeptGetUnlocksParams,
                ),
            ),
            cast_to=NeptGetUnlocksResponse,
        )


class AsyncNeptResource(AsyncAPIResource):
    @cached_property
    def staking(self) -> AsyncStakingResource:
        return AsyncStakingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNeptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/stainless-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNeptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNeptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/stainless-api-v2-python#with_streaming_response
        """
        return AsyncNeptResourceWithStreamingResponse(self)

    async def get_unlocks(
        self,
        address: str,
        *,
        with_percent: bool | Omit = omit,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NeptGetUnlocksResponse:
        """
        Get user NEPT unlocks

        Args:
          address: The user account address

          with_percent: Calculate and include proportional percentages, where applicable

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
            f"/api/v1/users/{address}/nept/unlocks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "with_percent": with_percent,
                        "with_text": with_text,
                        "with_value": with_value,
                    },
                    nept_get_unlocks_params.NeptGetUnlocksParams,
                ),
            ),
            cast_to=NeptGetUnlocksResponse,
        )


class NeptResourceWithRawResponse:
    def __init__(self, nept: NeptResource) -> None:
        self._nept = nept

        self.get_unlocks = to_raw_response_wrapper(
            nept.get_unlocks,
        )

    @cached_property
    def staking(self) -> StakingResourceWithRawResponse:
        return StakingResourceWithRawResponse(self._nept.staking)


class AsyncNeptResourceWithRawResponse:
    def __init__(self, nept: AsyncNeptResource) -> None:
        self._nept = nept

        self.get_unlocks = async_to_raw_response_wrapper(
            nept.get_unlocks,
        )

    @cached_property
    def staking(self) -> AsyncStakingResourceWithRawResponse:
        return AsyncStakingResourceWithRawResponse(self._nept.staking)


class NeptResourceWithStreamingResponse:
    def __init__(self, nept: NeptResource) -> None:
        self._nept = nept

        self.get_unlocks = to_streamed_response_wrapper(
            nept.get_unlocks,
        )

    @cached_property
    def staking(self) -> StakingResourceWithStreamingResponse:
        return StakingResourceWithStreamingResponse(self._nept.staking)


class AsyncNeptResourceWithStreamingResponse:
    def __init__(self, nept: AsyncNeptResource) -> None:
        self._nept = nept

        self.get_unlocks = async_to_streamed_response_wrapper(
            nept.get_unlocks,
        )

    @cached_property
    def staking(self) -> AsyncStakingResourceWithStreamingResponse:
        return AsyncStakingResourceWithStreamingResponse(self._nept.staking)
