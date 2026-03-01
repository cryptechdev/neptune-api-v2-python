# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .bantr import (
    BantrResource,
    AsyncBantrResource,
    BantrResourceWithRawResponse,
    AsyncBantrResourceWithRawResponse,
    BantrResourceWithStreamingResponse,
    AsyncBantrResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["IntegrationsResource", "AsyncIntegrationsResource"]


class IntegrationsResource(SyncAPIResource):
    @cached_property
    def bantr(self) -> BantrResource:
        return BantrResource(self._client)

    @cached_property
    def with_raw_response(self) -> IntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return IntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return IntegrationsResourceWithStreamingResponse(self)


class AsyncIntegrationsResource(AsyncAPIResource):
    @cached_property
    def bantr(self) -> AsyncBantrResource:
        return AsyncBantrResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncIntegrationsResourceWithStreamingResponse(self)


class IntegrationsResourceWithRawResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

    @cached_property
    def bantr(self) -> BantrResourceWithRawResponse:
        return BantrResourceWithRawResponse(self._integrations.bantr)


class AsyncIntegrationsResourceWithRawResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

    @cached_property
    def bantr(self) -> AsyncBantrResourceWithRawResponse:
        return AsyncBantrResourceWithRawResponse(self._integrations.bantr)


class IntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

    @cached_property
    def bantr(self) -> BantrResourceWithStreamingResponse:
        return BantrResourceWithStreamingResponse(self._integrations.bantr)


class AsyncIntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

    @cached_property
    def bantr(self) -> AsyncBantrResourceWithStreamingResponse:
        return AsyncBantrResourceWithStreamingResponse(self._integrations.bantr)
