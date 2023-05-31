"""
Exports various fideslang objects for easier use elsewhere.
"""

from typing import Dict, Type, Union

from fideslang.default_fixtures import COUNTRY_CODES
from fideslang.default_taxonomy import DEFAULT_TAXONOMY

# Export the Models
from .models import (
    DataCategory,
    DataFlow,
    DataQualifier,
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
    Registry,
    System,
    Taxonomy,
)

FidesModelType = Union[Type[FidesModel], Type[Evaluation]]
model_map: Dict[str, FidesModelType] = {
    "data_category": DataCategory,
    "data_qualifier": DataQualifier,
    "data_subject": DataSubject,
    "data_use": DataUse,
    "dataset": Dataset,
    "organization": Organization,
    "policy": Policy,
    "registry": Registry,
    "system": System,
    "evaluation": Evaluation,
}
model_list = list(model_map.keys())
