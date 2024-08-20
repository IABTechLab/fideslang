import pytest

from fideslang.gvl import (
    GVL_FEATURES,
    GVL_SPECIAL_FEATURES,
    Feature,
    data_category_id_to_data_categories,
    feature_id_to_feature_name,
    feature_name_to_feature,
    purpose_to_data_use,
)


def test_purpose_to_data_use():
    assert purpose_to_data_use(1) == ["functional.storage"]
    assert purpose_to_data_use(1, False) == [
        "functional.storage"
    ]  # assert False is the default

    # testing special purpose lookup
    assert purpose_to_data_use(1, True) == [
        "essential.fraud_detection",
        "essential.service.security",
    ]

    # let's test one other purpose just to be comprehensive
    assert purpose_to_data_use(4) == [
        "marketing.advertising.first_party.targeted",
        "marketing.advertising.third_party.targeted",
    ]

    assert purpose_to_data_use(11) == ["personalize.content.limited"]

    # assert invalid uses raise KeyErrors
    with pytest.raises(KeyError):
        purpose_to_data_use(12)

    with pytest.raises(KeyError):
        purpose_to_data_use(3, True)


def test_features():
    """Add a sanity check for features and special features parsing"""
    assert isinstance(GVL_FEATURES[1], Feature)
    assert GVL_FEATURES[1].name == "Match and combine data from other data sources"

    assert isinstance(GVL_SPECIAL_FEATURES[1], Feature)
    assert GVL_SPECIAL_FEATURES[1].name == "Use precise geolocation data"


def test_feature_name_to_feature():
    assert feature_name_to_feature("Link different devices").id == 2
    assert feature_name_to_feature("Use precise geolocation data").id == 1
    assert feature_name_to_feature("Name doesn't exist") is None


def test_feature_id_to_feature_name():
    assert (
        feature_id_to_feature_name(feature_id=1)
        == "Match and combine data from other data sources"
    )
    assert (
        feature_id_to_feature_name(feature_id=1, special_feature=True)
        == "Use precise geolocation data"
    )

    assert feature_id_to_feature_name(feature_id=1001) is None


def test_data_category_id_to_data_categories():
    assert data_category_id_to_data_categories(1) == ["user.device.ip_address"]

    # let's test one other data category just to be comprehensive
    assert data_category_id_to_data_categories(5) == [
        "user.account",
        "user.unique_id",
        "user.device",
    ]

    # assert invalid categories raise KeyErrors
    with pytest.raises(KeyError):
        data_category_id_to_data_categories(12)
