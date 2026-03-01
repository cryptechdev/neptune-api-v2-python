# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AssetMetadata"]


class AssetMetadata(BaseModel):
    """Additional metadata for assets"""

    decimals_denom: int
    """Denom exponent, or num.

    of decimal places that shift between denom/standard amounts (e.g. `18` for
    `INJ`)
    """

    decimals_display: int
    """
    Number of decimals used when displaying amounts of this asset (this is
    subjective and used for generating text representations)
    """

    name: str
    """Full name of the asset"""

    symbol: str
    """Symbol of the asset, e.g.: `NEPT` `INJ`"""

    symbol_denom: str
    """Denom symbol for the asset (e.g. `inj` for `INJ`, `sat` for `BTC`)"""
