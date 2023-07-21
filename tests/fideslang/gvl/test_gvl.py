import pytest

from fideslang.gvl import purpose_to_data_use


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

    assert (
        purpose_to_data_use(11) == []
    )  # purpose 11 is valid, but has no associated data uses

    # assert invalid uses raise KeyErrors
    with pytest.raises(KeyError):
        purpose_to_data_use(12)

    with pytest.raises(KeyError):
        purpose_to_data_use(3, True)
