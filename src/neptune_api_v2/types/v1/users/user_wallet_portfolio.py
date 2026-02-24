# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from ..asset_info import AssetInfo
from ..asset_spec import AssetSpec

__all__ = [
    "UserWalletPortfolio",
    "Balance",
    "BalanceValues",
    "BalanceValuesUnionMember0",
    "BalanceValuesUnionMember0Extra",
    "BalanceValuesUnionMember0ExtraText",
    "BalanceValuesUnionMember0ExtraValue",
    "BalanceValuesUnionMember0ExtraValueExtra",
    "BalanceValuesUnionMember0ExtraValueExtraText",
    "BalanceValuesUnknownWalletValues",
    "Extra",
    "ExtraText",
]


class BalanceValuesUnionMember0ExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    amount: str


class BalanceValuesUnionMember0ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    amount: str


class BalanceValuesUnionMember0ExtraValueExtra(BaseModel):
    text: Optional[BalanceValuesUnionMember0ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class BalanceValuesUnionMember0ExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    amount: str

    extra: BalanceValuesUnionMember0ExtraValueExtra


class BalanceValuesUnionMember0Extra(BaseModel):
    text: Optional[BalanceValuesUnionMember0ExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[BalanceValuesUnionMember0ExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class BalanceValuesUnionMember0(BaseModel):
    amount: str
    """Wallet balance in native denom."""

    amount_scaled: str
    """Amount scaled to the asset's standard unit / decimal places."""

    asset_info: AssetInfo
    """`AssetInfo`"""

    extra: BalanceValuesUnionMember0Extra

    kind: Literal["known_asset"]


class BalanceValuesUnknownWalletValues(BaseModel):
    """`UnknownWalletValues`"""

    kind: Literal["unknown_asset"]


BalanceValues: TypeAlias = Union[BalanceValuesUnionMember0, BalanceValuesUnknownWalletValues]


class Balance(BaseModel):
    """`WalletBalance`"""

    asset: AssetSpec
    """`AssetSpec`

    Provides a unique identifier for an asset for use throughout the Neptune API.
    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """

    values: BalanceValues
    """Derived values and amounts."""


class ExtraText(BaseModel):
    total_value: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None


class UserWalletPortfolio(BaseModel):
    """`UserWalletPortfolio`"""

    balances: List[Balance]
    """Array of each wallet balance"""

    extra: Extra

    total_value: Optional[str] = None
    """Sum value in USD. Only available when value calculation is enabled.

    **NOTE:** this only accounts for assets which are internally known & tracked.
    See the `/assets` endpoint for a list of supported assets.
    """
