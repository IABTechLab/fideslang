import pytest
from pydantic import TypeAdapter, ValidationError

from fideslang.models import (
    CollectionMeta,
    DataCategory,
    DataFlow,
    Dataset,
    DatasetCollection,
    DatasetField,
    DatasetMetadata,
    DataSubject,
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
from fideslang.validation import (
    AnyHttpUrlString,
    AnyUrlString,
    FidesValidationError,
    valid_data_type,
    validate_fides_key,
)
from tests.conftest import assert_error_message_includes

DEFAULT_TAXONOMY_CLASSES = [DataCategory, DataUse, DataSubject]


@pytest.mark.unit
class TestVersioning:
    """Test versioning functionality for default Taxonomy types."""

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_default_no_versions_error(self, TaxonomyClass):
        """There should be version info for default items."""
        with pytest.raises(ValidationError) as exc:
            TaxonomyClass(
                organization_fides_key="1",
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                is_default=True,
            )
        assert_error_message_includes(
            exc, "Default items must have version information!"
        )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_not_default_no_versions_error(self, TaxonomyClass):
        """There shouldn't be version info on a non-default item."""
        with pytest.raises(ValidationError) as exc:
            TaxonomyClass(
                organization_fides_key="1",
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                version_added="1.2.3",
            )
        assert_error_message_includes(
            exc, "Non-default items can't have version information!"
        )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_deprecated_when_added(self, TaxonomyClass):
        """Item can't be deprecated in a version earlier than it was added."""
        with pytest.raises(ValidationError) as exc:
            TaxonomyClass(
                organization_fides_key="1",
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                is_default=True,
                version_added="1.2",
                version_deprecated="1.2",
            )
        assert_error_message_includes(
            exc, "Deprecated version number can't be the same as the version added!"
        )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_deprecated_after_added(self, TaxonomyClass):
        """Item can't be deprecated in a version earlier than it was added."""
        with pytest.raises(ValidationError) as exc:
            TaxonomyClass(
                organization_fides_key="1",
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                is_default=True,
                version_added="1.2.3",
                version_deprecated="0.2",
            )
        assert_error_message_includes(
            exc, "Deprecated version number can't be earlier than version added!"
        )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_built_from_dict_with_empty_versions(self, TaxonomyClass) -> None:
        """Try building from a dictionary with explicit None values."""
        TaxonomyClass.model_validate(
            {
                "organization_fides_key": "1",
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
        tc = TaxonomyClass(
            organization_fides_key="1",
            fides_key="user",
            name="Custom Test Data",
            description="Custom Test Data Category",
            version_deprecated=None,
            version_added=None,
            replaced_by=None,
            is_default=False,
        )
        assert tc.version_added is None
        assert not tc.is_default

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_deprecated_not_added(self, TaxonomyClass):
        """Can't be deprecated without being added in an earlier version."""
        with pytest.raises(ValidationError) as exc:
            TaxonomyClass(
                organization_fides_key="1",
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                is_default=True,
                version_deprecated="0.2",
            )
        assert_error_message_includes(
            exc, "Default items must have version information!"
        )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_replaced_not_deprecated(self, TaxonomyClass):
        """If the field is replaced, it must also be deprecated."""
        with pytest.raises(ValidationError) as exc:
            TaxonomyClass(
                organization_fides_key="1",
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                is_default=True,
                version_added="1.2.3",
                replaced_by="some.field",
            )
        assert_error_message_includes(exc, "Cannot be replaced without deprecation!")

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_replaced_and_deprecated(self, TaxonomyClass):
        """If the field is replaced, it must also be deprecated."""
        tc = TaxonomyClass(
            organization_fides_key="1",
            fides_key="user",
            name="Custom Test Data",
            description="Custom Test Data Category",
            is_default=True,
            version_added="1.2.3",
            version_deprecated="1.3",
            replaced_by="some.field",
        )
        assert tc.version_added == "1.2.3"
        assert tc.version_deprecated == "1.3"
        assert tc.replaced_by == "some.field"

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_version_error(self, TaxonomyClass):
        """Check that versions are validated."""
        with pytest.raises(ValidationError) as exc:
            TaxonomyClass(
                organization_fides_key="1",
                fides_key="user",
                name="Custom Test Data",
                description="Custom Test Data Category",
                is_default=True,
                version_added="a.2.3",
            )
        assert_error_message_includes(
            exc, "Field 'version_added' does not have a valid version"
        )

    @pytest.mark.parametrize("TaxonomyClass", DEFAULT_TAXONOMY_CLASSES)
    def test_versions_valid(self, TaxonomyClass):
        """Check that versions are validated."""
        tc = TaxonomyClass(
            organization_fides_key="1",
            fides_key="user",
            name="Custom Test Data",
            description="Custom Test Data Category",
            is_default=True,
            version_added="1.2.3",
        )
        assert tc.version_added == "1.2.3"


@pytest.mark.unit
def test_collections_duplicate_fields_error():
    with pytest.raises(ValidationError) as exc:
        DatasetCollection(
            name="foo",
            description="Fides Generated Description for Table: foo",
            data_categories=[],
            fields=[
                DatasetField(
                    name="1",
                    description="Fides Generated Description for Column: 1",
                    data_categories=[],
                ),
                DatasetField(
                    name="2",
                    description="Fides Generated Description for Column: 1",
                    data_categories=[],
                ),
                DatasetField(
                    name="1",
                    description="Fides Generated Description for Column: 1",
                    data_categories=[],
                ),
            ],
        )
    assert_error_message_includes(exc, "Duplicate entries found: [1]")


@pytest.mark.unit
def test_dataset_duplicate_collections_error():
    with pytest.raises(ValidationError) as exc:
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
                            name="1",
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
                            name="4",
                            description="Fides Generated Description for Column: 4",
                            data_categories=[],
                        ),
                    ],
                ),
            ],
        )
    assert_error_message_includes(exc, "Duplicate entries found: [foo]")


@pytest.mark.unit
def test_top_level_resource():
    DataCategory(
        organization_fides_key="1",
        fides_key="user",
        name="Custom Test Data",
        description="Custom Test Data Category",
    )
    assert DataCategory


@pytest.mark.unit
def test_fides_key_doesnt_match_stated_parent_key():
    with pytest.raises(ValidationError) as exc:
        DataCategory(
            organization_fides_key="1",
            fides_key="user.custom_test_data",
            name="Custom Test Data",
            description="Custom Test Data Category",
            parent_key="user.account",
        )
    assert_error_message_includes(
        exc,
        "The parent_key (user.account) does not match the parent parsed (user) from the fides_key (user.custom_test_data)!",
    )


@pytest.mark.unit
def test_fides_key_matches_stated_parent_key():
    dc = DataCategory(
        organization_fides_key="1",
        fides_key="user.account.custom_test_data",
        name="Custom Test Data",
        description="Custom Test Data Category",
        parent_key="user.account",
    )
    assert dc.fides_key == "user.account.custom_test_data"
    assert dc.parent_key == "user.account"


@pytest.mark.unit
def test_no_parent_key_but_fides_key_contains_parent_key():
    with pytest.raises(ValidationError) as exc:
        DataCategory(
            organization_fides_key="1",
            fides_key="user.custom_test_data",
            name="Custom Test Data",
            description="Custom Test Data Category",
        )
    assert_error_message_includes(
        exc, "The parent_key (None) does not match the parent parsed"
    )


@pytest.mark.unit
def test_fides_key_with_carets():
    dc = DataCategory(
        organization_fides_key="1",
        fides_key="<replacement_text>",
        name="Example valid key with brackets",
        description="This key contains a <> which is valid",
    )
    assert dc.fides_key == "<replacement_text>"


@pytest.mark.unit
def test_invalid_chars_in_fides_key():
    with pytest.raises(ValidationError) as exc:
        DataCategory(
            organization_fides_key="1",
            fides_key="!",
            name="Example invalid key",
            description="This key contains a ! so it is invalid",
        )
    assert_error_message_includes(
        exc, "FidesKeys must only contain alphanumeric characters"
    )


@pytest.mark.unit
def test_create_valid_data_category():
    dc = DataCategory(
        organization_fides_key="1",
        fides_key="user.custom_test_data",
        name="Custom Test Data",
        description="Custom Test Data Category",
        parent_key="user",
    )
    assert dc.name == "Custom Test Data"


@pytest.mark.unit
def test_circular_dependency_data_category():
    with pytest.raises(ValidationError) as exc:
        DataCategory(
            organization_fides_key="1",
            fides_key="user",
            name="User Data",
            description="Test Data Category",
            parent_key="user",
        )
    assert_error_message_includes(exc, "FidesKey cannot self-reference!")


@pytest.mark.unit
def test_create_valid_data_use():
    du = DataUse(
        organization_fides_key="1",
        fides_key="provide.service",
        name="Provide the Product or Service",
        parent_key="provide",
        description="Test Data Use",
    )
    assert du.name == "Provide the Product or Service"


@pytest.mark.unit
def test_circular_dependency_data_use():
    with pytest.raises(ValidationError) as exc:
        DataUse(
            organization_fides_key="1",
            fides_key="provide.service",
            name="Provide the Product or Service",
            description="Test Data Use",
            parent_key="provide.service",
        )
    assert_error_message_includes(exc, "FidesKey cannot self-reference!")


@pytest.mark.unit
@pytest.mark.parametrize("fides_key", ["foo_bar", "foo-bar", "foo.bar", "foo_bar_8"])
def test_fides_model_fides_key_valid(fides_key: str):
    fides_key = FidesModel(fides_key=fides_key, name="Foo Bar")
    assert fides_key


@pytest.mark.unit
@pytest.mark.parametrize("fides_key", ["foo/bar", "foo%bar", "foo^bar"])
def test_fides_model_fides_key_invalid(fides_key):
    """Check for a bunch of different possible bad characters here."""
    with pytest.raises(ValidationError) as exc:
        FidesModel(fides_key=fides_key)
    assert_error_message_includes(
        exc, "FidesKeys must only contain alphanumeric characters"
    )


@pytest.mark.unit
def test_valid_privacy_rule():
    privacy_rule = PrivacyRule(matches="ANY", values=["foo_bar"])
    assert privacy_rule


@pytest.mark.unit
def test_invalid_fides_key_privacy_rule():
    with pytest.raises(ValidationError) as exc:
        PrivacyRule(matches="ANY", values=["foo^bar"])
    assert_error_message_includes(
        exc, "FidesKeys must only contain alphanumeric characters"
    )


@pytest.mark.unit
def test_invalid_matches_privacy_rule():
    with pytest.raises(ValidationError) as exc:
        PrivacyRule(matches="AN", values=["foo_bar"])
    assert_error_message_includes(exc, "Input should be 'ANY'")


@pytest.mark.unit
def test_valid_policy_rule():
    assert PolicyRule(
        organization_fides_key="1",
        policyId=1,
        fides_key="test_policy",
        name="Test Policy",
        description="Test Policy",
        data_categories=PrivacyRule(matches="NONE", values=[]),
        data_uses=PrivacyRule(matches="NONE", values=["provide.service"]),
        data_subjects=PrivacyRule(matches="ANY", values=[]),
    )


@pytest.mark.unit
def test_valid_policy():
    Policy(
        organization_fides_key="1",
        fides_key="test_policy",
        name="Test Policy",
        version="1.3",
        description="Test Policy",
        rules=[],
    )


@pytest.mark.unit
def test_create_valid_system():
    System(
        organization_fides_key="1",
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


@pytest.mark.unit
def test_fides_key_validate_bad_key():
    with pytest.raises(FidesValidationError):
        validate_fides_key("hi!")


@pytest.mark.unit
def test_fides_key_validate_good_key():
    validate_fides_key("hello_test_file<backup>.txt")


@pytest.mark.unit
class TestFidesDatasetReference:
    def test_dataset_invalid(self):
        with pytest.raises(ValidationError) as exc:
            FidesDatasetReference(dataset="bad fides key!", field="test_field")
        assert_error_message_includes(
            exc, "FidesKeys must only contain alphanumeric characters"
        )

    def test_invalid_direction(self):
        with pytest.raises(ValidationError) as exc:
            FidesDatasetReference(
                dataset="test_dataset", field="test_field", direction="backwards"
            )
        assert_error_message_includes(exc, "Input should be 'from' or 'to'")

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

    def test_specify_fides_meta_with_custom_request_field(self):
        """fidesops_meta copied to fides_meta"""
        field = DatasetField(
            name="test_field",
            fides_meta={"custom_request_field": "site_id", "primary_key": False},
            fields=[],
        )

        assert not hasattr(field, "fidesops_meta")
        assert field.fides_meta == FidesMeta(
            references=None,
            identity=None,
            primary_key=False,
            data_type=None,
            length=None,
            return_all_elements=None,
            read_only=None,
            custom_request_field="site_id"
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
    def test_return_all_elements_not_array_field(self):
        with pytest.raises(ValidationError) as exc:
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
        assert_error_message_includes(
            exc,
            "The 'return_all_elements' attribute can only be specified on array fields.",
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
        assert_error_message_includes(
            exc, "Object field 'test_field' cannot have specified data_categories"
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
        assert_error_message_includes(
            exc, "The data type 'string' on field 'test_field' is not compatible with"
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
        with pytest.raises(ValidationError) as exc:
            CollectionMeta(after=[FidesCollectionKey("test_key")])
        assert_error_message_includes(
            exc, "FidesCollection must be specified in the form 'FidesKey.FidesKey'"
        )

    def test_collection_key_has_too_many_components(self):
        with pytest.raises(ValidationError) as exc:
            CollectionMeta(
                after=[FidesCollectionKey("test_dataset.test_collection.test_field")]
            )
        assert_error_message_includes(
            exc, "FidesCollection must be specified in the form 'FidesKey.FidesKey'"
        )

    def test_valid_collection_key(self):
        CollectionMeta(after=[FidesCollectionKey("test_dataset.test_collection")])


class TestAnyUrlString:
    def test_valid_url(self):
        assert AnyUrlString("https://www.example.com/")

    def test_invalid_url(self):
        with pytest.raises(ValidationError) as exc:
            AnyUrlString("invalid_url")

        assert_error_message_includes(exc, "Input should be a valid URL")

    def test_validate_url(self):
        assert (
            TypeAdapter(AnyUrlString).validate_python("ftp://user:password@host")
            == "ftp://user:password@host/"
        ), "Trailing slash added"
        assert (
            TypeAdapter(AnyUrlString).validate_python("ftp:user:password@host/")
            == "ftp://user:password@host/"
        ), "Format corrected"
        assert (
            TypeAdapter(AnyUrlString).validate_python(
                "ftp://user:password@host:3341/path"
            )
            == "ftp://user:password@host:3341/path"
        ), "No change"
        assert (
            TypeAdapter(AnyUrlString).validate_python("https://www.example.com/hello")
            == "https://www.example.com/hello"
        ), "No change"
        assert (
            TypeAdapter(AnyUrlString).validate_python("https://www.example.com/hello/")
            == "https://www.example.com/hello/"
        ), "No change"

    def test_system_urls(self):
        system = System(
            description="Test Policy",
            fides_key="test_system",
            name="Test System",
            organization_fides_key="1",
            privacy_declarations=[],
            system_type="SYSTEM",
            privacy_policy="https://www.example.com",
        )

        # This is a string and not a Url type, because privacy_policy is using custom type AnyUrlString.
        # It also adds a trailing slash to example.com
        assert system.privacy_policy == "https://www.example.com/"

        system = System(
            description="Test Policy",
            fides_key="test_system",
            name="Test System",
            organization_fides_key="1",
            privacy_declarations=[],
            system_type="SYSTEM",
            privacy_policy="https://policy.samsungrs.com/consent/eu/nsc/privacy_policy_de.html",
            legitimate_interest_disclosure_url="https://policy.samsungrs.com/consent/eu/nsc/privacy_policy_de.html#gdpr-article",
        )

        # This is a string and not a Url type, because privacy_policy is using custom type AnyUrlString.
        # No trailing slash is added
        assert (
            system.privacy_policy
            == "https://policy.samsungrs.com/consent/eu/nsc/privacy_policy_de.html"
        )
        assert (
            system.legitimate_interest_disclosure_url
            == "https://policy.samsungrs.com/consent/eu/nsc/privacy_policy_de.html#gdpr-article"
        )


class TestAnyHttpUrlString:
    def test_valid_url(self):
        assert AnyHttpUrlString("https://www.example.com")

    def test_invalid_url(self):
        with pytest.raises(ValidationError) as exc:
            AnyHttpUrlString("invalid_url")

        assert_error_message_includes(exc, "Input should be a valid URL")

    def test_validate_path_of_url(self):
        assert (
            TypeAdapter(AnyHttpUrlString).validate_python("https://www.example.com")
            == "https://www.example.com/"
        ), "Trailing slash added"
        assert (
            TypeAdapter(AnyHttpUrlString).validate_python("https://www.example.com/")
            == "https://www.example.com/"
        ), "No change"
        assert (
            TypeAdapter(AnyHttpUrlString).validate_python(
                "https://www.example.com/hello"
            )
            == "https://www.example.com/hello"
        ), "No change"
        assert (
            TypeAdapter(AnyHttpUrlString).validate_python(
                "https://www.example.com/hello/"
            )
            == "https://www.example.com/hello/"
        ), "No change"

        with pytest.raises(ValidationError) as exc:
            TypeAdapter(AnyHttpUrlString).validate_python("ftp://user:password@host")

        assert_error_message_includes(exc, "URL scheme should be 'http' or 'https'")
