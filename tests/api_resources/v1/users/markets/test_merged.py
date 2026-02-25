# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.v1.users.markets import (
    MergedGetAllMarketsResponse,
    MergedLookupByAssetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMerged:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_all_markets(self, client: NeptuneAPIV2) -> None:
        merged = client.v1.users.markets.merged.get_all_markets(
            address="address",
        )
        assert_matches_type(MergedGetAllMarketsResponse, merged, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_all_markets_with_all_params(self, client: NeptuneAPIV2) -> None:
        merged = client.v1.users.markets.merged.get_all_markets(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(MergedGetAllMarketsResponse, merged, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_all_markets(self, client: NeptuneAPIV2) -> None:
        response = client.v1.users.markets.merged.with_raw_response.get_all_markets(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        merged = response.parse()
        assert_matches_type(MergedGetAllMarketsResponse, merged, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_all_markets(self, client: NeptuneAPIV2) -> None:
        with client.v1.users.markets.merged.with_streaming_response.get_all_markets(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            merged = response.parse()
            assert_matches_type(MergedGetAllMarketsResponse, merged, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_all_markets(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.v1.users.markets.merged.with_raw_response.get_all_markets(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup_by_asset(self, client: NeptuneAPIV2) -> None:
        merged = client.v1.users.markets.merged.lookup_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(MergedLookupByAssetResponse, merged, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup_by_asset_with_all_params(self, client: NeptuneAPIV2) -> None:
        merged = client.v1.users.markets.merged.lookup_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(MergedLookupByAssetResponse, merged, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookup_by_asset(self, client: NeptuneAPIV2) -> None:
        response = client.v1.users.markets.merged.with_raw_response.lookup_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        merged = response.parse()
        assert_matches_type(MergedLookupByAssetResponse, merged, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookup_by_asset(self, client: NeptuneAPIV2) -> None:
        with client.v1.users.markets.merged.with_streaming_response.lookup_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            merged = response.parse()
            assert_matches_type(MergedLookupByAssetResponse, merged, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_lookup_by_asset(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.v1.users.markets.merged.with_raw_response.lookup_by_asset(
                address="",
                asset_id="token;-K-//-//3-",
            )


class TestAsyncMerged:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_all_markets(self, async_client: AsyncNeptuneAPIV2) -> None:
        merged = await async_client.v1.users.markets.merged.get_all_markets(
            address="address",
        )
        assert_matches_type(MergedGetAllMarketsResponse, merged, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_all_markets_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        merged = await async_client.v1.users.markets.merged.get_all_markets(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(MergedGetAllMarketsResponse, merged, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_all_markets(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.users.markets.merged.with_raw_response.get_all_markets(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        merged = await response.parse()
        assert_matches_type(MergedGetAllMarketsResponse, merged, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_all_markets(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.users.markets.merged.with_streaming_response.get_all_markets(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            merged = await response.parse()
            assert_matches_type(MergedGetAllMarketsResponse, merged, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_all_markets(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.v1.users.markets.merged.with_raw_response.get_all_markets(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        merged = await async_client.v1.users.markets.merged.lookup_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(MergedLookupByAssetResponse, merged, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup_by_asset_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        merged = await async_client.v1.users.markets.merged.lookup_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(MergedLookupByAssetResponse, merged, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookup_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.users.markets.merged.with_raw_response.lookup_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        merged = await response.parse()
        assert_matches_type(MergedLookupByAssetResponse, merged, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookup_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.users.markets.merged.with_streaming_response.lookup_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            merged = await response.parse()
            assert_matches_type(MergedLookupByAssetResponse, merged, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_lookup_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.v1.users.markets.merged.with_raw_response.lookup_by_asset(
                address="",
                asset_id="token;-K-//-//3-",
            )
