# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..asset_info import AssetInfo

__all__ = ["WalletAssetKnown", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    amount: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    amount: str

    price: str
    """Text representation of price"""


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.

    ### Note

    This variant group contains an additional `price` field (set to the number used in value calculation).

    The embedded text group will contain the text variant if `with_text` was specified as well.
    """

    amount: str

    extra: ExtraValueExtra

    price: str
    """Price used in value calculations"""


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.

    ### Note

    This variant group contains an additional `price` field (set to the number used
    in value calculation).

    The embedded text group will contain the text variant if `with_text` was
    specified as well.
    """


class WalletAssetKnown(BaseModel):
    amount: str
    """Wallet balance in native denom."""

    amount_scaled: str
    """Amount scaled to the asset's standard unit / decimal places."""

    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    extra: Extra

    kind: Literal["known"]
