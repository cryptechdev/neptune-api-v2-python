from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `neptune_api_v2.resources` module.

    This is used so that we can lazily import `neptune_api_v2.resources` only when
    needed *and* so that users can just import `neptune_api_v2` and reference `neptune_api_v2.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("neptune_api_v2.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
