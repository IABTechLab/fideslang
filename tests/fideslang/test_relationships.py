import pytest

from fideslang import relationships
from fideslang.models import (
    ContactDetails,
    DataCategory,
    DataFlow,
    DataProtectionImpactAssessment,
    Dataset,
    DatasetCollection,
    DatasetField,
    DataUse,
    MatchesEnum,
    Organization,
    Policy,
    PolicyRule,
    PrivacyDeclaration,
    System,
    Taxonomy,
)


@pytest.mark.unit
class TestFindReferencedKeys:
    def test_dont_find_all_strings(self) -> None:
        """
        This test is to specifically check that it doesn't send back strings as
        FidesKeys, due to a bug that occurred with the HTTPUrl type.
        """
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
        found_keys = relationships.find_referenced_fides_keys(organization)
        assert found_keys == {"default_organization"}

    def test_dont_find_other_objects(self) -> None:
        """
        This test is to specifically check that it doesn't send back strings as
        FidesKeys, due to a bug that occurred with the HTTPUrl type.
        """
        system = System(
            fides_key="default_organization",
            name="Demo Organization",
            description="An e-commerce organization",
            third_country_transfers=["USA", "CAN", "GBR"],
            system_type="service",
            data_protection_impact_assessment=DataProtectionImpactAssessment(
                is_required=True, progress="ezpz", link="https://ethyca.com"
            ),
            privacy_declarations=[
                PrivacyDeclaration(
                    name="privacy_declaration_1",
                    data_categories=["privacy_declaration_data_category_1"],
                    data_use="privacy_declaration_data_use_1",
                    data_qualifier="privacy_declaration_data_qualifier_1",
                    data_subjects=[
                        "privacy_declaration_data_subject_1",
                        "privacy_declaration_data_subject_2",
                    ],
                    dataset_references=["privacy_declaration_data_set_1"],
                    egress=None,
                    ingress=None,
                    cookies=None,
                ),
            ],
        )
        found_keys = relationships.find_referenced_fides_keys(system)
        expected_keys = {
            "default_organization",
            "privacy_declaration_data_category_1",
            "privacy_declaration_data_use_1",
            "privacy_declaration_data_qualifier_1",
            "privacy_declaration_data_subject_1",
            "privacy_declaration_data_subject_2",
            "privacy_declaration_data_set_1",
        }
        assert not found_keys.difference(expected_keys)

    def test_find_referenced_fides_keys_1(self) -> None:
        test_data_category = DataCategory(
            name="test_dc",
            fides_key="key_1.test_dc",
            description="test description",
            parent_key="key_1",
        )
        expected_referenced_key = {"key_1", "key_1.test_dc", "default_organization"}
        referenced_keys = relationships.find_referenced_fides_keys(test_data_category)
        assert referenced_keys == set(expected_referenced_key)

    def test_find_referenced_fides_keys_2(self) -> None:
        test_system = System.construct(
            name="test_dc",
            fides_key="test_dc",
            description="test description",
            egress=[
                DataFlow(fides_key="key_1", type="system", data_categories=None),
                DataFlow(fides_key="key_2", type="system", data_categories=None),
            ],
            system_type="test",
            privacy_declarations=None,
        )
        expected_referenced_key = {"key_1", "key_2", "test_dc", "default_organization"}
        referenced_keys = relationships.find_referenced_fides_keys(test_system)
        assert referenced_keys == set(expected_referenced_key)

    def test_find_referenced_fides_keys_3(self) -> None:
        resource = DataUse(
            fides_key="direct_marketing",
            name="Direct Marketing",
            description="User information for direct marketing purposes",
            recipients=["Processor - marketing co."],
            legal_basis="Legitimate Interests",
            special_category="Vital Interests",
            legitimate_interest_impact_assessment="https://example.org/legitimate_interest_assessment",
            parent_key=None,
        )
        expected_referenced_key = {"direct_marketing", "default_organization"}
        referenced_keys = relationships.find_referenced_fides_keys(resource)
        assert referenced_keys == set(expected_referenced_key)


@pytest.mark.unit
class TestGetReferencedMissingKeys:
    def test_get_referenced_missing_keys(self):
        taxonomy = Taxonomy(
            data_category=[
                DataCategory(
                    name="test_dc",
                    fides_key="key_1.test_dc",
                    description="test description",
                    parent_key="key_1",
                ),
                DataCategory(
                    name="test_dc2",
                    fides_key="key_1.test_dc2",
                    description="test description",
                    parent_key="key_1",
                ),
            ],
            system=[
                System.construct(
                    name="test_system",
                    fides_key="test_system",
                    description="test description",
                    egress=[
                        DataFlow(
                            fides_key="key_3", type="system", data_categories=None
                        ),
                        DataFlow(
                            fides_key="key_4", type="system", data_categories=None
                        ),
                    ],
                    system_type="test",
                    privacy_declarations=None,
                )
            ],
        )
        expected_referenced_key = {"key_1", "key_3", "key_4", "default_organization"}
        referenced_keys = relationships.get_referenced_missing_keys(taxonomy)
        assert sorted(referenced_keys) == sorted(set(expected_referenced_key))

    def test_get_referenced_missing_privacy_declaration_keys(self):
        taxonomy = Taxonomy(
            system=[
                System(
                    fides_key="system_1",
                    system_type="system_type_1",
                    privacy_declarations=[
                        PrivacyDeclaration(
                            name="privacy_declaration_1",
                            data_categories=["privacy_declaration_data_category_1"],
                            data_use="privacy_declaration_data_use_1",
                            data_qualifier="privacy_declaration_data_qualifier_1",
                            data_subjects=["privacy_declaration_data_subject_1"],
                            dataset_references=["privacy_declaration_data_set_1"],
                        )
                    ],
                )
            ]
        )
        expected_referenced_key = {
            "default_organization",
            "privacy_declaration_data_category_1",
            "privacy_declaration_data_use_1",
            "privacy_declaration_data_qualifier_1",
            "privacy_declaration_data_subject_1",
            "privacy_declaration_data_set_1",
        }
        referenced_keys = relationships.get_referenced_missing_keys(taxonomy)
        assert not referenced_keys.difference(expected_referenced_key)

    def test_get_referenced_missing_policy_keys(self):
        taxonomy = Taxonomy(
            policy=[
                Policy(
                    fides_key="policy_1",
                    rules=[
                        PolicyRule(
                            name="policy_rule_1",
                            data_categories={
                                "values": ["policy_rule_data_category_1"],
                                "matches": MatchesEnum.ANY,
                            },
                            data_uses={
                                "values": ["policy_rule_data_use_1"],
                                "matches": MatchesEnum.ANY,
                            },
                            data_subjects={
                                "values": ["policy_rule_data_subject_1"],
                                "matches": MatchesEnum.ANY,
                            },
                            data_qualifier="policy_rule_data_qualifier_1",
                        )
                    ],
                )
            ],
        )
        expected_referenced_key = {
            "default_organization",
            "policy_rule_data_category_1",
            "policy_rule_data_use_1",
            "policy_rule_data_subject_1",
            "policy_rule_data_qualifier_1",
        }
        referenced_keys = relationships.get_referenced_missing_keys(taxonomy)
        assert not referenced_keys.difference(expected_referenced_key)

    def test_get_referenced_missing_dataset_keys(self):
        taxonomy = Taxonomy(
            dataset=[
                Dataset(
                    fides_key="dataset_1",
                    data_qualifier="dataset_qualifier_1",
                    data_categories=["dataset_data_category_1"],
                    collections=[
                        DatasetCollection(
                            name="dataset_collection_1",
                            data_qualifier="data_collection_data_qualifier_1",
                            data_categories=["dataset_collection_data_category_1"],
                            fields=[
                                DatasetField(
                                    name="dataset_field_1",
                                    data_categories=["dataset_field_data_category_1"],
                                    data_qualifier="dataset_field_data_qualifier_1",
                                )
                            ],
                        )
                    ],
                )
            ],
        )
        expected_referenced_key = {
            "default_organization",
            "dataset_qualifier_1",
            "dataset_data_category_1",
            "data_collection_data_qualifier_1",
            "dataset_collection_data_category_1",
            "dataset_field_data_category_1",
            "dataset_field_data_qualifier_1",
        }
        referenced_keys = relationships.get_referenced_missing_keys(taxonomy)
        assert not referenced_keys.difference(expected_referenced_key)
