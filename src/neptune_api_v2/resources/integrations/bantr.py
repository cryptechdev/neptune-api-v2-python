# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.integrations import bantr_get_transactions_params
from ...types.integrations.bantr_get_transactions_response import BantrGetTransactionsResponse

__all__ = ["BantrResource", "AsyncBantrResource"]


class BantrResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BantrResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return BantrResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BantrResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return BantrResourceWithStreamingResponse(self)

    def get_transactions(
        self,
        *,
        end_block: int,
        start_block: int,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BantrGetTransactionsResponse:
        """
        .

        Args:
          end_block: End block

          start_block: Start Block

          limit: Pagination limit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/integrations/bantr/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_block": end_block,
                        "start_block": start_block,
                        "limit": limit,
                    },
                    bantr_get_transactions_params.BantrGetTransactionsParams,
                ),
            ),
            cast_to=BantrGetTransactionsResponse,
        )


class AsyncBantrResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBantrResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBantrResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBantrResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return AsyncBantrResourceWithStreamingResponse(self)

    async def get_transactions(
        self,
        *,
        end_block: int,
        start_block: int,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BantrGetTransactionsResponse:
        """
        .

        Args:
          end_block: End block

          start_block: Start Block

          limit: Pagination limit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/integrations/bantr/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_block": end_block,
                        "start_block": start_block,
                        "limit": limit,
                    },
                    bantr_get_transactions_params.BantrGetTransactionsParams,
                ),
            ),
            cast_to=BantrGetTransactionsResponse,
        )


class BantrResourceWithRawResponse:
    def __init__(self, bantr: BantrResource) -> None:
        self._bantr = bantr

        self.get_transactions = to_raw_response_wrapper(
            bantr.get_transactions,
        )


class AsyncBantrResourceWithRawResponse:
    def __init__(self, bantr: AsyncBantrResource) -> None:
        self._bantr = bantr

        self.get_transactions = async_to_raw_response_wrapper(
            bantr.get_transactions,
        )


class BantrResourceWithStreamingResponse:
    def __init__(self, bantr: BantrResource) -> None:
        self._bantr = bantr

        self.get_transactions = to_streamed_response_wrapper(
            bantr.get_transactions,
        )


class AsyncBantrResourceWithStreamingResponse:
    def __init__(self, bantr: AsyncBantrResource) -> None:
        self._bantr = bantr

        self.get_transactions = async_to_streamed_response_wrapper(
            bantr.get_transactions,
        )
