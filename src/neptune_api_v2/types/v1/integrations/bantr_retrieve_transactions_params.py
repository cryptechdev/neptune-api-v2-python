# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BantrRetrieveTransactionsParams"]


class BantrRetrieveTransactionsParams(TypedDict, total=False):
    end_block: Required[int]
    """End block"""

    start_block: Required[int]
    """Start Block"""

    limit: Optional[int]
    """Pagination limit"""
