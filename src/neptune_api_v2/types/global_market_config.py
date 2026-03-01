# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .asset_spec import AssetSpec

__all__ = ["GlobalMarketConfig", "Extra", "ExtraText"]


class ExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    flash_loan_fee: str

    liquidation_fee: str

    stake_collateral_ratio: str

    stake_flash_loan_ratio: str

    staking_health_modifier: str

    time_window_nanos: str


class Extra(BaseModel):
    text: Optional[ExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class GlobalMarketConfig(BaseModel):
    dynamic_discount_width: str
    """
    The required change in account health below 1.0 to achieve the maximum discount.
    should be ~= 0.02 must be <= 1.0
    """

    extra: Extra

    flash_loan_fee: str
    """
    The coefficient used to calculate the flash loan fee. should be ~= 0.01 must be
    <= 1.0
    """

    flash_loans_enabled: bool
    """Whether flash loans are enabled or not"""

    hinj: AssetSpec
    """Provides a unique identifier for an asset for use throughout the Neptune API.

    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """

    liquidation_fee: str
    """
    The coefficient use to calculate the liquidation protocol fee. should be ~= 0.01
    must be <= 1.0
    """

    nept: AssetSpec
    """Provides a unique identifier for an asset for use throughout the Neptune API.

    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """

    partial_liquidation_threshold: str
    """Minimum account value to avoid complete liquidation."""

    stake_collateral_ratio: str
    """
    The required ratio of weighted staked NEPT to collateral value to obtain the
    maximum staking health modifier. should be ~= 0.1 must be <= 1.0
    """

    stake_flash_loan_ratio: str
    """
    The required ratio of weighted staked NEPT to flash loan value should be ~= 0.05
    must be <= 1.0
    """

    staking_health_modifier: str
    """
    The maximum health increase provided by staking. should be ~= 0.05 and must be
    <= 1.0
    """

    target_liquidation_health: str
    """The account health target for a liquidation. should be ~= 1.02 must be >= 1.0"""

    time_window_nanos: int
    """Number of nanoseconds that an oracle price is valid for."""
