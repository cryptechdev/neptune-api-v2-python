# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from ....asset_info import AssetInfo

__all__ = ["UserDebtAssetPool", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    debt: str

    interest: str

    principal: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    debt: str

    interest: str

    principal: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    debt: str

    extra: ExtraValueExtra

    interest: str

    principal: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class UserDebtAssetPool(BaseModel):
    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    debt: str
    """Sum open debt amount (this is simply the principal + interest)"""

    extra: Extra

    interest: str
    """Sum of accrued interest for open debt position"""

    principal: str
    """Initial amount borrowed (of debts which have not yet been repaid)"""
