# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types import (
    AssetListResponse,
    AssetListPricesResponse,
)
from neptune_api_v2.pagination import SyncIntervalMultiPage, AsyncIntervalMultiPage
from neptune_api_v2.types.asset_price_history import Series

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: NeptuneAPIV2) -> None:
        asset = client.assets.list()
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: NeptuneAPIV2) -> None:
        response = client.assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: NeptuneAPIV2) -> None:
        with client.assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetListResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_price_history(self, client: NeptuneAPIV2) -> None:
        asset = client.assets.get_price_history(
            end=0,
            period="h",
            start=0,
        )
        assert_matches_type(SyncIntervalMultiPage[Series], asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_price_history_with_all_params(self, client: NeptuneAPIV2) -> None:
        asset = client.assets.get_price_history(
            end=0,
            period="h",
            start=0,
            asset_ids="token;-K-//-//3-,token;v/-/g-/P",
            interval=1,
            limit=1,
            offset=0,
        )
        assert_matches_type(SyncIntervalMultiPage[Series], asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_price_history(self, client: NeptuneAPIV2) -> None:
        response = client.assets.with_raw_response.get_price_history(
            end=0,
            period="h",
            start=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(SyncIntervalMultiPage[Series], asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_price_history(self, client: NeptuneAPIV2) -> None:
        with client.assets.with_streaming_response.get_price_history(
            end=0,
            period="h",
            start=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(SyncIntervalMultiPage[Series], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_prices(self, client: NeptuneAPIV2) -> None:
        asset = client.assets.list_prices()
        assert_matches_type(AssetListPricesResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_prices_with_all_params(self, client: NeptuneAPIV2) -> None:
        asset = client.assets.list_prices(
            with_text=True,
        )
        assert_matches_type(AssetListPricesResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_prices(self, client: NeptuneAPIV2) -> None:
        response = client.assets.with_raw_response.list_prices()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetListPricesResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_prices(self, client: NeptuneAPIV2) -> None:
        with client.assets.with_streaming_response.list_prices() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetListPricesResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNeptuneAPIV2) -> None:
        asset = await async_client.assets.list()
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetListResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_price_history(self, async_client: AsyncNeptuneAPIV2) -> None:
        asset = await async_client.assets.get_price_history(
            end=0,
            period="h",
            start=0,
        )
        assert_matches_type(AsyncIntervalMultiPage[Series], asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_price_history_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        asset = await async_client.assets.get_price_history(
            end=0,
            period="h",
            start=0,
            asset_ids="token;-K-//-//3-,token;v/-/g-/P",
            interval=1,
            limit=1,
            offset=0,
        )
        assert_matches_type(AsyncIntervalMultiPage[Series], asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_price_history(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.assets.with_raw_response.get_price_history(
            end=0,
            period="h",
            start=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AsyncIntervalMultiPage[Series], asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_price_history(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.assets.with_streaming_response.get_price_history(
            end=0,
            period="h",
            start=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AsyncIntervalMultiPage[Series], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_prices(self, async_client: AsyncNeptuneAPIV2) -> None:
        asset = await async_client.assets.list_prices()
        assert_matches_type(AssetListPricesResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_prices_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        asset = await async_client.assets.list_prices(
            with_text=True,
        )
        assert_matches_type(AssetListPricesResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_prices(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.assets.with_raw_response.list_prices()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetListPricesResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_prices(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.assets.with_streaming_response.list_prices() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetListPricesResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True
