# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types import (
    UserGetUserResponse,
    UserGetTxHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_tx_history(self, client: NeptuneAPIV2) -> None:
        user = client.user.get_tx_history(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(UserGetTxHistoryResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_tx_history_with_all_params(self, client: NeptuneAPIV2) -> None:
        user = client.user.get_tx_history(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
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
        response = client.user.with_raw_response.get_tx_history(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserGetTxHistoryResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_tx_history(self, client: NeptuneAPIV2) -> None:
        with client.user.with_streaming_response.get_tx_history(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
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
            client.user.with_raw_response.get_tx_history(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_user(self, client: NeptuneAPIV2) -> None:
        user = client.user.get_user(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(UserGetUserResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_user_with_all_params(self, client: NeptuneAPIV2) -> None:
        user = client.user.get_user(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            with_percent=True,
            with_text=True,
            with_value=True,
        )
        assert_matches_type(UserGetUserResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_user(self, client: NeptuneAPIV2) -> None:
        response = client.user.with_raw_response.get_user(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserGetUserResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_user(self, client: NeptuneAPIV2) -> None:
        with client.user.with_streaming_response.get_user(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserGetUserResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_user(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.with_raw_response.get_user(
                address="",
            )


class TestAsyncUser:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_tx_history(self, async_client: AsyncNeptuneAPIV2) -> None:
        user = await async_client.user.get_tx_history(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(UserGetTxHistoryResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_tx_history_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        user = await async_client.user.get_tx_history(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
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
        response = await async_client.user.with_raw_response.get_tx_history(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserGetTxHistoryResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_tx_history(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.with_streaming_response.get_tx_history(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
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
            await async_client.user.with_raw_response.get_tx_history(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_user(self, async_client: AsyncNeptuneAPIV2) -> None:
        user = await async_client.user.get_user(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(UserGetUserResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_user_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        user = await async_client.user.get_user(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            with_percent=True,
            with_text=True,
            with_value=True,
        )
        assert_matches_type(UserGetUserResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_user(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.with_raw_response.get_user(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserGetUserResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_user(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.with_streaming_response.get_user(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserGetUserResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_user(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.with_raw_response.get_user(
                address="",
            )
