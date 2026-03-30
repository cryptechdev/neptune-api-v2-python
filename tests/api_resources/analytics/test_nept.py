# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.analytics import NeptUnlocksDistributionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNept:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unlocks_distribution(self, client: NeptuneAPIV2) -> None:
        nept = client.analytics.nept.unlocks_distribution()
        assert_matches_type(NeptUnlocksDistributionResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unlocks_distribution_with_all_params(self, client: NeptuneAPIV2) -> None:
        nept = client.analytics.nept.unlocks_distribution(
            with_percent=True,
            with_text=True,
            with_value=True,
        )
        assert_matches_type(NeptUnlocksDistributionResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unlocks_distribution(self, client: NeptuneAPIV2) -> None:
        response = client.analytics.nept.with_raw_response.unlocks_distribution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nept = response.parse()
        assert_matches_type(NeptUnlocksDistributionResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unlocks_distribution(self, client: NeptuneAPIV2) -> None:
        with client.analytics.nept.with_streaming_response.unlocks_distribution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nept = response.parse()
            assert_matches_type(NeptUnlocksDistributionResponse, nept, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNept:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unlocks_distribution(self, async_client: AsyncNeptuneAPIV2) -> None:
        nept = await async_client.analytics.nept.unlocks_distribution()
        assert_matches_type(NeptUnlocksDistributionResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unlocks_distribution_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        nept = await async_client.analytics.nept.unlocks_distribution(
            with_percent=True,
            with_text=True,
            with_value=True,
        )
        assert_matches_type(NeptUnlocksDistributionResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unlocks_distribution(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.analytics.nept.with_raw_response.unlocks_distribution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nept = await response.parse()
        assert_matches_type(NeptUnlocksDistributionResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unlocks_distribution(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.analytics.nept.with_streaming_response.unlocks_distribution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nept = await response.parse()
            assert_matches_type(NeptUnlocksDistributionResponse, nept, path=["response"])

        assert cast(Any, response.is_closed) is True
