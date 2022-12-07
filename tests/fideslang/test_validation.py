import pytest
from pydantic import ValidationError

from fideslang.models import (
    DataCategory,
    DataUse,
    FidesModel,
    Policy,
    PolicyRule,
    PrivacyDeclaration,
    PrivacyRule,
    System,
    FidesDatasetReference,
    FidesMeta,
    Dataset,
    DatasetMetadata,
    DatasetCollection,
    CollectionMeta,
    DatasetField,
)
from fideslang.validation import FidesKey, FidesValidationError, valid_data_type


@pytest.mark.unit
def test_top_level_resource():
    DataCategory(
        organization_fides_key=1,
        fides_key="user",
        name="Custom Test Data",
        description="Custom Test Data Category",
    )
    assert DataCategory


@pytest.mark.unit
def test_fides_key_doesnt_match_stated_parent_key():
    with pytest.raises(ValidationError):
        DataCategory(
            organization_fides_key=1,
            fides_key="user.custom_test_data",
            name="Custom Test Data",
            description="Custom Test Data Category",
            parent_key="user.account",
        )
    assert DataCategory


@pytest.mark.unit
def test_fides_key_matches_stated_parent_key():
    DataCategory(
        organization_fides_key=1,
        fides_key="user.account.custom_test_data",
        name="Custom Test Data",
        description="Custom Test Data Category",
        parent_key="user.account",
    )
    assert DataCategory


@pytest.mark.unit
def test_no_parent_key_but_fides_key_contains_parent_key():
    with pytest.raises(ValidationError):
        DataCategory(
            organization_fides_key=1,
            fides_key="user.custom_test_data",
            name="Custom Test Data",
            description="Custom Test Data Category",
        )
    assert DataCategory


@pytest.mark.unit
def test_fides_key_with_carets():
    DataCategory(
        organization_fides_key=1,
        fides_key="<replacement_text>",
        name="Example valid key with brackets",
        description="This key contains a <> which is valid",
    )
    assert DataCategory


@pytest.mark.unit
def test_invalid_chars_in_fides_key():
    with pytest.raises(ValidationError):
        DataCategory(
            organization_fides_key=1,
            fides_key="!",
            name="Example invalid key",
            description="This key contains a ! so it is invalid",
        )
    assert DataCategory


@pytest.mark.unit
def test_create_valid_data_category():
    DataCategory(
        organization_fides_key=1,
        fides_key="user.custom_test_data",
        name="Custom Test Data",
        description="Custom Test Data Category",
        parent_key="user",
    )
    assert DataCategory


@pytest.mark.unit
def test_circular_dependency_data_category():
    with pytest.raises(ValidationError):
        DataCategory(
            organization_fides_key=1,
            fides_key="user",
            name="User Data",
            description="Test Data Category",
            parent_key="user",
        )
    assert True


@pytest.mark.unit
def test_create_valid_data_use():
    DataUse(
        organization_fides_key=1,
        fides_key="provide.service",
        name="Provide the Product or Service",
        parent_key="provide",
        description="Test Data Use",
    )
    assert True


@pytest.mark.unit
def test_circular_dependency_data_use():
    with pytest.raises(ValidationError):
        DataUse(
            organization_fides_key=1,
            fides_key="provide.service",
            name="Provide the Product or Service",
            description="Test Data Use",
            parent_key="provide.service",
        )
    assert True


@pytest.mark.unit
@pytest.mark.parametrize("fides_key", ["foo_bar", "foo-bar", "foo.bar", "foo_bar_8"])
def test_fides_model_valid(fides_key: str):
    fides_key = FidesModel(fides_key=fides_key, name="Foo Bar")
    assert fides_key


@pytest.mark.unit
@pytest.mark.parametrize("fides_key", ["foo/bar", "foo%bar", "foo^bar"])
def test_fides_model_fides_key_invalid(fides_key):
    """Check for a bunch of different possible bad characters here."""
    with pytest.raises(ValidationError):
        FidesModel(fides_key=fides_key)


@pytest.mark.unit
def test_valid_privacy_rule():
    privacy_rule = PrivacyRule(matches="ANY", values=["foo_bar"])
    assert privacy_rule


@pytest.mark.unit
def test_invalid_fides_key_privacy_rule():
    with pytest.raises(ValidationError):
        PrivacyRule(matches="ANY", values=["foo^bar"])
    assert True


@pytest.mark.unit
def test_invalid_matches_privacy_rule():
    with pytest.raises(ValidationError):
        PrivacyRule(matches="AN", values=["foo_bar"])
    assert True


@pytest.mark.unit
def test_valid_policy_rule():
    assert PolicyRule(
        organization_fides_key=1,
        policyId=1,
        fides_key="test_policy",
        name="Test Policy",
        description="Test Policy",
        data_categories=PrivacyRule(matches="NONE", values=[]),
        data_uses=PrivacyRule(matches="NONE", values=["provide.service"]),
        data_subjects=PrivacyRule(matches="ANY", values=[]),
        data_qualifier="aggregated.anonymized.unlinked_pseudonymized.pseudonymized",
    )


@pytest.mark.unit
def test_valid_policy():
    Policy(
        organization_fides_key=1,
        fides_key="test_policy",
        name="Test Policy",
        version="1.3",
        description="Test Policy",
        rules=[],
    )
    assert True


@pytest.mark.unit
def test_create_valid_system():
    System(
        organization_fides_key=1,
        registryId=1,
        fides_key="test_system",
        system_type="SYSTEM",
        name="Test System",
        description="Test Policy",
        privacy_declarations=[
            PrivacyDeclaration(
                name="declaration-name",
                data_categories=[],
                data_use="provide.service",
                data_subjects=[],
                data_qualifier="aggregated_data",
                dataset_references=[],
            )
        ],
        system_dependencies=["another_system", "yet_another_system"],
    )
    assert True


@pytest.mark.unit
def test_circular_dependency_system():
    with pytest.raises(ValidationError):
        System(
            organization_fides_key=1,
            registryId=1,
            fides_key="test_system",
            system_type="SYSTEM",
            name="Test System",
            description="Test Policy",
            privacy_declarations=[
                PrivacyDeclaration(
                    name="declaration-name",
                    data_categories=[],
                    data_use="provide.service",
                    data_subjects=[],
                    data_qualifier="aggregated_data",
                    dataset_references=["test_system"],
                )
            ],
            system_dependencies=["test_system"],
        )
    assert True


@pytest.mark.unit
@pytest.mark.parametrize("country_code", ["United States", "US", "usa"])
def test_invalid_country_identifier(country_code: str):
    """Validate some invalid country identifiers raise an error"""
    with pytest.raises(ValidationError):
        System(
            organization_fides_key=1,
            registryId=1,
            fides_key="test_system",
            system_type="SYSTEM",
            name="Test System",
            description="Test Policy",
            third_country_transfers=[country_code],
            privacy_declarations=[
                PrivacyDeclaration(
                    name="declaration-name",
                    data_categories=[],
                    data_use="provide.service",
                    data_subjects=[],
                    data_qualifier="aggregated_data",
                    dataset_references=["test_system"],
                )
            ],
        )
    assert True


@pytest.mark.unit
@pytest.mark.parametrize("country_code", ["CAN", "USA", "GBR"])
def test_valid_country_identifier(country_code: str):
    """Validates usage of alpha-3 codes per ISO 3166"""
    System(
        organization_fides_key=1,
        registryId=1,
        fides_key="test_system",
        system_type="SYSTEM",
        name="Test System",
        description="Test Policy",
        third_country_transfers=[country_code],
        privacy_declarations=[
            PrivacyDeclaration(
                name="declaration-name",
                data_categories=[],
                data_use="provide.service",
                data_subjects=[],
                data_qualifier="aggregated_data",
                dataset_references=["test_system"],
            )
        ],
    )
    assert True


@pytest.mark.unit
def test_fides_key_validate_bad_key():
    with pytest.raises(FidesValidationError):
        FidesKey.validate("hi!")


@pytest.mark.unit
def test_fides_key_validate_good_key():
    FidesKey.validate("hello_test_file<backup>.txt")


@pytest.mark.unit
class TestFidesDatasetReference:
    def test_dataset_invalid(self):
        with pytest.raises(ValidationError):
            FidesDatasetReference(dataset="bad fides key!", field="test_field")

    def test_invalid_direction(self):
        with pytest.raises(ValidationError):
            FidesDatasetReference(
                dataset="test_dataset", field="test_field", direction="backwards"
            )

    def valid_dataset_reference_to(self):
        ref = FidesDatasetReference(
            dataset="test_dataset", field="test_field", direction="to"
        )

        assert ref

    def valid_dataset_reference_from(self):
        ref = FidesDatasetReference(
            dataset="test_dataset", field="test_field", direction="from"
        )

        assert ref

    def valid_dataset_reference_no_direction(self):
        ref = FidesDatasetReference(
            dataset="test_dataset",
            field="test_field",
        )

        assert ref


class TestValidateDataType:
    """Data types supported by fides"""

    def test_invalid_data_type(self):
        with pytest.raises(ValueError):
            valid_data_type("str")

    def test_valid_data_type(self):
        assert valid_data_type("string")


class TestValidateFidesMeta:
    def test_invalid_length(self):
        with pytest.raises(ValueError):
            FidesMeta(length=0)

    def test_valid_length(self):
        assert FidesMeta(length=1)


class TestFidesopsMetaConversion:
    """For backwards compatibility, allowing fidesops_meta to be passed in on various models"""

    def test_fidesops_meta_on_dataset(self):
        """fidesops_meta copied to fides_meta"""
        dataset = Dataset(
            fides_key="test_dataset",
            fidesops_meta={"after": ["other_dataset"]},
            collections=[],
        )

        assert dataset.fidesops_meta is None
        assert dataset.fides_meta == DatasetMetadata(
            after=["other_dataset"], resource_id=None
        )

    def test_fidesops_meta_on_collection(self):
        """fidesops_meta copied to fides_meta"""
        collection = DatasetCollection(
            name="orange_collection",
            fidesops_meta={"after": ["other_dataset.other_collection"]},
            fields=[],
        )

        assert collection.fidesops_meta is None
        assert collection.fides_meta == CollectionMeta(
            after=["other_dataset.other_collection"]
        )

    def test_fidesops_meta_on_field(self):
        """fidesops_meta copied to fides_meta"""
        field = DatasetField(
            name="test_field",
            fidesops_meta={"identity": "identifiable_field_name", "primary_key": False},
            fields=[],
        )

        assert field.fidesops_meta is None
        assert field.fides_meta == FidesMeta(
            references=None,
            identity="identifiable_field_name",
            primary_key=False,
            data_type=None,
            length=None,
            return_all_elements=None,
            read_only=None,
        )

    def test_specify_fides_meta_directly(self):
        """fidesops_meta copied to fides_meta"""
        field = DatasetField(
            name="test_field",
            fides_meta={"identity": "identifiable_field_name", "primary_key": False},
            fields=[],
        )

        assert field.fidesops_meta is None
        assert field.fides_meta == FidesMeta(
            references=None,
            identity="identifiable_field_name",
            primary_key=False,
            data_type=None,
            length=None,
            return_all_elements=None,
            read_only=None,
        )

    def test_specify_both_fidesops_meta_and_fides_meta(self):
        """fidesops_meta copied to fides_meta"""
        with pytest.raises(ValidationError):
            DatasetField(
                name="test_field",
                fides_meta={
                    "identity": "identifiable_field_name",
                    "primary_key": False,
                },
                fidesops_meta={
                    "identity": "identifiable_field_name",
                    "primary_key": False,
                },
                fields=[],
            )
