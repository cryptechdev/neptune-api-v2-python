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
from ......types.v1.users.markets.borrow import lookup_get_debt_accounts_params, lookup_get_collateral_accounts_params
from ......types.v1.users.markets.borrow.lookup_get_debt_accounts_response import LookupGetDebtAccountsResponse
from ......types.v1.users.markets.borrow.lookup_get_collateral_accounts_response import (
    LookupGetCollateralAccountsResponse,
)

__all__ = ["LookupResource", "AsyncLookupResource"]


class LookupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return LookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return LookupResourceWithStreamingResponse(self)

    def get_collateral_accounts(
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
    ) -> LookupGetCollateralAccountsResponse:
        """
        Lookup user borrow market collateral accounts by asset

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
            f"/api/v1/users/{address}/markets/borrow/lookup/collateral",
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
                    lookup_get_collateral_accounts_params.LookupGetCollateralAccountsParams,
                ),
            ),
            cast_to=LookupGetCollateralAccountsResponse,
        )

    def get_debt_accounts(
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
    ) -> LookupGetDebtAccountsResponse:
        """
        Lookup user borrow market debt by accounts by asset

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
            f"/api/v1/users/{address}/markets/borrow/lookup/debt",
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
                    lookup_get_debt_accounts_params.LookupGetDebtAccountsParams,
                ),
            ),
            cast_to=LookupGetDebtAccountsResponse,
        )


class AsyncLookupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncLookupResourceWithStreamingResponse(self)

    async def get_collateral_accounts(
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
    ) -> LookupGetCollateralAccountsResponse:
        """
        Lookup user borrow market collateral accounts by asset

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
            f"/api/v1/users/{address}/markets/borrow/lookup/collateral",
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
                    lookup_get_collateral_accounts_params.LookupGetCollateralAccountsParams,
                ),
            ),
            cast_to=LookupGetCollateralAccountsResponse,
        )

    async def get_debt_accounts(
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
    ) -> LookupGetDebtAccountsResponse:
        """
        Lookup user borrow market debt by accounts by asset

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
            f"/api/v1/users/{address}/markets/borrow/lookup/debt",
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
                    lookup_get_debt_accounts_params.LookupGetDebtAccountsParams,
                ),
            ),
            cast_to=LookupGetDebtAccountsResponse,
        )


class LookupResourceWithRawResponse:
    def __init__(self, lookup: LookupResource) -> None:
        self._lookup = lookup

        self.get_collateral_accounts = to_raw_response_wrapper(
            lookup.get_collateral_accounts,
        )
        self.get_debt_accounts = to_raw_response_wrapper(
            lookup.get_debt_accounts,
        )


class AsyncLookupResourceWithRawResponse:
    def __init__(self, lookup: AsyncLookupResource) -> None:
        self._lookup = lookup

        self.get_collateral_accounts = async_to_raw_response_wrapper(
            lookup.get_collateral_accounts,
        )
        self.get_debt_accounts = async_to_raw_response_wrapper(
            lookup.get_debt_accounts,
        )


class LookupResourceWithStreamingResponse:
    def __init__(self, lookup: LookupResource) -> None:
        self._lookup = lookup

        self.get_collateral_accounts = to_streamed_response_wrapper(
            lookup.get_collateral_accounts,
        )
        self.get_debt_accounts = to_streamed_response_wrapper(
            lookup.get_debt_accounts,
        )


class AsyncLookupResourceWithStreamingResponse:
    def __init__(self, lookup: AsyncLookupResource) -> None:
        self._lookup = lookup

        self.get_collateral_accounts = async_to_streamed_response_wrapper(
            lookup.get_collateral_accounts,
        )
        self.get_debt_accounts = async_to_streamed_response_wrapper(
            lookup.get_debt_accounts,
        )
