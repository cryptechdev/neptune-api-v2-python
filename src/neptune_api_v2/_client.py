# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import nept, swap, user, assets, status, markets, analytics, integrations
    from .resources.nept import NeptResource, AsyncNeptResource
    from .resources.assets import AssetsResource, AsyncAssetsResource
    from .resources.status import StatusResource, AsyncStatusResource
    from .resources.swap.swap import SwapResource, AsyncSwapResource
    from .resources.user.user import UserResource, AsyncUserResource
    from .resources.markets.markets import MarketsResource, AsyncMarketsResource
    from .resources.analytics.analytics import AnalyticsResource, AsyncAnalyticsResource
    from .resources.integrations.integrations import IntegrationsResource, AsyncIntegrationsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "NeptuneAPIV2",
    "AsyncNeptuneAPIV2",
    "Client",
    "AsyncClient",
]


class NeptuneAPIV2(SyncAPIClient):
    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous NeptuneAPIV2 client instance."""
        if base_url is None:
            base_url = os.environ.get("NEPTUNE_API_V2_BASE_URL")
        if base_url is None:
            base_url = f"https://api-v2.nept.finance"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def status(self) -> StatusResource:
        from .resources.status import StatusResource

        return StatusResource(self)

    @cached_property
    def assets(self) -> AssetsResource:
        from .resources.assets import AssetsResource

        return AssetsResource(self)

    @cached_property
    def markets(self) -> MarketsResource:
        from .resources.markets import MarketsResource

        return MarketsResource(self)

    @cached_property
    def nept(self) -> NeptResource:
        from .resources.nept import NeptResource

        return NeptResource(self)

    @cached_property
    def user(self) -> UserResource:
        from .resources.user import UserResource

        return UserResource(self)

    @cached_property
    def analytics(self) -> AnalyticsResource:
        from .resources.analytics import AnalyticsResource

        return AnalyticsResource(self)

    @cached_property
    def integrations(self) -> IntegrationsResource:
        from .resources.integrations import IntegrationsResource

        return IntegrationsResource(self)

    @cached_property
    def swap(self) -> SwapResource:
        from .resources.swap import SwapResource

        return SwapResource(self)

    @cached_property
    def with_raw_response(self) -> NeptuneAPIV2WithRawResponse:
        return NeptuneAPIV2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NeptuneAPIV2WithStreamedResponse:
        return NeptuneAPIV2WithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncNeptuneAPIV2(AsyncAPIClient):
    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncNeptuneAPIV2 client instance."""
        if base_url is None:
            base_url = os.environ.get("NEPTUNE_API_V2_BASE_URL")
        if base_url is None:
            base_url = f"https://api-v2.nept.finance"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def status(self) -> AsyncStatusResource:
        from .resources.status import AsyncStatusResource

        return AsyncStatusResource(self)

    @cached_property
    def assets(self) -> AsyncAssetsResource:
        from .resources.assets import AsyncAssetsResource

        return AsyncAssetsResource(self)

    @cached_property
    def markets(self) -> AsyncMarketsResource:
        from .resources.markets import AsyncMarketsResource

        return AsyncMarketsResource(self)

    @cached_property
    def nept(self) -> AsyncNeptResource:
        from .resources.nept import AsyncNeptResource

        return AsyncNeptResource(self)

    @cached_property
    def user(self) -> AsyncUserResource:
        from .resources.user import AsyncUserResource

        return AsyncUserResource(self)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        from .resources.analytics import AsyncAnalyticsResource

        return AsyncAnalyticsResource(self)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        from .resources.integrations import AsyncIntegrationsResource

        return AsyncIntegrationsResource(self)

    @cached_property
    def swap(self) -> AsyncSwapResource:
        from .resources.swap import AsyncSwapResource

        return AsyncSwapResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncNeptuneAPIV2WithRawResponse:
        return AsyncNeptuneAPIV2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNeptuneAPIV2WithStreamedResponse:
        return AsyncNeptuneAPIV2WithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class NeptuneAPIV2WithRawResponse:
    _client: NeptuneAPIV2

    def __init__(self, client: NeptuneAPIV2) -> None:
        self._client = client

    @cached_property
    def status(self) -> status.StatusResourceWithRawResponse:
        from .resources.status import StatusResourceWithRawResponse

        return StatusResourceWithRawResponse(self._client.status)

    @cached_property
    def assets(self) -> assets.AssetsResourceWithRawResponse:
        from .resources.assets import AssetsResourceWithRawResponse

        return AssetsResourceWithRawResponse(self._client.assets)

    @cached_property
    def markets(self) -> markets.MarketsResourceWithRawResponse:
        from .resources.markets import MarketsResourceWithRawResponse

        return MarketsResourceWithRawResponse(self._client.markets)

    @cached_property
    def nept(self) -> nept.NeptResourceWithRawResponse:
        from .resources.nept import NeptResourceWithRawResponse

        return NeptResourceWithRawResponse(self._client.nept)

    @cached_property
    def user(self) -> user.UserResourceWithRawResponse:
        from .resources.user import UserResourceWithRawResponse

        return UserResourceWithRawResponse(self._client.user)

    @cached_property
    def analytics(self) -> analytics.AnalyticsResourceWithRawResponse:
        from .resources.analytics import AnalyticsResourceWithRawResponse

        return AnalyticsResourceWithRawResponse(self._client.analytics)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithRawResponse:
        from .resources.integrations import IntegrationsResourceWithRawResponse

        return IntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def swap(self) -> swap.SwapResourceWithRawResponse:
        from .resources.swap import SwapResourceWithRawResponse

        return SwapResourceWithRawResponse(self._client.swap)


class AsyncNeptuneAPIV2WithRawResponse:
    _client: AsyncNeptuneAPIV2

    def __init__(self, client: AsyncNeptuneAPIV2) -> None:
        self._client = client

    @cached_property
    def status(self) -> status.AsyncStatusResourceWithRawResponse:
        from .resources.status import AsyncStatusResourceWithRawResponse

        return AsyncStatusResourceWithRawResponse(self._client.status)

    @cached_property
    def assets(self) -> assets.AsyncAssetsResourceWithRawResponse:
        from .resources.assets import AsyncAssetsResourceWithRawResponse

        return AsyncAssetsResourceWithRawResponse(self._client.assets)

    @cached_property
    def markets(self) -> markets.AsyncMarketsResourceWithRawResponse:
        from .resources.markets import AsyncMarketsResourceWithRawResponse

        return AsyncMarketsResourceWithRawResponse(self._client.markets)

    @cached_property
    def nept(self) -> nept.AsyncNeptResourceWithRawResponse:
        from .resources.nept import AsyncNeptResourceWithRawResponse

        return AsyncNeptResourceWithRawResponse(self._client.nept)

    @cached_property
    def user(self) -> user.AsyncUserResourceWithRawResponse:
        from .resources.user import AsyncUserResourceWithRawResponse

        return AsyncUserResourceWithRawResponse(self._client.user)

    @cached_property
    def analytics(self) -> analytics.AsyncAnalyticsResourceWithRawResponse:
        from .resources.analytics import AsyncAnalyticsResourceWithRawResponse

        return AsyncAnalyticsResourceWithRawResponse(self._client.analytics)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithRawResponse:
        from .resources.integrations import AsyncIntegrationsResourceWithRawResponse

        return AsyncIntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def swap(self) -> swap.AsyncSwapResourceWithRawResponse:
        from .resources.swap import AsyncSwapResourceWithRawResponse

        return AsyncSwapResourceWithRawResponse(self._client.swap)


class NeptuneAPIV2WithStreamedResponse:
    _client: NeptuneAPIV2

    def __init__(self, client: NeptuneAPIV2) -> None:
        self._client = client

    @cached_property
    def status(self) -> status.StatusResourceWithStreamingResponse:
        from .resources.status import StatusResourceWithStreamingResponse

        return StatusResourceWithStreamingResponse(self._client.status)

    @cached_property
    def assets(self) -> assets.AssetsResourceWithStreamingResponse:
        from .resources.assets import AssetsResourceWithStreamingResponse

        return AssetsResourceWithStreamingResponse(self._client.assets)

    @cached_property
    def markets(self) -> markets.MarketsResourceWithStreamingResponse:
        from .resources.markets import MarketsResourceWithStreamingResponse

        return MarketsResourceWithStreamingResponse(self._client.markets)

    @cached_property
    def nept(self) -> nept.NeptResourceWithStreamingResponse:
        from .resources.nept import NeptResourceWithStreamingResponse

        return NeptResourceWithStreamingResponse(self._client.nept)

    @cached_property
    def user(self) -> user.UserResourceWithStreamingResponse:
        from .resources.user import UserResourceWithStreamingResponse

        return UserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def analytics(self) -> analytics.AnalyticsResourceWithStreamingResponse:
        from .resources.analytics import AnalyticsResourceWithStreamingResponse

        return AnalyticsResourceWithStreamingResponse(self._client.analytics)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithStreamingResponse:
        from .resources.integrations import IntegrationsResourceWithStreamingResponse

        return IntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def swap(self) -> swap.SwapResourceWithStreamingResponse:
        from .resources.swap import SwapResourceWithStreamingResponse

        return SwapResourceWithStreamingResponse(self._client.swap)


class AsyncNeptuneAPIV2WithStreamedResponse:
    _client: AsyncNeptuneAPIV2

    def __init__(self, client: AsyncNeptuneAPIV2) -> None:
        self._client = client

    @cached_property
    def status(self) -> status.AsyncStatusResourceWithStreamingResponse:
        from .resources.status import AsyncStatusResourceWithStreamingResponse

        return AsyncStatusResourceWithStreamingResponse(self._client.status)

    @cached_property
    def assets(self) -> assets.AsyncAssetsResourceWithStreamingResponse:
        from .resources.assets import AsyncAssetsResourceWithStreamingResponse

        return AsyncAssetsResourceWithStreamingResponse(self._client.assets)

    @cached_property
    def markets(self) -> markets.AsyncMarketsResourceWithStreamingResponse:
        from .resources.markets import AsyncMarketsResourceWithStreamingResponse

        return AsyncMarketsResourceWithStreamingResponse(self._client.markets)

    @cached_property
    def nept(self) -> nept.AsyncNeptResourceWithStreamingResponse:
        from .resources.nept import AsyncNeptResourceWithStreamingResponse

        return AsyncNeptResourceWithStreamingResponse(self._client.nept)

    @cached_property
    def user(self) -> user.AsyncUserResourceWithStreamingResponse:
        from .resources.user import AsyncUserResourceWithStreamingResponse

        return AsyncUserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def analytics(self) -> analytics.AsyncAnalyticsResourceWithStreamingResponse:
        from .resources.analytics import AsyncAnalyticsResourceWithStreamingResponse

        return AsyncAnalyticsResourceWithStreamingResponse(self._client.analytics)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithStreamingResponse:
        from .resources.integrations import AsyncIntegrationsResourceWithStreamingResponse

        return AsyncIntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def swap(self) -> swap.AsyncSwapResourceWithStreamingResponse:
        from .resources.swap import AsyncSwapResourceWithStreamingResponse

        return AsyncSwapResourceWithStreamingResponse(self._client.swap)


Client = NeptuneAPIV2

AsyncClient = AsyncNeptuneAPIV2
