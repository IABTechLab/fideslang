"""
This module is responsible for calculating what resources are referenced
by each other and building a dependency graph of relationships.
"""

import inspect
from enum import Enum
from functools import reduce
from typing import List, Optional, Set

from fideslang.models import BaseModel, FidesKey, Taxonomy
from fideslang.utils import get_resource_by_fides_key


def find_nested_keys_in_list(parameter_value: List[BaseModel]) -> List[str]:
    """
    Iterates a nested object list and returns any keys nested fides keys
    """
    nested_keys = [
        nested_key
        for param_element in parameter_value
        for nested_key in find_referenced_fides_keys(param_element)
    ]
    return nested_keys


def find_referenced_fides_keys(resource: object) -> Set[FidesKey]:
    """
    Use type-signature introspection to figure out which fields
    include the FidesKey type and return all of those values.

    Note that this finds _all_ fides_keys, including the resource's own fides_key

    This function is used recursively for arbitrary-depth objects.
    """
    referenced_fides_keys: Set[FidesKey] = set()

    # Str type doesn't have a signature, so we return early
    if isinstance(resource, str) and not isinstance(resource, Enum):
        return set()

    signature = inspect.signature(type(resource), follow_wrapped=True)
    attributes = filter(
        lambda parameter: hasattr(resource, parameter.name),
        signature.parameters.values(),
    )

    for attribute in attributes:
        attribute_value = resource.__getattribute__(attribute.name)
        if attribute_value:
            # If it is a single FidesKey, add it directly
            if attribute.annotation in (FidesKey, Optional[FidesKey]):
                referenced_fides_keys.add(attribute_value)
            # Add the list of FidesKeys to the set
            elif attribute.annotation == List[FidesKey]:
                referenced_fides_keys.update(resource.__getattribute__(attribute.name))
            # If it is a list, but not of strings, recurse into each one
            elif (
                isinstance(attribute_value, list) and attribute.annotation != List[str]
            ):
                nested_keys = find_nested_keys_in_list(attribute_value)
                referenced_fides_keys.update(nested_keys)
            # If it is a Pydantic Model then recurse
            elif isinstance(attribute_value, BaseModel):
                referenced_fides_keys.update(
                    find_referenced_fides_keys(attribute_value)
                )
    return referenced_fides_keys


def get_referenced_missing_keys(taxonomy: Taxonomy) -> Set[FidesKey]:
    """
    Iterate through the Taxonomy and create a set of all of the FidesKeys
    that are contained within it.
    """
    referenced_keys: List[Set[FidesKey]] = [
        find_referenced_fides_keys(resource)
        for resource_type in taxonomy.model_fields_set
        for resource in getattr(taxonomy, resource_type)
    ]
    key_set: Set[FidesKey] = set(
        reduce(lambda x, y: set().union(x).union(y), referenced_keys)
    )
    keys_not_in_taxonomy = {
        fides_key
        for fides_key in key_set
        if get_resource_by_fides_key(taxonomy, fides_key) is None
    }
    return keys_not_in_taxonomy
