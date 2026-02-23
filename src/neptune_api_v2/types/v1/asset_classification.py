# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .asset_spec import AssetSpec

__all__ = ["AssetClassification", "UnionMember0", "UnionMember1", "UnionMember2"]


class UnionMember0(BaseModel):
    kind: Literal["regular"]

    neptune_receipt_asset: Optional[AssetSpec] = None
    """`AssetSpec`

    Provides a unique identifier for an asset for use throughout the Neptune API.
    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """


class UnionMember1(BaseModel):
    kind: Literal["neptune_receipt_token"]

    origin_asset: AssetSpec
    """`AssetSpec`

    Provides a unique identifier for an asset for use throughout the Neptune API.
    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """


class UnionMember2(BaseModel):
    kind: Literal["liquid_staking_token"]

    origin_asset: Optional[AssetSpec] = None
    """`AssetSpec`

    Provides a unique identifier for an asset for use throughout the Neptune API.
    IDs are unique across asset domains (contract tokens, native denoms, etc)
    """


AssetClassification: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2]
