# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from neptune_api_v2 import NeptuneAPIV2, AsyncNeptuneAPIV2
from neptune_api_v2.types.user.nept import (
    StakingGetOverviewResponse,
    StakingGetUnstakingResponse,
    StakingGetStakingPoolResponse,
    StakingGetStakingPoolsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStaking:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_overview(self, client: NeptuneAPIV2) -> None:
        staking = client.user.nept.staking.get_overview(
            address="address",
        )
        assert_matches_type(StakingGetOverviewResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_overview_with_all_params(self, client: NeptuneAPIV2) -> None:
        staking = client.user.nept.staking.get_overview(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(StakingGetOverviewResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_overview(self, client: NeptuneAPIV2) -> None:
        response = client.user.nept.staking.with_raw_response.get_overview(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staking = response.parse()
        assert_matches_type(StakingGetOverviewResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_overview(self, client: NeptuneAPIV2) -> None:
        with client.user.nept.staking.with_streaming_response.get_overview(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staking = response.parse()
            assert_matches_type(StakingGetOverviewResponse, staking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_overview(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.nept.staking.with_raw_response.get_overview(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_staking_pool(self, client: NeptuneAPIV2) -> None:
        staking = client.user.nept.staking.get_staking_pool(
            address="address",
        )
        assert_matches_type(StakingGetStakingPoolResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_staking_pool_with_all_params(self, client: NeptuneAPIV2) -> None:
        staking = client.user.nept.staking.get_staking_pool(
            address="address",
            duration=0,
            index=0,
            with_text=True,
            with_value=True,
        )
        assert_matches_type(StakingGetStakingPoolResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_staking_pool(self, client: NeptuneAPIV2) -> None:
        response = client.user.nept.staking.with_raw_response.get_staking_pool(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staking = response.parse()
        assert_matches_type(StakingGetStakingPoolResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_staking_pool(self, client: NeptuneAPIV2) -> None:
        with client.user.nept.staking.with_streaming_response.get_staking_pool(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staking = response.parse()
            assert_matches_type(StakingGetStakingPoolResponse, staking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_staking_pool(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.nept.staking.with_raw_response.get_staking_pool(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_staking_pools(self, client: NeptuneAPIV2) -> None:
        staking = client.user.nept.staking.get_staking_pools(
            address="address",
        )
        assert_matches_type(StakingGetStakingPoolsResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_staking_pools_with_all_params(self, client: NeptuneAPIV2) -> None:
        staking = client.user.nept.staking.get_staking_pools(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(StakingGetStakingPoolsResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_staking_pools(self, client: NeptuneAPIV2) -> None:
        response = client.user.nept.staking.with_raw_response.get_staking_pools(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staking = response.parse()
        assert_matches_type(StakingGetStakingPoolsResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_staking_pools(self, client: NeptuneAPIV2) -> None:
        with client.user.nept.staking.with_streaming_response.get_staking_pools(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staking = response.parse()
            assert_matches_type(StakingGetStakingPoolsResponse, staking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_staking_pools(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.nept.staking.with_raw_response.get_staking_pools(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_unstaking(self, client: NeptuneAPIV2) -> None:
        staking = client.user.nept.staking.get_unstaking(
            address="address",
        )
        assert_matches_type(StakingGetUnstakingResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_unstaking_with_all_params(self, client: NeptuneAPIV2) -> None:
        staking = client.user.nept.staking.get_unstaking(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(StakingGetUnstakingResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_unstaking(self, client: NeptuneAPIV2) -> None:
        response = client.user.nept.staking.with_raw_response.get_unstaking(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staking = response.parse()
        assert_matches_type(StakingGetUnstakingResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_unstaking(self, client: NeptuneAPIV2) -> None:
        with client.user.nept.staking.with_streaming_response.get_unstaking(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staking = response.parse()
            assert_matches_type(StakingGetUnstakingResponse, staking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_unstaking(self, client: NeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.user.nept.staking.with_raw_response.get_unstaking(
                address="",
            )


class TestAsyncStaking:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_overview(self, async_client: AsyncNeptuneAPIV2) -> None:
        staking = await async_client.user.nept.staking.get_overview(
            address="address",
        )
        assert_matches_type(StakingGetOverviewResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_overview_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        staking = await async_client.user.nept.staking.get_overview(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(StakingGetOverviewResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_overview(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.nept.staking.with_raw_response.get_overview(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staking = await response.parse()
        assert_matches_type(StakingGetOverviewResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_overview(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.nept.staking.with_streaming_response.get_overview(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staking = await response.parse()
            assert_matches_type(StakingGetOverviewResponse, staking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_overview(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.nept.staking.with_raw_response.get_overview(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_staking_pool(self, async_client: AsyncNeptuneAPIV2) -> None:
        staking = await async_client.user.nept.staking.get_staking_pool(
            address="address",
        )
        assert_matches_type(StakingGetStakingPoolResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_staking_pool_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        staking = await async_client.user.nept.staking.get_staking_pool(
            address="address",
            duration=0,
            index=0,
            with_text=True,
            with_value=True,
        )
        assert_matches_type(StakingGetStakingPoolResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_staking_pool(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.nept.staking.with_raw_response.get_staking_pool(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staking = await response.parse()
        assert_matches_type(StakingGetStakingPoolResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_staking_pool(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.nept.staking.with_streaming_response.get_staking_pool(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staking = await response.parse()
            assert_matches_type(StakingGetStakingPoolResponse, staking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_staking_pool(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.nept.staking.with_raw_response.get_staking_pool(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_staking_pools(self, async_client: AsyncNeptuneAPIV2) -> None:
        staking = await async_client.user.nept.staking.get_staking_pools(
            address="address",
        )
        assert_matches_type(StakingGetStakingPoolsResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_staking_pools_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        staking = await async_client.user.nept.staking.get_staking_pools(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(StakingGetStakingPoolsResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_staking_pools(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.nept.staking.with_raw_response.get_staking_pools(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staking = await response.parse()
        assert_matches_type(StakingGetStakingPoolsResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_staking_pools(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.nept.staking.with_streaming_response.get_staking_pools(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staking = await response.parse()
            assert_matches_type(StakingGetStakingPoolsResponse, staking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_staking_pools(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.nept.staking.with_raw_response.get_staking_pools(
                address="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_unstaking(self, async_client: AsyncNeptuneAPIV2) -> None:
        staking = await async_client.user.nept.staking.get_unstaking(
            address="address",
        )
        assert_matches_type(StakingGetUnstakingResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_unstaking_with_all_params(self, async_client: AsyncNeptuneAPIV2) -> None:
        staking = await async_client.user.nept.staking.get_unstaking(
            address="address",
            with_text=True,
            with_value=True,
        )
        assert_matches_type(StakingGetUnstakingResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_unstaking(self, async_client: AsyncNeptuneAPIV2) -> None:
        response = await async_client.user.nept.staking.with_raw_response.get_unstaking(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        staking = await response.parse()
        assert_matches_type(StakingGetUnstakingResponse, staking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_unstaking(self, async_client: AsyncNeptuneAPIV2) -> None:
        async with async_client.user.nept.staking.with_streaming_response.get_unstaking(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            staking = await response.parse()
            assert_matches_type(StakingGetUnstakingResponse, staking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_unstaking(self, async_client: AsyncNeptuneAPIV2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.user.nept.staking.with_raw_response.get_unstaking(
                address="",
            )
