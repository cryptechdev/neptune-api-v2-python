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
from ....types.markets.borrow import debt_list_params, debt_get_by_asset_params
from ....types.markets.borrow.debt_list_response import DebtListResponse
from ....types.markets.borrow.debt_get_by_asset_response import DebtGetByAssetResponse

__all__ = ["DebtsResource", "AsyncDebtsResource"]


class DebtsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DebtsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return DebtsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DebtsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return DebtsResourceWithStreamingResponse(self)

    def list(
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
    ) -> DebtListResponse:
        """
        Get borrowing debt markets

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/markets/borrow/debts",
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
                    debt_list_params.DebtListParams,
                ),
            ),
            cast_to=DebtListResponse,
        )

    def get_by_asset(
        self,
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
    ) -> DebtGetByAssetResponse:
        """
        Lookup borrowing debt market by asset

        Args:
          asset_id: Asset ID for lookup

          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/markets/borrow/debts/lookup",
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
                    debt_get_by_asset_params.DebtGetByAssetParams,
                ),
            ),
            cast_to=DebtGetByAssetResponse,
        )


class AsyncDebtsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDebtsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDebtsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDebtsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncDebtsResourceWithStreamingResponse(self)

    async def list(
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
    ) -> DebtListResponse:
        """
        Get borrowing debt markets

        Args:
          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/markets/borrow/debts",
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
                    debt_list_params.DebtListParams,
                ),
            ),
            cast_to=DebtListResponse,
        )

    async def get_by_asset(
        self,
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
    ) -> DebtGetByAssetResponse:
        """
        Lookup borrowing debt market by asset

        Args:
          asset_id: Asset ID for lookup

          with_text: Include text variation fields

          with_value: Calculate and include USD values for amounts, where applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/markets/borrow/debts/lookup",
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
                    debt_get_by_asset_params.DebtGetByAssetParams,
                ),
            ),
            cast_to=DebtGetByAssetResponse,
        )


class DebtsResourceWithRawResponse:
    def __init__(self, debts: DebtsResource) -> None:
        self._debts = debts

        self.list = to_raw_response_wrapper(
            debts.list,
        )
        self.get_by_asset = to_raw_response_wrapper(
            debts.get_by_asset,
        )


class AsyncDebtsResourceWithRawResponse:
    def __init__(self, debts: AsyncDebtsResource) -> None:
        self._debts = debts

        self.list = async_to_raw_response_wrapper(
            debts.list,
        )
        self.get_by_asset = async_to_raw_response_wrapper(
            debts.get_by_asset,
        )


class DebtsResourceWithStreamingResponse:
    def __init__(self, debts: DebtsResource) -> None:
        self._debts = debts

        self.list = to_streamed_response_wrapper(
            debts.list,
        )
        self.get_by_asset = to_streamed_response_wrapper(
            debts.get_by_asset,
        )


class AsyncDebtsResourceWithStreamingResponse:
    def __init__(self, debts: AsyncDebtsResource) -> None:
        self._debts = debts

        self.list = async_to_streamed_response_wrapper(
            debts.list,
        )
        self.get_by_asset = async_to_streamed_response_wrapper(
            debts.get_by_asset,
        )
