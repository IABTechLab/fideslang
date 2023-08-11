from fideslang.models import DataQualifier
from typing import Dict, Any


def default_factory(**kwargs: Dict[str, Any]) -> DataQualifier:
    """
    Generate default qualifiers.

    Given that we know these are defaults, set values accordingly.
    """

    kwargs["is_default"] = True

    if not kwargs.get("version_added"):
        # This is the version where we started tracking from, so
        # we use it as the default starting point.
        kwargs["version_added"] = "2.0.0"
    item = DataQualifier.parse_obj(kwargs)
    return item


DEFAULT_DATA_QUALIFIERS = [
    default_factory(
        fides_key="aggregated",
        organization_fides_key="default_organization",
        name="Aggregated Data",
        description="Statistical data that does not contain individually identifying information but includes information about groups of individuals that renders individual identification impossible.",
    ),
    default_factory(
        fides_key="aggregated.anonymized",
        organization_fides_key="default_organization",
        name="Anonymized Data",
        description="Data where all attributes have been sufficiently altered that the individaul cannot be reidentified by this data or in combination with other datasets.",
        parent_key="aggregated",
    ),
    default_factory(
        fides_key="aggregated.anonymized.unlinked_pseudonymized",
        organization_fides_key="default_organization",
        name="Unlinked Pseudonymized Data",
        description="Data for which all identifiers have been substituted with unrelated values and linkages broken such that it may not be reversed, even by the party that performed the pseudonymization.",
        parent_key="aggregated.anonymized",
    ),
    default_factory(
        fides_key="aggregated.anonymized.unlinked_pseudonymized.pseudonymized",
        organization_fides_key="default_organization",
        name="Pseudonymized Data",
        description="Data for which all identifiers have been substituted with unrelated values, rendering the individual unidentifiable and cannot be reasonably reversed other than by the party that performed the pseudonymization.",
        parent_key="aggregated.anonymized.unlinked_pseudonymized",
    ),
    default_factory(
        fides_key="aggregated.anonymized.unlinked_pseudonymized.pseudonymized.identified",
        organization_fides_key="default_organization",
        name="Identified Data",
        description="Data that directly identifies an individual.",
        parent_key="aggregated.anonymized.unlinked_pseudonymized.pseudonymized",
    ),
]
