# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime

from .._models import BaseModel
from .asset_info import AssetInfo
from .event_action import EventAction

__all__ = ["UserTx", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    action: str

    amount: str

    event_time: str

    price: str

    value: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    amount: Optional[str] = None


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    amount: Optional[str] = None

    extra: ExtraValueExtra


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class UserTx(BaseModel):
    account_address: str
    """Account address corresponding to the transaction"""

    account_index: Optional[int] = None
    """Neptune market sub-account index.

    Will be set for the following event types: `borrow`, `return`,
    `deposit_collateral`, `withdraw_collateral`, `liquidate`, `bond`, `unbond`.

    Otherwise the value is guaranteed to be null.
    """

    action: EventAction
    """Neptune event type for the given market/token contract execute call"""

    amount: Optional[str] = None
    """The relevant amount for the given tx/event.

    This value will be set for all currently implemented action types. It is set as
    nullable for forwards compatibility for future action types which may not have
    an associated amount.
    """

    asset: AssetInfo
    """Asset identifiers with associated metadata"""

    contract_address: str
    """Address for the event's corresponding contract"""

    destination_address: Optional[str] = None
    """Destination account address. Non-null for `send`/`transfer` transactions.

    This field will be null for all other action types.
    """

    event_time: datetime
    """Event/transaction block time"""

    event_uuid: str
    """Internal UUID created when the transaction was first indexed by Neptune.

    Primary usage for API clients is tx history pagination offsets.

    NOTE: event UUIDs should not be used as a guaranteed method of uniquely
    identifying a transaction event over extended periods of time.

    Future updates to our indexer may infrequently require a full re-index of
    transactions, resulting in newly generated UUIDs.
    """

    extra: Extra

    price: Union[str, float, None] = None
    """The price of the associated asset at the time of the transaction.

    This value will be set for all currently implemented action types. It is set as
    nullable for forwards compatibility for future action types which may not have
    an associated amount.
    """

    tx_hash: str
    """Transaction hash"""

    value: Union[str, float, None] = None
    """The USD value at the time of the transaction.

    Derived using the amount and historical price of the associated asset.

    This value will be set for all currently implemented action types. It is set as
    nullable for forwards compatibility for future action types which may not have
    an associated amount.
    """
