# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from ...asset_info import AssetInfo
from ...market_rate import MarketRate
from .user_lend_origin_amounts import UserLendOriginAmounts
from .user_lend_receipt_amounts import UserLendReceiptAmounts

__all__ = ["UserLendAssetPool"]


class UserLendAssetPool(BaseModel):
    asset_info: AssetInfo
    """Asset identifiers with associated metadata"""

    market_rate: MarketRate
    """Current market lending rate"""

    origin_equivalent: UserLendOriginAmounts
    """
    The lending amounts converted into the equivalent for the receipt token's
    origin/source asset
    """

    receipt_amounts: UserLendReceiptAmounts
    """The lending amounts in the original receipt token amounts"""
