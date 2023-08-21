"""
Contains all of the additional validation for the resource models.
"""
import re
from collections import Counter
from typing import Dict, Generator, List, Optional, Pattern, Set, Tuple

from packaging.version import Version
from pydantic import ConstrainedStr

from fideslang.default_fixtures import COUNTRY_CODES

VALID_COUNTRY_CODES = [country["alpha3Code"] for country in COUNTRY_CODES]


class FidesValidationError(ValueError):
    """Custom exception for when the pydantic ValidationError can't be used."""


class FidesVersion(Version):
    """Validate strings as proper semantic versions."""

    @classmethod
    def __get_validators__(cls) -> Generator:
        yield cls.validate

    @classmethod
    def validate(cls, value: str) -> Version:
        """Validates that the provided string is a valid Semantic Version."""
        return Version(value)


class FidesKey(ConstrainedStr):
    """
    A FidesKey type that creates a custom constrained string.
    """

    regex: Pattern[str] = re.compile(r"^[a-zA-Z0-9_.<>-]+$")

    @classmethod  # This overrides the default method to throw the custom FidesValidationError
    def validate(cls, value: str) -> str:
        """Throws ValueError if val is not a valid FidesKey"""

        if not cls.regex.match(value):
            raise FidesValidationError(
                f"FidesKeys must only contain alphanumeric characters, '.', '_', '<', '>' or '-'. Value provided: {value}"
            )

        return value


def sort_list_objects_by_name(values: List) -> List:
    """
    Sort objects in a list by their name.
    This makes resource comparisons deterministic.
    """
    values.sort(key=lambda value: value.name)
    return values


def unique_items_in_list(values: List) -> List:
    """
    Verify that the `name` attributes of each item in the provided list are unique.

    This is useful for fields where there is no FidesKey but we want to
    do a uniqueness check.
    """
    names = [item.name for item in values]
    duplicates: Dict[str, int] = {
        name: count for name, count in Counter(names).items() if count > 1
    }
    if duplicates:
        raise FidesValidationError(
            f"Duplicate entries found: [{','.join(duplicates.keys())}]"
        )

    return values


def no_self_reference(value: FidesKey, values: Dict) -> FidesKey:
    """
    Check to make sure that the fides_key doesn't match other fides_key
    references within an object.

    i.e. DataCategory.parent_key != DataCategory.fides_key
    """
    fides_key = FidesKey.validate(values.get("fides_key", ""))
    if value == fides_key:
        raise FidesValidationError("FidesKey can not self-reference!")
    return value


def deprecated_version_later_than_added(
    version_deprecated: Optional[FidesVersion], values: Dict
) -> Optional[FidesVersion]:
    """
    Check to make sure that the deprecated version is later than the added version.

    This will also catch errors where the deprecated version is defined but the added
    version is empty.
    """

    if not version_deprecated:
        return None

    if version_deprecated < values.get("version_added", Version("0")):
        raise FidesValidationError(
            "Deprecated version number can't be earlier than version added!"
        )

    if version_deprecated == values.get("version_added", Version("0")):
        raise FidesValidationError(
            "Deprecated version number can't be the same as the version added!"
        )
    return version_deprecated


def has_versioning_if_default(is_default: bool, values: Dict) -> bool:
    """
    Check to make sure that version fields are set for default items.
    """

    # If it's a default item, it at least needs a starting version
    if is_default:
        try:
            assert values.get("version_added")
        except AssertionError:
            raise FidesValidationError("Default items must have version information!")
    # If it's not default, it shouldn't have version info
    else:
        try:
            assert not values.get("version_added")
            assert not values.get("version_deprecated")
            assert not values.get("replaced_by")
        except AssertionError:
            raise FidesValidationError(
                "Non-default items can't have version information!"
            )

    return is_default


def is_deprecated_if_replaced(replaced_by: str, values: Dict) -> str:
    """
    Check to make sure that the item has been deprecated if there is a replacement.
    """

    if replaced_by and not values.get("version_deprecated"):
        raise FidesValidationError("Cannot be replaced without deprecation!")

    return replaced_by


def matching_parent_key(parent_key: FidesKey, values: Dict) -> FidesKey:
    """
    Confirm that the parent_key matches the parent parsed from the FidesKey.
    """

    fides_key = FidesKey.validate(values.get("fides_key", ""))
    split_fides_key = fides_key.split(".")

    # Check if it is a top-level resource
    if len(split_fides_key) == 1 and not parent_key:
        return parent_key

    # Reform the parent_key from the fides_key and compare
    parent_key_from_fides_key = ".".join(split_fides_key[:-1])
    if parent_key_from_fides_key != parent_key:
        raise FidesValidationError(
            "The parent_key ({0}) does match the parent parsed ({1}) from the fides_key ({2})!".format(
                parent_key, parent_key_from_fides_key, fides_key
            )
        )
    return parent_key


def check_valid_country_code(country_code_list: List) -> List:
    """
    Validate all listed countries (if present) are valid country codes.
    """
    if country_code_list is not None:
        for country_code in country_code_list:
            if country_code not in VALID_COUNTRY_CODES:
                raise FidesValidationError(
                    "The country identified as {} is not a valid Alpha-3 code per ISO 3166.".format(
                        country_code
                    )
                )
    return country_code_list


def parse_data_type_string(type_string: Optional[str]) -> Tuple[Optional[str], bool]:
    """Parse the data type string. Arrays are expressed in the form 'type[]'.

    e.g.
    - 'string' -> ('string', false)
    - 'string[]' -> ('string', true)

    These data_types are for use in DatasetField.fides_meta.
    """
    if not type_string:
        return None, False
    idx = type_string.find("[]")
    if idx == -1:
        return type_string, False
    return type_string[:idx], True


# Data types that Fides is currently configured to handle
DATA_TYPE_NAMES: Set[str] = {
    "string",
    "integer",
    "float",
    "boolean",
    "object_id",
    "object",
}


def is_valid_data_type(type_name: str) -> bool:
    """Is this type a valid data type identifier in fides?"""
    return type_name is None or type_name in DATA_TYPE_NAMES


def valid_data_type(data_type_str: Optional[str]) -> Optional[str]:
    """If the data_type is provided ensure that it is a member of DataType."""

    parsed_date_type, _ = parse_data_type_string(data_type_str)
    if not is_valid_data_type(parsed_date_type):  # type: ignore
        raise ValueError(f"The data type {data_type_str} is not supported.")

    return data_type_str
