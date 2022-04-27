"""
This module is responsible for calculating what resources are referenced
by each other and building a dependency graph of relationships.
"""

import inspect
from functools import reduce
from typing import List, Set


from fideslang.models import (
    FidesKey,
    Taxonomy,
    BaseModel,
)
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
    """
    referenced_fides_keys: Set[FidesKey] = set()
    signature = inspect.signature(type(resource), follow_wrapped=True)
    parameter_values = filter(
        lambda parameter: hasattr(resource, parameter.name),
        signature.parameters.values(),
    )
    for parameter in parameter_values:
        parameter_value = resource.__getattribute__(parameter.name)
        if parameter_value:
            if parameter.annotation == FidesKey:
                referenced_fides_keys.add(parameter_value)
            elif parameter.annotation == List[FidesKey]:
                referenced_fides_keys.update(resource.__getattribute__(parameter.name))
            elif (
                isinstance(parameter_value, list) and parameter.annotation != List[str]
            ):
                nested_keys = find_nested_keys_in_list(parameter_value)
                referenced_fides_keys.update(nested_keys)
            elif hasattr(parameter_value, "__dict__"):
                referenced_fides_keys.update(
                    find_referenced_fides_keys(parameter_value)
                )
    return referenced_fides_keys


def get_referenced_missing_keys(taxonomy: Taxonomy) -> List[FidesKey]:
    """
    Iterate through the Taxonomy and create a set of all of the FidesKeys
    that are contained within it.
    """
    referenced_keys: List[Set[FidesKey]] = [
        find_referenced_fides_keys(resource)
        for resource_type in taxonomy.__fields_set__
        for resource in getattr(taxonomy, resource_type)
    ]
    key_set: Set[FidesKey] = set(
        reduce(lambda x, y: set().union(x).union(y), referenced_keys)
    )
    keys_not_in_taxonomy = [
        fides_key
        for fides_key in key_set
        if get_resource_by_fides_key(taxonomy, fides_key) is None
    ]
    return keys_not_in_taxonomy
