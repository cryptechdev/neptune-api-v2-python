# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.integrations import BantrGetTransactionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBantr:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_transactions(self, client: NeptuneAPIV2) -> None:
        bantr = client.integrations.bantr.get_transactions(
            end_block=0,
            start_block=0,
        )
        assert_matches_type(BantrGetTransactionsResponse, bantr, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_transactions_with_all_params(self, client: NeptuneAPIV2) -> None:
        bantr = client.integrations.bantr.get_transactions(
            end_block=0,
            start_block=0,
            limit=0,
        )
        assert_matches_type(BantrGetTransactionsResponse, bantr, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_transactions(self, client: NeptuneAPIV2) -> None:
        response = client.integrations.bantr.with_raw_response.get_transactions(
            end_block=0,
            start_block=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bantr = response.parse()
        assert_matches_type(BantrGetTransactionsResponse, bantr, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_transactions(self, client: NeptuneAPIV2) -> None:
        with client.integrations.bantr.with_streaming_response.get_transactions(
            end_block=0,
            start_block=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bantr = response.parse()
            assert_matches_type(BantrGetTransactionsResponse, bantr, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBantr:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_transactions(self, async_client: AsyncNeptuneAPIV2) -> None:
        bantr = await async_client.integrations.bantr.get_transactions(
            end_block=0,
            start_block=0,
        )
        assert_matches_type(BantrGetTransactionsResponse, bantr, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_transactions_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        bantr = await async_client.integrations.bantr.get_transactions(
            end_block=0,
            start_block=0,
            limit=0,
        )
        assert_matches_type(BantrGetTransactionsResponse, bantr, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_transactions(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.integrations.bantr.with_raw_response.get_transactions(
            end_block=0,
            start_block=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bantr = await response.parse()
        assert_matches_type(BantrGetTransactionsResponse, bantr, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_transactions(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.integrations.bantr.with_streaming_response.get_transactions(
            end_block=0,
            start_block=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bantr = await response.parse()
            assert_matches_type(BantrGetTransactionsResponse, bantr, path=["response"])

        assert cast(Any, response.is_closed) is True
