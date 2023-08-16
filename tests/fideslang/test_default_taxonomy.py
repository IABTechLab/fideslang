from fideslang.default_taxonomy import DEFAULT_TAXONOMY
import pytest
from typing import Tuple
from collections import Counter

taxonomy_counts = {
    "data_category": 85,
    "data_use": 51,
    "data_subject": 15,
    "data_qualifier": 5,
    "organization": 1,
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
        keys = [x.description for x in getattr(DEFAULT_TAXONOMY, data_type)]
        duplicate_keys = {
            key: value for key, value in Counter(keys).items() if value > 1
        }
        print(duplicate_keys)
        assert not duplicate_keys
