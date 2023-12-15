"""
Exports various fideslang objects for easier use elsewhere.
"""

from typing import Dict, Type, Union

from fideslang.default_fixtures import COUNTRY_CODES
from fideslang.default_taxonomy import DEFAULT_TAXONOMY

from ._version import __version__

# export our GVL utilities
from .gvl import (
    GVL_DATA_CATEGORIES,
    GVL_PURPOSES,
    GVL_SPECIAL_PURPOSES,
    MAPPED_GVL_DATA_CATEGORIES,
    MAPPED_PURPOSES,
    MAPPED_PURPOSES_BY_DATA_USE,
    MAPPED_SPECIAL_PURPOSES,
    data_category_id_to_data_categories,
    data_use_to_purpose,
    purpose_to_data_use,
)

# Export the Models
from .models import (
    DataCategory,
    DataFlow,
    Dataset,
    DatasetField,
    DatasetFieldBase,
    DataSubject,
    DataUse,
    Evaluation,
    FidesCollectionKey,
    FidesDatasetReference,
    FidesMeta,
    FidesModel,
    Organization,
    Policy,
    PolicyRule,
    PrivacyDeclaration,
    PrivacyRule,
    System,
    Taxonomy,
)

FidesModelType = Union[Type[FidesModel], Type[Evaluation]]
model_map: Dict[str, FidesModelType] = {
    "data_category": DataCategory,
    "data_subject": DataSubject,
    "data_use": DataUse,
    "dataset": Dataset,
    "organization": Organization,
    "policy": Policy,
    "system": System,
    "evaluation": Evaluation,
}
model_list = list(model_map.keys())
