import os
from json import load
from os.path import join, dirname
from typing import List

from .models import MappedPurpose, Purpose


PURPOSE_MAPPING_FILE = join(
    dirname(__file__),
    "",
    "gvl_data_use_mapping.json",
)

# PURPOSE_MAPPING_FILE = "src/fideslang/gvl/gvl_data_use_mapping.json"

GVL_PURPOSES: dict[int, Purpose] = {}
MAPPED_PURPOSES: dict[int, MappedPurpose] = {}

GVL_SPECIAL_PURPOSES: dict[int, Purpose] = {}
MAPPED_SPECIAL_PURPOSES: dict[int, MappedPurpose] = {}


MAPPED_PURPOSES_BY_DATA_USE: dict[str, MappedPurpose] = {}


def _load_data():
    with open(
        os.path.join(os.curdir, PURPOSE_MAPPING_FILE), encoding="utf-8"
    ) as mapping_file:
        data = load(mapping_file)
        for raw_purpose in data["purposes"].values():
            purpose = Purpose.parse_obj(raw_purpose)
            mapped_purpose = MappedPurpose.parse_obj(raw_purpose)
            GVL_PURPOSES[purpose.id] = purpose
            MAPPED_PURPOSES[mapped_purpose.id] = mapped_purpose
            for data_use in mapped_purpose.data_uses:
                MAPPED_PURPOSES_BY_DATA_USE[data_use] = mapped_purpose

        for raw_special_purpose in data["specialPurposes"].values():
            special_purpose = Purpose.parse_obj(raw_special_purpose)
            mapped_special_purpose = MappedPurpose.parse_obj(raw_special_purpose)
            GVL_SPECIAL_PURPOSES[special_purpose.id] = special_purpose
            MAPPED_SPECIAL_PURPOSES[mapped_special_purpose.id] = mapped_special_purpose
            for data_use in mapped_special_purpose.data_uses:
                MAPPED_PURPOSES_BY_DATA_USE[data_use] = mapped_special_purpose


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


def data_use_to_purpose(data_use: str) -> Purpose:
    """
    Utility function to return the GVL purpose (or special purpose) associated
    with the given fideslang data use.

    Returns None if no associated purpose (or special purpose) is found
    """
    return MAPPED_PURPOSES_BY_DATA_USE.get(data_use, None)


_load_data()
