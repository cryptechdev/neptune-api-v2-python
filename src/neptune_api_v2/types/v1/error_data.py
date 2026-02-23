# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ErrorData", "Field"]


class Field(BaseModel):
    field: str

    message: str


class ErrorData(BaseModel):
    kind: Literal["invalid_request", "validation", "entity_not_found", "contract", "internal"]
    """Error kind/category

    Useful to match against for clients that require custom logic depending on the
    type of error encountered
    """

    message: str
    """Error message"""

    scope: Literal["user", "client", "server"]
    """The scope/region of the error.

    Clients may use this to determine how to handle an error message (e.g. log it to
    console or display it to the user).
    """

    fields: Optional[List[Field]] = None
    """List of names and error messages for invalid fields.

    Always set when `error.kind == 'validation'`. Always NULL/unset for all other
    cases.
    """
