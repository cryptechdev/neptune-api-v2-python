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
from ......types.v1.users.markets.borrow import sum_retrieve_debts_params, sum_retrieve_collaterals_params
from ......types.v1.users.markets.borrow.sum_retrieve_debts_response import SumRetrieveDebtsResponse
from ......types.v1.users.markets.borrow.sum_retrieve_collaterals_response import SumRetrieveCollateralsResponse

__all__ = ["SumResource", "AsyncSumResource"]


class SumResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SumResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return SumResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SumResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return SumResourceWithStreamingResponse(self)

    def retrieve_collaterals(
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
    ) -> SumRetrieveCollateralsResponse:
        """
        Get user combined collaterals for all subaccounts

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
            f"/api/v1/users/{address}/markets/borrow/sum/collaterals",
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
                    sum_retrieve_collaterals_params.SumRetrieveCollateralsParams,
                ),
            ),
            cast_to=SumRetrieveCollateralsResponse,
        )

    def retrieve_debts(
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
    ) -> SumRetrieveDebtsResponse:
        """
        Get user combined debts for all subaccounts

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
            f"/api/v1/users/{address}/markets/borrow/sum/debts",
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
                    sum_retrieve_debts_params.SumRetrieveDebtsParams,
                ),
            ),
            cast_to=SumRetrieveDebtsResponse,
        )


class AsyncSumResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSumResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSumResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSumResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncSumResourceWithStreamingResponse(self)

    async def retrieve_collaterals(
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
    ) -> SumRetrieveCollateralsResponse:
        """
        Get user combined collaterals for all subaccounts

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
            f"/api/v1/users/{address}/markets/borrow/sum/collaterals",
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
                    sum_retrieve_collaterals_params.SumRetrieveCollateralsParams,
                ),
            ),
            cast_to=SumRetrieveCollateralsResponse,
        )

    async def retrieve_debts(
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
    ) -> SumRetrieveDebtsResponse:
        """
        Get user combined debts for all subaccounts

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
            f"/api/v1/users/{address}/markets/borrow/sum/debts",
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
                    sum_retrieve_debts_params.SumRetrieveDebtsParams,
                ),
            ),
            cast_to=SumRetrieveDebtsResponse,
        )


class SumResourceWithRawResponse:
    def __init__(self, sum: SumResource) -> None:
        self._sum = sum

        self.retrieve_collaterals = to_raw_response_wrapper(
            sum.retrieve_collaterals,
        )
        self.retrieve_debts = to_raw_response_wrapper(
            sum.retrieve_debts,
        )


class AsyncSumResourceWithRawResponse:
    def __init__(self, sum: AsyncSumResource) -> None:
        self._sum = sum

        self.retrieve_collaterals = async_to_raw_response_wrapper(
            sum.retrieve_collaterals,
        )
        self.retrieve_debts = async_to_raw_response_wrapper(
            sum.retrieve_debts,
        )


class SumResourceWithStreamingResponse:
    def __init__(self, sum: SumResource) -> None:
        self._sum = sum

        self.retrieve_collaterals = to_streamed_response_wrapper(
            sum.retrieve_collaterals,
        )
        self.retrieve_debts = to_streamed_response_wrapper(
            sum.retrieve_debts,
        )


class AsyncSumResourceWithStreamingResponse:
    def __init__(self, sum: AsyncSumResource) -> None:
        self._sum = sum

        self.retrieve_collaterals = async_to_streamed_response_wrapper(
            sum.retrieve_collaterals,
        )
        self.retrieve_debts = async_to_streamed_response_wrapper(
            sum.retrieve_debts,
        )
