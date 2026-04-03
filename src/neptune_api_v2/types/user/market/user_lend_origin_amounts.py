# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["UserLendOriginAmounts", "Extra", "ExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    collateralized: str

    held: str

    total: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class UserLendOriginAmounts(BaseModel):
    collateralized: str
    """
    Total equivalent amount of origin token collateralized across this user's
    borrowing portfolio

    **NOTE:** This is **not** the amount of the origin asset that the user holds,
    but the amount held in the receipt token rendered as the equivalent amount in
    the origin asset.

    Or, more formally:
    `origin_equivalent_collateralized = receipt_collateralized / receipt_redemption_ratio`
    """

    extra: Extra

    held: str
    """Total equivalent amount of origin token held in address balance

    **NOTE:** This is **not** the amount of the origin asset that the user holds,
    but the amount held in the receipt token rendered as the equivalent amount in
    the origin asset.

    Or, more formally:
    `origin_equivalent_held = receipt_held / receipt_redemption_ratio`
    """

    total: str
    """Total of held and collateralized equivalent for origin asset

    Or, more formally:
    `origin_equivalent_total = receipt_lent_total / receipt_redemption_ratio`
    """
