import pytest

import fideslang as models


@pytest.mark.unit
class TestSystem:
    def test_system_valid(self) -> None:
        system = (
            models.System(
                organization_fides_key=1,
                registry_id=1,
                meta={"some": "meta stuff"},
                fides_key="test_system",
                system_type="SYSTEM",
                name="Test System",
                tags=["some", "tags"],
                description="Test Policy",
                privacy_declarations=[
                    models.PrivacyDeclaration(
                        name="declaration-name",
                        data_categories=[],
                        data_use="provide",
                        data_subjects=[],
                        data_qualifier="aggregated_data",
                        dataset_references=[],
                    )
                ],
                system_dependencies=[],
            ),
        )
        assert system
