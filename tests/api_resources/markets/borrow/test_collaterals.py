# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.markets.borrow import (
    CollateralListResponse,
    CollateralGetByAssetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollaterals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: NeptuneAPIV2) -> None:
        collateral = client.markets.borrow.collaterals.list()
        assert_matches_type(CollateralListResponse, collateral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: NeptuneAPIV2) -> None:
        collateral = client.markets.borrow.collaterals.list(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(CollateralListResponse, collateral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: NeptuneAPIV2) -> None:
        response = client.markets.borrow.collaterals.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collateral = response.parse()
        assert_matches_type(CollateralListResponse, collateral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: NeptuneAPIV2) -> None:
        with client.markets.borrow.collaterals.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collateral = response.parse()
            assert_matches_type(CollateralListResponse, collateral, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_asset(self, client: NeptuneAPIV2) -> None:
        collateral = client.markets.borrow.collaterals.get_by_asset(
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(CollateralGetByAssetResponse, collateral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_asset_with_all_params(self, client: NeptuneAPIV2) -> None:
        collateral = client.markets.borrow.collaterals.get_by_asset(
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(CollateralGetByAssetResponse, collateral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_asset(self, client: NeptuneAPIV2) -> None:
        response = client.markets.borrow.collaterals.with_raw_response.get_by_asset(
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collateral = response.parse()
        assert_matches_type(CollateralGetByAssetResponse, collateral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_asset(self, client: NeptuneAPIV2) -> None:
        with client.markets.borrow.collaterals.with_streaming_response.get_by_asset(
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collateral = response.parse()
            assert_matches_type(CollateralGetByAssetResponse, collateral, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCollaterals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNeptuneAPIV2) -> None:
        collateral = await async_client.markets.borrow.collaterals.list()
        assert_matches_type(CollateralListResponse, collateral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        collateral = await async_client.markets.borrow.collaterals.list(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(CollateralListResponse, collateral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.markets.borrow.collaterals.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collateral = await response.parse()
        assert_matches_type(CollateralListResponse, collateral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.markets.borrow.collaterals.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collateral = await response.parse()
            assert_matches_type(CollateralListResponse, collateral, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        collateral = await async_client.markets.borrow.collaterals.get_by_asset(
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(CollateralGetByAssetResponse, collateral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_asset_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        collateral = await async_client.markets.borrow.collaterals.get_by_asset(
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(CollateralGetByAssetResponse, collateral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.markets.borrow.collaterals.with_raw_response.get_by_asset(
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collateral = await response.parse()
        assert_matches_type(CollateralGetByAssetResponse, collateral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.markets.borrow.collaterals.with_streaming_response.get_by_asset(
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collateral = await response.parse()
            assert_matches_type(CollateralGetByAssetResponse, collateral, path=["response"])

        assert cast(Any, response.is_closed) is True
