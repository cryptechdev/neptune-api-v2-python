# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = [
    "UserNeptUnlockAmounts",
    "Extra",
    "ExtraPercent",
    "ExtraPercentExtra",
    "ExtraPercentExtraText",
    "ExtraText",
    "ExtraValue",
    "ExtraValueExtra",
    "ExtraValueExtraText",
]


class ExtraPercentExtraText(BaseModel):
    """Human-readable variants of percentages for unlock amounts.

    Will not be null when query params `with_text` and `with_percent` are `true`.
    """

    claimable: str

    claimed: str

    expired: str

    locked: str

    reclaimed: str


class ExtraPercentExtra(BaseModel):
    text: Optional[ExtraPercentExtraText] = None
    """Human-readable variants of percentages for unlock amounts.

    Will not be null when query params `with_text` and `with_percent` are `true`.
    """


class ExtraPercent(BaseModel):
    """Percentages for unlock amounts.

    Will not be null when query param `with_percent` is `true`.
    """

    claimable: str

    claimed: str

    expired: str

    extra: ExtraPercentExtra

    locked: str

    reclaimed: str


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    amount: str

    claimable: str

    claimed: str

    expired: str

    locked: str

    reclaimed: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    amount: str

    claimable: str

    claimed: str

    expired: str

    locked: str

    reclaimed: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    amount: str

    claimable: str

    claimed: str

    expired: str

    extra: ExtraValueExtra

    locked: str

    reclaimed: str


class Extra(BaseModel):
    percent: Optional[ExtraPercent] = None
    """Percentages for unlock amounts.

    Will not be null when query param `with_percent` is `true`.
    """

    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class UserNeptUnlockAmounts(BaseModel):
    amount: str
    """The full unlock amount

    This value is immutable and does not change with regards to
    expiry/reclamation/lock states.
    """

    claimable: str
    """The amount currently claimable

    This takes into account: reclamation, lock state, expiry, and previously
    claimed. In other words, this is an accurate representation of what the user can
    currently claim.
    """

    claimed: str
    """The amount that has already been successfully claimed by the user."""

    expired: str
    """
    The amount that was claimable but has now expired due to the presence and
    subsequent passing of `expires_at`
    """

    extra: Extra

    locked: str
    """
    The total amount of NEPT currently awaiting unlock **NOTE:** any reclaimed
    unlocks are excluded from the total, regardless of how much the user had claimed
    prior to reclamation.
    """

    reclaimed: str
    """The amount that has been reclaimed from the unlock arrangement admin"""
