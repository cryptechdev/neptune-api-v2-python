# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["StakingPoolState", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    total_bonded: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    total_bonded: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    extra: ExtraValueExtra

    total_bonded: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class StakingPoolState(BaseModel):
    """`StakingPoolState`"""

    extra: Extra

    total_bonded: str
    """The total amount staked to this pool"""
