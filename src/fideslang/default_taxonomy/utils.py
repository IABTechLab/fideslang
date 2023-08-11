from typing import Dict, Union
from fideslang.models import DataCategory, DataSubject, DataQualifier, DataUse

CustomType = Union[DataCategory, DataSubject, DataQualifier, DataUse]


def default_factory(TaxonomyClass: CustomType, **kwargs: Dict) -> CustomType:
    """
    Generate default data categories.

    Given that we know these are defaults, set values accordingly.
    """

    kwargs["is_default"] = True

    if not kwargs.get("version_added"):
        # This is the version where we started tracking from, so
        # we use it as the default starting point.
        kwargs["version_added"] = "2.0.0"
    item = TaxonomyClass.parse_obj(kwargs)
    return item
