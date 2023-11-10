from collections import Counter
from typing import Tuple

import pytest

from fideslang.default_taxonomy import DEFAULT_TAXONOMY

taxonomy_counts = {
    "data_category": 85,
    "data_use": 55,
    "data_subject": 15,
}


class TestDefaultTaxonomy:
    @pytest.mark.parametrize(
        "type_and_count", taxonomy_counts.items(), ids=lambda items: items[0]
    )
    def test_taxonomy_count(self, type_and_count: Tuple[str, int]) -> None:
        data_type = type_and_count[0]
        expected_count = type_and_count[1]
        assert len(getattr(DEFAULT_TAXONOMY, data_type)) == expected_count

    @pytest.mark.parametrize("data_type", taxonomy_counts.keys())
    def test_are_set_as_default(self, data_type: str) -> None:
        assert all([x.is_default for x in getattr(DEFAULT_TAXONOMY, data_type)])

    @pytest.mark.parametrize("data_type", taxonomy_counts.keys())
    def test_key_uniqueness(self, data_type: str) -> None:
        keys = [x.fides_key for x in getattr(DEFAULT_TAXONOMY, data_type)]
        duplicate_keys = {
            key: value for key, value in Counter(keys).items() if value > 1
        }
        print(duplicate_keys)
        assert not duplicate_keys

    @pytest.mark.parametrize("data_type", taxonomy_counts.keys())
    def test_name_uniqueness(self, data_type: str) -> None:
        keys = [x.name for x in getattr(DEFAULT_TAXONOMY, data_type)]
        duplicate_keys = {
            key: value for key, value in Counter(keys).items() if value > 1
        }
        print(duplicate_keys)
        assert not duplicate_keys

    @pytest.mark.parametrize("data_type", taxonomy_counts.keys())
    def test_description_uniqueness(self, data_type: str) -> None:
        keys = [
            x.description
            for x in getattr(DEFAULT_TAXONOMY, data_type)
            if not x.version_deprecated
        ]
        duplicate_keys = {
            key: value for key, value in Counter(keys).items() if value > 1
        }
        print(duplicate_keys)
        assert not duplicate_keys

    @pytest.mark.parametrize("data_type", ["data_category", "data_use"])
    def test_parent_keys_exist(self, data_type: str) -> None:
        """This test catches any keys that are used as parents but don't exist as fides keys."""
        fides_keys = set([x.fides_key for x in getattr(DEFAULT_TAXONOMY, data_type)])
        parent_keys = set(
            [x.parent_key for x in getattr(DEFAULT_TAXONOMY, data_type) if x.parent_key]
        )
        diff = parent_keys.difference(fides_keys)
        assert not diff
