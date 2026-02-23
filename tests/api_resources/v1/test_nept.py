# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.v1 import (
    NeptGetTokenStateResponse,
    NeptGetTokenParamsResponse,
    NeptGetStakingOverviewResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNept:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_staking_overview(self, client: NeptuneAPIV2) -> None:
        nept = client.v1.nept.get_staking_overview()
        assert_matches_type(NeptGetStakingOverviewResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_staking_overview_with_all_params(self, client: NeptuneAPIV2) -> None:
        nept = client.v1.nept.get_staking_overview(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(NeptGetStakingOverviewResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_staking_overview(self, client: NeptuneAPIV2) -> None:
        response = client.v1.nept.with_raw_response.get_staking_overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nept = response.parse()
        assert_matches_type(NeptGetStakingOverviewResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_staking_overview(self, client: NeptuneAPIV2) -> None:
        with client.v1.nept.with_streaming_response.get_staking_overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nept = response.parse()
            assert_matches_type(NeptGetStakingOverviewResponse, nept, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_token_params(self, client: NeptuneAPIV2) -> None:
        nept = client.v1.nept.get_token_params()
        assert_matches_type(NeptGetTokenParamsResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_token_params_with_all_params(self, client: NeptuneAPIV2) -> None:
        nept = client.v1.nept.get_token_params(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(NeptGetTokenParamsResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_token_params(self, client: NeptuneAPIV2) -> None:
        response = client.v1.nept.with_raw_response.get_token_params()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nept = response.parse()
        assert_matches_type(NeptGetTokenParamsResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_token_params(self, client: NeptuneAPIV2) -> None:
        with client.v1.nept.with_streaming_response.get_token_params() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nept = response.parse()
            assert_matches_type(NeptGetTokenParamsResponse, nept, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_token_state(self, client: NeptuneAPIV2) -> None:
        nept = client.v1.nept.get_token_state()
        assert_matches_type(NeptGetTokenStateResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_token_state_with_all_params(self, client: NeptuneAPIV2) -> None:
        nept = client.v1.nept.get_token_state(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(NeptGetTokenStateResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_token_state(self, client: NeptuneAPIV2) -> None:
        response = client.v1.nept.with_raw_response.get_token_state()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nept = response.parse()
        assert_matches_type(NeptGetTokenStateResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_token_state(self, client: NeptuneAPIV2) -> None:
        with client.v1.nept.with_streaming_response.get_token_state() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nept = response.parse()
            assert_matches_type(NeptGetTokenStateResponse, nept, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNept:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_staking_overview(self, async_client: AsyncNeptuneAPIV2) -> None:
        nept = await async_client.v1.nept.get_staking_overview()
        assert_matches_type(NeptGetStakingOverviewResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_staking_overview_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        nept = await async_client.v1.nept.get_staking_overview(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(NeptGetStakingOverviewResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_staking_overview(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.nept.with_raw_response.get_staking_overview()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nept = await response.parse()
        assert_matches_type(NeptGetStakingOverviewResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_staking_overview(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.nept.with_streaming_response.get_staking_overview() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nept = await response.parse()
            assert_matches_type(NeptGetStakingOverviewResponse, nept, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_token_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        nept = await async_client.v1.nept.get_token_params()
        assert_matches_type(NeptGetTokenParamsResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_token_params_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        nept = await async_client.v1.nept.get_token_params(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(NeptGetTokenParamsResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_token_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.nept.with_raw_response.get_token_params()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nept = await response.parse()
        assert_matches_type(NeptGetTokenParamsResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_token_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.nept.with_streaming_response.get_token_params() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nept = await response.parse()
            assert_matches_type(NeptGetTokenParamsResponse, nept, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_token_state(self, async_client: AsyncNeptuneAPIV2) -> None:
        nept = await async_client.v1.nept.get_token_state()
        assert_matches_type(NeptGetTokenStateResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_token_state_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        nept = await async_client.v1.nept.get_token_state(
            with_text=True,
            with_value=True,
        )
        assert_matches_type(NeptGetTokenStateResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_token_state(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.nept.with_raw_response.get_token_state()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nept = await response.parse()
        assert_matches_type(NeptGetTokenStateResponse, nept, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_token_state(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.nept.with_streaming_response.get_token_state() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nept = await response.parse()
            assert_matches_type(NeptGetTokenStateResponse, nept, path=["response"])

        assert cast(Any, response.is_closed) is True
