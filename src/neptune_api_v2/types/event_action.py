# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["EventAction"]

EventAction: TypeAlias = Literal[
    "borrow_flash_loan",
    "return_flash_loan",
    "create_token_unlock",
    "reclaim_token_unlock",
    "liquidate",
    "borrow",
    "return",
    "lend",
    "redeem",
    "deposit_collateral",
    "withdraw_collateral",
    "claim_war_chest",
    "bond",
    "unbond",
    "claim_unbonded",
    "claim_token_unlock",
    "claim_rewards",
    "cascade",
    "send",
]
