# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .asset_spec import AssetSpec
from .error_data import ErrorData
from .asset_metadata import AssetMetadata
from .asset_classification import AssetClassification

__all__ = ["AssetListPricesResponse", "Data", "DataPrice", "DataPriceExtra", "DataPriceExtraText"]


class DataPriceExtraText(BaseModel):
    """Human-readable field variants.

    Will not be null when query param `with-text` is `true`.
    """

    last_updated_at: str

    price: str


class DataPriceExtra(BaseModel):
    text: Optional[DataPriceExtraText] = None
    """Human-readable field variants.

    Will not be null when query param `with-text` is `true`.
    """


class DataPrice(BaseModel):
    """> **Note**: Prices are sourced from Neptune's Price Oracle"""

    extra: DataPriceExtra

    last_updated_at: datetime
    """Asset price value, as per Neptune Price Oracle"""

    price: str
    """Asset price"""


class Data(BaseModel):
    """Asset identifiers with associated metadata"""

    asset: AssetSpec
    """Provides a unique identifier for an asset for use throughout the Neptune API.

    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """

    classification: AssetClassification
    """The asset's classification metadata.

    Assets are classfied to provide context on their usage throughout the Neptune
    API (e.g. regular assets, neptune receipt tokens, LSTs, etc.)

    Each asset belongs to only a single classification type. This object contains
    metadata pertaining to the given classification.

    While some fields may be common among the distinct classifcations, each
    classification is distinct and subject to independent change.
    """

    metadata: AssetMetadata
    """Additional metadata for assets"""

    price: DataPrice
    """> **Note**: Prices are sourced from Neptune's Price Oracle"""


class AssetListPricesResponse(BaseModel):
    count: Optional[int] = None
    """Total number of objects in all pages"""

    data: Optional[List[Data]] = None
    """List contents"""

    error: Optional[ErrorData] = None
    """Error message, if any"""

    status: int
    """Request status"""

    status_text: str
    """Request status text"""
