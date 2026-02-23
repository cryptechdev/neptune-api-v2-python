# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["StakingPoolParams"]


class StakingPoolParams(BaseModel):
    """`StakingPoolParams`"""

    flash_loan_weight: str
    """The pool's weight (multiplier) for flash loans volume"""

    gov_weight: str
    """The pool's weight (multiplier) on governance for an associated stake"""

    health_weight: str
    """The pool's weight (multiplier) on account health for an associated stake"""

    reward_weight: str
    """The pool's weight (multiplier) on rewards for an associated stake"""
