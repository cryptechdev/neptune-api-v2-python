# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.swap import (
    RouteListAllResponse,
    RouteListByDenomResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_all(self, client: NeptuneAPIV2) -> None:
        route = client.swap.routes.list_all(
            contract_address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(RouteListAllResponse, route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_all(self, client: NeptuneAPIV2) -> None:
        response = client.swap.routes.with_raw_response.list_all(
            contract_address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteListAllResponse, route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_all(self, client: NeptuneAPIV2) -> None:
        with client.swap.routes.with_streaming_response.list_all(
            contract_address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteListAllResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_denom(self, client: NeptuneAPIV2) -> None:
        route = client.swap.routes.list_by_denom(
            contract_address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            source_denom="source_denom",
        )
        assert_matches_type(RouteListByDenomResponse, route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_by_denom(self, client: NeptuneAPIV2) -> None:
        response = client.swap.routes.with_raw_response.list_by_denom(
            contract_address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            source_denom="source_denom",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteListByDenomResponse, route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_by_denom(self, client: NeptuneAPIV2) -> None:
        with client.swap.routes.with_streaming_response.list_by_denom(
            contract_address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            source_denom="source_denom",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteListByDenomResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoutes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_all(self, async_client: AsyncNeptuneAPIV2) -> None:
        route = await async_client.swap.routes.list_all(
            contract_address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(RouteListAllResponse, route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_all(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.swap.routes.with_raw_response.list_all(
            contract_address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteListAllResponse, route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_all(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.swap.routes.with_streaming_response.list_all(
            contract_address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteListAllResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_denom(self, async_client: AsyncNeptuneAPIV2) -> None:
        route = await async_client.swap.routes.list_by_denom(
            contract_address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            source_denom="source_denom",
        )
        assert_matches_type(RouteListByDenomResponse, route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_by_denom(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.swap.routes.with_raw_response.list_by_denom(
            contract_address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            source_denom="source_denom",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteListByDenomResponse, route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_denom(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.swap.routes.with_streaming_response.list_by_denom(
            contract_address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            source_denom="source_denom",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteListByDenomResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True
