# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from ...asset_info import AssetInfo

__all__ = [
    "UserMergedMarket",
    "BorrowCollateral",
    "BorrowCollateralExtra",
    "BorrowCollateralExtraText",
    "BorrowCollateralExtraValue",
    "BorrowCollateralExtraValueExtra",
    "BorrowCollateralExtraValueExtraText",
    "BorrowDebt",
    "BorrowDebtExtra",
    "BorrowDebtExtraText",
    "BorrowDebtExtraValue",
    "BorrowDebtExtraValueExtra",
    "BorrowDebtExtraValueExtraText",
    "Lend",
    "LendExtra",
    "LendExtraText",
    "LendExtraValue",
    "LendExtraValueExtra",
    "LendExtraValueExtraText",
]


class BorrowCollateralExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    amount: str


class BorrowCollateralExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    amount: str


class BorrowCollateralExtraValueExtra(BaseModel):
    text: Optional[BorrowCollateralExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class BorrowCollateralExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    amount: str

    extra: BorrowCollateralExtraValueExtra


class BorrowCollateralExtra(BaseModel):
    text: Optional[BorrowCollateralExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[BorrowCollateralExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class BorrowCollateral(BaseModel):
    """`UserMergedCollateralAccount`"""

    amount: str
    """Amount of this asset which is actively collateralized"""

    extra: BorrowCollateralExtra

    index: int
    """Account index"""


class BorrowDebtExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    debt: str

    interest: str

    principal: str


class BorrowDebtExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    debt: str

    interest: str

    principal: str


class BorrowDebtExtraValueExtra(BaseModel):
    text: Optional[BorrowDebtExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class BorrowDebtExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    debt: str

    extra: BorrowDebtExtraValueExtra

    interest: str

    principal: str


class BorrowDebtExtra(BaseModel):
    text: Optional[BorrowDebtExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[BorrowDebtExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class BorrowDebt(BaseModel):
    """`UserMergedDebtAccount`"""

    debt: str
    """Sum open debt amount (this is simply the principal + interest)"""

    extra: BorrowDebtExtra

    index: int
    """Account index"""

    interest: str
    """Sum of accrued interest for open debt position"""

    principal: str
    """Initial amount borrowed (of debts which have not yet been repaid)"""


class LendExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    debt: str

    interest: str

    principal: str


class LendExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    debt: str

    interest: str

    principal: str


class LendExtraValueExtra(BaseModel):
    text: Optional[LendExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class LendExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    debt: str

    extra: LendExtraValueExtra

    interest: str

    principal: str


class LendExtra(BaseModel):
    text: Optional[LendExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[LendExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class Lend(BaseModel):
    """`UserDebtPoolData`"""

    debt: str
    """Sum open debt amount (this is simply the principal + interest)"""

    extra: LendExtra

    interest: str
    """Sum of accrued interest for open debt position"""

    principal: str
    """Initial amount borrowed (of debts which have not yet been repaid)"""


class UserMergedMarket(BaseModel):
    """`UserMergedMarket`"""

    asset_info: AssetInfo
    """`AssetInfo`"""

    borrow_collateral: List[BorrowCollateral]
    """User collateral contribution for asset in borrow market, listed by subaccount"""

    borrow_debt: List[BorrowDebt]
    """User debt contribution for asset in borrow market, listed by subaccount"""

    lend: Optional[Lend] = None
    """`UserDebtPoolData`"""
