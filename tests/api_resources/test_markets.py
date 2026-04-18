# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types import (
    MarketGetMergedResponse,
    MarketGetParamsResponse,
    MarketGetSupplyResponse,
    MarketGetOverviewResponse,
    MarketGetMergedByAssetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarkets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_merged(self, client: NeptuneAPIV2) -> None:
        market = client.markets.get_merged()
        assert_matches_type(MarketGetMergedResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_merged_with_all_params(self, client: NeptuneAPIV2) -> None:
        market = client.markets.get_merged(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(MarketGetMergedResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_merged(self, client: NeptuneAPIV2) -> None:
        response = client.markets.with_raw_response.get_merged()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(MarketGetMergedResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_merged(self, client: NeptuneAPIV2) -> None:
        with client.markets.with_streaming_response.get_merged() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(MarketGetMergedResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_merged_by_asset(self, client: NeptuneAPIV2) -> None:
        market = client.markets.get_merged_by_asset(
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(MarketGetMergedByAssetResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_merged_by_asset_with_all_params(self, client: NeptuneAPIV2) -> None:
        market = client.markets.get_merged_by_asset(
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(MarketGetMergedByAssetResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_merged_by_asset(self, client: NeptuneAPIV2) -> None:
        response = client.markets.with_raw_response.get_merged_by_asset(
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(MarketGetMergedByAssetResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_merged_by_asset(self, client: NeptuneAPIV2) -> None:
        with client.markets.with_streaming_response.get_merged_by_asset(
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(MarketGetMergedByAssetResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_overview(self, client: NeptuneAPIV2) -> None:
        market = client.markets.get_overview()
        assert_matches_type(MarketGetOverviewResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_overview_with_all_params(self, client: NeptuneAPIV2) -> None:
        market = client.markets.get_overview(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(MarketGetOverviewResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_overview(self, client: NeptuneAPIV2) -> None:
        response = client.markets.with_raw_response.get_overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(MarketGetOverviewResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_overview(self, client: NeptuneAPIV2) -> None:
        with client.markets.with_streaming_response.get_overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(MarketGetOverviewResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_params(self, client: NeptuneAPIV2) -> None:
        market = client.markets.get_params()
        assert_matches_type(MarketGetParamsResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_params_with_all_params(self, client: NeptuneAPIV2) -> None:
        market = client.markets.get_params(
            with_text=True,
        )
        assert_matches_type(MarketGetParamsResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_params(self, client: NeptuneAPIV2) -> None:
        response = client.markets.with_raw_response.get_params()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(MarketGetParamsResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_params(self, client: NeptuneAPIV2) -> None:
        with client.markets.with_streaming_response.get_params() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(MarketGetParamsResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_supply(self, client: NeptuneAPIV2) -> None:
        market = client.markets.get_supply()
        assert_matches_type(MarketGetSupplyResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_supply_with_all_params(self, client: NeptuneAPIV2) -> None:
        market = client.markets.get_supply(
            with_text=True,
        )
        assert_matches_type(MarketGetSupplyResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_supply(self, client: NeptuneAPIV2) -> None:
        response = client.markets.with_raw_response.get_supply()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(MarketGetSupplyResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_supply(self, client: NeptuneAPIV2) -> None:
        with client.markets.with_streaming_response.get_supply() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(MarketGetSupplyResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMarkets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_merged(self, async_client: AsyncNeptuneAPIV2) -> None:
        market = await async_client.markets.get_merged()
        assert_matches_type(MarketGetMergedResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_merged_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        market = await async_client.markets.get_merged(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(MarketGetMergedResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_merged(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.markets.with_raw_response.get_merged()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(MarketGetMergedResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_merged(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.markets.with_streaming_response.get_merged() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(MarketGetMergedResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_merged_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        market = await async_client.markets.get_merged_by_asset(
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(MarketGetMergedByAssetResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_merged_by_asset_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        market = await async_client.markets.get_merged_by_asset(
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(MarketGetMergedByAssetResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_merged_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.markets.with_raw_response.get_merged_by_asset(
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(MarketGetMergedByAssetResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_merged_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.markets.with_streaming_response.get_merged_by_asset(
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(MarketGetMergedByAssetResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_overview(self, async_client: AsyncNeptuneAPIV2) -> None:
        market = await async_client.markets.get_overview()
        assert_matches_type(MarketGetOverviewResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_overview_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        market = await async_client.markets.get_overview(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(MarketGetOverviewResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_overview(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.markets.with_raw_response.get_overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(MarketGetOverviewResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_overview(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.markets.with_streaming_response.get_overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(MarketGetOverviewResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        market = await async_client.markets.get_params()
        assert_matches_type(MarketGetParamsResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_params_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        market = await async_client.markets.get_params(
            with_text=True,
        )
        assert_matches_type(MarketGetParamsResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.markets.with_raw_response.get_params()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(MarketGetParamsResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.markets.with_streaming_response.get_params() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(MarketGetParamsResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_supply(self, async_client: AsyncNeptuneAPIV2) -> None:
        market = await async_client.markets.get_supply()
        assert_matches_type(MarketGetSupplyResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_supply_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        market = await async_client.markets.get_supply(
            with_text=True,
        )
        assert_matches_type(MarketGetSupplyResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_supply(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.markets.with_raw_response.get_supply()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(MarketGetSupplyResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_supply(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.markets.with_streaming_response.get_supply() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(MarketGetSupplyResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True
