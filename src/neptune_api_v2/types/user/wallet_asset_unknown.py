# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WalletAssetUnknown"]


class WalletAssetUnknown(BaseModel):
    amount: str
    """Wallet balance in native denom."""

    kind: Literal["unknown"]
