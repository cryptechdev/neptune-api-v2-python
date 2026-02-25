# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.v1 import (
    UserRetrieveResponse,
    UserGetTxHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: NeptuneAPIV2) -> None:
        user = client.v1.users.retrieve(
            address="address",
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: NeptuneAPIV2) -> None:
        user = client.v1.users.retrieve(
            address="address",
            with_percent=True,
            with_text=True,
            with_value=True,
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: NeptuneAPIV2) -> None:
        response = client.v1.users.with_raw_response.retrieve(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: NeptuneAPIV2) -> None:
        with client.v1.users.with_streaming_response.retrieve(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.v1.users.with_raw_response.retrieve(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_tx_history(self, client: NeptuneAPIV2) -> None:
        user = client.v1.users.get_tx_history(
            address="address",
        )
        assert_matches_type(UserGetTxHistoryResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_tx_history_with_all_params(self, client: NeptuneAPIV2) -> None:
        user = client.v1.users.get_tx_history(
            address="address",
            action="borrow_flash_loan",
            limit=1,
            prev_event_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort_order="asc",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(UserGetTxHistoryResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_tx_history(self, client: NeptuneAPIV2) -> None:
        response = client.v1.users.with_raw_response.get_tx_history(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserGetTxHistoryResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_tx_history(self, client: NeptuneAPIV2) -> None:
        with client.v1.users.with_streaming_response.get_tx_history(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserGetTxHistoryResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_tx_history(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.v1.users.with_raw_response.get_tx_history(
                address="",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNeptuneAPIV2) -> None:
        user = await async_client.v1.users.retrieve(
            address="address",
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        user = await async_client.v1.users.retrieve(
            address="address",
            with_percent=True,
            with_text=True,
            with_value=True,
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.users.with_raw_response.retrieve(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.users.with_streaming_response.retrieve(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.v1.users.with_raw_response.retrieve(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_tx_history(self, async_client: AsyncNeptuneAPIV2) -> None:
        user = await async_client.v1.users.get_tx_history(
            address="address",
        )
        assert_matches_type(UserGetTxHistoryResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_tx_history_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        user = await async_client.v1.users.get_tx_history(
            address="address",
            action="borrow_flash_loan",
            limit=1,
            prev_event_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort_order="asc",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(UserGetTxHistoryResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_tx_history(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.users.with_raw_response.get_tx_history(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserGetTxHistoryResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_tx_history(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.users.with_streaming_response.get_tx_history(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserGetTxHistoryResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_tx_history(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.v1.users.with_raw_response.get_tx_history(
                address="",
            )
