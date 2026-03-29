# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.user import (
    WalletGetBalancesResponse,
    WalletGetBalanceByAssetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWallet:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_balance_by_asset(self, client: NeptuneAPIV2) -> None:
        wallet = client.user.wallet.get_balance_by_asset(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(WalletGetBalanceByAssetResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_balance_by_asset_with_all_params(self, client: NeptuneAPIV2) -> None:
        wallet = client.user.wallet.get_balance_by_asset(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(WalletGetBalanceByAssetResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_balance_by_asset(self, client: NeptuneAPIV2) -> None:
        response = client.user.wallet.with_raw_response.get_balance_by_asset(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletGetBalanceByAssetResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_balance_by_asset(self, client: NeptuneAPIV2) -> None:
        with client.user.wallet.with_streaming_response.get_balance_by_asset(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletGetBalanceByAssetResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_balance_by_asset(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.wallet.with_raw_response.get_balance_by_asset(
                address="",
                asset_id="token;-K-//-//3-",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_balances(self, client: NeptuneAPIV2) -> None:
        wallet = client.user.wallet.get_balances(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(WalletGetBalancesResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_balances_with_all_params(self, client: NeptuneAPIV2) -> None:
        wallet = client.user.wallet.get_balances(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(WalletGetBalancesResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_balances(self, client: NeptuneAPIV2) -> None:
        response = client.user.wallet.with_raw_response.get_balances(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletGetBalancesResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_balances(self, client: NeptuneAPIV2) -> None:
        with client.user.wallet.with_streaming_response.get_balances(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletGetBalancesResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_balances(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.wallet.with_raw_response.get_balances(
                address="",
            )


class TestAsyncWallet:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_balance_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        wallet = await async_client.user.wallet.get_balance_by_asset(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(WalletGetBalanceByAssetResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_balance_by_asset_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        wallet = await async_client.user.wallet.get_balance_by_asset(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(WalletGetBalanceByAssetResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_balance_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.wallet.with_raw_response.get_balance_by_asset(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletGetBalanceByAssetResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_balance_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.wallet.with_streaming_response.get_balance_by_asset(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletGetBalanceByAssetResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_balance_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.wallet.with_raw_response.get_balance_by_asset(
                address="",
                asset_id="token;-K-//-//3-",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_balances(self, async_client: AsyncNeptuneAPIV2) -> None:
        wallet = await async_client.user.wallet.get_balances(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(WalletGetBalancesResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_balances_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        wallet = await async_client.user.wallet.get_balances(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(WalletGetBalancesResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_balances(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.wallet.with_raw_response.get_balances(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletGetBalancesResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_balances(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.wallet.with_streaming_response.get_balances(
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletGetBalancesResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_balances(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.wallet.with_raw_response.get_balances(
                address="",
            )
