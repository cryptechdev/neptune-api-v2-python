# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.analytics import MarketGetCurrentStateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarket:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_current_state(self, client: NeptuneAPIV2) -> None:
        market = client.analytics.market.get_current_state()
        assert_matches_type(MarketGetCurrentStateResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_current_state(self, client: NeptuneAPIV2) -> None:
        response = client.analytics.market.with_raw_response.get_current_state()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(MarketGetCurrentStateResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_current_state(self, client: NeptuneAPIV2) -> None:
        with client.analytics.market.with_streaming_response.get_current_state() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(MarketGetCurrentStateResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMarket:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_current_state(self, async_client: AsyncNeptuneAPIV2) -> None:
        market = await async_client.analytics.market.get_current_state()
        assert_matches_type(MarketGetCurrentStateResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_current_state(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.analytics.market.with_raw_response.get_current_state()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(MarketGetCurrentStateResponse, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_current_state(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.analytics.market.with_streaming_response.get_current_state() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(MarketGetCurrentStateResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True
