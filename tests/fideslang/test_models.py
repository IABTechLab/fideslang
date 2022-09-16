import pytest

from fideslang import PrivacyDeclaration, System


@pytest.mark.unit
class TestSystem:
    def test_system_valid(self) -> None:
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
                    dataset_references=[],
                    name="declaration-name",
                )
            ],
            registry_id=1,
            system_dependencies=[],
            system_type="SYSTEM",
            tags=["some", "tags"],
        )
