# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .wallet import (
    WalletResource,
    AsyncWalletResource,
    WalletResourceWithRawResponse,
    AsyncWalletResourceWithRawResponse,
    WalletResourceWithStreamingResponse,
    AsyncWalletResourceWithStreamingResponse,
)
from ...types import EventAction, user_get_user_params, user_get_tx_history_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .nept.nept import (
    NeptResource,
    AsyncNeptResource,
    NeptResourceWithRawResponse,
    AsyncNeptResourceWithRawResponse,
    NeptResourceWithStreamingResponse,
    AsyncNeptResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .market.market import (
    MarketResource,
    AsyncMarketResource,
    MarketResourceWithRawResponse,
    AsyncMarketResourceWithRawResponse,
    MarketResourceWithStreamingResponse,
    AsyncMarketResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.event_action import EventAction
from ...types.user_get_user_response import UserGetUserResponse
from ...types.user_get_tx_history_response import UserGetTxHistoryResponse

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def market(self) -> MarketResource:
        return MarketResource(self._client)

    @cached_property
    def nept(self) -> NeptResource:
        return NeptResource(self._client)

    @cached_property
    def wallet(self) -> WalletResource:
        return WalletResource(self._client)

    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return UserResourceWithStreamingResponse(self)

    def get_tx_history(
        self,
        address: str,
        *,
        action: Optional[EventAction] | Omit = omit,
        limit: int | Omit = omit,
        prev_event_uuid: Optional[str] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetTxHistoryResponse:
        """
        Get user tx history

        Args:
          address: The user account address

          action: Optional event/tx action to filter against

          limit: Maximum number of transactions to return.

              Optional and defaults to `20` if missing.

          prev_event_uuid: Optional UUID skip parameter used for pagination.

              Providing the last event UUID on a given page will return the next page
              beginning with the following (unseen) item.

          sort_order: Changes the sort order for the returned txs.

              Transactions are always sorted by event time, however the direction (e.g. newest
              to oldest) can be changed using this parameter.

              Optional and defaults to `desc` if missing.

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
            path_template("/api/v1/users/{address}/tx-history", address=address),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "limit": limit,
                        "prev_event_uuid": prev_event_uuid,
                        "sort_order": sort_order,
                        "with_text": with_text,
                        "with_value": with_value,
                    },
                    user_get_tx_history_params.UserGetTxHistoryParams,
                ),
            ),
            cast_to=UserGetTxHistoryResponse,
        )

    def get_user(
        self,
        address: str,
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
    ) -> UserGetUserResponse:
        """
        Get user

        Args:
          address: The user account address

          with_percent: Calculate and include proportional percentages, where applicable

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
            path_template("/api/v1/users/{address}/user", address=address),
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
                    user_get_user_params.UserGetUserParams,
                ),
            ),
            cast_to=UserGetUserResponse,
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def market(self) -> AsyncMarketResource:
        return AsyncMarketResource(self._client)

    @cached_property
    def nept(self) -> AsyncNeptResource:
        return AsyncNeptResource(self._client)

    @cached_property
    def wallet(self) -> AsyncWalletResource:
        return AsyncWalletResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return AsyncUserResourceWithStreamingResponse(self)

    async def get_tx_history(
        self,
        address: str,
        *,
        action: Optional[EventAction] | Omit = omit,
        limit: int | Omit = omit,
        prev_event_uuid: Optional[str] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        with_text: bool | Omit = omit,
        with_value: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetTxHistoryResponse:
        """
        Get user tx history

        Args:
          address: The user account address

          action: Optional event/tx action to filter against

          limit: Maximum number of transactions to return.

              Optional and defaults to `20` if missing.

          prev_event_uuid: Optional UUID skip parameter used for pagination.

              Providing the last event UUID on a given page will return the next page
              beginning with the following (unseen) item.

          sort_order: Changes the sort order for the returned txs.

              Transactions are always sorted by event time, however the direction (e.g. newest
              to oldest) can be changed using this parameter.

              Optional and defaults to `desc` if missing.

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
            path_template("/api/v1/users/{address}/tx-history", address=address),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "action": action,
                        "limit": limit,
                        "prev_event_uuid": prev_event_uuid,
                        "sort_order": sort_order,
                        "with_text": with_text,
                        "with_value": with_value,
                    },
                    user_get_tx_history_params.UserGetTxHistoryParams,
                ),
            ),
            cast_to=UserGetTxHistoryResponse,
        )

    async def get_user(
        self,
        address: str,
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
    ) -> UserGetUserResponse:
        """
        Get user

        Args:
          address: The user account address

          with_percent: Calculate and include proportional percentages, where applicable

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
            path_template("/api/v1/users/{address}/user", address=address),
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
                    user_get_user_params.UserGetUserParams,
                ),
            ),
            cast_to=UserGetUserResponse,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.get_tx_history = to_raw_response_wrapper(
            user.get_tx_history,
        )
        self.get_user = to_raw_response_wrapper(
            user.get_user,
        )

    @cached_property
    def market(self) -> MarketResourceWithRawResponse:
        return MarketResourceWithRawResponse(self._user.market)

    @cached_property
    def nept(self) -> NeptResourceWithRawResponse:
        return NeptResourceWithRawResponse(self._user.nept)

    @cached_property
    def wallet(self) -> WalletResourceWithRawResponse:
        return WalletResourceWithRawResponse(self._user.wallet)


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.get_tx_history = async_to_raw_response_wrapper(
            user.get_tx_history,
        )
        self.get_user = async_to_raw_response_wrapper(
            user.get_user,
        )

    @cached_property
    def market(self) -> AsyncMarketResourceWithRawResponse:
        return AsyncMarketResourceWithRawResponse(self._user.market)

    @cached_property
    def nept(self) -> AsyncNeptResourceWithRawResponse:
        return AsyncNeptResourceWithRawResponse(self._user.nept)

    @cached_property
    def wallet(self) -> AsyncWalletResourceWithRawResponse:
        return AsyncWalletResourceWithRawResponse(self._user.wallet)


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.get_tx_history = to_streamed_response_wrapper(
            user.get_tx_history,
        )
        self.get_user = to_streamed_response_wrapper(
            user.get_user,
        )

    @cached_property
    def market(self) -> MarketResourceWithStreamingResponse:
        return MarketResourceWithStreamingResponse(self._user.market)

    @cached_property
    def nept(self) -> NeptResourceWithStreamingResponse:
        return NeptResourceWithStreamingResponse(self._user.nept)

    @cached_property
    def wallet(self) -> WalletResourceWithStreamingResponse:
        return WalletResourceWithStreamingResponse(self._user.wallet)


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.get_tx_history = async_to_streamed_response_wrapper(
            user.get_tx_history,
        )
        self.get_user = async_to_streamed_response_wrapper(
            user.get_user,
        )

    @cached_property
    def market(self) -> AsyncMarketResourceWithStreamingResponse:
        return AsyncMarketResourceWithStreamingResponse(self._user.market)

    @cached_property
    def nept(self) -> AsyncNeptResourceWithStreamingResponse:
        return AsyncNeptResourceWithStreamingResponse(self._user.nept)

    @cached_property
    def wallet(self) -> AsyncWalletResourceWithStreamingResponse:
        return AsyncWalletResourceWithStreamingResponse(self._user.wallet)
