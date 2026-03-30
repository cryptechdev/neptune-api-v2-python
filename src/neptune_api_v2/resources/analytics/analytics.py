# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .nept import (
    NeptResource,
    AsyncNeptResource,
    NeptResourceWithRawResponse,
    AsyncNeptResourceWithRawResponse,
    NeptResourceWithStreamingResponse,
    AsyncNeptResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .market.market import (
    MarketResource,
    AsyncMarketResource,
    MarketResourceWithRawResponse,
    AsyncMarketResourceWithRawResponse,
    MarketResourceWithStreamingResponse,
    AsyncMarketResourceWithStreamingResponse,
)

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    @cached_property
    def market(self) -> MarketResource:
        return MarketResource(self._client)

    @cached_property
    def nept(self) -> NeptResource:
        return NeptResource(self._client)

    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return AnalyticsResourceWithStreamingResponse(self)


class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def market(self) -> AsyncMarketResource:
        return AsyncMarketResource(self._client)

    @cached_property
    def nept(self) -> AsyncNeptResource:
        return AsyncNeptResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cryptechdev/neptune-api-v2-python#with_streaming_response
        """
        return AsyncAnalyticsResourceWithStreamingResponse(self)


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def market(self) -> MarketResourceWithRawResponse:
        return MarketResourceWithRawResponse(self._analytics.market)

    @cached_property
    def nept(self) -> NeptResourceWithRawResponse:
        return NeptResourceWithRawResponse(self._analytics.nept)


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def market(self) -> AsyncMarketResourceWithRawResponse:
        return AsyncMarketResourceWithRawResponse(self._analytics.market)

    @cached_property
    def nept(self) -> AsyncNeptResourceWithRawResponse:
        return AsyncNeptResourceWithRawResponse(self._analytics.nept)


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def market(self) -> MarketResourceWithStreamingResponse:
        return MarketResourceWithStreamingResponse(self._analytics.market)

    @cached_property
    def nept(self) -> NeptResourceWithStreamingResponse:
        return NeptResourceWithStreamingResponse(self._analytics.nept)


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def market(self) -> AsyncMarketResourceWithStreamingResponse:
        return AsyncMarketResourceWithStreamingResponse(self._analytics.market)

    @cached_property
    def nept(self) -> AsyncNeptResourceWithStreamingResponse:
        return AsyncNeptResourceWithStreamingResponse(self._analytics.nept)
