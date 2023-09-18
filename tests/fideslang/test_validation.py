import pytest
from pydantic import ValidationError

from fideslang.models import (
    CollectionMeta,
    DataCategory,
    DataFlow,
    Dataset,
    DataUse,
    DataSubject,
    DataQualifier,
    DatasetCollection,
    DatasetField,
    DatasetMetadata,
    DataUse,
    FidesCollectionKey,
    FidesDatasetReference,
    FidesMeta,
    FidesModel,
    Policy,
    PolicyRule,
    PrivacyDeclaration,
    PrivacyRule,
    System,
)
from fideslang.validation import FidesKey, FidesValidationError, valid_data_type

DEFAULT_TAXONOMY_CLASSES = [DataCategory, DataUse, DataQualifier, DataSubject]


@pytest.mark.unit
class TestVersioning:
    """Test versioning functionality for default Taxonomy types."""

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_default_no_versions_error(self, TaxonomyClass):
        """There should be version info for default items."""
        with pytest.raises(ValidationError):
            TaxonomyClass(
                organization_fides_key=1,
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                is_default=True,
            )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_not_default_no_versions_error(self, TaxonomyClass):
        """There shouldn't be version info on a non-default item."""
        with pytest.raises(ValidationError):
            TaxonomyClass(
                organization_fides_key=1,
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                version_added="1.2.3",
            )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_deprecated_when_added(self, TaxonomyClass):
        """Item can't be deprecated in a version earlier than it was added."""
        with pytest.raises(ValidationError):
            TaxonomyClass(
                organization_fides_key=1,
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                is_default=True,
                version_added="1.2",
                version_deprecated="1.2",
            )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_deprecated_after_added(self, TaxonomyClass):
        """Item can't be deprecated in a version earlier than it was added."""
        with pytest.raises(ValidationError):
            TaxonomyClass(
                organization_fides_key=1,
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                is_default=True,
                version_added="1.2.3",
                version_deprecated="0.2",
            )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_built_from_dict_with_empty_versions(self, TaxonomyClass) -> None:
        """Try building from a dictionary with explicit None values."""
        TaxonomyClass.parse_obj(
            {
                "organization_fides_key": 1,
                "fides_key": "user",
                "name": "Custom Test Data",
                "description": "Custom Test Data Category",
                "version_deprecated": None,
                "version_added": None,
                "replaced_by": None,
                "is_default": False,
            }
        )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_built_with_empty_versions(self, TaxonomyClass) -> None:
        """Try building directly with explicit None values."""
        TaxonomyClass(
            organization_fides_key=1,
            fides_key="user",
            name="Custom Test Data",
            description="Custom Test Data Category",
            version_deprecated=None,
            version_added=None,
            replaced_by=None,
            is_default=False,
        )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_deprecated_not_added(self, TaxonomyClass):
        """Can't be deprecated without being added in an earlier version."""
        with pytest.raises(ValidationError):
            TaxonomyClass(
                organization_fides_key=1,
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                is_default=True,
                version_deprecated="0.2",
            )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_replaced_not_deprecated(self, TaxonomyClass):
        """If the field is replaced, it must also be deprecated."""
        with pytest.raises(ValidationError):
            TaxonomyClass(
                organization_fides_key=1,
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                is_default=True,
                version_added="1.2.3",
                replaced_by="some.field",
            )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_replaced_and_deprecated(self, TaxonomyClass):
        """If the field is replaced, it must also be deprecated."""
        assert TaxonomyClass(
            organization_fides_key=1,
            fides_key="user",
            name="Custom Test Data",
            description="Custom Test Data Category",
            is_default=True,
            version_added="1.2.3",
            version_deprecated="1.3",
            replaced_by="some.field",
        )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_version_error(self, TaxonomyClass):
        """Check that versions are validated."""
        with pytest.raises(ValidationError):
            TaxonomyClass(
                organization_fides_key=1,
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                is_default=True,
                version_added="a.2.3",
            )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_versions_valid(self, TaxonomyClass):
        """Check that versions are validated."""
        assert TaxonomyClass(
            organization_fides_key=1,
            fides_key="user",
            name="Custom Test Data",
            description="Custom Test Data Category",
            is_default=True,
            version_added="1.2.3",
        )


@pytest.mark.unit
def test_collections_duplicate_fields_error():
    with pytest.raises(ValidationError):
        DatasetCollection(
            name="foo",
            description="Fides Generated Description for Table: foo",
            data_categories=[],
            fields=[
                DatasetField(
                    name=1,
                    description="Fides Generated Description for Column: 1",
                    data_categories=[],
                ),
                DatasetField(
                    name=2,
                    description="Fides Generated Description for Column: 1",
                    data_categories=[],
                ),
                DatasetField(
                    name=1,
                    description="Fides Generated Description for Column: 1",
                    data_categories=[],
                ),
            ],
        )


@pytest.mark.unit
def test_dataset_duplicate_collections_error():
    with pytest.raises(ValidationError):
        Dataset(
            name="ds",
            fides_key="ds",
            data_categories=[],
            description="Fides Generated Description for Schema: ds",
            collections=[
                DatasetCollection(
                    name="foo",
                    description="Fides Generated Description for Table: foo",
                    data_categories=[],
                    fields=[
                        DatasetField(
                            name=1,
                            description="Fides Generated Description for Column: 1",
                            data_categories=[],
                        ),
                    ],
                ),
                DatasetCollection(
                    name="foo",
                    description="Fides Generated Description for Table: foo",
                    data_categories=[],
                    fields=[
                        DatasetField(
                            name=4,
                            description="Fides Generated Description for Column: 4",
                            data_categories=[],
                        ),
                    ],
                ),
            ],
        )


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
        egress=[
            DataFlow(fides_key="another_system", type="system", data_categories=None),
            DataFlow(
                fides_key="yet_another_system", type="system", data_categories=None
            ),
        ],
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


class TestValidateFidesopsMeta:
    """For backwards compatibility, allowing fidesops_meta to be passed in on various models"""

    def test_fidesops_meta_on_dataset(self):
        """fidesops_meta copied to fides_meta"""
        dataset = Dataset(
            fides_key="test_dataset",
            fidesops_meta={"after": ["other_dataset"]},
            collections=[],
        )

        assert not hasattr(dataset, "fidesops_meta")
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

        assert not hasattr(collection, "fidesops_meta")
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

        assert not hasattr(field, "fidesops_meta")

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

        assert not hasattr(field, "fidesops_meta")
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
        """fidesops_meta copied to fides_meta - fides_meta field takes priority"""
        field = DatasetField(
            name="test_field",
            fides_meta={
                "identity": "identifiable_field_name",
                "primary_key": False,
            },
            fidesops_meta={
                "identity": "other_identifiable_field_name",
                "primary_key": False,
            },
            fields=[],
        )
        assert not hasattr(field, "fidesops_meta")
        assert field.fides_meta == FidesMeta(
            references=None,
            identity="identifiable_field_name",
            primary_key=False,
            data_type=None,
            length=None,
            return_all_elements=None,
            read_only=None,
        )


class TestValidateFidesMeta:
    def test_invalid_length(self):
        with pytest.raises(ValueError):
            FidesMeta(length=0)

    def test_valid_length(self):
        assert FidesMeta(length=1)


class TestValidateDatasetField:
    def test_return_all_elements_not_string_field(self):
        with pytest.raises(ValidationError):
            DatasetField(
                name="test_field",
                fides_meta=FidesMeta(
                    references=None,
                    identity="identifiable_field_name",
                    primary_key=False,
                    data_type="string",
                    length=None,
                    return_all_elements=True,
                    read_only=None,
                ),
            )

    def test_return_all_elements_on_array_field(self):
        assert DatasetField(
            name="test_field",
            fides_meta=FidesMeta(
                references=None,
                identity="identifiable_field_name",
                primary_key=False,
                data_type="string[]",
                length=None,
                return_all_elements=True,
                read_only=None,
            ),
        )

    def test_data_categories_at_object_level(self):
        with pytest.raises(ValidationError) as exc:
            DatasetField(
                name="test_field",
                data_categories=["user"],
                fides_meta=FidesMeta(
                    references=None,
                    identify=None,
                    primary_key=False,
                    data_type="object",
                    length=None,
                    return_all_elements=None,
                    read_only=None,
                ),
                fields=[DatasetField(name="nested_field")],
            )
        assert "Object field 'test_field' cannot have specified data_categories" in str(
            exc
        )

    def test_object_field_conflicting_types(self):
        with pytest.raises(ValidationError) as exc:
            DatasetField(
                name="test_field",
                data_categories=["user"],
                fides_meta=FidesMeta(
                    references=None,
                    identify=None,
                    primary_key=False,
                    data_type="string",
                    length=None,
                    return_all_elements=None,
                    read_only=None,
                ),
                fields=[DatasetField(name="nested_field")],
            )
        assert (
            "The data type 'string' on field 'test_field' is not compatible with specified sub-fields."
            in str(exc)
        )

    def test_data_categories_on_nested_fields(self):
        DatasetField(
            name="test_field",
            fides_meta=FidesMeta(
                references=None,
                identify=None,
                primary_key=False,
                data_type="object",
                length=None,
                read_only=None,
            ),
            fields=[DatasetField(name="nested_field", data_categories=["user"])],
        )


class TestCollectionMeta:
    def test_invalid_collection_key(self):
        with pytest.raises(ValidationError):
            CollectionMeta(after=[FidesCollectionKey("test_key")])

    def test_collection_key_has_too_many_components(self):
        with pytest.raises(ValidationError):
            CollectionMeta(
                after=[FidesCollectionKey("test_dataset.test_collection.test_field")]
            )

    def test_valid_collection_key(self):
        CollectionMeta(after=[FidesCollectionKey("test_dataset.test_collection")])
