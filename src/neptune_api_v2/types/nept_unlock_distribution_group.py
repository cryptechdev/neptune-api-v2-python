# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "NeptUnlockDistributionGroup",
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

    amount_claimable: str

    amount_claimed: str

    amount_expired: str

    amount_locked: str

    amount_reclaimed: str

    amount_unlocked: str


class ExtraPercentExtra(BaseModel):
    text: Optional[ExtraPercentExtraText] = None
    """Human-readable variants of percentages for unlock amounts.

    Will not be null when query params `with_text` and `with_percent` are `true`.
    """


class ExtraPercent(BaseModel):
    """Percentages for unlock amounts.

    These do not factor in the `amount_staked` or `amount_held` values. Will not be null when query param `with_percent` is `true`.
    """

    amount_claimable: str

    amount_claimed: str

    amount_expired: str

    amount_locked: str

    amount_reclaimed: str

    amount_unlocked: str

    extra: ExtraPercentExtra


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    amount: str

    amount_claimable: str

    amount_claimed: str

    amount_expired: str

    amount_held: str

    amount_locked: str

    amount_reclaimed: str

    amount_staked: str

    amount_unlocked: str

    member_class: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    amount: str

    amount_claimable: str

    amount_claimed: str

    amount_expired: str

    amount_held: str

    amount_locked: str

    amount_reclaimed: str

    amount_staked: str

    amount_unlocked: str


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

    amount_claimable: str

    amount_claimed: str

    amount_expired: str

    amount_held: str

    amount_locked: str

    amount_reclaimed: str

    amount_staked: str

    amount_unlocked: str

    extra: ExtraValueExtra


class Extra(BaseModel):
    percent: Optional[ExtraPercent] = None
    """Percentages for unlock amounts.

    These do not factor in the `amount_staked` or `amount_held` values. Will not be
    null when query param `with_percent` is `true`.
    """

    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class NeptUnlockDistributionGroup(BaseModel):
    amount: str
    """The sum of all token distribution unlock amounts for this group.

    This value is immutable and does not change with regards to
    expiry/reclamation/lock states.
    """

    amount_claimable: str
    """The amount currently claimable

    This takes into account: reclamation, lock state, expiry, and previously
    claimed. In other words, this is an accurate representation of what the user can
    currently claim.
    """

    amount_claimed: str
    """The amount that has already been successfully claimed by the user"""

    amount_expired: str
    """The amount that has expired.

    This will be the remaining unclaimed amount (if any) once the time specified by
    the `expires_at` is past (if one is set).

    **NOTE:** Reclaimed amouts take priority.

    - If the remaining amount is reclaimed prior to a configured `expires_at`, this
      will remain at 0 and will not change even after the `expires_at` time is
      reached.
    """

    amount_held: str
    """The total amount of NEPT currently held by the addresses in this group."""

    amount_locked: str
    """The total amount of NEPT currently time-locked.

    **NOTE:** This does not factor in reclaimed or expired states.

    - For linear unlock schedules:

      - This represents how much NEPT is time-locked by the `begins_at` and the
        `ends_at` properties.

    - For lump sum unlocks:
      - This will be the full amount prior to the `begins_at` unlock property.
      - Once the time indicated by the `begins_at` property has been reached, this
        value will be 0.
    """

    amount_reclaimed: str
    """The amount that has been reclaimed from the unlock arrangement admin

    This will be the amount of the remaining unclaimed and locked at the time the
    reclaim is issued.
    """

    amount_staked: str
    """The total amount of NEPT current staked by the addresses in this group."""

    amount_unlocked: str
    """The total amount of NEPT currently unlocked

    **NOTE:** This does not factor in reclaimed or expired states.

    - For linear unlock schedules:

      - This represents the "progress" of unlocked NEPT from the time range between
        the `begins_at` and the `ends_at` properties.

    - For lump sum unlocks:
      - This will be 0 at any given time prior to the timestamp provided by the
        `begins_at` unlock property.
      - Once the time indicated by the `begins_at` property has been reached, this
        value will be the full amount of the unlock.
    """

    extra: Extra

    member_class: Literal["team", "advisor", "investor"]
    """The group category"""
