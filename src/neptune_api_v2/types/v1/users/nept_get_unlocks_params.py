# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NeptGetUnlocksParams"]


class NeptGetUnlocksParams(TypedDict, total=False):
    with_percent: bool
    """Calculate and include proportion percentages, where applicable"""

    with_text: bool
    """Include text variation fields"""

    with_value: bool
    """Calculate and include USD values for amounts, where applicable"""
