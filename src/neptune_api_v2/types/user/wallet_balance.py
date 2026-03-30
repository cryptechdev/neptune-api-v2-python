# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..asset_spec import AssetSpec
from .wallet_asset import WalletAsset

__all__ = ["WalletBalance"]


class WalletBalance(BaseModel):
    asset: AssetSpec
    """Provides a unique identifier for an asset for use throughout the Neptune API.

    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """

    values: WalletAsset
    """Derived values and amounts."""
