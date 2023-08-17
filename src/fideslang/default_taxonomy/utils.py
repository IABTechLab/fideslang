from typing import Dict, Union

from fideslang.models import DataCategory, DataQualifier, DataSubject, DataUse

CustomType = Union[DataCategory, DataSubject, DataQualifier, DataUse]


def default_factory(taxonomy_class: CustomType, **kwargs: Dict) -> CustomType:
    """
    Generate default taxonomy objects.

    Given that we know these are defaults, set default values accordingly.
    """

    kwargs["is_default"] = True  # type: ignore[assignment]

    if not kwargs.get("version_added"):
        # This is the version where we started tracking from, so
        # we use it as the default starting point.
        kwargs["version_added"] = "2.0.0"  # type: ignore[assignment]
    item = taxonomy_class.parse_obj(kwargs)
    return item
