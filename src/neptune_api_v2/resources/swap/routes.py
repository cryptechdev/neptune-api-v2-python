# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.swap import route_list_all_params, route_list_by_denom_params
from ..._base_client import make_request_options
from ...types.swap.route_list_all_response import RouteListAllResponse
from ...types.swap.route_list_by_denom_response import RouteListByDenomResponse

__all__ = ["RoutesResource", "AsyncRoutesResource"]


class RoutesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return RoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return RoutesResourceWithStreamingResponse(self)

    def list_all(
        self,
        *,
        contract_address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteListAllResponse:
        """
        Get swap routes for all denoms

        Args:
          contract_address: Swap contract address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/swap/routes/all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"contract_address": contract_address}, route_list_all_params.RouteListAllParams),
            ),
            cast_to=RouteListAllResponse,
        )

    def list_by_denom(
        self,
        *,
        contract_address: str,
        source_denom: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteListByDenomResponse:
        """
        Get swap routes for a denom

        Args:
          contract_address: Swap contract address

          source_denom: Source asset denom to fetch target routes for

              **Note**: This is a normal injective asset denom, and not an `AssetSpec` ID.
              E.g. While `inj` is a valid `source_denom, `native;inj` is not valid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/swap/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "contract_address": contract_address,
                        "source_denom": source_denom,
                    },
                    route_list_by_denom_params.RouteListByDenomParams,
                ),
            ),
            cast_to=RouteListByDenomResponse,
        )


class AsyncRoutesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return AsyncRoutesResourceWithStreamingResponse(self)

    async def list_all(
        self,
        *,
        contract_address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteListAllResponse:
        """
        Get swap routes for all denoms

        Args:
          contract_address: Swap contract address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/swap/routes/all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"contract_address": contract_address}, route_list_all_params.RouteListAllParams
                ),
            ),
            cast_to=RouteListAllResponse,
        )

    async def list_by_denom(
        self,
        *,
        contract_address: str,
        source_denom: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RouteListByDenomResponse:
        """
        Get swap routes for a denom

        Args:
          contract_address: Swap contract address

          source_denom: Source asset denom to fetch target routes for

              **Note**: This is a normal injective asset denom, and not an `AssetSpec` ID.
              E.g. While `inj` is a valid `source_denom, `native;inj` is not valid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/swap/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "contract_address": contract_address,
                        "source_denom": source_denom,
                    },
                    route_list_by_denom_params.RouteListByDenomParams,
                ),
            ),
            cast_to=RouteListByDenomResponse,
        )


class RoutesResourceWithRawResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.list_all = to_raw_response_wrapper(
            routes.list_all,
        )
        self.list_by_denom = to_raw_response_wrapper(
            routes.list_by_denom,
        )


class AsyncRoutesResourceWithRawResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.list_all = async_to_raw_response_wrapper(
            routes.list_all,
        )
        self.list_by_denom = async_to_raw_response_wrapper(
            routes.list_by_denom,
        )


class RoutesResourceWithStreamingResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.list_all = to_streamed_response_wrapper(
            routes.list_all,
        )
        self.list_by_denom = to_streamed_response_wrapper(
            routes.list_by_denom,
        )


class AsyncRoutesResourceWithStreamingResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.list_all = async_to_streamed_response_wrapper(
            routes.list_all,
        )
        self.list_by_denom = async_to_streamed_response_wrapper(
            routes.list_by_denom,
        )
