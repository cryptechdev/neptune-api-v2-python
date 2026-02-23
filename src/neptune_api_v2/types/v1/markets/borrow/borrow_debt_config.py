# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["BorrowDebtConfig", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    borrow_cap: str

    borrow_halt_utilization: str

    interest_fee: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    borrow_cap: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    borrow_cap: str

    extra: ExtraValueExtra


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class BorrowDebtConfig(BaseModel):
    """`BorrowDebtConfig`"""

    borrow_halt_utilization: str
    """The maximum utilization ratio at which new borrow positions can be opened."""

    enabled: bool
    """Market enabled state"""

    extra: Extra

    interest_fee: str
    """The protocol (base) interest rate that is charged to borrowers."""

    borrow_cap: Optional[str] = None
    """The global max amount which can be borrowed"""
