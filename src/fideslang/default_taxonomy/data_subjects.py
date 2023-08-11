from fideslang.models import DataSubject
from typing import Dict, Any


def default_factory(**kwargs: Dict[str, Any]) -> DataSubject:
    """
    Generate default data categories.

    Given that we know these are defaults, set values accordingly.
    """

    kwargs["is_default"] = True

    if not kwargs.get("version_added"):
        # This is the version where we started tracking from, so
        # we use it as the default starting point.
        kwargs["version_added"] = "2.0.0"
    item = DataSubject.parse_obj(kwargs)
    return item


DEFAULT_DATA_SUBJECTS = [
    default_factory(
        fides_key="anonymous_user",
        organization_fides_key="default_organization",
        name="Anonymous User",
        description="An individual that is unidentifiable to the systems. Note - This should only be applied to truly anonymous users where there is no risk of re-identification",
        is_default=True,
    ),
    default_factory(
        fides_key="citizen_voter",
        organization_fides_key="default_organization",
        name="Citizen Voter",
        description="An individual registered to voter with a state or authority.",
        is_default=True,
    ),
    default_factory(
        fides_key="commuter",
        organization_fides_key="default_organization",
        name="Commuter",
        description="An individual that is traveling or transiting in the context of location tracking.",
        is_default=True,
    ),
    default_factory(
        fides_key="consultant",
        organization_fides_key="default_organization",
        name="Consultant",
        description="An individual employed in a consultative/temporary capacity by the organization.",
        is_default=True,
    ),
    default_factory(
        fides_key="customer",
        organization_fides_key="default_organization",
        name="Customer",
        description="An individual or other organization that purchases goods or services from the organization.",
        is_default=True,
    ),
    default_factory(
        fides_key="employee",
        organization_fides_key="default_organization",
        name="Employee",
        description="An individual employed by the organization.",
        is_default=True,
    ),
    default_factory(
        fides_key="job_applicant",
        organization_fides_key="default_organization",
        name="Job Applicant",
        description="An individual applying for employment to the organization.",
        is_default=True,
    ),
    default_factory(
        fides_key="next_of_kin",
        organization_fides_key="default_organization",
        name="Next of Kin",
        description="A relative of any other individual subject where such a relationship is known.",
        is_default=True,
    ),
    default_factory(
        fides_key="passenger",
        organization_fides_key="default_organization",
        name="Passenger",
        description="An individual traveling on some means of provided transport.",
        is_default=True,
    ),
    default_factory(
        fides_key="patient",
        organization_fides_key="default_organization",
        name="Patient",
        description="An individual identified for the purposes of any medical care.",
        is_default=True,
    ),
    default_factory(
        fides_key="prospect",
        organization_fides_key="default_organization",
        name="Prospect",
        description="An individual or organization to whom an organization is selling goods or services.",
        is_default=True,
    ),
    default_factory(
        fides_key="shareholder",
        organization_fides_key="default_organization",
        name="Shareholder",
        description="An individual or organization that holds equity in the organization.",
        is_default=True,
    ),
    default_factory(
        fides_key="supplier_vendor",
        organization_fides_key="default_organization",
        name="Supplier/Vendor",
        description="An individual or organization that provides services or goods to the organization.",
        is_default=True,
    ),
    default_factory(
        fides_key="trainee",
        organization_fides_key="default_organization",
        name="Trainee",
        description="An individual undergoing training by the organization.",
        is_default=True,
    ),
    default_factory(
        fides_key="visitor",
        organization_fides_key="default_organization",
        name="Visitor",
        description="An individual visiting a location.",
        is_default=True,
    ),
]
