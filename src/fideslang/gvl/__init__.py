# pylint: disable=too-many-locals

import os
from json import load
from os.path import dirname, join
from typing import Dict, List, Optional

from .models import Feature, GVLDataCategory, MappedDataCategory, MappedPurpose, Purpose

### (Special) Purposes

PURPOSE_MAPPING_FILE = join(
    dirname(__file__),
    "",
    "gvl_data_use_mapping.json",
)

GVL_PURPOSES: Dict[int, Purpose] = {}
MAPPED_PURPOSES: Dict[int, MappedPurpose] = {}
GVL_SPECIAL_PURPOSES: Dict[int, Purpose] = {}
MAPPED_SPECIAL_PURPOSES: Dict[int, MappedPurpose] = {}
MAPPED_PURPOSES_BY_DATA_USE: Dict[str, MappedPurpose] = {}

### (Special) Features

FEATURE_MAPPING_FILE = join(
    dirname(__file__),
    "",
    "gvl_feature_mapping.json",
)
GVL_FEATURES: Dict[int, Feature] = {}
GVL_SPECIAL_FEATURES: Dict[int, Feature] = {}
FEATURES_BY_NAME: Dict[str, Feature] = {}


### Data Categories

DATA_CATEGORY_MAPPING_FILE = join(
    dirname(__file__),
    "",
    "gvl_data_category_mapping.json",
)
GVL_DATA_CATEGORIES: Dict[int, GVLDataCategory] = {}
MAPPED_GVL_DATA_CATEGORIES: Dict[int, MappedDataCategory] = {}


def _load_data() -> None:
    with open(
        os.path.join(os.curdir, PURPOSE_MAPPING_FILE), encoding="utf-8"
    ) as mapping_file:
        data = load(mapping_file)
        for raw_purpose in data["purposes"].values():
            purpose = Purpose.model_validate(raw_purpose)
            mapped_purpose = MappedPurpose.model_validate(raw_purpose)
            GVL_PURPOSES[purpose.id] = purpose
            MAPPED_PURPOSES[mapped_purpose.id] = mapped_purpose
            for data_use in mapped_purpose.data_uses:
                MAPPED_PURPOSES_BY_DATA_USE[data_use] = mapped_purpose

        for raw_special_purpose in data["specialPurposes"].values():
            special_purpose = Purpose.model_validate(raw_special_purpose)
            mapped_special_purpose = MappedPurpose.model_validate(raw_special_purpose)
            GVL_SPECIAL_PURPOSES[special_purpose.id] = special_purpose
            MAPPED_SPECIAL_PURPOSES[mapped_special_purpose.id] = mapped_special_purpose
            for data_use in mapped_special_purpose.data_uses:
                MAPPED_PURPOSES_BY_DATA_USE[data_use] = mapped_special_purpose

    with open(
        os.path.join(os.curdir, FEATURE_MAPPING_FILE), encoding="utf-8"
    ) as feature_mapping_file:
        feature_data = load(feature_mapping_file)

        for raw_feature in feature_data["features"].values():
            feature = Feature.model_validate(raw_feature)
            GVL_FEATURES[feature.id] = feature
            FEATURES_BY_NAME[feature.name] = feature

        for raw_special_feature in feature_data["specialFeatures"].values():
            special_feature = Feature.model_validate(raw_special_feature)
            GVL_SPECIAL_FEATURES[special_feature.id] = special_feature
            FEATURES_BY_NAME[special_feature.name] = special_feature

    with open(
        os.path.join(os.curdir, DATA_CATEGORY_MAPPING_FILE), encoding="utf-8"
    ) as data_category_mapping_file:
        data_category_data = load(data_category_mapping_file)

        for raw_data_category in data_category_data.values():
            data_category = GVLDataCategory.model_validate(raw_data_category)
            mapped_data_category = MappedDataCategory.model_validate(raw_data_category)
            GVL_DATA_CATEGORIES[data_category.id] = data_category
            MAPPED_GVL_DATA_CATEGORIES[mapped_data_category.id] = mapped_data_category


def purpose_to_data_use(purpose_id: int, special_purpose: bool = False) -> List[str]:
    """
    Utility function to return the fideslang data uses associated with the
    given GVL purpose (or special purpose) ID.

    By default, the given ID is treated as a purpose ID. The `special_purpose`
    argument can be set to `True` if looking up special purpose IDs.

    Raises a KeyError if an invalid purpose ID is provided.
    """
    purpose_map = MAPPED_SPECIAL_PURPOSES if special_purpose else MAPPED_PURPOSES
    return purpose_map[purpose_id].data_uses


def data_use_to_purpose(data_use: str) -> Optional[Purpose]:
    """
    Utility function to return the GVL purpose (or special purpose) associated
    with the given fideslang data use.

    Returns None if no associated purpose (or special purpose) is found
    """
    return MAPPED_PURPOSES_BY_DATA_USE.get(data_use, None)


def feature_name_to_feature(feature_name: str) -> Optional[Feature]:
    """Utility function to return a GVL feature (or special feature) given the feature's name"""
    return FEATURES_BY_NAME.get(feature_name, None)


def feature_id_to_feature_name(
    feature_id: int, special_feature: bool = False
) -> Optional[str]:
    """Utility function to return a GVL feature/special feature name given the feature/special feature's id"""
    feature_map = GVL_SPECIAL_FEATURES if special_feature else GVL_FEATURES
    feature = feature_map.get(feature_id, None)
    if not feature:
        return None
    return feature.name


def data_category_id_to_data_categories(data_category_id: int) -> List[str]:
    """
    Utility function to return the fideslang data categories associated with the
    given GVL data category ID.

    Raises a KeyError if an invalid GVL data category ID is provided.
    """
    return MAPPED_GVL_DATA_CATEGORIES[data_category_id].fides_data_categories


_load_data()
