# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.user.market import (
    BorrowGetPortfolioResponse,
    BorrowGetDebtsTotalsResponse,
    BorrowGetCollateralTotalsResponse,
    BorrowGetDebtAccountsByAssetResponse,
    BorrowGetCollateralAccountsByAssetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBorrow:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_collateral_accounts_by_asset(self, client: NeptuneAPIV2) -> None:
        borrow = client.user.market.borrow.get_collateral_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(BorrowGetCollateralAccountsByAssetResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_collateral_accounts_by_asset_with_all_params(self, client: NeptuneAPIV2) -> None:
        borrow = client.user.market.borrow.get_collateral_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(BorrowGetCollateralAccountsByAssetResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_collateral_accounts_by_asset(self, client: NeptuneAPIV2) -> None:
        response = client.user.market.borrow.with_raw_response.get_collateral_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = response.parse()
        assert_matches_type(BorrowGetCollateralAccountsByAssetResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_collateral_accounts_by_asset(self, client: NeptuneAPIV2) -> None:
        with client.user.market.borrow.with_streaming_response.get_collateral_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = response.parse()
            assert_matches_type(BorrowGetCollateralAccountsByAssetResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_collateral_accounts_by_asset(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.market.borrow.with_raw_response.get_collateral_accounts_by_asset(
                address="",
                asset_id="token;-K-//-//3-",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_collateral_totals(self, client: NeptuneAPIV2) -> None:
        borrow = client.user.market.borrow.get_collateral_totals(
            address="address",
        )
        assert_matches_type(BorrowGetCollateralTotalsResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_collateral_totals_with_all_params(self, client: NeptuneAPIV2) -> None:
        borrow = client.user.market.borrow.get_collateral_totals(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(BorrowGetCollateralTotalsResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_collateral_totals(self, client: NeptuneAPIV2) -> None:
        response = client.user.market.borrow.with_raw_response.get_collateral_totals(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = response.parse()
        assert_matches_type(BorrowGetCollateralTotalsResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_collateral_totals(self, client: NeptuneAPIV2) -> None:
        with client.user.market.borrow.with_streaming_response.get_collateral_totals(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = response.parse()
            assert_matches_type(BorrowGetCollateralTotalsResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_collateral_totals(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.market.borrow.with_raw_response.get_collateral_totals(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_debt_accounts_by_asset(self, client: NeptuneAPIV2) -> None:
        borrow = client.user.market.borrow.get_debt_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(BorrowGetDebtAccountsByAssetResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_debt_accounts_by_asset_with_all_params(self, client: NeptuneAPIV2) -> None:
        borrow = client.user.market.borrow.get_debt_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(BorrowGetDebtAccountsByAssetResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_debt_accounts_by_asset(self, client: NeptuneAPIV2) -> None:
        response = client.user.market.borrow.with_raw_response.get_debt_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = response.parse()
        assert_matches_type(BorrowGetDebtAccountsByAssetResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_debt_accounts_by_asset(self, client: NeptuneAPIV2) -> None:
        with client.user.market.borrow.with_streaming_response.get_debt_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = response.parse()
            assert_matches_type(BorrowGetDebtAccountsByAssetResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_debt_accounts_by_asset(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.market.borrow.with_raw_response.get_debt_accounts_by_asset(
                address="",
                asset_id="token;-K-//-//3-",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_debts_totals(self, client: NeptuneAPIV2) -> None:
        borrow = client.user.market.borrow.get_debts_totals(
            address="address",
        )
        assert_matches_type(BorrowGetDebtsTotalsResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_debts_totals_with_all_params(self, client: NeptuneAPIV2) -> None:
        borrow = client.user.market.borrow.get_debts_totals(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(BorrowGetDebtsTotalsResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_debts_totals(self, client: NeptuneAPIV2) -> None:
        response = client.user.market.borrow.with_raw_response.get_debts_totals(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = response.parse()
        assert_matches_type(BorrowGetDebtsTotalsResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_debts_totals(self, client: NeptuneAPIV2) -> None:
        with client.user.market.borrow.with_streaming_response.get_debts_totals(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = response.parse()
            assert_matches_type(BorrowGetDebtsTotalsResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_debts_totals(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.market.borrow.with_raw_response.get_debts_totals(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_portfolio(self, client: NeptuneAPIV2) -> None:
        borrow = client.user.market.borrow.get_portfolio(
            address="address",
        )
        assert_matches_type(BorrowGetPortfolioResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_portfolio_with_all_params(self, client: NeptuneAPIV2) -> None:
        borrow = client.user.market.borrow.get_portfolio(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(BorrowGetPortfolioResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_portfolio(self, client: NeptuneAPIV2) -> None:
        response = client.user.market.borrow.with_raw_response.get_portfolio(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = response.parse()
        assert_matches_type(BorrowGetPortfolioResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_portfolio(self, client: NeptuneAPIV2) -> None:
        with client.user.market.borrow.with_streaming_response.get_portfolio(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = response.parse()
            assert_matches_type(BorrowGetPortfolioResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_portfolio(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.market.borrow.with_raw_response.get_portfolio(
                address="",
            )


class TestAsyncBorrow:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_collateral_accounts_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        borrow = await async_client.user.market.borrow.get_collateral_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(BorrowGetCollateralAccountsByAssetResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_collateral_accounts_by_asset_with_all_params(
        self, async_client: AsyncNeptuneAPIV2
    ) -> None:
        borrow = await async_client.user.market.borrow.get_collateral_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(BorrowGetCollateralAccountsByAssetResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_collateral_accounts_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.market.borrow.with_raw_response.get_collateral_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = await response.parse()
        assert_matches_type(BorrowGetCollateralAccountsByAssetResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_collateral_accounts_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.market.borrow.with_streaming_response.get_collateral_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = await response.parse()
            assert_matches_type(BorrowGetCollateralAccountsByAssetResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_collateral_accounts_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.market.borrow.with_raw_response.get_collateral_accounts_by_asset(
                address="",
                asset_id="token;-K-//-//3-",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_collateral_totals(self, async_client: AsyncNeptuneAPIV2) -> None:
        borrow = await async_client.user.market.borrow.get_collateral_totals(
            address="address",
        )
        assert_matches_type(BorrowGetCollateralTotalsResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_collateral_totals_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        borrow = await async_client.user.market.borrow.get_collateral_totals(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(BorrowGetCollateralTotalsResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_collateral_totals(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.market.borrow.with_raw_response.get_collateral_totals(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = await response.parse()
        assert_matches_type(BorrowGetCollateralTotalsResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_collateral_totals(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.market.borrow.with_streaming_response.get_collateral_totals(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = await response.parse()
            assert_matches_type(BorrowGetCollateralTotalsResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_collateral_totals(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.market.borrow.with_raw_response.get_collateral_totals(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_debt_accounts_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        borrow = await async_client.user.market.borrow.get_debt_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        )
        assert_matches_type(BorrowGetDebtAccountsByAssetResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_debt_accounts_by_asset_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        borrow = await async_client.user.market.borrow.get_debt_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(BorrowGetDebtAccountsByAssetResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_debt_accounts_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.market.borrow.with_raw_response.get_debt_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = await response.parse()
        assert_matches_type(BorrowGetDebtAccountsByAssetResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_debt_accounts_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.market.borrow.with_streaming_response.get_debt_accounts_by_asset(
            address="address",
            asset_id="token;-K-//-//3-",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = await response.parse()
            assert_matches_type(BorrowGetDebtAccountsByAssetResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_debt_accounts_by_asset(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.market.borrow.with_raw_response.get_debt_accounts_by_asset(
                address="",
                asset_id="token;-K-//-//3-",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_debts_totals(self, async_client: AsyncNeptuneAPIV2) -> None:
        borrow = await async_client.user.market.borrow.get_debts_totals(
            address="address",
        )
        assert_matches_type(BorrowGetDebtsTotalsResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_debts_totals_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        borrow = await async_client.user.market.borrow.get_debts_totals(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(BorrowGetDebtsTotalsResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_debts_totals(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.market.borrow.with_raw_response.get_debts_totals(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = await response.parse()
        assert_matches_type(BorrowGetDebtsTotalsResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_debts_totals(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.market.borrow.with_streaming_response.get_debts_totals(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = await response.parse()
            assert_matches_type(BorrowGetDebtsTotalsResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_debts_totals(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.market.borrow.with_raw_response.get_debts_totals(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_portfolio(self, async_client: AsyncNeptuneAPIV2) -> None:
        borrow = await async_client.user.market.borrow.get_portfolio(
            address="address",
        )
        assert_matches_type(BorrowGetPortfolioResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_portfolio_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        borrow = await async_client.user.market.borrow.get_portfolio(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(BorrowGetPortfolioResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_portfolio(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.market.borrow.with_raw_response.get_portfolio(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        borrow = await response.parse()
        assert_matches_type(BorrowGetPortfolioResponse, borrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_portfolio(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.market.borrow.with_streaming_response.get_portfolio(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            borrow = await response.parse()
            assert_matches_type(BorrowGetPortfolioResponse, borrow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_portfolio(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.market.borrow.with_raw_response.get_portfolio(
                address="",
            )
