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
    MarketGetParamsResponse,
    MarketOverviewResponse,
)
```

Methods:

- <code title="get /api/v1/markets/config">client.v1.markets.<a href="./src/neptune_api_v2/resources/v1/markets/markets.py">get_params</a>(\*\*<a href="src/neptune_api_v2/types/v1/market_get_params_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/market_get_params_response.py">MarketGetParamsResponse</a></code>
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
    BorrowGetRateHistoryResponse,
    BorrowOverviewResponse,
)
```

Methods:

- <code title="get /api/v1/markets/borrow/rate-history">client.v1.markets.borrow.<a href="./src/neptune_api_v2/resources/v1/markets/borrow/borrow.py">get_rate_history</a>(\*\*<a href="src/neptune_api_v2/types/v1/markets/borrow_get_rate_history_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/markets/borrow_get_rate_history_response.py">BorrowGetRateHistoryResponse</a></code>
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
    NeptGetParamsResponse,
    NeptGetStakingOverviewResponse,
    NeptGetStateResponse,
)
```

Methods:

- <code title="get /api/v1/nept/params">client.v1.nept.<a href="./src/neptune_api_v2/resources/v1/nept.py">get_params</a>(\*\*<a href="src/neptune_api_v2/types/v1/nept_get_params_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/nept_get_params_response.py">NeptGetParamsResponse</a></code>
- <code title="get /api/v1/nept/staking">client.v1.nept.<a href="./src/neptune_api_v2/resources/v1/nept.py">get_staking_overview</a>(\*\*<a href="src/neptune_api_v2/types/v1/nept_get_staking_overview_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/nept_get_staking_overview_response.py">NeptGetStakingOverviewResponse</a></code>
- <code title="get /api/v1/nept/state">client.v1.nept.<a href="./src/neptune_api_v2/resources/v1/nept.py">get_state</a>(\*\*<a href="src/neptune_api_v2/types/v1/nept_get_state_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/nept_get_state_response.py">NeptGetStateResponse</a></code>

## Users

Types:

```python
from neptune_api_v2.types.v1 import EventAction, UserRetrieveResponse, UserGetTxHistoryResponse
```

Methods:

- <code title="get /api/v1/users/{address}/user">client.v1.users.<a href="./src/neptune_api_v2/resources/v1/users/users.py">retrieve</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/user_retrieve_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="get /api/v1/users/{address}/tx-history">client.v1.users.<a href="./src/neptune_api_v2/resources/v1/users/users.py">get_tx_history</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/user_get_tx_history_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/user_get_tx_history_response.py">UserGetTxHistoryResponse</a></code>

### Markets

Types:

```python
from neptune_api_v2.types.v1.users import UserMarket, MarketGetPortfolioResponse
```

Methods:

- <code title="get /api/v1/users/{address}/markets">client.v1.users.markets.<a href="./src/neptune_api_v2/resources/v1/users/markets/markets.py">get_portfolio</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/market_get_portfolio_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/market_get_portfolio_response.py">MarketGetPortfolioResponse</a></code>

#### Lend

Types:

```python
from neptune_api_v2.types.v1.users.markets import (
    UserDebtAssetPool,
    LendGetPortfolioResponse,
    LendLookupDistributionResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/lend">client.v1.users.markets.lend.<a href="./src/neptune_api_v2/resources/v1/users/markets/lend.py">get_portfolio</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/lend_get_portfolio_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/lend_get_portfolio_response.py">LendGetPortfolioResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/lend/lookup">client.v1.users.markets.lend.<a href="./src/neptune_api_v2/resources/v1/users/markets/lend.py">lookup_distribution</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/lend_lookup_distribution_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/lend_lookup_distribution_response.py">LendLookupDistributionResponse</a></code>

#### Borrow

Types:

```python
from neptune_api_v2.types.v1.users.markets import BorrowGetPortfolioResponse
```

Methods:

- <code title="get /api/v1/users/{address}/markets/borrow">client.v1.users.markets.borrow.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/borrow.py">get_portfolio</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow_get_portfolio_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow_get_portfolio_response.py">BorrowGetPortfolioResponse</a></code>

##### Accounts

Types:

```python
from neptune_api_v2.types.v1.users.markets.borrow import (
    UserAccountHealth,
    UserBorrowMarketAccount,
    UserCollateralAssetPool,
    AccountRetrieveResponse,
    AccountGetCollateralsResponse,
    AccountGetDebtsResponse,
    AccountGetHealthResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/borrow/accounts/{index}">client.v1.users.markets.borrow.accounts.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/accounts.py">retrieve</a>(index, \*, address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/account_retrieve_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/accounts/{index}/collaterals">client.v1.users.markets.borrow.accounts.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/accounts.py">get_collaterals</a>(index, \*, address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/account_get_collaterals_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/account_get_collaterals_response.py">AccountGetCollateralsResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/accounts/{index}/debts">client.v1.users.markets.borrow.accounts.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/accounts.py">get_debts</a>(index, \*, address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/account_get_debts_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/account_get_debts_response.py">AccountGetDebtsResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/accounts/{index}/health">client.v1.users.markets.borrow.accounts.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/accounts.py">get_health</a>(index, \*, address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/account_get_health_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/account_get_health_response.py">AccountGetHealthResponse</a></code>

##### Sum

Types:

```python
from neptune_api_v2.types.v1.users.markets.borrow import (
    SumGetCollateralsResponse,
    SumGetDebtsResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/borrow/sum/collaterals">client.v1.users.markets.borrow.sum.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/sum.py">get_collaterals</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/sum_get_collaterals_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/sum_get_collaterals_response.py">SumGetCollateralsResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/sum/debts">client.v1.users.markets.borrow.sum.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/sum.py">get_debts</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/sum_get_debts_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/sum_get_debts_response.py">SumGetDebtsResponse</a></code>

##### Lookup

Types:

```python
from neptune_api_v2.types.v1.users.markets.borrow import (
    LookupGetCollateralAccountsResponse,
    LookupGetDebtAccountsResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/borrow/lookup/collateral">client.v1.users.markets.borrow.lookup.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/lookup.py">get_collateral_accounts</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/lookup_get_collateral_accounts_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/lookup_get_collateral_accounts_response.py">LookupGetCollateralAccountsResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/lookup/debt">client.v1.users.markets.borrow.lookup.<a href="./src/neptune_api_v2/resources/v1/users/markets/borrow/lookup.py">get_debt_accounts</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/borrow/lookup_get_debt_accounts_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/borrow/lookup_get_debt_accounts_response.py">LookupGetDebtAccountsResponse</a></code>

#### Merged

Types:

```python
from neptune_api_v2.types.v1.users.markets import (
    UserMergedMarket,
    MergedGetAllMarketsResponse,
    MergedLookupByAssetResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/merged">client.v1.users.markets.merged.<a href="./src/neptune_api_v2/resources/v1/users/markets/merged.py">get_all_markets</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/merged_get_all_markets_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/merged_get_all_markets_response.py">MergedGetAllMarketsResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/merged/lookup">client.v1.users.markets.merged.<a href="./src/neptune_api_v2/resources/v1/users/markets/merged.py">lookup_by_asset</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/markets/merged_lookup_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/markets/merged_lookup_by_asset_response.py">MergedLookupByAssetResponse</a></code>

### Nept

Types:

```python
from neptune_api_v2.types.v1.users import (
    UserNeptUnlockAmounts,
    UserNeptUnlockOverview,
    NeptGetUnlocksResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/nept/unlocks">client.v1.users.nept.<a href="./src/neptune_api_v2/resources/v1/users/nept/nept.py">get_unlocks</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/nept_get_unlocks_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/nept_get_unlocks_response.py">NeptGetUnlocksResponse</a></code>

#### Staking

Types:

```python
from neptune_api_v2.types.v1.users.nept import (
    UserStake,
    UserStakeUnbondingEntry,
    StakingGetOverviewResponse,
    StakingGetUnstakingPoolResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/nept/staking">client.v1.users.nept.staking.<a href="./src/neptune_api_v2/resources/v1/users/nept/staking/staking.py">get_overview</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/nept/staking_get_overview_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/nept/staking_get_overview_response.py">StakingGetOverviewResponse</a></code>
- <code title="get /api/v1/users/{address}/nept/staking/unstaking">client.v1.users.nept.staking.<a href="./src/neptune_api_v2/resources/v1/users/nept/staking/staking.py">get_unstaking_pool</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/nept/staking_get_unstaking_pool_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/nept/staking_get_unstaking_pool_response.py">StakingGetUnstakingPoolResponse</a></code>

##### Pools

Types:

```python
from neptune_api_v2.types.v1.users.nept.staking import (
    UserStakePool,
    PoolGetAllResponse,
    PoolLookupResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/nept/staking/pools">client.v1.users.nept.staking.pools.<a href="./src/neptune_api_v2/resources/v1/users/nept/staking/pools.py">get_all</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/nept/staking/pool_get_all_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/nept/staking/pool_get_all_response.py">PoolGetAllResponse</a></code>
- <code title="get /api/v1/users/{address}/nept/staking/pools/lookup">client.v1.users.nept.staking.pools.<a href="./src/neptune_api_v2/resources/v1/users/nept/staking/pools.py">lookup</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/nept/staking/pool_lookup_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/nept/staking/pool_lookup_response.py">PoolLookupResponse</a></code>

### Wallet

Types:

```python
from neptune_api_v2.types.v1.users import UserWalletPortfolio, WalletGetBalancesResponse
```

Methods:

- <code title="get /api/v1/users/{address}/wallet/balances">client.v1.users.wallet.<a href="./src/neptune_api_v2/resources/v1/users/wallet.py">get_balances</a>(address, \*\*<a href="src/neptune_api_v2/types/v1/users/wallet_get_balances_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/users/wallet_get_balances_response.py">WalletGetBalancesResponse</a></code>

## Analytics

### Market

Types:

```python
from neptune_api_v2.types.v1.analytics import MarketGetCurrentStateResponse
```

Methods:

- <code title="get /api/v1/analytics/market/state">client.v1.analytics.market.<a href="./src/neptune_api_v2/resources/v1/analytics/market/market.py">get_current_state</a>() -> <a href="./src/neptune_api_v2/types/v1/analytics/market_get_current_state_response.py">MarketGetCurrentStateResponse</a></code>

#### History

##### LoansOriginated

Types:

```python
from neptune_api_v2.types.v1.analytics.market.history import (
    LoansOriginatedGetAllResponse,
    LoansOriginatedGetByAssetResponse,
)
```

Methods:

- <code title="get /api/v1/analytics/market/history/loans-originated">client.v1.analytics.market.history.loans_originated.<a href="./src/neptune_api_v2/resources/v1/analytics/market/history/loans_originated.py">get_all</a>(\*\*<a href="src/neptune_api_v2/types/v1/analytics/market/history/loans_originated_get_all_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/analytics/market/history/loans_originated_get_all_response.py">LoansOriginatedGetAllResponse</a></code>
- <code title="get /api/v1/analytics/market/history/loans-originated/by-asset">client.v1.analytics.market.history.loans_originated.<a href="./src/neptune_api_v2/resources/v1/analytics/market/history/loans_originated.py">get_by_asset</a>(\*\*<a href="src/neptune_api_v2/types/v1/analytics/market/history/loans_originated_get_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/analytics/market/history/loans_originated_get_by_asset_response.py">LoansOriginatedGetByAssetResponse</a></code>

## Integrations

### Bantr

Types:

```python
from neptune_api_v2.types.v1.integrations import BantrGetTransactionsResponse
```

Methods:

- <code title="get /api/v1/integrations/bantr/transactions">client.v1.integrations.bantr.<a href="./src/neptune_api_v2/resources/v1/integrations/bantr.py">get_transactions</a>(\*\*<a href="src/neptune_api_v2/types/v1/integrations/bantr_get_transactions_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/v1/integrations/bantr_get_transactions_response.py">BantrGetTransactionsResponse</a></code>
