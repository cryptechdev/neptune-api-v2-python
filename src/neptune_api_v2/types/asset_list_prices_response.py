# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .asset_spec import AssetSpec
from .asset_price import AssetPrice
from .asset_metadata import AssetMetadata
from .asset_classification import AssetClassification

__all__ = ["AssetListPricesResponse", "Data"]


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

    price: AssetPrice
    """> **Note**: Prices are sourced from Neptune's Price Oracle"""


class AssetListPricesResponse(BaseModel):
    count: int
    """Total number of objects irrespective of any pagination parameters."""

    data: List[Data]

    error: None = None
    """Error data. Guaranteed `null` for successful response."""

    status: int
    """HTTP status.

    Successful responses are guaranteed to be < `400`. Conversely, error responses
    are guaranteed to be >= `400`.
    """

    status_text: str
    """HTTP status text"""
