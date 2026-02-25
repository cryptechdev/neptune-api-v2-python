# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel
from ..asset_info import AssetInfo
from ..asset_spec import AssetSpec

__all__ = [
    "UserWalletPortfolio",
    "Balance",
    "BalanceValues",
    "BalanceValuesKnownAsset",
    "BalanceValuesKnownAssetKnownAsset",
    "BalanceValuesKnownAssetKnownAssetExtra",
    "BalanceValuesKnownAssetKnownAssetExtraText",
    "BalanceValuesKnownAssetKnownAssetExtraValue",
    "BalanceValuesKnownAssetKnownAssetExtraValueExtra",
    "BalanceValuesKnownAssetKnownAssetExtraValueExtraText",
    "BalanceValuesUnknownAsset",
    "BalanceValuesUnknownAssetUnknownAsset",
    "Extra",
    "ExtraText",
]


class BalanceValuesKnownAssetKnownAssetExtraText(BaseModel):
    """Human-readable field variants. Must provide `?with-text=true`"""

    amount: str


class BalanceValuesKnownAssetKnownAssetExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """

    amount: str


class BalanceValuesKnownAssetKnownAssetExtraValueExtra(BaseModel):
    text: Optional[BalanceValuesKnownAssetKnownAssetExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Must provide `?with-text=true&with-value=true`
    """


class BalanceValuesKnownAssetKnownAssetExtraValue(BaseModel):
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""

    amount: str

    extra: BalanceValuesKnownAssetKnownAssetExtraValueExtra


class BalanceValuesKnownAssetKnownAssetExtra(BaseModel):
    text: Optional[BalanceValuesKnownAssetKnownAssetExtraText] = None
    """Human-readable field variants. Must provide `?with-text=true`"""

    value: Optional[BalanceValuesKnownAssetKnownAssetExtraValue] = None
    """USD values for the corresponding amounts above. Must provide `?with-value=true`"""


class BalanceValuesKnownAssetKnownAsset(BaseModel):
    """`KnownWalletValues`"""

    amount: str
    """Wallet balance in native denom."""

    amount_scaled: str
    """Amount scaled to the asset's standard unit / decimal places."""

    asset_info: AssetInfo
    """`AssetInfo`"""

    extra: BalanceValuesKnownAssetKnownAssetExtra


class BalanceValuesKnownAsset(BaseModel):
    """
    This will be provided given the denom matches that of an asset included in the /assets endpoint.
    """

    known_asset: BalanceValuesKnownAssetKnownAsset
    """`KnownWalletValues`"""


class BalanceValuesUnknownAssetUnknownAsset(BaseModel):
    """`UnknownWalletValues`"""

    amount: str
    """Wallet balance in native denom."""


class BalanceValuesUnknownAsset(BaseModel):
    unknown_asset: BalanceValuesUnknownAssetUnknownAsset
    """`UnknownWalletValues`"""


BalanceValues: TypeAlias = Union[BalanceValuesKnownAsset, BalanceValuesUnknownAsset]


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
