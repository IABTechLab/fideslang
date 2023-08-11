from functools import partial

from fideslang.models import DataSubject

from .utils import default_factory

default_subject_factory = partial(default_factory, taxonomy_class=DataSubject)


DEFAULT_DATA_SUBJECTS = [
    default_subject_factory(
        fides_key="anonymous_user",
        organization_fides_key="default_organization",
        name="Anonymous User",
        description="An individual that is unidentifiable to the systems. Note - This should only be applied to truly anonymous users where there is no risk of re-identification",
    ),
    default_subject_factory(
        fides_key="citizen_voter",
        organization_fides_key="default_organization",
        name="Citizen Voter",
        description="An individual registered to voter with a state or authority.",
    ),
    default_subject_factory(
        fides_key="commuter",
        organization_fides_key="default_organization",
        name="Commuter",
        description="An individual that is traveling or transiting in the context of location tracking.",
    ),
    default_subject_factory(
        fides_key="consultant",
        organization_fides_key="default_organization",
        name="Consultant",
        description="An individual employed in a consultative/temporary capacity by the organization.",
    ),
    default_subject_factory(
        fides_key="customer",
        organization_fides_key="default_organization",
        name="Customer",
        description="An individual or other organization that purchases goods or services from the organization.",
    ),
    default_subject_factory(
        fides_key="employee",
        organization_fides_key="default_organization",
        name="Employee",
        description="An individual employed by the organization.",
    ),
    default_subject_factory(
        fides_key="job_applicant",
        organization_fides_key="default_organization",
        name="Job Applicant",
        description="An individual applying for employment to the organization.",
    ),
    default_subject_factory(
        fides_key="next_of_kin",
        organization_fides_key="default_organization",
        name="Next of Kin",
        description="A relative of any other individual subject where such a relationship is known.",
    ),
    default_subject_factory(
        fides_key="passenger",
        organization_fides_key="default_organization",
        name="Passenger",
        description="An individual traveling on some means of provided transport.",
    ),
    default_subject_factory(
        fides_key="patient",
        organization_fides_key="default_organization",
        name="Patient",
        description="An individual identified for the purposes of any medical care.",
    ),
    default_subject_factory(
        fides_key="prospect",
        organization_fides_key="default_organization",
        name="Prospect",
        description="An individual or organization to whom an organization is selling goods or services.",
    ),
    default_subject_factory(
        fides_key="shareholder",
        organization_fides_key="default_organization",
        name="Shareholder",
        description="An individual or organization that holds equity in the organization.",
    ),
    default_subject_factory(
        fides_key="supplier_vendor",
        organization_fides_key="default_organization",
        name="Supplier/Vendor",
        description="An individual or organization that provides services or goods to the organization.",
    ),
    default_subject_factory(
        fides_key="trainee",
        organization_fides_key="default_organization",
        name="Trainee",
        description="An individual undergoing training by the organization.",
    ),
    default_subject_factory(
        fides_key="visitor",
        organization_fides_key="default_organization",
        name="Visitor",
        description="An individual visiting a location.",
    ),
]
