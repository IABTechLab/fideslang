from datetime import datetime

from pytest import mark, raises

from fideslang import DataFlow, Dataset, Organization, PrivacyDeclaration, System
from fideslang.models import (
    ContactDetails,
    Cookies,
    DataResponsibilityTitle,
    DatasetCollection,
    DatasetField,
    DataUse,
)
from tests.conftest import assert_error_message_includes

pytestmark = mark.unit


class TestOrganization:
    def test_valid_organization(self) -> None:
        """Create a standard organization"""

    organization = Organization(
        fides_key="default_organization",
        name="Demo Organization",
        description="An e-commerce organization",
        security_policy="https://ethyca.com/privacy-policy/",
        controller=ContactDetails(
            name="Con Troller",
            address="123 demo street, New York, NY, USA",
            email="controller@demo_company.com",
            phone="+1 555 555 5555",
        ),
        data_protection_officer=ContactDetails(
            name="DataPro Tection",
            address="123 demo street, New York, NY, USA",
            email="dpo@demo_company.com",
            phone="+1 555 555 5555",
        ),
        representative=ContactDetails(
            name="Rep Resentative",
            address="123 demo street, New York, NY, USA",
            email="representative@demo_company.com",
            phone="+1 555 555 5555",
        ),
        fidesctl_meta=None,
    )
    assert organization


class TestDataFlow:
    def test_dataflow_valid(self) -> None:
        assert DataFlow(
            fides_key="test_system_1",
            type="system",
            data_categories=[],
        )

    def test_dataflow_user_fides_key_no_user_type(self) -> None:
        with raises(ValueError) as exc:
            assert DataFlow(fides_key="user", type="system")
        assert_error_message_includes(
            exc, "The 'user' fides_key is required for, and requires, the type 'user'"
        )

    def test_dataflow_user_type_no_user_fides_key(self) -> None:
        with raises(ValueError) as exc:
            assert DataFlow(fides_key="test_system_1", type="user")
        assert_error_message_includes(
            exc, "The 'user' fides_key is required for, and requires, the type 'user'"
        )

    def test_dataflow_invalid_type(self) -> None:
        with raises(ValueError) as exc:
            assert DataFlow(fides_key="test_system_1", type="invalid")
        assert_error_message_includes(
            exc, "'type' must be one of dataset, system, user"
        )


class TestPrivacyDeclaration:
    def test_privacydeclaration_valid(self) -> None:
        assert PrivacyDeclaration(
            data_categories=[],
            data_subjects=[],
            data_use="provide",
            egress=[],
            ingress=[],
            name="declaration-name",
        )


class TestSystem:
    # TODO: these tests are not effectively evaluating whether the provided constructor args
    # are actually supported, because our `System` model does not prohibit "extra" fields.
    # We need to update these tests to assert that the provided args are actually being set
    # as attributes on the System instance that's instantiated.
    def test_system_valid(self) -> None:
        system = System(
            description="Test Policy",
            egress=[
                DataFlow(
                    fides_key="test_system_2",
                    type="system",
                    data_categories=[],
                )
            ],
            fides_key="test_system",
            ingress=[
                DataFlow(
                    fides_key="test_system_3",
                    type="system",
                    data_categories=[],
                )
            ],
            meta={"some": "meta stuff"},
            name="Test System",
            organization_fides_key="1",
            cookies=[{"name": "test_cookie"}],
            privacy_declarations=[
                PrivacyDeclaration(
                    data_categories=[],
                    data_subjects=[],
                    data_use="provide",
                    egress=["test_system_2"],
                    ingress=["test_system_3"],
                    name="declaration-name",
                    cookies=[
                        {"name": "test_cookie", "path": "/", "domain": "example.com"}
                    ],
                )
            ],
            system_type="SYSTEM",
            tags=["some", "tags"],
        )
        assert system.name == "Test System"
        assert system.fides_key == "test_system"
        assert system.description == "Test Policy"
        assert system.egress == [
            DataFlow(
                fides_key="test_system_2",
                type="system",
                data_categories=[],
            )
        ]
        assert system.ingress == [
            DataFlow(
                fides_key="test_system_3",
                type="system",
                data_categories=[],
            )
        ]
        assert system.meta == {"some": "meta stuff"}
        assert system.organization_fides_key == "1"
        assert system.cookies == [Cookies(name="test_cookie", path=None, domain=None)]
        assert system.system_type == "SYSTEM"
        assert system.tags == ["some", "tags"]
        assert system.privacy_declarations == [
            PrivacyDeclaration(
                name="declaration-name",
                data_categories=[],
                data_use="provide",
                data_subjects=[],
                dataset_references=None,
                egress=["test_system_2"],
                ingress=["test_system_3"],
                features=[],
                flexible_legal_basis_for_processing=True,
                legal_basis_for_processing=None,
                impact_assessment_location=None,
                retention_period=None,
                processes_special_category_data=False,
                special_category_legal_basis=None,
                data_shared_with_third_parties=False,
                third_parties=None,
                shared_categories=[],
                cookies=[Cookies(name="test_cookie", path="/", domain="example.com")],
            )
        ]

    def test_system_valid_nested_meta(self) -> None:
        system = System(
            description="Test Policy",
            egress=[
                DataFlow(
                    fides_key="test_system_2",
                    type="system",
                    data_categories=[],
                )
            ],
            fides_key="test_system",
            ingress=[
                DataFlow(
                    fides_key="test_system_3",
                    type="system",
                    data_categories=[],
                )
            ],
            meta={
                "some": "meta stuff",
                "some": {
                    "nested": "meta stuff",
                    "more nested": "meta stuff",
                },
                "some more": {
                    "doubly": {
                        "nested": "meta stuff",
                    }
                },
            },
            name="Test System",
            organization_fides_key="1",
            privacy_declarations=[
                PrivacyDeclaration(
                    data_categories=[],
                    data_subjects=[],
                    data_use="provide",
                    egress=["test_system_2"],
                    ingress=["test_system_3"],
                    name="declaration-name",
                )
            ],
            system_type="SYSTEM",
            tags=["some", "tags"],
        )
        assert system.meta == {
            "some": "meta stuff",
            "some": {
                "nested": "meta stuff",
                "more nested": "meta stuff",
            },
            "some more": {
                "doubly": {
                    "nested": "meta stuff",
                }
            },
        }

    def test_system_valid_no_meta(self) -> None:
        system = System(
            description="Test Policy",
            egress=[
                DataFlow(
                    fides_key="test_system_2",
                    type="system",
                    data_categories=[],
                )
            ],
            fides_key="test_system",
            ingress=[
                DataFlow(
                    fides_key="test_system_3",
                    type="system",
                    data_categories=[],
                )
            ],
            # purposefully omitting the `meta` property to ensure it's effectively optional
            name="Test System",
            organization_fides_key="1",
            privacy_declarations=[
                PrivacyDeclaration(
                    data_categories=[],
                    data_subjects=[],
                    data_use="provide",
                    egress=["test_system_2"],
                    ingress=["test_system_3"],
                    name="declaration-name",
                )
            ],
            system_type="SYSTEM",
            tags=["some", "tags"],
        )
        assert system.meta == None

    def test_system_valid_no_egress_or_ingress(self) -> None:
        assert System(
            description="Test Policy",
            fides_key="test_system",
            meta={"some": "meta stuff"},
            name="Test System",
            organization_fides_key="1",
            privacy_declarations=[
                PrivacyDeclaration(
                    data_categories=[],
                    data_subjects=[],
                    data_use="provide",
                    name="declaration-name",
                )
            ],
            system_type="SYSTEM",
            tags=["some", "tags"],
        )

    def test_system_no_egress(self) -> None:
        with raises(ValueError) as exc:
            assert System(
                description="Test Policy",
                fides_key="test_system",
                ingress=[
                    DataFlow(
                        fides_key="test_system_3",
                        type="system",
                        data_categories=[],
                    )
                ],
                meta={"some": "meta stuff"},
                name="Test System",
                organization_fides_key="1",
                privacy_declarations=[
                    PrivacyDeclaration(
                        data_categories=[],
                        data_subjects=[],
                        data_use="provide",
                        egress=["test_system_2"],
                        ingress=["test_system_3"],
                        name="declaration-name",
                    )
                ],
                system_type="SYSTEM",
                tags=["some", "tags"],
            )
        assert_error_message_includes(
            exc,
            "PrivacyDeclaration 'declaration-name' defines egress with one or more resources and is applied to the System 'test_system', which does not itself define any egress.",
        )

    def test_system_no_ingress(self) -> None:
        with raises(ValueError) as exc:
            assert System(
                description="Test Policy",
                egress=[
                    DataFlow(
                        fides_key="test_system_2",
                        type="system",
                        data_categories=[],
                    )
                ],
                fides_key="test_system",
                meta={"some": "meta stuff"},
                name="Test System",
                organization_fides_key="1",
                privacy_declarations=[
                    PrivacyDeclaration(
                        data_categories=[],
                        data_subjects=[],
                        data_use="provide",
                        egress=["test_system_2"],
                        ingress=["test_system_3"],
                        name="declaration-name",
                    )
                ],
                system_type="SYSTEM",
                tags=["some", "tags"],
            )
        assert_error_message_includes(
            exc,
            "PrivacyDeclaration 'declaration-name' defines ingress with one or more resources and is applied to the System 'test_system', which does not itself define any ingress.",
        )

    def test_system_user_ingress_valid(self) -> None:
        assert System(
            description="Test Policy",
            fides_key="test_system",
            ingress=[
                DataFlow(
                    fides_key="user",
                    type="user",
                    data_categories=[],
                )
            ],
            meta={"some": "meta stuff"},
            name="Test System",
            organization_fides_key="1",
            privacy_declarations=[
                PrivacyDeclaration(
                    data_categories=[],
                    data_subjects=[],
                    data_use="provide",
                    ingress=["user"],
                    name="declaration-name",
                )
            ],
            system_type="SYSTEM",
            tags=["some", "tags"],
        )

    def test_expanded_system(self):
        system = System(
            fides_key="test_system",
            organization_fides_key="1",
            tags=["some", "tags"],
            name="Exponential Interactive, Inc d/b/a VDX.tv",
            description="My system test",
            meta={"some": "meta stuff"},
            system_type="SYSTEM",
            egress=[
                DataFlow(
                    fides_key="test_system_2",
                    type="system",
                    data_categories=[],
                )
            ],
            ingress=[
                DataFlow(
                    fides_key="test_system_3",
                    type="system",
                    data_categories=[],
                )
            ],
            privacy_declarations=[
                PrivacyDeclaration(
                    name="declaration-name",
                    data_categories=[
                        "user.device.ip_address",
                        "user.device.cookie_id",
                        "user.device.device_id",
                        "user.id.pseudonymous",
                        "user.behavior.purchase_history",
                        "user.behavior",
                        "user.behavior.browsing_history",
                        "user.behavior.media_consumption",
                        "user.behavior.search_history",
                        "user.location.imprecise",
                        "user.demographic",
                        "user.privacy_preferences",
                    ],
                    data_use="functional.storage",
                    data_subjects=[],
                    egress=["test_system_2"],
                    ingress=["test_system_3"],
                    features=[
                        "Match and combine data from other data sources",
                        "Link different devices",
                        "Receive and use automatically-sent device characteristics for identification",
                    ],
                    legal_basis_for_processing="Legitimate interests",
                    impact_assessment_location="www.example.com/impact_asessment_location",
                    retention_period="3-5 years",
                    processes_special_category_data=True,
                    special_category_legal_basis="Reasons of substantial public interest (with a basis in law)",
                    data_shared_with_third_parties=True,
                    third_parties="advertising; marketing",
                    shared_categories=[],
                    flexible_legal_basis_for_processing=True,
                    cookies=[
                        {"name": "ANON_ID", "path": "/", "domain": "tribalfusion.com"}
                    ],
                )
            ],
            vendor_id="gvl.1",
            vendor_deleted_date=datetime.now(),
            dataset_references=["test_fides_key_dataset"],
            processes_personal_data=True,
            exempt_from_privacy_regulations=False,
            reason_for_exemption=None,
            uses_profiling=True,
            legal_basis_for_profiling=["Explicit consent", "Contract"],
            does_international_transfers=True,
            legal_basis_for_transfers=["Adequacy Decision", "SCCs", "New legal basis"],
            requires_data_protection_assessments=True,
            dpa_location="www.example.com/dpa_location",
            privacy_policy="https://vdx.tv/privacy/",
            legal_name="Exponential Interactive, Inc d/b/a VDX.tv",
            legal_address="Exponential Interactive Spain S.L.;General Martinez Campos Num 41;Madrid;28010;Spain",
            administrating_department="Privacy Department",
            responsibility=[DataResponsibilityTitle.CONTROLLER],
            dpo="privacyofficertest@vdx.tv",
            data_security_practices=None,
            cookie_max_age_seconds="31536000",
            uses_cookies=True,
            cookie_refresh=True,
            uses_non_cookie_access=True,
            legitimate_interest_disclosure_url="http://www.example.com/legitimate_interest_disclosure",
            previous_vendor_id="gacp.10",
            cookies=[
                {
                    "name": "COOKIE_ID_EXAMPLE",
                    "path": "/",
                    "domain": "example.com/cookie",
                }
            ],
        )
        print(f"dumped={system.model_dump()}")

    def test_flexible_legal_basis_default(self):
        pd = PrivacyDeclaration(
            data_categories=[],
            data_subjects=[],
            data_use="provide",
            ingress=["user"],
            name="declaration-name",
        )
        assert pd.flexible_legal_basis_for_processing


class TestDataset:
    def test_valid_dataset(self):
        Dataset(
            fides_key="dataset_1",
            meta={
                "some": "meta stuff",
                "some": {
                    "nested": "meta stuff",
                    "more nested": "meta stuff",
                },
                "some more": {
                    "doubly": {
                        "nested": "meta stuff",
                    }
                },
            },
            data_categories=["dataset_data_category_1"],
            fides_meta={"after": ["other_dataset"]},
            collections=[
                DatasetCollection(
                    name="dataset_collection_1",
                    data_categories=["dataset_collection_data_category_1"],
                    fides_meta={"after": ["third_dataset.blue_collection"]},
                    fields=[
                        DatasetField(
                            name="dataset_field_1",
                            data_categories=["dataset_field_data_category_1"],
                            fides_meta={
                                "references": [
                                    {
                                        "dataset": "second_dataset",
                                        "field": "red_collection.id",
                                        "direction": "from",
                                    }
                                ],
                                "primary_key": True,
                                "data_type": "integer",
                            },
                        )
                    ],
                ),
                DatasetCollection(
                    name="dataset_collection_2",
                    data_categories=["dataset_collection_data_category_2"],
                    fides_meta={"after": ["orange_dataset.dataset_collection_1"]},
                    fields=[
                        DatasetField(
                            name="dataset_field_2",
                            data_categories=["dataset_field_data_category_2"],
                            fides_meta={
                                "identity": "email",
                                "primary_key": False,
                                "data_type": "string",
                            },
                        )
                    ],
                ),
            ],
        )

    def test_dataset_collection_skip_processing(self):
        collection = DatasetCollection(
            name="dataset_collection_1",
            data_categories=["dataset_collection_data_category_1"],
            fields=[],
        )
        assert not collection.fides_meta

        collection = DatasetCollection(
            name="dataset_collection_1",
            data_categories=["dataset_collection_data_category_1"],
            fides_meta={"after": ["third_dataset.blue_collection"]},
            fields=[],
        )

        assert collection.fides_meta.skip_processing is False

        collection = DatasetCollection(
            name="dataset_collection_1",
            data_categories=["dataset_collection_data_category_1"],
            fides_meta={"skip_processing": True},
            fields=[],
        )

        assert collection.fides_meta.skip_processing


class TestDataUse:
    def test_minimal_data_use(self):
        assert DataUse(fides_key="new_use")
