# Core

Types:

```python
from neptune_api_v2.types import (
    ErrorData,
    ErrorDataVariants,
    ErrorKind,
    ErrorResponse,
    ErrorScope,
    FieldValidationError,
    Interval,
    IntervalUnit,
    ValidationErrorData,
    ValidationFieldSource,
)
```

# Status

Types:

```python
from neptune_api_v2.types import StatusCheckHealthResponse
```

Methods:

- <code title="get /api/v1/status/health">client.status.<a href="./src/neptune_api_v2/resources/status.py">check_health</a>() -> <a href="./src/neptune_api_v2/types/status_check_health_response.py">StatusCheckHealthResponse</a></code>

# Assets

Types:

```python
from neptune_api_v2.types import (
    AssetClassification,
    AssetInfo,
    AssetMetadata,
    AssetPrice,
    AssetPriceHistory,
    AssetRateHistory,
    AssetSpec,
    AssetListResponse,
    AssetGetPriceHistoryResponse,
    AssetListPricesResponse,
)
```

Methods:

- <code title="get /api/v1/assets">client.assets.<a href="./src/neptune_api_v2/resources/assets.py">list</a>() -> <a href="./src/neptune_api_v2/types/asset_list_response.py">AssetListResponse</a></code>
- <code title="get /api/v1/assets/price-history">client.assets.<a href="./src/neptune_api_v2/resources/assets.py">get_price_history</a>(\*\*<a href="src/neptune_api_v2/types/asset_get_price_history_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/asset_get_price_history_response.py">AssetGetPriceHistoryResponse</a></code>
- <code title="get /api/v1/assets/prices">client.assets.<a href="./src/neptune_api_v2/resources/assets.py">list_prices</a>(\*\*<a href="src/neptune_api_v2/types/asset_list_prices_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/asset_list_prices_response.py">AssetListPricesResponse</a></code>

# Markets

Types:

```python
from neptune_api_v2.types import (
    GlobalMarketConfig,
    MarketRate,
    MergedMarket,
    MarketGetMergedResponse,
    MarketGetMergedByAssetResponse,
    MarketGetOverviewResponse,
    MarketGetParamsResponse,
)
```

Methods:

- <code title="get /api/v1/markets/merged">client.markets.<a href="./src/neptune_api_v2/resources/markets/markets.py">get_merged</a>(\*\*<a href="src/neptune_api_v2/types/market_get_merged_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/market_get_merged_response.py">MarketGetMergedResponse</a></code>
- <code title="get /api/v1/markets/merged/lookup">client.markets.<a href="./src/neptune_api_v2/resources/markets/markets.py">get_merged_by_asset</a>(\*\*<a href="src/neptune_api_v2/types/market_get_merged_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/market_get_merged_by_asset_response.py">MarketGetMergedByAssetResponse</a></code>
- <code title="get /api/v1/markets">client.markets.<a href="./src/neptune_api_v2/resources/markets/markets.py">get_overview</a>(\*\*<a href="src/neptune_api_v2/types/market_get_overview_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/market_get_overview_response.py">MarketGetOverviewResponse</a></code>
- <code title="get /api/v1/markets/config">client.markets.<a href="./src/neptune_api_v2/resources/markets/markets.py">get_params</a>(\*\*<a href="src/neptune_api_v2/types/market_get_params_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/market_get_params_response.py">MarketGetParamsResponse</a></code>

## Lend

Types:

```python
from neptune_api_v2.types.markets import (
    LendMarket,
    LendMarketData,
    LendMarketState,
    LendListResponse,
    LendGetByAssetResponse,
    LendGetRateHistoryResponse,
)
```

Methods:

- <code title="get /api/v1/markets/lend">client.markets.lend.<a href="./src/neptune_api_v2/resources/markets/lend.py">list</a>(\*\*<a href="src/neptune_api_v2/types/markets/lend_list_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/markets/lend_list_response.py">LendListResponse</a></code>
- <code title="get /api/v1/markets/lend/lookup">client.markets.lend.<a href="./src/neptune_api_v2/resources/markets/lend.py">get_by_asset</a>(\*\*<a href="src/neptune_api_v2/types/markets/lend_get_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/markets/lend_get_by_asset_response.py">LendGetByAssetResponse</a></code>
- <code title="get /api/v1/markets/lend/rate-history">client.markets.lend.<a href="./src/neptune_api_v2/resources/markets/lend.py">get_rate_history</a>(\*\*<a href="src/neptune_api_v2/types/markets/lend_get_rate_history_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/markets/lend_get_rate_history_response.py">LendGetRateHistoryResponse</a></code>

## Borrow

Types:

```python
from neptune_api_v2.types.markets import (
    BorrowMarketOverview,
    BorrowGetOverviewResponse,
    BorrowGetRateHistoryResponse,
)
```

Methods:

- <code title="get /api/v1/markets/borrow">client.markets.borrow.<a href="./src/neptune_api_v2/resources/markets/borrow/borrow.py">get_overview</a>(\*\*<a href="src/neptune_api_v2/types/markets/borrow_get_overview_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/markets/borrow_get_overview_response.py">BorrowGetOverviewResponse</a></code>
- <code title="get /api/v1/markets/borrow/rate-history">client.markets.borrow.<a href="./src/neptune_api_v2/resources/markets/borrow/borrow.py">get_rate_history</a>(\*\*<a href="src/neptune_api_v2/types/markets/borrow_get_rate_history_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/markets/borrow_get_rate_history_response.py">BorrowGetRateHistoryResponse</a></code>

### Collaterals

Types:

```python
from neptune_api_v2.types.markets.borrow import (
    BorrowCollateralConfig,
    BorrowCollateralMarket,
    BorrowCollateralMarketData,
    BorrowCollateralState,
    CollateralListResponse,
    CollateralGetByAssetResponse,
)
```

Methods:

- <code title="get /api/v1/markets/borrow/collaterals">client.markets.borrow.collaterals.<a href="./src/neptune_api_v2/resources/markets/borrow/collaterals.py">list</a>(\*\*<a href="src/neptune_api_v2/types/markets/borrow/collateral_list_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/markets/borrow/collateral_list_response.py">CollateralListResponse</a></code>
- <code title="get /api/v1/markets/borrow/collaterals/lookup">client.markets.borrow.collaterals.<a href="./src/neptune_api_v2/resources/markets/borrow/collaterals.py">get_by_asset</a>(\*\*<a href="src/neptune_api_v2/types/markets/borrow/collateral_get_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/markets/borrow/collateral_get_by_asset_response.py">CollateralGetByAssetResponse</a></code>

### Debts

Types:

```python
from neptune_api_v2.types.markets.borrow import (
    BorrowDebtConfig,
    BorrowDebtMarket,
    BorrowDebtMarketData,
    BorrowDebtState,
    DebtListResponse,
    DebtGetByAssetResponse,
)
```

Methods:

- <code title="get /api/v1/markets/borrow/debts">client.markets.borrow.debts.<a href="./src/neptune_api_v2/resources/markets/borrow/debts.py">list</a>(\*\*<a href="src/neptune_api_v2/types/markets/borrow/debt_list_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/markets/borrow/debt_list_response.py">DebtListResponse</a></code>
- <code title="get /api/v1/markets/borrow/debts/lookup">client.markets.borrow.debts.<a href="./src/neptune_api_v2/resources/markets/borrow/debts.py">get_by_asset</a>(\*\*<a href="src/neptune_api_v2/types/markets/borrow/debt_get_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/markets/borrow/debt_get_by_asset_response.py">DebtGetByAssetResponse</a></code>

# Nept

Types:

```python
from neptune_api_v2.types import (
    NeptParams,
    NeptState,
    NeptUnlockDistributionGroup,
    StakingPoolFull,
    StakingPoolParams,
    StakingPoolState,
    NeptGetParamsResponse,
    NeptGetStakingOverviewResponse,
    NeptGetStateResponse,
)
```

Methods:

- <code title="get /api/v1/nept/params">client.nept.<a href="./src/neptune_api_v2/resources/nept.py">get_params</a>(\*\*<a href="src/neptune_api_v2/types/nept_get_params_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/nept_get_params_response.py">NeptGetParamsResponse</a></code>
- <code title="get /api/v1/nept/staking">client.nept.<a href="./src/neptune_api_v2/resources/nept.py">get_staking_overview</a>(\*\*<a href="src/neptune_api_v2/types/nept_get_staking_overview_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/nept_get_staking_overview_response.py">NeptGetStakingOverviewResponse</a></code>
- <code title="get /api/v1/nept/state">client.nept.<a href="./src/neptune_api_v2/resources/nept.py">get_state</a>(\*\*<a href="src/neptune_api_v2/types/nept_get_state_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/nept_get_state_response.py">NeptGetStateResponse</a></code>

# User

Types:

```python
from neptune_api_v2.types import EventAction, User, UserTx, UserGetUserResponse
```

Methods:

- <code title="get /api/v1/users/{address}/tx-history">client.user.<a href="./src/neptune_api_v2/resources/user/user.py">get_tx_history</a>(address, \*\*<a href="src/neptune_api_v2/types/user_get_tx_history_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user_tx.py">SyncTxHistoryPage[UserTx]</a></code>
- <code title="get /api/v1/users/{address}/user">client.user.<a href="./src/neptune_api_v2/resources/user/user.py">get_user</a>(address, \*\*<a href="src/neptune_api_v2/types/user_get_user_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user_get_user_response.py">UserGetUserResponse</a></code>

## Market

Types:

```python
from neptune_api_v2.types.user import (
    UserMarket,
    UserMergedMarket,
    MarketGetMergedResponse,
    MarketGetMergedByAssetResponse,
    MarketGetPortfolioResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/merged">client.user.market.<a href="./src/neptune_api_v2/resources/user/market/market.py">get_merged</a>(address, \*\*<a href="src/neptune_api_v2/types/user/market_get_merged_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market_get_merged_response.py">MarketGetMergedResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/merged/lookup">client.user.market.<a href="./src/neptune_api_v2/resources/user/market/market.py">get_merged_by_asset</a>(address, \*\*<a href="src/neptune_api_v2/types/user/market_get_merged_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market_get_merged_by_asset_response.py">MarketGetMergedByAssetResponse</a></code>
- <code title="get /api/v1/users/{address}/markets">client.user.market.<a href="./src/neptune_api_v2/resources/user/market/market.py">get_portfolio</a>(address, \*\*<a href="src/neptune_api_v2/types/user/market_get_portfolio_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market_get_portfolio_response.py">MarketGetPortfolioResponse</a></code>

### Lend

Types:

```python
from neptune_api_v2.types.user.market import (
    UserLendAssetPool,
    UserLendMarket,
    UserLendOriginAmounts,
    UserLendReceiptAmounts,
    LendListResponse,
    LendGetByAssetResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/lend">client.user.market.lend.<a href="./src/neptune_api_v2/resources/user/market/lend.py">list</a>(address, \*\*<a href="src/neptune_api_v2/types/user/market/lend_list_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market/lend_list_response.py">LendListResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/lend/lookup">client.user.market.lend.<a href="./src/neptune_api_v2/resources/user/market/lend.py">get_by_asset</a>(address, \*\*<a href="src/neptune_api_v2/types/user/market/lend_get_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market/lend_get_by_asset_response.py">LendGetByAssetResponse</a></code>

### Borrow

Types:

```python
from neptune_api_v2.types.user.market import (
    UserBorrowMarket,
    UserBorrowMarketPools,
    BorrowGetCollateralAccountsByAssetResponse,
    BorrowGetCollateralTotalsResponse,
    BorrowGetDebtAccountsByAssetResponse,
    BorrowGetDebtsTotalsResponse,
    BorrowGetPortfolioResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/borrow/lookup/collateral">client.user.market.borrow.<a href="./src/neptune_api_v2/resources/user/market/borrow/borrow.py">get_collateral_accounts_by_asset</a>(address, \*\*<a href="src/neptune_api_v2/types/user/market/borrow_get_collateral_accounts_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market/borrow_get_collateral_accounts_by_asset_response.py">BorrowGetCollateralAccountsByAssetResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/sum/collaterals">client.user.market.borrow.<a href="./src/neptune_api_v2/resources/user/market/borrow/borrow.py">get_collateral_totals</a>(address, \*\*<a href="src/neptune_api_v2/types/user/market/borrow_get_collateral_totals_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market/borrow_get_collateral_totals_response.py">BorrowGetCollateralTotalsResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/lookup/debt">client.user.market.borrow.<a href="./src/neptune_api_v2/resources/user/market/borrow/borrow.py">get_debt_accounts_by_asset</a>(address, \*\*<a href="src/neptune_api_v2/types/user/market/borrow_get_debt_accounts_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market/borrow_get_debt_accounts_by_asset_response.py">BorrowGetDebtAccountsByAssetResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/sum/debts">client.user.market.borrow.<a href="./src/neptune_api_v2/resources/user/market/borrow/borrow.py">get_debts_totals</a>(address, \*\*<a href="src/neptune_api_v2/types/user/market/borrow_get_debts_totals_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market/borrow_get_debts_totals_response.py">BorrowGetDebtsTotalsResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow">client.user.market.borrow.<a href="./src/neptune_api_v2/resources/user/market/borrow/borrow.py">get_portfolio</a>(address, \*\*<a href="src/neptune_api_v2/types/user/market/borrow_get_portfolio_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market/borrow_get_portfolio_response.py">BorrowGetPortfolioResponse</a></code>

#### Subaccount

Types:

```python
from neptune_api_v2.types.user.market.borrow import (
    UserAccountHealth,
    UserBorrowMarketAccount,
    UserCollateralAccountPool,
    UserCollateralAssetPool,
    UserDebtAccountPool,
    UserDebtAssetPool,
    SubaccountGetSubaccountResponse,
    SubaccountGetSubaccountCollateralsResponse,
    SubaccountGetSubaccountDebtsResponse,
    SubaccountGetSubaccountHealthResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/markets/borrow/accounts/{index}">client.user.market.borrow.subaccount.<a href="./src/neptune_api_v2/resources/user/market/borrow/subaccount.py">get_subaccount</a>(index, \*, address, \*\*<a href="src/neptune_api_v2/types/user/market/borrow/subaccount_get_subaccount_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market/borrow/subaccount_get_subaccount_response.py">SubaccountGetSubaccountResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/accounts/{index}/collaterals">client.user.market.borrow.subaccount.<a href="./src/neptune_api_v2/resources/user/market/borrow/subaccount.py">get_subaccount_collaterals</a>(index, \*, address, \*\*<a href="src/neptune_api_v2/types/user/market/borrow/subaccount_get_subaccount_collaterals_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market/borrow/subaccount_get_subaccount_collaterals_response.py">SubaccountGetSubaccountCollateralsResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/accounts/{index}/debts">client.user.market.borrow.subaccount.<a href="./src/neptune_api_v2/resources/user/market/borrow/subaccount.py">get_subaccount_debts</a>(index, \*, address, \*\*<a href="src/neptune_api_v2/types/user/market/borrow/subaccount_get_subaccount_debts_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market/borrow/subaccount_get_subaccount_debts_response.py">SubaccountGetSubaccountDebtsResponse</a></code>
- <code title="get /api/v1/users/{address}/markets/borrow/accounts/{index}/health">client.user.market.borrow.subaccount.<a href="./src/neptune_api_v2/resources/user/market/borrow/subaccount.py">get_subaccount_health</a>(index, \*, address, \*\*<a href="src/neptune_api_v2/types/user/market/borrow/subaccount_get_subaccount_health_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/market/borrow/subaccount_get_subaccount_health_response.py">SubaccountGetSubaccountHealthResponse</a></code>

## Nept

Types:

```python
from neptune_api_v2.types.user import (
    UserUnlockAmounts,
    UserUnlockOverview,
    UserUnlockSchedule,
    UserUnlockScheduleLinear,
    UserUnlockScheduleLumpSum,
    NeptGetUnlocksResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/nept/unlocks">client.user.nept.<a href="./src/neptune_api_v2/resources/user/nept/nept.py">get_unlocks</a>(address, \*\*<a href="src/neptune_api_v2/types/user/nept_get_unlocks_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/nept_get_unlocks_response.py">NeptGetUnlocksResponse</a></code>

### Staking

Types:

```python
from neptune_api_v2.types.user.nept import (
    UserStake,
    UserStakeBondingEntry,
    UserStakePool,
    UserStakeUnbonding,
    UserStakeUnbondingEntry,
    StakingGetOverviewResponse,
    StakingGetStakingPoolResponse,
    StakingGetStakingPoolsResponse,
    StakingGetUnstakingResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/nept/staking">client.user.nept.staking.<a href="./src/neptune_api_v2/resources/user/nept/staking.py">get_overview</a>(address, \*\*<a href="src/neptune_api_v2/types/user/nept/staking_get_overview_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/nept/staking_get_overview_response.py">StakingGetOverviewResponse</a></code>
- <code title="get /api/v1/users/{address}/nept/staking/pools/lookup">client.user.nept.staking.<a href="./src/neptune_api_v2/resources/user/nept/staking.py">get_staking_pool</a>(address, \*\*<a href="src/neptune_api_v2/types/user/nept/staking_get_staking_pool_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/nept/staking_get_staking_pool_response.py">StakingGetStakingPoolResponse</a></code>
- <code title="get /api/v1/users/{address}/nept/staking/pools">client.user.nept.staking.<a href="./src/neptune_api_v2/resources/user/nept/staking.py">get_staking_pools</a>(address, \*\*<a href="src/neptune_api_v2/types/user/nept/staking_get_staking_pools_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/nept/staking_get_staking_pools_response.py">StakingGetStakingPoolsResponse</a></code>
- <code title="get /api/v1/users/{address}/nept/staking/unstaking">client.user.nept.staking.<a href="./src/neptune_api_v2/resources/user/nept/staking.py">get_unstaking</a>(address, \*\*<a href="src/neptune_api_v2/types/user/nept/staking_get_unstaking_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/nept/staking_get_unstaking_response.py">StakingGetUnstakingResponse</a></code>

## Wallet

Types:

```python
from neptune_api_v2.types.user import (
    UserWalletPortfolio,
    WalletAsset,
    WalletAssetKnown,
    WalletAssetUnknown,
    WalletBalance,
    WalletGetBalanceByAssetResponse,
    WalletGetBalancesResponse,
)
```

Methods:

- <code title="get /api/v1/users/{address}/wallet/balance">client.user.wallet.<a href="./src/neptune_api_v2/resources/user/wallet.py">get_balance_by_asset</a>(address, \*\*<a href="src/neptune_api_v2/types/user/wallet_get_balance_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/wallet_get_balance_by_asset_response.py">WalletGetBalanceByAssetResponse</a></code>
- <code title="get /api/v1/users/{address}/wallet/balances">client.user.wallet.<a href="./src/neptune_api_v2/resources/user/wallet.py">get_balances</a>(address, \*\*<a href="src/neptune_api_v2/types/user/wallet_get_balances_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/user/wallet_get_balances_response.py">WalletGetBalancesResponse</a></code>

# Analytics

## Market

Types:

```python
from neptune_api_v2.types.analytics import MarketGetCurrentStateResponse
```

Methods:

- <code title="get /api/v1/analytics/market/state">client.analytics.market.<a href="./src/neptune_api_v2/resources/analytics/market/market.py">get_current_state</a>() -> <a href="./src/neptune_api_v2/types/analytics/market_get_current_state_response.py">MarketGetCurrentStateResponse</a></code>

### History

Types:

```python
from neptune_api_v2.types.analytics.market import (
    HistoryGetLoansOriginatedResponse,
    HistoryGetLoansOriginatedByAssetResponse,
)
```

Methods:

- <code title="get /api/v1/analytics/market/history/loans-originated">client.analytics.market.history.<a href="./src/neptune_api_v2/resources/analytics/market/history.py">get_loans_originated</a>(\*\*<a href="src/neptune_api_v2/types/analytics/market/history_get_loans_originated_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/analytics/market/history_get_loans_originated_response.py">SyncIntervalSinglePage[HistoryGetLoansOriginatedResponse]</a></code>
- <code title="get /api/v1/analytics/market/history/loans-originated/by-asset">client.analytics.market.history.<a href="./src/neptune_api_v2/resources/analytics/market/history.py">get_loans_originated_by_asset</a>(\*\*<a href="src/neptune_api_v2/types/analytics/market/history_get_loans_originated_by_asset_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/analytics/market/history_get_loans_originated_by_asset_response.py">HistoryGetLoansOriginatedByAssetResponse</a></code>

## Nept

Types:

```python
from neptune_api_v2.types.analytics import NeptUnlocksDistributionResponse
```

Methods:

- <code title="get /api/v1/analytics/nept/unlocks-distribution">client.analytics.nept.<a href="./src/neptune_api_v2/resources/analytics/nept.py">unlocks_distribution</a>(\*\*<a href="src/neptune_api_v2/types/analytics/nept_unlocks_distribution_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/analytics/nept_unlocks_distribution_response.py">NeptUnlocksDistributionResponse</a></code>

# Swap

## Routes

Types:

```python
from neptune_api_v2.types.swap import (
    SwapRouteTargetSet,
    RouteListAllResponse,
    RouteListByDenomResponse,
)
```

Methods:

- <code title="get /api/v1/swap/routes/all">client.swap.routes.<a href="./src/neptune_api_v2/resources/swap/routes.py">list_all</a>(\*\*<a href="src/neptune_api_v2/types/swap/route_list_all_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/swap/route_list_all_response.py">RouteListAllResponse</a></code>
- <code title="get /api/v1/swap/routes">client.swap.routes.<a href="./src/neptune_api_v2/resources/swap/routes.py">list_by_denom</a>(\*\*<a href="src/neptune_api_v2/types/swap/route_list_by_denom_params.py">params</a>) -> <a href="./src/neptune_api_v2/types/swap/route_list_by_denom_response.py">RouteListByDenomResponse</a></code>
