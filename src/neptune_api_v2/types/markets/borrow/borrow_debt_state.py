# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["BorrowDebtState", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    debt_sum: str

    interest_sum: str

    principal_sum: str

    time_last_distributed_interest: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    debt_sum: str

    interest_sum: str

    principal_sum: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    debt_sum: str

    extra: ExtraValueExtra

    interest_sum: str

    principal_sum: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class BorrowDebtState(BaseModel):
    debt_sum: str
    """Sum open debt amount (this is simply the principal sum + interest sum)"""

    extra: Extra

    interest_sum: str
    """
    Sum of accrued interest for all open debts (those which have not yet been
    repaid)
    """

    principal_sum: str
    """
    Sum of initial amount borrowed for all open debts (those which have not yet been
    repaid)
    """

    time_last_distributed_interest: datetime
    """Timestamp used to keep track of the last time interest was distributed."""

    utilization_accumulator: str
    """Asset utilization tracker."""
