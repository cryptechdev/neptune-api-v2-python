# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .interval_unit import IntervalUnit

__all__ = ["Interval"]


class Interval(BaseModel):
    """Interval period & size"""

    unit: IntervalUnit

    value: int
