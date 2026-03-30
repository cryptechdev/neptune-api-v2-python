# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.user.market.borrow import (
    SubaccountGetSubaccountResponse,
    SubaccountGetSubaccountDebtsResponse,
    SubaccountGetSubaccountHealthResponse,
    SubaccountGetSubaccountCollateralsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubaccount:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subaccount(self, client: NeptuneAPIV2) -> None:
        subaccount = client.user.market.borrow.subaccount.get_subaccount(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(SubaccountGetSubaccountResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subaccount_with_all_params(self, client: NeptuneAPIV2) -> None:
        subaccount = client.user.market.borrow.subaccount.get_subaccount(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(SubaccountGetSubaccountResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_subaccount(self, client: NeptuneAPIV2) -> None:
        response = client.user.market.borrow.subaccount.with_raw_response.get_subaccount(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subaccount = response.parse()
        assert_matches_type(SubaccountGetSubaccountResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_subaccount(self, client: NeptuneAPIV2) -> None:
        with client.user.market.borrow.subaccount.with_streaming_response.get_subaccount(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subaccount = response.parse()
            assert_matches_type(SubaccountGetSubaccountResponse, subaccount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_subaccount(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.market.borrow.subaccount.with_raw_response.get_subaccount(
                index=0,
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subaccount_collaterals(self, client: NeptuneAPIV2) -> None:
        subaccount = client.user.market.borrow.subaccount.get_subaccount_collaterals(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(SubaccountGetSubaccountCollateralsResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subaccount_collaterals_with_all_params(self, client: NeptuneAPIV2) -> None:
        subaccount = client.user.market.borrow.subaccount.get_subaccount_collaterals(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(SubaccountGetSubaccountCollateralsResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_subaccount_collaterals(self, client: NeptuneAPIV2) -> None:
        response = client.user.market.borrow.subaccount.with_raw_response.get_subaccount_collaterals(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subaccount = response.parse()
        assert_matches_type(SubaccountGetSubaccountCollateralsResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_subaccount_collaterals(self, client: NeptuneAPIV2) -> None:
        with client.user.market.borrow.subaccount.with_streaming_response.get_subaccount_collaterals(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subaccount = response.parse()
            assert_matches_type(SubaccountGetSubaccountCollateralsResponse, subaccount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_subaccount_collaterals(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.market.borrow.subaccount.with_raw_response.get_subaccount_collaterals(
                index=0,
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subaccount_debts(self, client: NeptuneAPIV2) -> None:
        subaccount = client.user.market.borrow.subaccount.get_subaccount_debts(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(SubaccountGetSubaccountDebtsResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subaccount_debts_with_all_params(self, client: NeptuneAPIV2) -> None:
        subaccount = client.user.market.borrow.subaccount.get_subaccount_debts(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(SubaccountGetSubaccountDebtsResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_subaccount_debts(self, client: NeptuneAPIV2) -> None:
        response = client.user.market.borrow.subaccount.with_raw_response.get_subaccount_debts(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subaccount = response.parse()
        assert_matches_type(SubaccountGetSubaccountDebtsResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_subaccount_debts(self, client: NeptuneAPIV2) -> None:
        with client.user.market.borrow.subaccount.with_streaming_response.get_subaccount_debts(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subaccount = response.parse()
            assert_matches_type(SubaccountGetSubaccountDebtsResponse, subaccount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_subaccount_debts(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.market.borrow.subaccount.with_raw_response.get_subaccount_debts(
                index=0,
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subaccount_health(self, client: NeptuneAPIV2) -> None:
        subaccount = client.user.market.borrow.subaccount.get_subaccount_health(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(SubaccountGetSubaccountHealthResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subaccount_health_with_all_params(self, client: NeptuneAPIV2) -> None:
        subaccount = client.user.market.borrow.subaccount.get_subaccount_health(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            with_text=True,
        )
        assert_matches_type(SubaccountGetSubaccountHealthResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_subaccount_health(self, client: NeptuneAPIV2) -> None:
        response = client.user.market.borrow.subaccount.with_raw_response.get_subaccount_health(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subaccount = response.parse()
        assert_matches_type(SubaccountGetSubaccountHealthResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_subaccount_health(self, client: NeptuneAPIV2) -> None:
        with client.user.market.borrow.subaccount.with_streaming_response.get_subaccount_health(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subaccount = response.parse()
            assert_matches_type(SubaccountGetSubaccountHealthResponse, subaccount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_subaccount_health(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.market.borrow.subaccount.with_raw_response.get_subaccount_health(
                index=0,
                address="",
            )


class TestAsyncSubaccount:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subaccount(self, async_client: AsyncNeptuneAPIV2) -> None:
        subaccount = await async_client.user.market.borrow.subaccount.get_subaccount(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(SubaccountGetSubaccountResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subaccount_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        subaccount = await async_client.user.market.borrow.subaccount.get_subaccount(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(SubaccountGetSubaccountResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_subaccount(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.market.borrow.subaccount.with_raw_response.get_subaccount(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subaccount = await response.parse()
        assert_matches_type(SubaccountGetSubaccountResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_subaccount(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.market.borrow.subaccount.with_streaming_response.get_subaccount(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subaccount = await response.parse()
            assert_matches_type(SubaccountGetSubaccountResponse, subaccount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_subaccount(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.market.borrow.subaccount.with_raw_response.get_subaccount(
                index=0,
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subaccount_collaterals(self, async_client: AsyncNeptuneAPIV2) -> None:
        subaccount = await async_client.user.market.borrow.subaccount.get_subaccount_collaterals(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(SubaccountGetSubaccountCollateralsResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subaccount_collaterals_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        subaccount = await async_client.user.market.borrow.subaccount.get_subaccount_collaterals(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(SubaccountGetSubaccountCollateralsResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_subaccount_collaterals(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.market.borrow.subaccount.with_raw_response.get_subaccount_collaterals(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subaccount = await response.parse()
        assert_matches_type(SubaccountGetSubaccountCollateralsResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_subaccount_collaterals(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.market.borrow.subaccount.with_streaming_response.get_subaccount_collaterals(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subaccount = await response.parse()
            assert_matches_type(SubaccountGetSubaccountCollateralsResponse, subaccount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_subaccount_collaterals(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.market.borrow.subaccount.with_raw_response.get_subaccount_collaterals(
                index=0,
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subaccount_debts(self, async_client: AsyncNeptuneAPIV2) -> None:
        subaccount = await async_client.user.market.borrow.subaccount.get_subaccount_debts(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(SubaccountGetSubaccountDebtsResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subaccount_debts_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        subaccount = await async_client.user.market.borrow.subaccount.get_subaccount_debts(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(SubaccountGetSubaccountDebtsResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_subaccount_debts(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.market.borrow.subaccount.with_raw_response.get_subaccount_debts(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subaccount = await response.parse()
        assert_matches_type(SubaccountGetSubaccountDebtsResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_subaccount_debts(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.market.borrow.subaccount.with_streaming_response.get_subaccount_debts(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subaccount = await response.parse()
            assert_matches_type(SubaccountGetSubaccountDebtsResponse, subaccount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_subaccount_debts(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.market.borrow.subaccount.with_raw_response.get_subaccount_debts(
                index=0,
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subaccount_health(self, async_client: AsyncNeptuneAPIV2) -> None:
        subaccount = await async_client.user.market.borrow.subaccount.get_subaccount_health(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )
        assert_matches_type(SubaccountGetSubaccountHealthResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subaccount_health_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        subaccount = await async_client.user.market.borrow.subaccount.get_subaccount_health(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
            with_text=True,
        )
        assert_matches_type(SubaccountGetSubaccountHealthResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_subaccount_health(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.market.borrow.subaccount.with_raw_response.get_subaccount_health(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subaccount = await response.parse()
        assert_matches_type(SubaccountGetSubaccountHealthResponse, subaccount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_subaccount_health(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.market.borrow.subaccount.with_streaming_response.get_subaccount_health(
            index=0,
            address="injvalcons1a03k0ztfyjnd70apawva003pkh0adqmau0a9q0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subaccount = await response.parse()
            assert_matches_type(SubaccountGetSubaccountHealthResponse, subaccount, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_subaccount_health(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.market.borrow.subaccount.with_raw_response.get_subaccount_health(
                index=0,
                address="",
            )
