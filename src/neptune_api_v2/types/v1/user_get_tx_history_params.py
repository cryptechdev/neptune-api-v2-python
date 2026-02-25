# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .event_action import EventAction

__all__ = ["UserGetTxHistoryParams"]


class UserGetTxHistoryParams(TypedDict, total=False):
    action: Optional[EventAction]
    """Optional event/tx action to filter against"""

    limit: int
    """Maximum number of transactions to return.

    Optional and defaults to `20` if missing.
    """

    prev_event_uuid: Optional[str]
    """Optional UUID skip parameter used for pagination.

    Providing the last event UUID on a given page will return the next page
    beginning with the following (unseen) item.
    """

    sort_order: Literal["asc", "desc"]
    """Changes the sort order for the returned txs.

    Transactions are always sorted by event time, however the direction (e.g. newest
    to oldest) can be changed using this parameter.

    Optional and defaults to `desc` if missing.
    """

    with_text: bool
    """Include text variation fields"""

    with_value: bool
    """Calculate and include USD values for amounts, where applicable"""
