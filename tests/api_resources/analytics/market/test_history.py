# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.pagination import SyncIntervalSinglePage, AsyncIntervalSinglePage
from neptune_api_v2.types.analytics.market import (
    HistoryGetLoansOriginatedResponse,
    HistoryGetLoansOriginatedByAssetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_loans_originated(self, client: NeptuneAPIV2) -> None:
        history = client.analytics.market.history.get_loans_originated(
            end=0,
            period="h",
            start=0,
        )
        assert_matches_type(SyncIntervalSinglePage[HistoryGetLoansOriginatedResponse], history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_loans_originated_with_all_params(self, client: NeptuneAPIV2) -> None:
        history = client.analytics.market.history.get_loans_originated(
            end=0,
            period="h",
            start=0,
            interval=1,
            limit=1,
            offset=0,
        )
        assert_matches_type(SyncIntervalSinglePage[HistoryGetLoansOriginatedResponse], history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_loans_originated(self, client: NeptuneAPIV2) -> None:
        response = client.analytics.market.history.with_raw_response.get_loans_originated(
            end=0,
            period="h",
            start=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(SyncIntervalSinglePage[HistoryGetLoansOriginatedResponse], history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_loans_originated(self, client: NeptuneAPIV2) -> None:
        with client.analytics.market.history.with_streaming_response.get_loans_originated(
            end=0,
            period="h",
            start=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(SyncIntervalSinglePage[HistoryGetLoansOriginatedResponse], history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_loans_originated_by_asset(self, client: NeptuneAPIV2) -> None:
        history = client.analytics.market.history.get_loans_originated_by_asset(
            end=0,
            period="h",
            start=0,
        )
        assert_matches_type(HistoryGetLoansOriginatedByAssetResponse, history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_loans_originated_by_asset_with_all_params(self, client: NeptuneAPIV2) -> None:
        history = client.analytics.market.history.get_loans_originated_by_asset(
            end=0,
            period="h",
            start=0,
            asset_ids="token;-K-//-//3-,token;v/-/g-/P",
            interval=1,
            limit=1,
            offset=0,
        )
        assert_matches_type(HistoryGetLoansOriginatedByAssetResponse, history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_loans_originated_by_asset(self, client: NeptuneAPIV2) -> None:
        response = client.analytics.market.history.with_raw_response.get_loans_originated_by_asset(
            end=0,
            period="h",
            start=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(HistoryGetLoansOriginatedByAssetResponse, history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_loans_originated_by_asset(self, client: NeptuneAPIV2) -> None:
        with client.analytics.market.history.with_streaming_response.get_loans_originated_by_asset(
            end=0,
            period="h",
            start=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(HistoryGetLoansOriginatedByAssetResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHistory:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_loans_originated(self, async_client: AsyncNeptuneAPIV2) -> None:
        history = await async_client.analytics.market.history.get_loans_originated(
            end=0,
            period="h",
            start=0,
        )
        assert_matches_type(AsyncIntervalSinglePage[HistoryGetLoansOriginatedResponse], history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_loans_originated_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        history = await async_client.analytics.market.history.get_loans_originated(
            end=0,
            period="h",
            start=0,
            interval=1,
            limit=1,
            offset=0,
        )
        assert_matches_type(AsyncIntervalSinglePage[HistoryGetLoansOriginatedResponse], history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_loans_originated(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.analytics.market.history.with_raw_response.get_loans_originated(
            end=0,
            period="h",
            start=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(AsyncIntervalSinglePage[HistoryGetLoansOriginatedResponse], history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_loans_originated(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.analytics.market.history.with_streaming_response.get_loans_originated(
            end=0,
            period="h",
            start=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(AsyncIntervalSinglePage[HistoryGetLoansOriginatedResponse], history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_loans_originated_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        history = await async_client.analytics.market.history.get_loans_originated_by_asset(
            end=0,
            period="h",
            start=0,
        )
        assert_matches_type(HistoryGetLoansOriginatedByAssetResponse, history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_loans_originated_by_asset_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        history = await async_client.analytics.market.history.get_loans_originated_by_asset(
            end=0,
            period="h",
            start=0,
            asset_ids="token;-K-//-//3-,token;v/-/g-/P",
            interval=1,
            limit=1,
            offset=0,
        )
        assert_matches_type(HistoryGetLoansOriginatedByAssetResponse, history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_loans_originated_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.analytics.market.history.with_raw_response.get_loans_originated_by_asset(
            end=0,
            period="h",
            start=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(HistoryGetLoansOriginatedByAssetResponse, history, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_loans_originated_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.analytics.market.history.with_streaming_response.get_loans_originated_by_asset(
            end=0,
            period="h",
            start=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(HistoryGetLoansOriginatedByAssetResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True
