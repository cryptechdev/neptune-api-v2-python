# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from .loans_originated import (
    LoansOriginatedResource,
    AsyncLoansOriginatedResource,
    LoansOriginatedResourceWithRawResponse,
    AsyncLoansOriginatedResourceWithRawResponse,
    LoansOriginatedResourceWithStreamingResponse,
    AsyncLoansOriginatedResourceWithStreamingResponse,
)

__all__ = ["HistoryResource", "AsyncHistoryResource"]


class HistoryResource(SyncAPIResource):
    @cached_property
    def loans_originated(self) -> LoansOriginatedResource:
        return LoansOriginatedResource(self._client)

    @cached_property
    def with_raw_response(self) -> HistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return HistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return HistoryResourceWithStreamingResponse(self)


class AsyncHistoryResource(AsyncAPIResource):
    @cached_property
    def loans_originated(self) -> AsyncLoansOriginatedResource:
        return AsyncLoansOriginatedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/neptune-api-v2-python#with_streaming_response
        """
        return AsyncHistoryResourceWithStreamingResponse(self)


class HistoryResourceWithRawResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

    @cached_property
    def loans_originated(self) -> LoansOriginatedResourceWithRawResponse:
        return LoansOriginatedResourceWithRawResponse(self._history.loans_originated)


class AsyncHistoryResourceWithRawResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

    @cached_property
    def loans_originated(self) -> AsyncLoansOriginatedResourceWithRawResponse:
        return AsyncLoansOriginatedResourceWithRawResponse(self._history.loans_originated)


class HistoryResourceWithStreamingResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

    @cached_property
    def loans_originated(self) -> LoansOriginatedResourceWithStreamingResponse:
        return LoansOriginatedResourceWithStreamingResponse(self._history.loans_originated)


class AsyncHistoryResourceWithStreamingResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

    @cached_property
    def loans_originated(self) -> AsyncLoansOriginatedResourceWithStreamingResponse:
        return AsyncLoansOriginatedResourceWithStreamingResponse(self._history.loans_originated)
