# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["StakingGetStakingPoolParams"]


class StakingGetStakingPoolParams(TypedDict, total=False):
    duration: int
    """Duration of pool to lookup (**in nanoseconds**)

    **NOTE:** Either index or duration must be provided. Cannot specify both.
    """

    index: int
    """Index of pool to lookup

    **NOTE:** Either index or duration must be provided. Cannot specify both.
    """

    with_text: bool
    """Include text variation fields"""

    with_value: bool
    """Calculate and include USD values for amounts, where applicable"""
