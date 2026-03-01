# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LendGetByAssetParams"]


class LendGetByAssetParams(TypedDict, total=False):
    asset_id: Required[str]
    """Asset ID for lookup"""

    with_text: bool
    """Include text variation fields"""

    with_value: bool
    """Calculate and include USD values for amounts, where applicable"""
