# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .lend_market import LendMarket

__all__ = ["LendListResponse", "Data", "DataSupply", "DataSupplyExtra", "DataSupplyExtraText"]


class DataSupplyExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """

    principal: str


class DataSupplyExtra(BaseModel):
    text: Optional[DataSupplyExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with_text` is `true`.
    """


class DataSupply(BaseModel):
    """Supply breakdown for lending markets"""

    extra: DataSupplyExtra

    principal: str
    """Sum USD value of lending principal"""


class Data(BaseModel):
    """Lending markets overview"""

    contents: List[LendMarket]
    """Lending markets"""

    supply: DataSupply
    """Supply breakdown for lending markets"""


class LendListResponse(BaseModel):
    data: Data
    """Lending markets overview"""

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
