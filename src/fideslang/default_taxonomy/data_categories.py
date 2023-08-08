from fideslang.models import DataCategory


DEFAULT_DATA_CATEGORIES = [
    # user
    DataCategory(
        fides_key="user",
        name="User Data",
        description="Data related to the user of the system, either provided directly or derived based on their usage.",
        parent_key=None,
    ),
    # user.account
    DataCategory(
        fides_key="user.account",
        name="Account Information.",
        description="Account creation or registration information.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.account.settings",
        name="Account Information",
        description="Account preferences and settings.",
        parent_key="user.account",
    ),
    DataCategory(
        fides_key="user.account.username",
        name="Account Username",
        description="Username associated with account.",
        parent_key="user.account",
    ),
    # user.authorization
    DataCategory(
        fides_key="user.authorization",
        name="Authorization Information.",
        description="Account creation or registration information.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.authorization.credentials",
        name="Account Credentials.",
        description="Unencrypted authentication credentials to a system.",
        parent_key="user.authorization",
    ),
    DataCategory(
        fides_key="user.authorization.credentials.unencrypted",
        name="Account password.",
        description="Unencrypted authentication credentials to a system.",
        parent_key="user.authorization",
    ),
    # user.biometric
    DataCategory(
        fides_key="user.biometric",
        name="Biometric Data",
        description="Encoded characteristics provided by a user.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.biometric.fingerprint",
        name="Fingerprint",
        description="Fingerprint encoded data about a subject.",
        parent_key="user.biometric",
    ),
    DataCategory(
        fides_key="user.biometric_health",
        name="Biometric Health Data",
        description="Encoded characteristic collected about a user.",
        parent_key="user",
    ),
    # user.browsing
    DataCategory(
        fides_key="user.browsing_history",
        name="Browsing History",
        description="Content browsing history of a user.",
        parent_key="user",
    ),
    # user.demographic
    DataCategory(
        fides_key="user.demographic",
        name="Demographic Data",
        description="Demographic data about a user.",
        parent_key="user",
    ),
    # user.contact
    DataCategory(
        fides_key="user.contact",
        name="Contact Data",
        description="Contact data collected about a user.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.contact.address",
        name="Contact Data",
        description="Contact address data collected about a user.",
        parent_key="user.contact",
    ),
    # user.device
    DataCategory(
        fides_key="user.device",
        name="Device Data",
        description="Data related to a user's device, configuration and setting.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.device.cookie_id",
        name="Cookie ID",
        description="Cookie unique identification number.",
        parent_key="user.device",
    ),
    DataCategory(
        fides_key="user.device.device_id",
        name="Device ID",
        description="Device unique identification number.",
        parent_key="user.device",
    ),
    DataCategory(
        fides_key="user.device.ip_address",
        name="IP Address",
        description="Unique identifier related to device connection.",
        parent_key="user.device",
    ),
    DataCategory(
        fides_key="user.gender",
        name="Gender",
        description="Gender of an individual.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.location",
        name="Location Data",
        description="Records of the location of a user.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.media_consumption",
        name="Media Consumption",
        description="Content Consumption history of the subject",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.non_specific_age",
        name="Non-Specific Age",
        description="Age range data.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.observed",
        name="Observed Data",
        description="Data collected through observation of use of the system.",
        parent_key="user",
    ),
    # user.payment
    DataCategory(
        fides_key="user.payment",
        name="Payment Data",
        description="Payment data related to user.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.profiling",
        name="Profiling Data",
        description="Preference and interest data about a user.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.race",
        name="Race",
        description="Racial or ethnic origin data.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.religious_belief",
        name="Religious Belief",
        description="Religion or religious belief.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.search_history",
        name="Search History",
        description="Records of search history and queries of a user.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.sexual_orientation",
        name="Sexual Orientation",
        description="Personal sex life or sexual data.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.social",
        name="Social Data",
        description="Social activity and interaction data.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.telemetry",
        name="Telemetry Data",
        description="User identifiable measurement data from system sensors and monitoring.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.user_sensor",
        name="User Sensor Data",
        description="Measurement data about a user's environment through system use.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.organization",
        name="Organization Identifiable Data",
        description="Data that is linked to, or identifies an organization.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.workplace",
        name="Workplace",
        description="Organization of employment.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.sensor",
        name="Sensor Data",
        description="Measurement data from sensors and monitoring systems.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.childrens",
        name="Children's Data",
        description="Data relating to children.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.contact.address.city",
        name="User Contact City",
        description="User's city level address data.",
        parent_key="user.contact.address",
    ),
    DataCategory(
        fides_key="user.contact.address.country",
        name="User Contact Country",
        description="User's country level address data.",
        parent_key="user.contact.address",
    ),
    DataCategory(
        fides_key="user.contact.email",
        name="User Contact Email",
        description="User's contact email address.",
        parent_key="user.contact",
    ),
    DataCategory(
        fides_key="user.contact.phone_number",
        name="User Contact Phone Number",
        description="User's phone number.",
        parent_key="user.contact",
    ),
    DataCategory(
        fides_key="user.contact.address.postal_code",
        name="User Contact Postal Code",
        description="User's postal code.",
        parent_key="user.contact.address",
    ),
    DataCategory(
        fides_key="user.contact.address.state",
        name="User Contact State",
        description="User's state level address data.",
        parent_key="user.contact.address",
    ),
    DataCategory(
        fides_key="user.contact.address.street",
        name="User Contact Street",
        description="User's street level address data.",
        parent_key="user.contact.address",
    ),
    DataCategory(
        fides_key="user.credentials",
        name="Credentials",
        description="User authentication data.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.credentials.biometric_credentials",
        name="Biometric Credentials",
        description="Credentials for system authentication.",
        parent_key="user.credentials",
    ),
    DataCategory(
        fides_key="user.credentials.password",
        name="Password",
        description="Password for system authentication.",
        parent_key="user.credentials",
    ),
    DataCategory(
        fides_key="user.date_of_birth",
        name="Date of Birth",
        description="User's date of birth.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.financial",
        name="Financial Data",
        description="Payment data and financial history.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.financial.account_number",
        name="User Financial Account Number",
        description="User's account number for a payment card, bank account, or other financial system.",
        parent_key="user.financial",
    ),
    DataCategory(
        fides_key="user.genetic",
        name="Genetic Data",
        description="Data about the genetic makeup provided by a user.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.government_id",
        name="Government ID",
        description="State provided identification data.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.government_id.national_identification_number",
        name="National Identification Number",
        description="State issued personal identification number.",
        parent_key="user.government_id",
    ),
    DataCategory(
        fides_key="user.government_id.passport_number",
        name="Passport Number",
        description="State issued passport data.",
        parent_key="user.government_id",
    ),
    DataCategory(
        fides_key="user.health_and_medical",
        name="Health and Medical Data",
        description="Health records or individual's personal medical information.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.job_title",
        name="Job Title",
        description="Professional data.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.name",
        name="Name",
        description="User's real name.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="user.political_opinion",
        name="Political Opinion",
        description="Data related to the individual's political opinions.",
        parent_key="user",
    ),
    DataCategory(
        fides_key="system",
        name="System Data",
        description="Data unique to, and under control of the system.",
        parent_key=None,
    ),
    DataCategory(
        fides_key="system.authentication",
        name="Authentication Data",
        description="Data used to manage access to the system.",
        parent_key="system",
    ),
    DataCategory(
        fides_key="system.operations",
        name="Operations Data",
        description="Data used for system operations.",
        parent_key="system",
    ),
]

for category in DEFAULT_DATA_CATEGORIES:
    category.is_default = True
