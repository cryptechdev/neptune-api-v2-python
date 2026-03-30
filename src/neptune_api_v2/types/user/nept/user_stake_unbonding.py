# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .user_stake_unbonding_entry import UserStakeUnbondingEntry

__all__ = ["UserStakeUnbonding", "Extra", "ExtraText", "ExtraValue", "ExtraValueExtra", "ExtraValueExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    amount_sum: str


class ExtraValueExtraText(BaseModel):
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """

    amount_sum: str


class ExtraValueExtra(BaseModel):
    text: Optional[ExtraValueExtraText] = None
    """Human-readable variants of USD values.

    Will not be null when query params `with_text` and `with_value` are `true`.
    """


class ExtraValue(BaseModel):
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """

    amount_sum: str

    extra: ExtraValueExtra


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    value: Optional[ExtraValue] = None
    """USD values for the corresponding amounts above.

    Will not be null when query param `with_value` is `true`.
    """


class UserStakeUnbonding(BaseModel):
    amount_sum: str
    """Total amount of all unbond entries

    **NOTE:** this value is affected by active filters, if any (e.g. filtering over
    account index)
    """

    contents: List[UserStakeUnbondingEntry]
    """Unbonding/unstake entries

    **NOTE:** cascade unbondings from pool >= 2 are contained in the bondings list
    of the lower adjacent pool from which the unbond occurred.
    """

    extra: Extra
