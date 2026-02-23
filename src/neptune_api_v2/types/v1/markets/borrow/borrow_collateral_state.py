# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["BorrowCollateralState", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    collateral_sum: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    collateral_sum: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    collateral_sum: str

    extra: ExtraValueExtra


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class BorrowCollateralState(BaseModel):
    """`BorrowCollateralState`"""

    balance: str

    collateral_sum: str
    """Total amount of this asset which is actively collateralized"""

    extra: Extra
