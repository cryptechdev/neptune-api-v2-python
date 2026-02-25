# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import nept_get_state_params, nept_get_params_params, nept_get_staking_overview_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.nept_get_state_response import NeptGetStateResponse
from ...types.v1.nept_get_params_response import NeptGetParamsResponse
from ...types.v1.nept_get_staking_overview_response import NeptGetStakingOverviewResponse

__all__ = ["NeptResource", "AsyncNeptResource"]


class NeptResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NeptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return NeptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NeptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return NeptResourceWithStreamingResponse(self)

    def get_params(
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
    ) -> NeptGetParamsResponse:
        """
        Get NEPT token params

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/nept/params",
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
                    nept_get_params_params.NeptGetParamsParams,
                ),
            ),
            cast_to=NeptGetParamsResponse,
        )

    def get_staking_overview(
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
    ) -> NeptGetStakingOverviewResponse:
        """Get NEPT staking overview (incl.

        state + params)

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/nept/staking",
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
                    nept_get_staking_overview_params.NeptGetStakingOverviewParams,
                ),
            ),
            cast_to=NeptGetStakingOverviewResponse,
        )

    def get_state(
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
    ) -> NeptGetStateResponse:
        """
        Get NEPT token state

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/nept/state",
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
                    nept_get_state_params.NeptGetStateParams,
                ),
            ),
            cast_to=NeptGetStateResponse,
        )


class AsyncNeptResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNeptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNeptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNeptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncNeptResourceWithStreamingResponse(self)

    async def get_params(
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
    ) -> NeptGetParamsResponse:
        """
        Get NEPT token params

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/nept/params",
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
                    nept_get_params_params.NeptGetParamsParams,
                ),
            ),
            cast_to=NeptGetParamsResponse,
        )

    async def get_staking_overview(
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
    ) -> NeptGetStakingOverviewResponse:
        """Get NEPT staking overview (incl.

        state + params)

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/nept/staking",
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
                    nept_get_staking_overview_params.NeptGetStakingOverviewParams,
                ),
            ),
            cast_to=NeptGetStakingOverviewResponse,
        )

    async def get_state(
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
    ) -> NeptGetStateResponse:
        """
        Get NEPT token state

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/nept/state",
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
                    nept_get_state_params.NeptGetStateParams,
                ),
            ),
            cast_to=NeptGetStateResponse,
        )


class NeptResourceWithRawResponse:
    def __init__(self, nept: NeptResource) -> None:
        self._nept = nept

        self.get_params = to_raw_response_wrapper(
            nept.get_params,
        )
        self.get_staking_overview = to_raw_response_wrapper(
            nept.get_staking_overview,
        )
        self.get_state = to_raw_response_wrapper(
            nept.get_state,
        )


class AsyncNeptResourceWithRawResponse:
    def __init__(self, nept: AsyncNeptResource) -> None:
        self._nept = nept

        self.get_params = async_to_raw_response_wrapper(
            nept.get_params,
        )
        self.get_staking_overview = async_to_raw_response_wrapper(
            nept.get_staking_overview,
        )
        self.get_state = async_to_raw_response_wrapper(
            nept.get_state,
        )


class NeptResourceWithStreamingResponse:
    def __init__(self, nept: NeptResource) -> None:
        self._nept = nept

        self.get_params = to_streamed_response_wrapper(
            nept.get_params,
        )
        self.get_staking_overview = to_streamed_response_wrapper(
            nept.get_staking_overview,
        )
        self.get_state = to_streamed_response_wrapper(
            nept.get_state,
        )


class AsyncNeptResourceWithStreamingResponse:
    def __init__(self, nept: AsyncNeptResource) -> None:
        self._nept = nept

        self.get_params = async_to_streamed_response_wrapper(
            nept.get_params,
        )
        self.get_staking_overview = async_to_streamed_response_wrapper(
            nept.get_staking_overview,
        )
        self.get_state = async_to_streamed_response_wrapper(
            nept.get_state,
        )
