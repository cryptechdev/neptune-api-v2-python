# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["LendMarketState", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    principal_sum: str

    receipt_total_supply: str

    redemption_ratio: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    principal_sum: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    extra: ExtraValueExtra

    principal_sum: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class LendMarketState(BaseModel):
    """`LendMarketState`"""

    extra: Extra

    principal_sum: str
    """The total amount of the asset deposited for lending in the market."""

    receipt_total_supply: str

    redemption_ratio: str
