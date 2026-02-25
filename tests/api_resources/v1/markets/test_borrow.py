# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.v1.markets import (
    BorrowOverviewResponse,
    BorrowGetRateHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBorrow:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_rate_history(self, client: NeptuneAPIV2) -> None:
        borrow = client.v1.markets.borrow.get_rate_history(
            end=0,
            period="h",
            start=0,
        )
        assert_matches_type(BorrowGetRateHistoryResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_rate_history_with_all_params(self, client: NeptuneAPIV2) -> None:
        borrow = client.v1.markets.borrow.get_rate_history(
            end=0,
            period="h",
            start=0,
            asset_ids="token;-K-//-//3-,token;v/-/g-/P",
            interval=1,
            limit=1,
            offset=0,
        )
        assert_matches_type(BorrowGetRateHistoryResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_rate_history(self, client: NeptuneAPIV2) -> None:
        response = client.v1.markets.borrow.with_raw_response.get_rate_history(
            end=0,
            period="h",
            start=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = response.parse()
        assert_matches_type(BorrowGetRateHistoryResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_rate_history(self, client: NeptuneAPIV2) -> None:
        with client.v1.markets.borrow.with_streaming_response.get_rate_history(
            end=0,
            period="h",
            start=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = response.parse()
            assert_matches_type(BorrowGetRateHistoryResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_overview(self, client: NeptuneAPIV2) -> None:
        borrow = client.v1.markets.borrow.overview()
        assert_matches_type(BorrowOverviewResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_overview_with_all_params(self, client: NeptuneAPIV2) -> None:
        borrow = client.v1.markets.borrow.overview(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(BorrowOverviewResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_overview(self, client: NeptuneAPIV2) -> None:
        response = client.v1.markets.borrow.with_raw_response.overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = response.parse()
        assert_matches_type(BorrowOverviewResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_overview(self, client: NeptuneAPIV2) -> None:
        with client.v1.markets.borrow.with_streaming_response.overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = response.parse()
            assert_matches_type(BorrowOverviewResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBorrow:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_rate_history(self, async_client: AsyncNeptuneAPIV2) -> None:
        borrow = await async_client.v1.markets.borrow.get_rate_history(
            end=0,
            period="h",
            start=0,
        )
        assert_matches_type(BorrowGetRateHistoryResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_rate_history_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        borrow = await async_client.v1.markets.borrow.get_rate_history(
            end=0,
            period="h",
            start=0,
            asset_ids="token;-K-//-//3-,token;v/-/g-/P",
            interval=1,
            limit=1,
            offset=0,
        )
        assert_matches_type(BorrowGetRateHistoryResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_rate_history(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.markets.borrow.with_raw_response.get_rate_history(
            end=0,
            period="h",
            start=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = await response.parse()
        assert_matches_type(BorrowGetRateHistoryResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_rate_history(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.markets.borrow.with_streaming_response.get_rate_history(
            end=0,
            period="h",
            start=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = await response.parse()
            assert_matches_type(BorrowGetRateHistoryResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_overview(self, async_client: AsyncNeptuneAPIV2) -> None:
        borrow = await async_client.v1.markets.borrow.overview()
        assert_matches_type(BorrowOverviewResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_overview_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        borrow = await async_client.v1.markets.borrow.overview(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(BorrowOverviewResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_overview(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.markets.borrow.with_raw_response.overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = await response.parse()
        assert_matches_type(BorrowOverviewResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_overview(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.markets.borrow.with_streaming_response.overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = await response.parse()
            assert_matches_type(BorrowOverviewResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True
