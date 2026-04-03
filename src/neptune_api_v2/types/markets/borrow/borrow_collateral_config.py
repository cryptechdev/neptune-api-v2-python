# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BorrowCollateralConfig", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    allowable_ltv: str

    collateral_cap: str

    liquidation_ltv: str

    max_discount: str

    min_discount: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    collateral_cap: Optional[str] = None

    price: Optional[str] = None
    """Text representation of price"""


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

    collateral_cap: Optional[str] = None

    extra: ExtraValueExtra

    price: str
    """Price used in value calculations"""


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


class BorrowCollateralConfig(BaseModel):
    allowable_ltv: str
    """The loan to value ratio at which we allow collateral withdrawals or borrows."""

    collateral_cap: Optional[str] = None
    """The optional, global/shared maximum deposit limit for this collateral."""

    enabled: bool
    """Collateral enabled state"""

    extra: Extra

    liquidation_ltv: str
    """The loan to value ratio at which the collateral can be liquidated."""

    max_discount: str
    """The maximum dynamic discount"""

    min_discount: str
    """The minimum dynamic discount."""
