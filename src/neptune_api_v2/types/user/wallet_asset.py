# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .wallet_asset_known import WalletAssetKnown
from .wallet_asset_unknown import WalletAssetUnknown

__all__ = ["WalletAsset"]

WalletAsset: TypeAlias = Union[WalletAssetKnown, WalletAssetUnknown]
