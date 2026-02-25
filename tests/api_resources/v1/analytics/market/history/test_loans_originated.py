# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.v1.analytics.market.history import (
    LoansOriginatedGetAllResponse,
    LoansOriginatedGetByAssetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLoansOriginated:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_all(self, client: NeptuneAPIV2) -> None:
        loans_originated = client.v1.analytics.market.history.loans_originated.get_all(
            end=0,
            period="h",
            start=0,
        )
        assert_matches_type(LoansOriginatedGetAllResponse, loans_originated, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_all_with_all_params(self, client: NeptuneAPIV2) -> None:
        loans_originated = client.v1.analytics.market.history.loans_originated.get_all(
            end=0,
            period="h",
            start=0,
            interval=1,
            limit=1,
            offset=0,
        )
        assert_matches_type(LoansOriginatedGetAllResponse, loans_originated, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_all(self, client: NeptuneAPIV2) -> None:
        response = client.v1.analytics.market.history.loans_originated.with_raw_response.get_all(
            end=0,
            period="h",
            start=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loans_originated = response.parse()
        assert_matches_type(LoansOriginatedGetAllResponse, loans_originated, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_all(self, client: NeptuneAPIV2) -> None:
        with client.v1.analytics.market.history.loans_originated.with_streaming_response.get_all(
            end=0,
            period="h",
            start=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loans_originated = response.parse()
            assert_matches_type(LoansOriginatedGetAllResponse, loans_originated, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_asset(self, client: NeptuneAPIV2) -> None:
        loans_originated = client.v1.analytics.market.history.loans_originated.get_by_asset(
            end=0,
            period="h",
            start=0,
        )
        assert_matches_type(LoansOriginatedGetByAssetResponse, loans_originated, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_asset_with_all_params(self, client: NeptuneAPIV2) -> None:
        loans_originated = client.v1.analytics.market.history.loans_originated.get_by_asset(
            end=0,
            period="h",
            start=0,
            asset_ids="token;-K-//-//3-,token;v/-/g-/P",
            interval=1,
            limit=1,
            offset=0,
        )
        assert_matches_type(LoansOriginatedGetByAssetResponse, loans_originated, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_asset(self, client: NeptuneAPIV2) -> None:
        response = client.v1.analytics.market.history.loans_originated.with_raw_response.get_by_asset(
            end=0,
            period="h",
            start=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loans_originated = response.parse()
        assert_matches_type(LoansOriginatedGetByAssetResponse, loans_originated, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_asset(self, client: NeptuneAPIV2) -> None:
        with client.v1.analytics.market.history.loans_originated.with_streaming_response.get_by_asset(
            end=0,
            period="h",
            start=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loans_originated = response.parse()
            assert_matches_type(LoansOriginatedGetByAssetResponse, loans_originated, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLoansOriginated:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_all(self, async_client: AsyncNeptuneAPIV2) -> None:
        loans_originated = await async_client.v1.analytics.market.history.loans_originated.get_all(
            end=0,
            period="h",
            start=0,
        )
        assert_matches_type(LoansOriginatedGetAllResponse, loans_originated, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_all_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        loans_originated = await async_client.v1.analytics.market.history.loans_originated.get_all(
            end=0,
            period="h",
            start=0,
            interval=1,
            limit=1,
            offset=0,
        )
        assert_matches_type(LoansOriginatedGetAllResponse, loans_originated, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_all(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.analytics.market.history.loans_originated.with_raw_response.get_all(
            end=0,
            period="h",
            start=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loans_originated = await response.parse()
        assert_matches_type(LoansOriginatedGetAllResponse, loans_originated, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_all(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.analytics.market.history.loans_originated.with_streaming_response.get_all(
            end=0,
            period="h",
            start=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loans_originated = await response.parse()
            assert_matches_type(LoansOriginatedGetAllResponse, loans_originated, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        loans_originated = await async_client.v1.analytics.market.history.loans_originated.get_by_asset(
            end=0,
            period="h",
            start=0,
        )
        assert_matches_type(LoansOriginatedGetByAssetResponse, loans_originated, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_asset_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        loans_originated = await async_client.v1.analytics.market.history.loans_originated.get_by_asset(
            end=0,
            period="h",
            start=0,
            asset_ids="token;-K-//-//3-,token;v/-/g-/P",
            interval=1,
            limit=1,
            offset=0,
        )
        assert_matches_type(LoansOriginatedGetByAssetResponse, loans_originated, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.analytics.market.history.loans_originated.with_raw_response.get_by_asset(
            end=0,
            period="h",
            start=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loans_originated = await response.parse()
        assert_matches_type(LoansOriginatedGetByAssetResponse, loans_originated, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.analytics.market.history.loans_originated.with_streaming_response.get_by_asset(
            end=0,
            period="h",
            start=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loans_originated = await response.parse()
            assert_matches_type(LoansOriginatedGetByAssetResponse, loans_originated, path=["response"])

        assert cast(Any, response.is_closed) is True
