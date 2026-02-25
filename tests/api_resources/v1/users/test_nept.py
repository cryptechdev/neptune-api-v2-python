# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.v1.users import NeptGetUnlocksResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNept:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_unlocks(self, client: NeptuneAPIV2) -> None:
        nept = client.v1.users.nept.get_unlocks(
            address="address",
        )
        assert_matches_type(NeptGetUnlocksResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_unlocks_with_all_params(self, client: NeptuneAPIV2) -> None:
        nept = client.v1.users.nept.get_unlocks(
            address="address",
            with_percent=True,
            with_text=True,
            with_value=True,
        )
        assert_matches_type(NeptGetUnlocksResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_unlocks(self, client: NeptuneAPIV2) -> None:
        response = client.v1.users.nept.with_raw_response.get_unlocks(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nept = response.parse()
        assert_matches_type(NeptGetUnlocksResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_unlocks(self, client: NeptuneAPIV2) -> None:
        with client.v1.users.nept.with_streaming_response.get_unlocks(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nept = response.parse()
            assert_matches_type(NeptGetUnlocksResponse, nept, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_unlocks(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.v1.users.nept.with_raw_response.get_unlocks(
                address="",
            )


class TestAsyncNept:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_unlocks(self, async_client: AsyncNeptuneAPIV2) -> None:
        nept = await async_client.v1.users.nept.get_unlocks(
            address="address",
        )
        assert_matches_type(NeptGetUnlocksResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_unlocks_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        nept = await async_client.v1.users.nept.get_unlocks(
            address="address",
            with_percent=True,
            with_text=True,
            with_value=True,
        )
        assert_matches_type(NeptGetUnlocksResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_unlocks(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.users.nept.with_raw_response.get_unlocks(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nept = await response.parse()
        assert_matches_type(NeptGetUnlocksResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_unlocks(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.users.nept.with_streaming_response.get_unlocks(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nept = await response.parse()
            assert_matches_type(NeptGetUnlocksResponse, nept, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_unlocks(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.v1.users.nept.with_raw_response.get_unlocks(
                address="",
            )
