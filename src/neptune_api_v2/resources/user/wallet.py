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
from ...types.user import wallet_get_balances_params, wallet_get_balance_by_asset_params
from ..._base_client import make_request_options
from ...types.user.wallet_get_balances_response import WalletGetBalancesResponse
from ...types.user.wallet_get_balance_by_asset_response import WalletGetBalanceByAssetResponse

__all__ = ["WalletResource", "AsyncWalletResource"]


class WalletResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WalletResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return WalletResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WalletResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return WalletResourceWithStreamingResponse(self)

    def get_balance_by_asset(
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
    ) -> WalletGetBalanceByAssetResponse:
        """
        Get user balance by asset

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
            f"/api/v1/users/{address}/wallet/balance",
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
                    wallet_get_balance_by_asset_params.WalletGetBalanceByAssetParams,
                ),
            ),
            cast_to=WalletGetBalanceByAssetResponse,
        )

    def get_balances(
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
    ) -> WalletGetBalancesResponse:
        """
        Get user portfolio

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
            f"/api/v1/users/{address}/wallet/balances",
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
                    wallet_get_balances_params.WalletGetBalancesParams,
                ),
            ),
            cast_to=WalletGetBalancesResponse,
        )


class AsyncWalletResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWalletResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWalletResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWalletResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncWalletResourceWithStreamingResponse(self)

    async def get_balance_by_asset(
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
    ) -> WalletGetBalanceByAssetResponse:
        """
        Get user balance by asset

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
            f"/api/v1/users/{address}/wallet/balance",
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
                    wallet_get_balance_by_asset_params.WalletGetBalanceByAssetParams,
                ),
            ),
            cast_to=WalletGetBalanceByAssetResponse,
        )

    async def get_balances(
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
    ) -> WalletGetBalancesResponse:
        """
        Get user portfolio

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
            f"/api/v1/users/{address}/wallet/balances",
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
                    wallet_get_balances_params.WalletGetBalancesParams,
                ),
            ),
            cast_to=WalletGetBalancesResponse,
        )


class WalletResourceWithRawResponse:
    def __init__(self, wallet: WalletResource) -> None:
        self._wallet = wallet

        self.get_balance_by_asset = to_raw_response_wrapper(
            wallet.get_balance_by_asset,
        )
        self.get_balances = to_raw_response_wrapper(
            wallet.get_balances,
        )


class AsyncWalletResourceWithRawResponse:
    def __init__(self, wallet: AsyncWalletResource) -> None:
        self._wallet = wallet

        self.get_balance_by_asset = async_to_raw_response_wrapper(
            wallet.get_balance_by_asset,
        )
        self.get_balances = async_to_raw_response_wrapper(
            wallet.get_balances,
        )


class WalletResourceWithStreamingResponse:
    def __init__(self, wallet: WalletResource) -> None:
        self._wallet = wallet

        self.get_balance_by_asset = to_streamed_response_wrapper(
            wallet.get_balance_by_asset,
        )
        self.get_balances = to_streamed_response_wrapper(
            wallet.get_balances,
        )


class AsyncWalletResourceWithStreamingResponse:
    def __init__(self, wallet: AsyncWalletResource) -> None:
        self._wallet = wallet

        self.get_balance_by_asset = async_to_streamed_response_wrapper(
            wallet.get_balance_by_asset,
        )
        self.get_balances = async_to_streamed_response_wrapper(
            wallet.get_balances,
        )
