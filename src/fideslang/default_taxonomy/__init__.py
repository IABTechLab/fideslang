"""This module contains the the default taxonomy resources that Fideslang ships with."""

from fideslang.models import Taxonomy

from .data_categories import DEFAULT_DATA_CATEGORIES
from .data_qualifiers import DEFAULT_DATA_QUALIFIERS
from .data_subjects import DEFAULT_DATA_SUBJECTS
from .data_uses import DEFAULT_DATA_USES
from .organizations import DEFAULT_ORGANIZATIONS

DEFAULT_TAXONOMY = Taxonomy(
    data_category=DEFAULT_DATA_CATEGORIES,
    data_qualifier=DEFAULT_DATA_QUALIFIERS,
    data_subject=DEFAULT_DATA_SUBJECTS,
    data_use=DEFAULT_DATA_USES,
    organization=DEFAULT_ORGANIZATIONS,
)
