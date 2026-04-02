# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RouteListByDenomParams"]


class RouteListByDenomParams(TypedDict, total=False):
    contract_address: Required[str]
    """Swap contract address"""

    source_denom: Required[str]
    """Source asset denom to fetch target routes for

    **Note**: This is a normal injective asset denom, and not an `AssetSpec` ID.

    E.g.

    - `inj` is a **valid** value for `source_denom`.
    - `native;inj` is **not a valid value** for `source_denom`.
    """
