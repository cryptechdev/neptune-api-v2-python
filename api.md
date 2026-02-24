# V1

## Status

Types:

```python
from neptune_api_v2.types.v1 import StatusCheckHealthResponse
```

Methods:

- <code title="get /api/v1/status/health">client.v1.status.<a href="./src/neptune_api_v2/resources/v1/status.py">check_health</a>() -> <a href="./src/neptune_api_v2/types/v1/status_check_health_response.py">StatusCheckHealthResponse</a></code>

## Assets

Types:

```python
from neptune_api_v2.types.v1 import (
    AssetClassification,
    AssetInfo,
    AssetMetadata,
    AssetSpec,
    ErrorData,
    Interval,
    IntervalUnit,
    AssetListResponse,
    AssetGetPriceHistoryResponse,
    AssetListPricesResponse,
)
```

Methods:

- <code title="get /api/v1/assets">client.v1.assets.<a href="./src/neptune_api_v2/resources/v1/assets.py">list</a>() -> <a href="./src/neptune_api_v2/types/v1/asset_list_response.py">AssetListResponse</a></code>
- <code title="get /api/v1/assets/price-history">client.v1.assets.<a href="./src/neptune_api_v2/resources/v1/assets.py">get_price_history</a>(\*\*<a href="src/neptune_api_v2/types/v1/asset_get_price_history_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/asset_get_price_history_response.py">AssetGetPriceHistoryResponse</a></code>
- <code title="get /api/v1/assets/prices">client.v1.assets.<a href="./src/neptune_api_v2/resources/v1/assets.py">list_prices</a>(\*\*<a href="src/neptune_api_v2/types/v1/asset_list_prices_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/asset_list_prices_response.py">AssetListPricesResponse</a></code>

## Markets

Types:

```python
from neptune_api_v2.types.v1 import (
    GlobalMarketConfig,
    MarketGetMarketParamsResponse,
    MarketOverviewResponse,
)
```

Methods:

- <code title="get /api/v1/markets/config">client.v1.markets.<a href="./src/neptune_api_v2/resources/v1/markets/markets.py">get_market_params</a>(\*\*<a href="src/neptune_api_v2/types/v1/market_get_market_params_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/market_get_market_params_response.py">MarketGetMarketParamsResponse</a></code>
- <code title="get /api/v1/markets">client.v1.markets.<a href="./src/neptune_api_v2/resources/v1/markets/markets.py">overview</a>(\*\*<a href="src/neptune_api_v2/types/v1/market_overview_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/market_overview_response.py">MarketOverviewResponse</a></code>

### Merged

Types:

```python
from neptune_api_v2.types.v1.markets import (
    MergedMarket,
    MergedGetMergedDataResponse,
    MergedLookupByAssetResponse,
)
```

Methods:

- <code title="get /api/v1/markets/merged">client.v1.markets.merged.<a href="./src/neptune_api_v2/resources/v1/markets/merged.py">get_merged_data</a>(\*\*<a href="src/neptune_api_v2/types/v1/markets/merged_get_merged_data_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/markets/merged_get_merged_data_response.py">MergedGetMergedDataResponse</a></code>
- <code title="get /api/v1/markets/merged/lookup">client.v1.markets.merged.<a href="./src/neptune_api_v2/resources/v1/markets/merged.py">lookup_by_asset</a>(\*\*<a href="src/neptune_api_v2/types/v1/markets/merged_lookup_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/markets/merged_lookup_by_asset_response.py">MergedLookupByAssetResponse</a></code>

### Lend

Types:

```python
from neptune_api_v2.types.v1.markets import (
    AssetRateHistory,
    LendMarket,
    LendMarketState,
    MarketRate,
    LendGetLendingMarketsResponse,
    LendGetRateHistoryResponse,
    LendLookupByAssetResponse,
)
```

Methods:

- <code title="get /api/v1/markets/lend">client.v1.markets.lend.<a href="./src/neptune_api_v2/resources/v1/markets/lend.py">get_lending_markets</a>(\*\*<a href="src/neptune_api_v2/types/v1/markets/lend_get_lending_markets_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/markets/lend_get_lending_markets_response.py">LendGetLendingMarketsResponse</a></code>
- <code title="get /api/v1/markets/lend/rate-history">client.v1.markets.lend.<a href="./src/neptune_api_v2/resources/v1/markets/lend.py">get_rate_history</a>(\*\*<a href="src/neptune_api_v2/types/v1/markets/lend_get_rate_history_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/markets/lend_get_rate_history_response.py">LendGetRateHistoryResponse</a></code>
- <code title="get /api/v1/markets/lend/lookup">client.v1.markets.lend.<a href="./src/neptune_api_v2/resources/v1/markets/lend.py">lookup_by_asset</a>(\*\*<a href="src/neptune_api_v2/types/v1/markets/lend_lookup_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/markets/lend_lookup_by_asset_response.py">LendLookupByAssetResponse</a></code>

### Borrow

Types:

```python
from neptune_api_v2.types.v1.markets import (
    BorrowMarketOverview,
    BorrowGetBorrowRateHistoryResponse,
    BorrowOverviewResponse,
)
```

Methods:

- <code title="get /api/v1/markets/borrow/rate-history">client.v1.markets.borrow.<a href="./src/neptune_api_v2/resources/v1/markets/borrow/borrow.py">get_borrow_rate_history</a>(\*\*<a href="src/neptune_api_v2/types/v1/markets/borrow_get_borrow_rate_history_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/markets/borrow_get_borrow_rate_history_response.py">BorrowGetBorrowRateHistoryResponse</a></code>
- <code title="get /api/v1/markets/borrow">client.v1.markets.borrow.<a href="./src/neptune_api_v2/resources/v1/markets/borrow/borrow.py">overview</a>(\*\*<a href="src/neptune_api_v2/types/v1/markets/borrow_overview_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/markets/borrow_overview_response.py">BorrowOverviewResponse</a></code>

#### Collaterals

Types:

```python
from neptune_api_v2.types.v1.markets.borrow import (
    BorrowCollateralConfig,
    BorrowCollateralMarket,
    BorrowCollateralState,
    CollateralListResponse,
    CollateralLookupByAssetResponse,
)
```

Methods:

- <code title="get /api/v1/markets/borrow/collaterals">client.v1.markets.borrow.collaterals.<a href="./src/neptune_api_v2/resources/v1/markets/borrow/collaterals.py">list</a>(\*\*<a href="src/neptune_api_v2/types/v1/markets/borrow/collateral_list_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/markets/borrow/collateral_list_response.py">CollateralListResponse</a></code>
- <code title="get /api/v1/markets/borrow/collaterals/lookup">client.v1.markets.borrow.collaterals.<a href="./src/neptune_api_v2/resources/v1/markets/borrow/collaterals.py">lookup_by_asset</a>(\*\*<a href="src/neptune_api_v2/types/v1/markets/borrow/collateral_lookup_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/markets/borrow/collateral_lookup_by_asset_response.py">CollateralLookupByAssetResponse</a></code>

#### Debts

Types:

```python
from neptune_api_v2.types.v1.markets.borrow import (
    BorrowDebtConfig,
    BorrowDebtMarket,
    BorrowDebtState,
    DebtListResponse,
    DebtLookupByAssetResponse,
)
```

Methods:

- <code title="get /api/v1/markets/borrow/debts">client.v1.markets.borrow.debts.<a href="./src/neptune_api_v2/resources/v1/markets/borrow/debts.py">list</a>(\*\*<a href="src/neptune_api_v2/types/v1/markets/borrow/debt_list_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/markets/borrow/debt_list_response.py">DebtListResponse</a></code>
- <code title="get /api/v1/markets/borrow/debts/lookup">client.v1.markets.borrow.debts.<a href="./src/neptune_api_v2/resources/v1/markets/borrow/debts.py">lookup_by_asset</a>(\*\*<a href="src/neptune_api_v2/types/v1/markets/borrow/debt_lookup_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/markets/borrow/debt_lookup_by_asset_response.py">DebtLookupByAssetResponse</a></code>

## Nept

Types:

```python
from neptune_api_v2.types.v1 import (
    Duration,
    StakingPoolFull,
    StakingPoolParams,
    StakingPoolState,
    NeptGetStakingOverviewResponse,
    NeptGetTokenParamsResponse,
    NeptGetTokenStateResponse,
)
```

Methods:

- <code title="get /api/v1/nept/staking">client.v1.nept.<a href="./src/neptune_api_v2/resources/v1/nept.py">get_staking_overview</a>(\*\*<a href="src/neptune_api_v2/types/v1/nept_get_staking_overview_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/nept_get_staking_overview_response.py">NeptGetStakingOverviewResponse</a></code>
- <code title="get /api/v1/nept/params">client.v1.nept.<a href="./src/neptune_api_v2/resources/v1/nept.py">get_token_params</a>(\*\*<a href="src/neptune_api_v2/types/v1/nept_get_token_params_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/nept_get_token_params_response.py">NeptGetTokenParamsResponse</a></code>
- <code title="get /api/v1/nept/state">client.v1.nept.<a href="./src/neptune_api_v2/resources/v1/nept.py">get_token_state</a>(\*\*<a href="src/neptune_api_v2/types/v1/nept_get_token_state_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/nept_get_token_state_response.py">NeptGetTokenStateResponse</a></code>

## Users

Types:

```python
from neptune_api_v2.types.v1 import (
    EventAction,
    UserRetrieveTxHistoryResponse,
    UserRetrieveUserResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/tx-history">client.v1.users.<a href="./src/neptune_api_v2/resources/v1/users/users.py">retrieve_tx_history</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/user_retrieve_tx_history_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/user_retrieve_tx_history_response.py">UserRetrieveTxHistoryResponse</a></code>
- <code title="get /api/v1/users/{address}/user">client.v1.users.<a href="./src/neptune_api_v2/resources/v1/users/users.py">retrieve_user</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/user_retrieve_user_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/user_retrieve_user_response.py">UserRetrieveUserResponse</a></code>

### Markets

Types:

```python
from neptune_api_v2.types.v1.users import UserMarket, MarketListResponse
```

Methods:

- <code title="get /api/v1/users/{address}/markets">client.v1.users.markets.<a href="./src/neptune_api_v2/resources/v1/users/markets/markets.py">list</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/market_list_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/market_list_response.py">MarketListResponse</a></code>

#### Lend

Types:

```python
from neptune_api_v2.types.v1.users.markets import (
    UserDebtAssetPool,
    LendListResponse,
    LendRetrieveLookupResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/lend">client.v1.users.markets.lend.<a href="./src/neptune_api_v2/resources/v1/users/markets/lend.py">list</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/lend_list_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/lend_list_response.py">LendListResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/lend/lookup">client.v1.users.markets.lend.<a href="./src/neptune_api_v2/resources/v1/users/markets/lend.py">retrieve_lookup</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/lend_retrieve_lookup_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/lend_retrieve_lookup_response.py">LendRetrieveLookupResponse</a></code>

#### Borrow

Types:

```python
from neptune_api_v2.types.v1.users.markets import BorrowListResponse
```

Methods:

- <code title="get /api/v1/users/{address}/markets/borrow">client.v1.users.markets.borrow.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/borrow.py">list</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow_list_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow_list_response.py">BorrowListResponse</a></code>

##### Accounts

Types:

```python
from neptune_api_v2.types.v1.users.markets.borrow import (
    UserAccountHealth,
    UserBorrowMarketAccount,
    UserCollateralAssetPool,
    AccountRetrieveResponse,
    AccountRetrieveCollateralsResponse,
    AccountRetrieveDebtsResponse,
    AccountRetrieveHealthResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/borrow/accounts/{index}">client.v1.users.markets.borrow.accounts.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/accounts.py">retrieve</a>(index, \*, address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/account_retrieve_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/accounts/{index}/collaterals">client.v1.users.markets.borrow.accounts.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/accounts.py">retrieve_collaterals</a>(index, \*, address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/account_retrieve_collaterals_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/account_retrieve_collaterals_response.py">AccountRetrieveCollateralsResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/accounts/{index}/debts">client.v1.users.markets.borrow.accounts.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/accounts.py">retrieve_debts</a>(index, \*, address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/account_retrieve_debts_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/account_retrieve_debts_response.py">AccountRetrieveDebtsResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/accounts/{index}/health">client.v1.users.markets.borrow.accounts.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/accounts.py">retrieve_health</a>(index, \*, address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/account_retrieve_health_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/account_retrieve_health_response.py">AccountRetrieveHealthResponse</a></code>

##### Sum

Types:

```python
from neptune_api_v2.types.v1.users.markets.borrow import (
    SumRetrieveCollateralsResponse,
    SumRetrieveDebtsResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/borrow/sum/collaterals">client.v1.users.markets.borrow.sum.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/sum.py">retrieve_collaterals</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/sum_retrieve_collaterals_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/sum_retrieve_collaterals_response.py">SumRetrieveCollateralsResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/sum/debts">client.v1.users.markets.borrow.sum.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/sum.py">retrieve_debts</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/sum_retrieve_debts_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/sum_retrieve_debts_response.py">SumRetrieveDebtsResponse</a></code>

##### Lookup

Types:

```python
from neptune_api_v2.types.v1.users.markets.borrow import (
    LookupRetrieveCollateralResponse,
    LookupRetrieveDebtResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/borrow/lookup/collateral">client.v1.users.markets.borrow.lookup.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/lookup.py">retrieve_collateral</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/lookup_retrieve_collateral_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/lookup_retrieve_collateral_response.py">LookupRetrieveCollateralResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/lookup/debt">client.v1.users.markets.borrow.lookup.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/lookup.py">retrieve_debt</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/lookup_retrieve_debt_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/lookup_retrieve_debt_response.py">LookupRetrieveDebtResponse</a></code>

#### Merged

Types:

```python
from neptune_api_v2.types.v1.users.markets import (
    UserMergedMarket,
    MergedListResponse,
    MergedRetrieveLookupResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/merged">client.v1.users.markets.merged.<a href="./src/neptune_api_v2/resources/v1/users/markets/merged.py">list</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/merged_list_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/merged_list_response.py">MergedListResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/merged/lookup">client.v1.users.markets.merged.<a href="./src/neptune_api_v2/resources/v1/users/markets/merged.py">retrieve_lookup</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/merged_retrieve_lookup_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/merged_retrieve_lookup_response.py">MergedRetrieveLookupResponse</a></code>

### Nept

Types:

```python
from neptune_api_v2.types.v1.users import (
    UserNeptUnlockAmounts,
    UserNeptUnlockOverview,
    NeptRetrieveUnlocksResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/nept/unlocks">client.v1.users.nept.<a href="./src/neptune_api_v2/resources/v1/users/nept/nept.py">retrieve_unlocks</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/nept_retrieve_unlocks_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/nept_retrieve_unlocks_response.py">NeptRetrieveUnlocksResponse</a></code>

#### Staking

Types:

```python
from neptune_api_v2.types.v1.users.nept import (
    UserStake,
    UserStakeUnbondingEntry,
    StakingListResponse,
    StakingRetrieveUnstakingResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/nept/staking">client.v1.users.nept.staking.<a href="./src/neptune_api_v2/resources/v1/users/nept/staking/staking.py">list</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/nept/staking_list_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/nept/staking_list_response.py">StakingListResponse</a></code>
- <code title="get /api/v1/users/{address}/nept/staking/unstaking">client.v1.users.nept.staking.<a href="./src/neptune_api_v2/resources/v1/users/nept/staking/staking.py">retrieve_unstaking</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/nept/staking_retrieve_unstaking_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/nept/staking_retrieve_unstaking_response.py">StakingRetrieveUnstakingResponse</a></code>

##### Pools

Types:

```python
from neptune_api_v2.types.v1.users.nept.staking import (
    UserStakePool,
    PoolListResponse,
    PoolRetrieveLookupResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/nept/staking/pools">client.v1.users.nept.staking.pools.<a href="./src/neptune_api_v2/resources/v1/users/nept/staking/pools.py">list</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/nept/staking/pool_list_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/nept/staking/pool_list_response.py">PoolListResponse</a></code>
- <code title="get /api/v1/users/{address}/nept/staking/pools/lookup">client.v1.users.nept.staking.pools.<a href="./src/neptune_api_v2/resources/v1/users/nept/staking/pools.py">retrieve_lookup</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/nept/staking/pool_retrieve_lookup_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/nept/staking/pool_retrieve_lookup_response.py">PoolRetrieveLookupResponse</a></code>

### Wallet

Types:

```python
from neptune_api_v2.types.v1.users import UserWalletPortfolio, WalletRetrieveBalancesResponse
```

Methods:

- <code title="get /api/v1/users/{address}/wallet/balances">client.v1.users.wallet.<a href="./src/neptune_api_v2/resources/v1/users/wallet.py">retrieve_balances</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/wallet_retrieve_balances_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/wallet_retrieve_balances_response.py">WalletRetrieveBalancesResponse</a></code>

## Analytics

### Market

Types:

```python
from neptune_api_v2.types.v1.analytics import MarketRetrieveStateResponse
```

Methods:

- <code title="get /api/v1/analytics/market/state">client.v1.analytics.market.<a href="./src/neptune_api_v2/resources/v1/analytics/market/market.py">retrieve_state</a>() -> <a href="./src/neptune_api_v2/types/v1/analytics/market_retrieve_state_response.py">MarketRetrieveStateResponse</a></code>

#### History

##### LoansOriginated

Types:

```python
from neptune_api_v2.types.v1.analytics.market.history import (
    LoansOriginatedRetrieveByAssetResponse,
    LoansOriginatedRetrieveLoansOriginatedResponse,
)
```

Methods:

- <code title="get /api/v1/analytics/market/history/loans-originated/by-asset">client.v1.analytics.market.history.loans_originated.<a href="./src/neptune_api_v2/resources/v1/analytics/market/history/loans_originated.py">retrieve_by_asset</a>(\*\*<a href="src/neptune_api_v2/types/v1/analytics/market/history/loans_originated_retrieve_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/analytics/market/history/loans_originated_retrieve_by_asset_response.py">LoansOriginatedRetrieveByAssetResponse</a></code>
- <code title="get /api/v1/analytics/market/history/loans-originated">client.v1.analytics.market.history.loans_originated.<a href="./src/neptune_api_v2/resources/v1/analytics/market/history/loans_originated.py">retrieve_loans_originated</a>(\*\*<a href="src/neptune_api_v2/types/v1/analytics/market/history/loans_originated_retrieve_loans_originated_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/analytics/market/history/loans_originated_retrieve_loans_originated_response.py">LoansOriginatedRetrieveLoansOriginatedResponse</a></code>

## Integrations

### Bantr

Types:

```python
from neptune_api_v2.types.v1.integrations import BantrRetrieveTransactionsResponse
```

Methods:

- <code title="get /api/v1/integrations/bantr/transactions">client.v1.integrations.bantr.<a href="./src/neptune_api_v2/resources/v1/integrations/bantr.py">retrieve_transactions</a>(\*\*<a href="src/neptune_api_v2/types/v1/integrations/bantr_retrieve_transactions_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/integrations/bantr_retrieve_transactions_response.py">BantrRetrieveTransactionsResponse</a></code>
