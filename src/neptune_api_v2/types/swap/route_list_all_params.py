# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RouteListAllParams"]


class RouteListAllParams(TypedDict, total=False):
    contract_address: Required[str]
    """Swap contract address"""
