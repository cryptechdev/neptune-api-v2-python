# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime

from ...._models import BaseModel
from ...asset_spec import AssetSpec

__all__ = ["HistoryGetLoansOriginatedByAssetResponse", "Point"]


class Point(BaseModel):
    """Time + value pair representing a point in time for use with time series"""

    t: datetime

    v: Union[str, float, None] = None


class HistoryGetLoansOriginatedByAssetResponse(BaseModel):
    """Item and associated points"""

    asset: AssetSpec
    """Provides a unique identifier for an asset for use throughout the Neptune API.

    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """

    points: List[Point]
