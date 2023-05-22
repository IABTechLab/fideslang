"""This module contains the the default taxonomy resources that Fideslang ships with."""

from fideslang.models import Taxonomy

from .data_categories import DEFAULT_DATA_CATEGORIES
from .data_qualifiers import DEFAULT_DATA_QUALIFIERS
from .data_subjects import DEFAULT_DATA_SUBJECTS
from .data_uses import DEFAULT_DATA_USES
from .organizations import DEFAULT_ORGANIZATIONS

sort_data_types = (
    lambda x: x.parent_key if hasattr(x, "parent_key") and x.parent_key else x.fides_key
)

DEFAULT_TAXONOMY = Taxonomy(
    data_category=sorted(DEFAULT_DATA_CATEGORIES, key=sort_data_types),
    data_qualifier=sorted(DEFAULT_DATA_QUALIFIERS, key=sort_data_types),
    data_subject=sorted(DEFAULT_DATA_SUBJECTS, key=sort_data_types),
    data_use=sorted(DEFAULT_DATA_USES, key=sort_data_types),
    organization=DEFAULT_ORGANIZATIONS,
)
