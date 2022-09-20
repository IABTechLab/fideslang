from pytest import deprecated_call, mark, raises

from fideslang import DataFlow, PrivacyDeclaration, System

pytestmark = mark.unit


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

    def test_system_dependencies_deprecation(self) -> None:
        with deprecated_call(match="system_dependencies"):
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
                system_dependencies=[],
                system_type="SYSTEM",
                tags=["some", "tags"],
            )

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
