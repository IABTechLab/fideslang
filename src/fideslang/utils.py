"""
Utils for use within various fideslang modules.
"""

from typing import Dict, Optional

from fideslang import models


def get_resource_by_fides_key(
    taxonomy: "models.Taxonomy", fides_key: str
) -> Optional[Dict[str, "models.FidesModel"]]:
    """
    Recurse through a taxonomy to find a specific resource its fides_key.
    """

    return {
        resource_type: resource
        for resource_type in taxonomy.__fields_set__
        for resource in getattr(taxonomy, resource_type)
        if resource.fides_key == fides_key
    } or None
