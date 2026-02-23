# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["BorrowCollateralConfig", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    allowable_ltv: str

    collateral_cap: str

    liquidation_ltv: str

    max_discount: str

    min_discount: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    collateral_cap: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    collateral_cap: str

    extra: ExtraValueExtra


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class BorrowCollateralConfig(BaseModel):
    """`BorrowCollateralConfig`"""

    allowable_ltv: str
    """The loan to value ratio at which we allow collateral withdrawals or borrows."""

    enabled: bool
    """Collateral enabled state"""

    extra: Extra

    liquidation_ltv: str
    """The loan to value ratio at which the collateral can be liquidated."""

    max_discount: str
    """The maximum dynamic discount"""

    min_discount: str
    """The minimum dynamic discount."""

    collateral_cap: Optional[str] = None
    """The optional, global/shared maximum deposit limit for this collateral."""
