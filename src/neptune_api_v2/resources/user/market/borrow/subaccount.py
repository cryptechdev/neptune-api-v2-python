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
from .....types.user.market.borrow import (
    subaccount_get_subaccount_params,
    subaccount_get_subaccount_debts_params,
    subaccount_get_subaccount_health_params,
    subaccount_get_subaccount_collaterals_params,
)
from .....types.user.market.borrow.subaccount_get_subaccount_response import SubaccountGetSubaccountResponse
from .....types.user.market.borrow.subaccount_get_subaccount_debts_response import SubaccountGetSubaccountDebtsResponse
from .....types.user.market.borrow.subaccount_get_subaccount_health_response import (
    SubaccountGetSubaccountHealthResponse,
)
from .....types.user.market.borrow.subaccount_get_subaccount_collaterals_response import (
    SubaccountGetSubaccountCollateralsResponse,
)

__all__ = ["SubaccountResource", "AsyncSubaccountResource"]


class SubaccountResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubaccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return SubaccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubaccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return SubaccountResourceWithStreamingResponse(self)

    def get_subaccount(
        self,
        index: int,
        *,
        address: str,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubaccountGetSubaccountResponse:
        """
        Get user borrow subaccount

        Args:
          address: The user account address

          index: The user account index

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
            f"/api/v1/users/{address}/markets/borrow/accounts/{index}",
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
                    subaccount_get_subaccount_params.SubaccountGetSubaccountParams,
                ),
            ),
            cast_to=SubaccountGetSubaccountResponse,
        )

    def get_subaccount_collaterals(
        self,
        index: int,
        *,
        address: str,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubaccountGetSubaccountCollateralsResponse:
        """
        Get user borrow subaccount collaterals

        Args:
          address: The user account address

          index: The user account index

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
            f"/api/v1/users/{address}/markets/borrow/accounts/{index}/collaterals",
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
                    subaccount_get_subaccount_collaterals_params.SubaccountGetSubaccountCollateralsParams,
                ),
            ),
            cast_to=SubaccountGetSubaccountCollateralsResponse,
        )

    def get_subaccount_debts(
        self,
        index: int,
        *,
        address: str,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubaccountGetSubaccountDebtsResponse:
        """
        Get user borrow subaccount debts

        Args:
          address: The user account address

          index: The user account index

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
            f"/api/v1/users/{address}/markets/borrow/accounts/{index}/debts",
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
                    subaccount_get_subaccount_debts_params.SubaccountGetSubaccountDebtsParams,
                ),
            ),
            cast_to=SubaccountGetSubaccountDebtsResponse,
        )

    def get_subaccount_health(
        self,
        index: int,
        *,
        address: str,
        with_text: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubaccountGetSubaccountHealthResponse:
        """
        Get user borrow subaccount health

        Args:
          address: The user account address

          index: The user account index

          with_text: Include text variation fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return self._get(
            f"/api/v1/users/{address}/markets/borrow/accounts/{index}/health",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"with_text": with_text},
                    subaccount_get_subaccount_health_params.SubaccountGetSubaccountHealthParams,
                ),
            ),
            cast_to=SubaccountGetSubaccountHealthResponse,
        )


class AsyncSubaccountResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubaccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubaccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubaccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return AsyncSubaccountResourceWithStreamingResponse(self)

    async def get_subaccount(
        self,
        index: int,
        *,
        address: str,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubaccountGetSubaccountResponse:
        """
        Get user borrow subaccount

        Args:
          address: The user account address

          index: The user account index

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
            f"/api/v1/users/{address}/markets/borrow/accounts/{index}",
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
                    subaccount_get_subaccount_params.SubaccountGetSubaccountParams,
                ),
            ),
            cast_to=SubaccountGetSubaccountResponse,
        )

    async def get_subaccount_collaterals(
        self,
        index: int,
        *,
        address: str,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubaccountGetSubaccountCollateralsResponse:
        """
        Get user borrow subaccount collaterals

        Args:
          address: The user account address

          index: The user account index

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
            f"/api/v1/users/{address}/markets/borrow/accounts/{index}/collaterals",
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
                    subaccount_get_subaccount_collaterals_params.SubaccountGetSubaccountCollateralsParams,
                ),
            ),
            cast_to=SubaccountGetSubaccountCollateralsResponse,
        )

    async def get_subaccount_debts(
        self,
        index: int,
        *,
        address: str,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubaccountGetSubaccountDebtsResponse:
        """
        Get user borrow subaccount debts

        Args:
          address: The user account address

          index: The user account index

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
            f"/api/v1/users/{address}/markets/borrow/accounts/{index}/debts",
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
                    subaccount_get_subaccount_debts_params.SubaccountGetSubaccountDebtsParams,
                ),
            ),
            cast_to=SubaccountGetSubaccountDebtsResponse,
        )

    async def get_subaccount_health(
        self,
        index: int,
        *,
        address: str,
        with_text: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubaccountGetSubaccountHealthResponse:
        """
        Get user borrow subaccount health

        Args:
          address: The user account address

          index: The user account index

          with_text: Include text variation fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        return await self._get(
            f"/api/v1/users/{address}/markets/borrow/accounts/{index}/health",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"with_text": with_text},
                    subaccount_get_subaccount_health_params.SubaccountGetSubaccountHealthParams,
                ),
            ),
            cast_to=SubaccountGetSubaccountHealthResponse,
        )


class SubaccountResourceWithRawResponse:
    def __init__(self, subaccount: SubaccountResource) -> None:
        self._subaccount = subaccount

        self.get_subaccount = to_raw_response_wrapper(
            subaccount.get_subaccount,
        )
        self.get_subaccount_collaterals = to_raw_response_wrapper(
            subaccount.get_subaccount_collaterals,
        )
        self.get_subaccount_debts = to_raw_response_wrapper(
            subaccount.get_subaccount_debts,
        )
        self.get_subaccount_health = to_raw_response_wrapper(
            subaccount.get_subaccount_health,
        )


class AsyncSubaccountResourceWithRawResponse:
    def __init__(self, subaccount: AsyncSubaccountResource) -> None:
        self._subaccount = subaccount

        self.get_subaccount = async_to_raw_response_wrapper(
            subaccount.get_subaccount,
        )
        self.get_subaccount_collaterals = async_to_raw_response_wrapper(
            subaccount.get_subaccount_collaterals,
        )
        self.get_subaccount_debts = async_to_raw_response_wrapper(
            subaccount.get_subaccount_debts,
        )
        self.get_subaccount_health = async_to_raw_response_wrapper(
            subaccount.get_subaccount_health,
        )


class SubaccountResourceWithStreamingResponse:
    def __init__(self, subaccount: SubaccountResource) -> None:
        self._subaccount = subaccount

        self.get_subaccount = to_streamed_response_wrapper(
            subaccount.get_subaccount,
        )
        self.get_subaccount_collaterals = to_streamed_response_wrapper(
            subaccount.get_subaccount_collaterals,
        )
        self.get_subaccount_debts = to_streamed_response_wrapper(
            subaccount.get_subaccount_debts,
        )
        self.get_subaccount_health = to_streamed_response_wrapper(
            subaccount.get_subaccount_health,
        )


class AsyncSubaccountResourceWithStreamingResponse:
    def __init__(self, subaccount: AsyncSubaccountResource) -> None:
        self._subaccount = subaccount

        self.get_subaccount = async_to_streamed_response_wrapper(
            subaccount.get_subaccount,
        )
        self.get_subaccount_collaterals = async_to_streamed_response_wrapper(
            subaccount.get_subaccount_collaterals,
        )
        self.get_subaccount_debts = async_to_streamed_response_wrapper(
            subaccount.get_subaccount_debts,
        )
        self.get_subaccount_health = async_to_streamed_response_wrapper(
            subaccount.get_subaccount_health,
        )
