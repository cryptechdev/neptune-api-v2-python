# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from ...asset_info import AssetInfo

__all__ = ["UserDebtAssetPool", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    debt: str

    interest: str

    principal: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    debt: str

    interest: str

    principal: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    debt: str

    extra: ExtraValueExtra

    interest: str

    principal: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class UserDebtAssetPool(BaseModel):
    """`UserDebtAssetPool`"""

    asset_info: AssetInfo
    """`AssetInfo`"""

    debt: str
    """Sum open debt amount (this is simply the principal + interest)"""

    extra: Extra

    interest: str
    """Sum of accrued interest for open debt position"""

    principal: str
    """Initial amount borrowed (of debts which have not yet been repaid)"""
