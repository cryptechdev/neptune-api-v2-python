# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .sum import (
    SumResource,
    AsyncSumResource,
    SumResourceWithRawResponse,
    AsyncSumResourceWithRawResponse,
    SumResourceWithStreamingResponse,
    AsyncSumResourceWithStreamingResponse,
)
from .lookup import (
    LookupResource,
    AsyncLookupResource,
    LookupResourceWithRawResponse,
    AsyncLookupResourceWithRawResponse,
    LookupResourceWithStreamingResponse,
    AsyncLookupResourceWithStreamingResponse,
)
from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
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
from ......types.v1.users.markets import borrow_get_portfolio_params
from ......types.v1.users.markets.borrow_get_portfolio_response import BorrowGetPortfolioResponse

__all__ = ["BorrowResource", "AsyncBorrowResource"]


class BorrowResource(SyncAPIResource):
    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def sum(self) -> SumResource:
        return SumResource(self._client)

    @cached_property
    def lookup(self) -> LookupResource:
        return LookupResource(self._client)

    @cached_property
    def with_raw_response(self) -> BorrowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return BorrowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BorrowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return BorrowResourceWithStreamingResponse(self)

    def get_portfolio(
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
    ) -> BorrowGetPortfolioResponse:
        """
        Get user borrow portfolio

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
            f"/api/v1/users/{address}/markets/borrow",
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
                    borrow_get_portfolio_params.BorrowGetPortfolioParams,
                ),
            ),
            cast_to=BorrowGetPortfolioResponse,
        )


class AsyncBorrowResource(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        return AsyncAccountsResource(self._client)

    @cached_property
    def sum(self) -> AsyncSumResource:
        return AsyncSumResource(self._client)

    @cached_property
    def lookup(self) -> AsyncLookupResource:
        return AsyncLookupResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBorrowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBorrowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBorrowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncBorrowResourceWithStreamingResponse(self)

    async def get_portfolio(
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
    ) -> BorrowGetPortfolioResponse:
        """
        Get user borrow portfolio

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
            f"/api/v1/users/{address}/markets/borrow",
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
                    borrow_get_portfolio_params.BorrowGetPortfolioParams,
                ),
            ),
            cast_to=BorrowGetPortfolioResponse,
        )


class BorrowResourceWithRawResponse:
    def __init__(self, borrow: BorrowResource) -> None:
        self._borrow = borrow

        self.get_portfolio = to_raw_response_wrapper(
            borrow.get_portfolio,
        )

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self._borrow.accounts)

    @cached_property
    def sum(self) -> SumResourceWithRawResponse:
        return SumResourceWithRawResponse(self._borrow.sum)

    @cached_property
    def lookup(self) -> LookupResourceWithRawResponse:
        return LookupResourceWithRawResponse(self._borrow.lookup)


class AsyncBorrowResourceWithRawResponse:
    def __init__(self, borrow: AsyncBorrowResource) -> None:
        self._borrow = borrow

        self.get_portfolio = async_to_raw_response_wrapper(
            borrow.get_portfolio,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self._borrow.accounts)

    @cached_property
    def sum(self) -> AsyncSumResourceWithRawResponse:
        return AsyncSumResourceWithRawResponse(self._borrow.sum)

    @cached_property
    def lookup(self) -> AsyncLookupResourceWithRawResponse:
        return AsyncLookupResourceWithRawResponse(self._borrow.lookup)


class BorrowResourceWithStreamingResponse:
    def __init__(self, borrow: BorrowResource) -> None:
        self._borrow = borrow

        self.get_portfolio = to_streamed_response_wrapper(
            borrow.get_portfolio,
        )

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self._borrow.accounts)

    @cached_property
    def sum(self) -> SumResourceWithStreamingResponse:
        return SumResourceWithStreamingResponse(self._borrow.sum)

    @cached_property
    def lookup(self) -> LookupResourceWithStreamingResponse:
        return LookupResourceWithStreamingResponse(self._borrow.lookup)


class AsyncBorrowResourceWithStreamingResponse:
    def __init__(self, borrow: AsyncBorrowResource) -> None:
        self._borrow = borrow

        self.get_portfolio = async_to_streamed_response_wrapper(
            borrow.get_portfolio,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self._borrow.accounts)

    @cached_property
    def sum(self) -> AsyncSumResourceWithStreamingResponse:
        return AsyncSumResourceWithStreamingResponse(self._borrow.sum)

    @cached_property
    def lookup(self) -> AsyncLookupResourceWithStreamingResponse:
        return AsyncLookupResourceWithStreamingResponse(self._borrow.lookup)
