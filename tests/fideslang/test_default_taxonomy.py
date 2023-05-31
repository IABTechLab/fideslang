from fideslang.default_taxonomy import DEFAULT_TAXONOMY


class TestDefaultTaxonomy:
    def test_category_count(self):
        assert len(DEFAULT_TAXONOMY.data_category) == 56

    def test_use_count(self):
        assert len(DEFAULT_TAXONOMY.data_use) == 45

    def test_subject_count(self):
        assert len(DEFAULT_TAXONOMY.data_subject) == 15

    def test_qualifier_count(self):
        assert len(DEFAULT_TAXONOMY.data_qualifier) == 5

    def test_organization_count(self):
        assert len(DEFAULT_TAXONOMY.organization) == 1
