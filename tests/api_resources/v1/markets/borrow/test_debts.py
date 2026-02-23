# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.v1.markets.borrow import (
    DebtListResponse,
    DebtLookupByAssetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDebts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: NeptuneAPIV2) -> None:
        debt = client.v1.markets.borrow.debts.list()
        assert_matches_type(DebtListResponse, debt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: NeptuneAPIV2) -> None:
        debt = client.v1.markets.borrow.debts.list(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(DebtListResponse, debt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: NeptuneAPIV2) -> None:
        response = client.v1.markets.borrow.debts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        debt = response.parse()
        assert_matches_type(DebtListResponse, debt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: NeptuneAPIV2) -> None:
        with client.v1.markets.borrow.debts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            debt = response.parse()
            assert_matches_type(DebtListResponse, debt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup_by_asset(self, client: NeptuneAPIV2) -> None:
        debt = client.v1.markets.borrow.debts.lookup_by_asset(
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(DebtLookupByAssetResponse, debt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup_by_asset_with_all_params(self, client: NeptuneAPIV2) -> None:
        debt = client.v1.markets.borrow.debts.lookup_by_asset(
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(DebtLookupByAssetResponse, debt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookup_by_asset(self, client: NeptuneAPIV2) -> None:
        response = client.v1.markets.borrow.debts.with_raw_response.lookup_by_asset(
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        debt = response.parse()
        assert_matches_type(DebtLookupByAssetResponse, debt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookup_by_asset(self, client: NeptuneAPIV2) -> None:
        with client.v1.markets.borrow.debts.with_streaming_response.lookup_by_asset(
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            debt = response.parse()
            assert_matches_type(DebtLookupByAssetResponse, debt, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDebts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNeptuneAPIV2) -> None:
        debt = await async_client.v1.markets.borrow.debts.list()
        assert_matches_type(DebtListResponse, debt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        debt = await async_client.v1.markets.borrow.debts.list(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(DebtListResponse, debt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.markets.borrow.debts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        debt = await response.parse()
        assert_matches_type(DebtListResponse, debt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.markets.borrow.debts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            debt = await response.parse()
            assert_matches_type(DebtListResponse, debt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        debt = await async_client.v1.markets.borrow.debts.lookup_by_asset(
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(DebtLookupByAssetResponse, debt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup_by_asset_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        debt = await async_client.v1.markets.borrow.debts.lookup_by_asset(
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(DebtLookupByAssetResponse, debt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookup_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.markets.borrow.debts.with_raw_response.lookup_by_asset(
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        debt = await response.parse()
        assert_matches_type(DebtLookupByAssetResponse, debt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookup_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.markets.borrow.debts.with_streaming_response.lookup_by_asset(
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            debt = await response.parse()
            assert_matches_type(DebtLookupByAssetResponse, debt, path=["response"])

        assert cast(Any, response.is_closed) is True
