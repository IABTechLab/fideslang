from pytest import deprecated_call, mark, raises

from fideslang import DataFlow, Dataset, Organization, PrivacyDeclaration, System
from fideslang.models import ContactDetails, DatasetCollection, DatasetField

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
        with raises(ValueError):
            assert DataFlow(fides_key="user", type="system")

    def test_dataflow_user_type_no_user_fides_key(self) -> None:
        with raises(ValueError):
            assert DataFlow(fides_key="test_system_1", type="user")

    def test_dataflow_invalid_type(self) -> None:
        with raises(ValueError):
            assert DataFlow(fides_key="test_system_1", type="invalid")


class TestPrivacyDeclaration:
    def test_privacydeclaration_valid(self) -> None:
        assert PrivacyDeclaration(
            data_categories=[],
            data_qualifier="aggregated_data",
            data_subjects=[],
            data_use="provide",
            egress=[],
            ingress=[],
            name="declaration-name",
        )

    def test_dataset_references_deprecation(self) -> None:
        with deprecated_call(match="dataset_references"):
            assert PrivacyDeclaration(
                data_categories=[],
                data_qualifier="aggregated_data",
                data_subjects=[],
                data_use="provide",
                dataset_references=[],
                egress=["test_system_2"],
                ingress=["test_system_3"],
                name="declaration-name",
            )


class TestSystem:
    def test_system_valid(self) -> None:
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
            ingress=[
                DataFlow(
                    fides_key="test_system_3",
                    type="system",
                    data_categories=[],
                )
            ],
            meta={"some": "meta stuff"},
            name="Test System",
            organization_fides_key=1,
            cookies=[{"name": "test_cookie"}],
            privacy_declarations=[
                PrivacyDeclaration(
                    data_categories=[],
                    data_qualifier="aggregated_data",
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
            registry_id=1,
            system_type="SYSTEM",
            tags=["some", "tags"],
        )

    def test_system_valid_nested_meta(self) -> None:
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
            organization_fides_key=1,
            privacy_declarations=[
                PrivacyDeclaration(
                    data_categories=[],
                    data_qualifier="aggregated_data",
                    data_subjects=[],
                    data_use="provide",
                    egress=["test_system_2"],
                    ingress=["test_system_3"],
                    name="declaration-name",
                )
            ],
            registry_id=1,
            system_type="SYSTEM",
            tags=["some", "tags"],
        )

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
            organization_fides_key=1,
            privacy_declarations=[
                PrivacyDeclaration(
                    data_categories=[],
                    data_qualifier="aggregated_data",
                    data_subjects=[],
                    data_use="provide",
                    egress=["test_system_2"],
                    ingress=["test_system_3"],
                    name="declaration-name",
                )
            ],
            registry_id=1,
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
            organization_fides_key=1,
            privacy_declarations=[
                PrivacyDeclaration(
                    data_categories=[],
                    data_qualifier="aggregated_data",
                    data_subjects=[],
                    data_use="provide",
                    name="declaration-name",
                )
            ],
            registry_id=1,
            system_type="SYSTEM",
            tags=["some", "tags"],
        )

    def test_system_no_egress(self) -> None:
        with raises(ValueError):
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
                organization_fides_key=1,
                privacy_declarations=[
                    PrivacyDeclaration(
                        data_categories=[],
                        data_qualifier="aggregated_data",
                        data_subjects=[],
                        data_use="provide",
                        egress=["test_system_2"],
                        ingress=["test_system_3"],
                        name="declaration-name",
                    )
                ],
                registry_id=1,
                system_type="SYSTEM",
                tags=["some", "tags"],
            )

    def test_system_no_ingress(self) -> None:
        with raises(ValueError):
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
                organization_fides_key=1,
                privacy_declarations=[
                    PrivacyDeclaration(
                        data_categories=[],
                        data_qualifier="aggregated_data",
                        data_subjects=[],
                        data_use="provide",
                        egress=["test_system_2"],
                        ingress=["test_system_3"],
                        name="declaration-name",
                    )
                ],
                registry_id=1,
                system_type="SYSTEM",
                tags=["some", "tags"],
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
            organization_fides_key=1,
            privacy_declarations=[
                PrivacyDeclaration(
                    data_categories=[],
                    data_qualifier="aggregated_data",
                    data_subjects=[],
                    data_use="provide",
                    ingress=["user"],
                    name="declaration-name",
                )
            ],
            registry_id=1,
            system_type="SYSTEM",
            tags=["some", "tags"],
        )


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
            data_qualifier="dataset_qualifier_1",
            data_categories=["dataset_data_category_1"],
            fides_meta={"after": ["other_dataset"]},
            collections=[
                DatasetCollection(
                    name="dataset_collection_1",
                    data_qualifier="data_collection_data_qualifier_1",
                    data_categories=["dataset_collection_data_category_1"],
                    fides_meta={"after": ["third_dataset.blue_collection"]},
                    fields=[
                        DatasetField(
                            name="dataset_field_1",
                            data_categories=["dataset_field_data_category_1"],
                            data_qualifier="dataset_field_data_qualifier_1",
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
                    data_qualifier="data_collection_data_qualifier_2",
                    data_categories=["dataset_collection_data_category_2"],
                    fides_meta={"after": ["orange_dataset.dataset_collection_1"]},
                    fields=[
                        DatasetField(
                            name="dataset_field_2",
                            data_categories=["dataset_field_data_category_2"],
                            data_qualifier="dataset_field_data_qualifier_2",
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
