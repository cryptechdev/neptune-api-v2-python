# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.v1.users.markets.borrow import (
    AccountRetrieveResponse,
    AccountRetrieveDebtsResponse,
    AccountRetrieveHealthResponse,
    AccountRetrieveCollateralsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: NeptuneAPIV2) -> None:
        account = client.v1.users.markets.borrow.accounts.retrieve(
            index=0,
            address="address",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: NeptuneAPIV2) -> None:
        account = client.v1.users.markets.borrow.accounts.retrieve(
            index=0,
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: NeptuneAPIV2) -> None:
        response = client.v1.users.markets.borrow.accounts.with_raw_response.retrieve(
            index=0,
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: NeptuneAPIV2) -> None:
        with client.v1.users.markets.borrow.accounts.with_streaming_response.retrieve(
            index=0,
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.v1.users.markets.borrow.accounts.with_raw_response.retrieve(
                index=0,
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_collaterals(self, client: NeptuneAPIV2) -> None:
        account = client.v1.users.markets.borrow.accounts.retrieve_collaterals(
            index=0,
            address="address",
        )
        assert_matches_type(AccountRetrieveCollateralsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_collaterals_with_all_params(self, client: NeptuneAPIV2) -> None:
        account = client.v1.users.markets.borrow.accounts.retrieve_collaterals(
            index=0,
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(AccountRetrieveCollateralsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_collaterals(self, client: NeptuneAPIV2) -> None:
        response = client.v1.users.markets.borrow.accounts.with_raw_response.retrieve_collaterals(
            index=0,
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveCollateralsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_collaterals(self, client: NeptuneAPIV2) -> None:
        with client.v1.users.markets.borrow.accounts.with_streaming_response.retrieve_collaterals(
            index=0,
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveCollateralsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_collaterals(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.v1.users.markets.borrow.accounts.with_raw_response.retrieve_collaterals(
                index=0,
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_debts(self, client: NeptuneAPIV2) -> None:
        account = client.v1.users.markets.borrow.accounts.retrieve_debts(
            index=0,
            address="address",
        )
        assert_matches_type(AccountRetrieveDebtsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_debts_with_all_params(self, client: NeptuneAPIV2) -> None:
        account = client.v1.users.markets.borrow.accounts.retrieve_debts(
            index=0,
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(AccountRetrieveDebtsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_debts(self, client: NeptuneAPIV2) -> None:
        response = client.v1.users.markets.borrow.accounts.with_raw_response.retrieve_debts(
            index=0,
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveDebtsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_debts(self, client: NeptuneAPIV2) -> None:
        with client.v1.users.markets.borrow.accounts.with_streaming_response.retrieve_debts(
            index=0,
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveDebtsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_debts(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.v1.users.markets.borrow.accounts.with_raw_response.retrieve_debts(
                index=0,
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_health(self, client: NeptuneAPIV2) -> None:
        account = client.v1.users.markets.borrow.accounts.retrieve_health(
            index=0,
            address="address",
        )
        assert_matches_type(AccountRetrieveHealthResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_health_with_all_params(self, client: NeptuneAPIV2) -> None:
        account = client.v1.users.markets.borrow.accounts.retrieve_health(
            index=0,
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(AccountRetrieveHealthResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_health(self, client: NeptuneAPIV2) -> None:
        response = client.v1.users.markets.borrow.accounts.with_raw_response.retrieve_health(
            index=0,
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveHealthResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_health(self, client: NeptuneAPIV2) -> None:
        with client.v1.users.markets.borrow.accounts.with_streaming_response.retrieve_health(
            index=0,
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveHealthResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_health(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.v1.users.markets.borrow.accounts.with_raw_response.retrieve_health(
                index=0,
                address="",
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNeptuneAPIV2) -> None:
        account = await async_client.v1.users.markets.borrow.accounts.retrieve(
            index=0,
            address="address",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        account = await async_client.v1.users.markets.borrow.accounts.retrieve(
            index=0,
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.users.markets.borrow.accounts.with_raw_response.retrieve(
            index=0,
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.users.markets.borrow.accounts.with_streaming_response.retrieve(
            index=0,
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.v1.users.markets.borrow.accounts.with_raw_response.retrieve(
                index=0,
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_collaterals(self, async_client: AsyncNeptuneAPIV2) -> None:
        account = await async_client.v1.users.markets.borrow.accounts.retrieve_collaterals(
            index=0,
            address="address",
        )
        assert_matches_type(AccountRetrieveCollateralsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_collaterals_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        account = await async_client.v1.users.markets.borrow.accounts.retrieve_collaterals(
            index=0,
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(AccountRetrieveCollateralsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_collaterals(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.users.markets.borrow.accounts.with_raw_response.retrieve_collaterals(
            index=0,
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveCollateralsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_collaterals(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.users.markets.borrow.accounts.with_streaming_response.retrieve_collaterals(
            index=0,
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveCollateralsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_collaterals(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.v1.users.markets.borrow.accounts.with_raw_response.retrieve_collaterals(
                index=0,
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_debts(self, async_client: AsyncNeptuneAPIV2) -> None:
        account = await async_client.v1.users.markets.borrow.accounts.retrieve_debts(
            index=0,
            address="address",
        )
        assert_matches_type(AccountRetrieveDebtsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_debts_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        account = await async_client.v1.users.markets.borrow.accounts.retrieve_debts(
            index=0,
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(AccountRetrieveDebtsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_debts(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.users.markets.borrow.accounts.with_raw_response.retrieve_debts(
            index=0,
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveDebtsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_debts(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.users.markets.borrow.accounts.with_streaming_response.retrieve_debts(
            index=0,
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveDebtsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_debts(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.v1.users.markets.borrow.accounts.with_raw_response.retrieve_debts(
                index=0,
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_health(self, async_client: AsyncNeptuneAPIV2) -> None:
        account = await async_client.v1.users.markets.borrow.accounts.retrieve_health(
            index=0,
            address="address",
        )
        assert_matches_type(AccountRetrieveHealthResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_health_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        account = await async_client.v1.users.markets.borrow.accounts.retrieve_health(
            index=0,
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(AccountRetrieveHealthResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_health(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.v1.users.markets.borrow.accounts.with_raw_response.retrieve_health(
            index=0,
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveHealthResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_health(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.v1.users.markets.borrow.accounts.with_streaming_response.retrieve_health(
            index=0,
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveHealthResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_health(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.v1.users.markets.borrow.accounts.with_raw_response.retrieve_health(
                index=0,
                address="",
            )
