# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MarketGetSupplyParams"]


class MarketGetSupplyParams(TypedDict, total=False):
    with_text: bool
    """Include text variation fields"""
