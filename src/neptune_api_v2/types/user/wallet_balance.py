# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..asset_spec import AssetSpec
from .wallet_asset_known import WalletAssetKnown

__all__ = ["WalletBalance", "Values", "ValuesWalletAssetUnknown"]


class ValuesWalletAssetUnknown(BaseModel):
    amount: str
    """Wallet balance in native denom."""

    kind: Literal["unknown"]


Values: TypeAlias = Union[WalletAssetKnown, ValuesWalletAssetUnknown]


class WalletBalance(BaseModel):
    asset: AssetSpec
    """Provides a unique identifier for an asset for use throughout the Neptune API.

    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """

    values: Values
    """Derived values and amounts."""
