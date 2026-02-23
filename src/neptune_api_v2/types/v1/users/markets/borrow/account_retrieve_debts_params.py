# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountRetrieveDebtsParams"]


class AccountRetrieveDebtsParams(TypedDict, total=False):
    address: Required[str]
    """The user account address"""

    with_text: bool
    """Include text variation fields"""

    with_value: bool
    """Calculate and include USD values for amounts, where applicable"""
