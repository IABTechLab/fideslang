import pytest

from fideslang import DataFlow, PrivacyDeclaration, System


@pytest.mark.unit
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
                    dataset_references=[],
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
