# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["BorrowDebtState", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    balance_sum: str

    principal_sum: str

    time_last_distributed_interest: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    balance_sum: str

    price: str
    """Text representation of price"""

    principal_sum: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.

    ### Note

    This variant group contains an additional `price` field (set to the number used in value calculation).

    The embedded text group will contain the text variant if `with_text` was specified as well.
    """

    balance_sum: str

    extra: ExtraValueExtra

    price: str
    """Price used in value calculations"""

    principal_sum: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.

    ### Note

    This variant group contains an additional `price` field (set to the number used
    in value calculation).

    The embedded text group will contain the text variant if `with_text` was
    specified as well.
    """


class BorrowDebtState(BaseModel):
    balance_sum: str

    extra: Extra

    principal_sum: str

    time_last_distributed_interest: datetime
    """Timestamp used to keep track of the last time interest was distributed."""

    utilization_accumulator: str
    """Asset utilization tracker."""
