# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ErrorKind"]

ErrorKind: TypeAlias = Literal[
    "entity_not_found",
    "path_invalid",
    "path_unknown",
    "path_parameter_invalid",
    "query_invalid",
    "query_parameter_invalid",
    "query_parameter_unknown",
    "query_parameter_missing",
    "json_invalid",
    "json_decode",
    "json_body_deserialize_failure",
    "content_type_unsupported",
    "validation",
    "internal",
]
