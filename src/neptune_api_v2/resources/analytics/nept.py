# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.analytics import nept_unlocks_distribution_params
from ...types.analytics.nept_unlocks_distribution_response import NeptUnlocksDistributionResponse

__all__ = ["NeptResource", "AsyncNeptResource"]


class NeptResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NeptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return NeptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NeptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return NeptResourceWithStreamingResponse(self)

    def unlocks_distribution(
        self,
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
    ) -> NeptUnlocksDistributionResponse:
        """
        Get distribution analytics for NEPT unlocks

        Args:
          with_percent: Calculate and include proportional percentages, where applicable

          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/analytics/nept/unlocks-distribution",
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
                    nept_unlocks_distribution_params.NeptUnlocksDistributionParams,
                ),
            ),
            cast_to=NeptUnlocksDistributionResponse,
        )


class AsyncNeptResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNeptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNeptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNeptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return AsyncNeptResourceWithStreamingResponse(self)

    async def unlocks_distribution(
        self,
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
    ) -> NeptUnlocksDistributionResponse:
        """
        Get distribution analytics for NEPT unlocks

        Args:
          with_percent: Calculate and include proportional percentages, where applicable

          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/analytics/nept/unlocks-distribution",
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
                    nept_unlocks_distribution_params.NeptUnlocksDistributionParams,
                ),
            ),
            cast_to=NeptUnlocksDistributionResponse,
        )


class NeptResourceWithRawResponse:
    def __init__(self, nept: NeptResource) -> None:
        self._nept = nept

        self.unlocks_distribution = to_raw_response_wrapper(
            nept.unlocks_distribution,
        )


class AsyncNeptResourceWithRawResponse:
    def __init__(self, nept: AsyncNeptResource) -> None:
        self._nept = nept

        self.unlocks_distribution = async_to_raw_response_wrapper(
            nept.unlocks_distribution,
        )


class NeptResourceWithStreamingResponse:
    def __init__(self, nept: NeptResource) -> None:
        self._nept = nept

        self.unlocks_distribution = to_streamed_response_wrapper(
            nept.unlocks_distribution,
        )


class AsyncNeptResourceWithStreamingResponse:
    def __init__(self, nept: AsyncNeptResource) -> None:
        self._nept = nept

        self.unlocks_distribution = async_to_streamed_response_wrapper(
            nept.unlocks_distribution,
        )
