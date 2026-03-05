# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from .subaccount import (
    SubaccountResource,
    AsyncSubaccountResource,
    SubaccountResourceWithRawResponse,
    AsyncSubaccountResourceWithRawResponse,
    SubaccountResourceWithStreamingResponse,
    AsyncSubaccountResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.user.market import (
    borrow_get_portfolio_params,
    borrow_get_debts_totals_params,
    borrow_get_collateral_totals_params,
    borrow_get_debt_accounts_by_asset_params,
    borrow_get_collateral_accounts_by_asset_params,
)
from .....types.user.market.borrow_get_portfolio_response import BorrowGetPortfolioResponse
from .....types.user.market.borrow_get_debts_totals_response import BorrowGetDebtsTotalsResponse
from .....types.user.market.borrow_get_collateral_totals_response import BorrowGetCollateralTotalsResponse
from .....types.user.market.borrow_get_debt_accounts_by_asset_response import BorrowGetDebtAccountsByAssetResponse
from .....types.user.market.borrow_get_collateral_accounts_by_asset_response import (
    BorrowGetCollateralAccountsByAssetResponse,
)

__all__ = ["BorrowResource", "AsyncBorrowResource"]


class BorrowResource(SyncAPIResource):
    @cached_property
    def subaccount(self) -> SubaccountResource:
        return SubaccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> BorrowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return BorrowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BorrowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return BorrowResourceWithStreamingResponse(self)

    def get_collateral_accounts_by_asset(
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
    ) -> BorrowGetCollateralAccountsByAssetResponse:
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
                    borrow_get_collateral_accounts_by_asset_params.BorrowGetCollateralAccountsByAssetParams,
                ),
            ),
            cast_to=BorrowGetCollateralAccountsByAssetResponse,
        )

    def get_collateral_totals(
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
    ) -> BorrowGetCollateralTotalsResponse:
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
                    borrow_get_collateral_totals_params.BorrowGetCollateralTotalsParams,
                ),
            ),
            cast_to=BorrowGetCollateralTotalsResponse,
        )

    def get_debt_accounts_by_asset(
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
    ) -> BorrowGetDebtAccountsByAssetResponse:
        """
        Lookup user borrow market debt accounts by asset

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
                    borrow_get_debt_accounts_by_asset_params.BorrowGetDebtAccountsByAssetParams,
                ),
            ),
            cast_to=BorrowGetDebtAccountsByAssetResponse,
        )

    def get_debts_totals(
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
    ) -> BorrowGetDebtsTotalsResponse:
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
                    borrow_get_debts_totals_params.BorrowGetDebtsTotalsParams,
                ),
            ),
            cast_to=BorrowGetDebtsTotalsResponse,
        )

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
    def subaccount(self) -> AsyncSubaccountResource:
        return AsyncSubaccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBorrowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBorrowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBorrowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return AsyncBorrowResourceWithStreamingResponse(self)

    async def get_collateral_accounts_by_asset(
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
    ) -> BorrowGetCollateralAccountsByAssetResponse:
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
                    borrow_get_collateral_accounts_by_asset_params.BorrowGetCollateralAccountsByAssetParams,
                ),
            ),
            cast_to=BorrowGetCollateralAccountsByAssetResponse,
        )

    async def get_collateral_totals(
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
    ) -> BorrowGetCollateralTotalsResponse:
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
                    borrow_get_collateral_totals_params.BorrowGetCollateralTotalsParams,
                ),
            ),
            cast_to=BorrowGetCollateralTotalsResponse,
        )

    async def get_debt_accounts_by_asset(
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
    ) -> BorrowGetDebtAccountsByAssetResponse:
        """
        Lookup user borrow market debt accounts by asset

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
                    borrow_get_debt_accounts_by_asset_params.BorrowGetDebtAccountsByAssetParams,
                ),
            ),
            cast_to=BorrowGetDebtAccountsByAssetResponse,
        )

    async def get_debts_totals(
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
    ) -> BorrowGetDebtsTotalsResponse:
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
                    borrow_get_debts_totals_params.BorrowGetDebtsTotalsParams,
                ),
            ),
            cast_to=BorrowGetDebtsTotalsResponse,
        )

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

        self.get_collateral_accounts_by_asset = to_raw_response_wrapper(
            borrow.get_collateral_accounts_by_asset,
        )
        self.get_collateral_totals = to_raw_response_wrapper(
            borrow.get_collateral_totals,
        )
        self.get_debt_accounts_by_asset = to_raw_response_wrapper(
            borrow.get_debt_accounts_by_asset,
        )
        self.get_debts_totals = to_raw_response_wrapper(
            borrow.get_debts_totals,
        )
        self.get_portfolio = to_raw_response_wrapper(
            borrow.get_portfolio,
        )

    @cached_property
    def subaccount(self) -> SubaccountResourceWithRawResponse:
        return SubaccountResourceWithRawResponse(self._borrow.subaccount)


class AsyncBorrowResourceWithRawResponse:
    def __init__(self, borrow: AsyncBorrowResource) -> None:
        self._borrow = borrow

        self.get_collateral_accounts_by_asset = async_to_raw_response_wrapper(
            borrow.get_collateral_accounts_by_asset,
        )
        self.get_collateral_totals = async_to_raw_response_wrapper(
            borrow.get_collateral_totals,
        )
        self.get_debt_accounts_by_asset = async_to_raw_response_wrapper(
            borrow.get_debt_accounts_by_asset,
        )
        self.get_debts_totals = async_to_raw_response_wrapper(
            borrow.get_debts_totals,
        )
        self.get_portfolio = async_to_raw_response_wrapper(
            borrow.get_portfolio,
        )

    @cached_property
    def subaccount(self) -> AsyncSubaccountResourceWithRawResponse:
        return AsyncSubaccountResourceWithRawResponse(self._borrow.subaccount)


class BorrowResourceWithStreamingResponse:
    def __init__(self, borrow: BorrowResource) -> None:
        self._borrow = borrow

        self.get_collateral_accounts_by_asset = to_streamed_response_wrapper(
            borrow.get_collateral_accounts_by_asset,
        )
        self.get_collateral_totals = to_streamed_response_wrapper(
            borrow.get_collateral_totals,
        )
        self.get_debt_accounts_by_asset = to_streamed_response_wrapper(
            borrow.get_debt_accounts_by_asset,
        )
        self.get_debts_totals = to_streamed_response_wrapper(
            borrow.get_debts_totals,
        )
        self.get_portfolio = to_streamed_response_wrapper(
            borrow.get_portfolio,
        )

    @cached_property
    def subaccount(self) -> SubaccountResourceWithStreamingResponse:
        return SubaccountResourceWithStreamingResponse(self._borrow.subaccount)


class AsyncBorrowResourceWithStreamingResponse:
    def __init__(self, borrow: AsyncBorrowResource) -> None:
        self._borrow = borrow

        self.get_collateral_accounts_by_asset = async_to_streamed_response_wrapper(
            borrow.get_collateral_accounts_by_asset,
        )
        self.get_collateral_totals = async_to_streamed_response_wrapper(
            borrow.get_collateral_totals,
        )
        self.get_debt_accounts_by_asset = async_to_streamed_response_wrapper(
            borrow.get_debt_accounts_by_asset,
        )
        self.get_debts_totals = async_to_streamed_response_wrapper(
            borrow.get_debts_totals,
        )
        self.get_portfolio = async_to_streamed_response_wrapper(
            borrow.get_portfolio,
        )

    @cached_property
    def subaccount(self) -> AsyncSubaccountResourceWithStreamingResponse:
        return AsyncSubaccountResourceWithStreamingResponse(self._borrow.subaccount)
