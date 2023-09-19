# Data Categories Reference

Data Categories are labels to describe the type of data processed by your software. Data Category objects form a hierarchy: A Data Category can contain any number of children, but a given Category may only have one parent. You assign a child Category to a parent by setting the child's `parent_key` property. For example, the `user.job_title` Category is used for personally-identifiable job title information for a user.

These are most heavily used by the System and Dataset resources, where you can assign one or more data categories to each field.

## Object Structure

**fides_key**<span class="required"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_constrained string_

A string token that uniquely identifies this Data Category. The value is a dot-separated concatenation of the `fides_key` values of the resource's ancestors plus a final element for this resource:

`grandparent.parent.this_data_category`

The final element (`this_data_category`) may only contain alphanumeric characters and underscores (`[A-Za-z0-9_.-]`). The dot character is reserved as a separator.

**name**<span class="spacer"/>_string_

A UI-friendly label for the Data Category.

**description**<span class="spacer"/>_string_

A human-readable description of the Data Category.

**parent_key**<span class="spacer"/>_string_<span class="spacer"/>

The fides key of the Data Category's parent.

**organization_fides_key**<span class="spacer"/>_string_<span class="spacer"/>default: `default_organization`

The fides key of the organization to which this Data Category belongs.

!!! Note "Extensibility and interoperability"
    Data Categories in the taxonomy are designed to support common privacy regulations and standards out of the box, these include GDPR, CCPA, LGPD and ISO 19944.

    You can extend the taxonomy to support your system needs. If you do this, we recommend extending from the existing class structures to ensure interoperability inside and outside your organization.

    If you have suggestions for core classes that should ship with the taxonomy, [please submit your requests here](https://github.com/ethyca/privacy-taxonomy/issues).


## Top Level Data Categories

There are two top-level categories:


| Label     | Parent Key    | Description                                           |
| ---       | ---           | ---                                                   |
| `system`  | `-`           | Data unique to, and under control of the system.      |
| `user`    | `-`           | Data related to the user of the system.               |

For each top level category there can be multiple subcategories that provide richer context.

Below is a reference for all subcategories of `system` and `user` to assist with describing all data across systems.

## System Data Categories

| Label             | Parent Key    | Description                               |
| ---               | ---           | ---                                       |
| `authentication`  | `system`      | Data used to manage access to the system. |
| `operations`      | `system` 	    | Data used for system operations.          |

## User Data Categories

| Label                             | Parent Key                                | Description                                                                                   |
| ---                               | ---                                       | ---                                                                                           |
|  `user.account`  |	   `user`   | 	Account creation or registration information.   | 
|  `user.authorization`  |	   `user`   | 	Scope of permissions and access to a system.   | 
|  `user.behavior`  |	   `user`   | 	Behavioral data about the subject.   | 
|  `user.biometric`  |	   `user`   | 	Encoded characteristics provided by a user.   | 
|  `user.childrens`  |	   `user`   | 	Data relating to children.   | 
|  `user.contact`  |	   `user`   | 	Contact data collected about a user.   | 
|  `user.content`  |	   `user`   | 	Content related to, or created by the subject.   | 
|  `user.demographic`  |	   `user`   | 	Demographic data about a user.   | 
|  `user.location`  |	   `user`   | 	Records of the location of a user.   | 
|  `user.device`  |	   `user`   | 	Data related to a user's device, configuration and setting.   | 
|  `user.payment`  |	   `user`   | 	Payment data related to user.   | 
|  `user.social`  |	   `user`   | 	Social activity and interaction data.   | 
|  `user.unique_id`  |	   `user`   | 	Unique identifier for a user assigned through system use.   | 
|  `user.telemetry`  |	   `user`   | 	User identifiable measurement data from system sensors and monitoring.   | 
|  `user.user_sensor`  |	   `user`   | 	Measurement data about a user's environment through system use.   | 
|  `user.workplace`  |	   `user`   | 	Organization of employment.   | 
|  `user.sensor`  |	   `user`   | 	Measurement data from sensors and monitoring systems.   | 
|  `user.financial`  |	   `user`   | 	Payment data and financial history.   | 
|  `user.government_id`  |	   `user`   | 	State provided identification data.   | 
|  `user.health_and_medical`  |	   `user`   | 	Health records or individual's personal medical information.   | 
|  `user.name`  |	   `user`   | 	User's real name.   | 
|  `user.criminal_history`  |	   `user`   | 	Criminal records or information about the data subject.   | 
|  `user.privacy_preferences`  |	   `user`   | 	Privacy preferences or settings set by the subject.   | 
|  `user.job_title`  |	   `user`   | 	Professional data.   | 
|  `user.account.settings`  |	   `user.account`   | 	Account preferences and settings.   | 
|  `user.account.username`  |	   `user.account`   | 	Username associated with account.   | 
|  `user.authorization.credentials`  |	   `user.authorization`   | 	Authentication credentials to a system.   | 
|  `user.authorization.biometric`  |	   `user.authorization`   | 	Credentials for system authentication.   | 
|  `user.authorization.password`  |	   `user.authorization`   | 	Password for system authentication.   | 
|  `user.behavior.browsing_history`  |	   `user.behavior`   | 	Content browsing history of a user.   | 
|  `user.behavior.media_consumption`  |	   `user.behavior`   | 	Content consumption history of the subject.   | 
|  `user.behavior.purchase_history`  |	   `user.behavior`   | 	Purchase history of the subject.   | 
|  `user.behavior.search_history`  |	   `user.behavior`   | 	Search history of the subject.   | 
|  `user.biometric.fingerprint`  |	   `user.biometric`   | 	Fingerprint encoded data about a subject.   | 
|  `user.biometric.retinal`  |	   `user.biometric`   | 	Retinal data about a subject.   | 
|  `user.biometric.voice`  |	   `user.biometric`   | 	Voice encoded data about a subject.   | 
|  `user.biometric.health`  |	   `user.biometric`   | 	Encoded characteristic collected about a user.   | 
|  `user.contact.address`  |	   `user.contact`   | 	Contact address data collected about a user.   | 
|  `user.contact.email`  |	   `user.contact`   | 	User's contact email address.   | 
|  `user.contact.phone_number`  |	   `user.contact`   | 	User's phone number.   | 
|  `user.contact.url`  |	   `user.contact`   | 	Subject's websites or links to social and personal profiles.   | 
|  `user.contact.fax_number`  |	   `user.contact`   | 	Data Subject's fax number.   | 
|  `user.contact.organization`  |	   `user.contact`   | 	Data Subject's Organization.   | 
|  `user.contact.address.city`  |	   `user.contact.address`   | 	User's city level address data.   | 
|  `user.contact.address.country`  |	   `user.contact.address`   | 	User's country level address data.   | 
|  `user.contact.address.postal_code`  |	   `user.contact.address`   | 	User's postal code.   | 
|  `user.contact.address.state`  |	   `user.contact.address`   | 	User's state level address data.   | 
|  `user.contact.address.street`  |	   `user.contact.address`   | 	User's street level address data.   | 
|  `user.content.private`  |	   `user.content`   | 	Private content related to, or created by the subject, not publicly available.   | 
|  `user.content.public`  |	   `user.content`   | 	Publicly shared Content related to, or created by the subject.   | 
|  `user.content.self_image`  |	   `user.content`   | 	Photograph or image in which subject is whole or partially recognized.   | 
|  `user.demographic.age_range`  |	   `user.demographic`   | 	Non specific age or age-range of data subject.   | 
|  `user.demographic.date_of_birth`  |	   `user.demographic`   | 	Date of birth of data subject.   | 
|  `user.demographic.gender`  |	   `user.demographic`   | 	Gender of data subject.   | 
|  `user.demographic.language`  |	   `user.demographic`   | 	Spoken or written language of subject.   | 
|  `user.demographic.marital_status`  |	   `user.demographic`   | 	Marital status of data subject.   | 
|  `user.demographic.political_opinion`  |	   `user.demographic`   | 	Political opinion or belief of data subject.   | 
|  `user.demographic.profile`  |	   `user.demographic`   | 	Profile or preference information about the data subject.   | 
|  `user.demographic.race_ethnicity`  |	   `user.demographic`   | 	Race or ethnicity of data subject.   | 
|  `user.demographic.religious_belief`  |	   `user.demographic`   | 	Religion or religious beliefs of the data subject.   | 
|  `user.demographic.sexual_orientation`  |	   `user.demographic`   | 	Sexual orientation of data subject.   | 
|  `user.device.cookie`  |	   `user.device`   | 	Data related to a subject, stored within a cookie.   | 
|  `user.device.cookie_id`  |	   `user.device`   | 	Cookie unique identification number.   | 
|  `user.device.device_id`  |	   `user.device`   | 	Device unique identification number.   | 
|  `user.device.ip_address`  |	   `user.device`   | 	Unique identifier related to device connection.   | 
|  `user.financial.bank_account`  |	   `user.financial`   | 	Bank account information belonging to the subject.   | 
|  `user.financial.credit_card`  |	   `user.financial`   | 	Credit card information belonging to the subject.   | 
|  `user.government_id.birth_certificate`  |	   `user.government_id`   | 	State issued certificate of birth.   | 
|  `user.government_id.drivers_license_number`  |	   `user.government_id`   | 	State issued driving identification number.   | 
|  `user.government_id.immigration`  |	   `user.government_id`   | 	State issued immigration or residency data.   | 
|  `user.government_id.national_identification_number`  |	   `user.government_id`   | 	State issued personal identification number.   | 
|  `user.government_id.passport_number`  |	   `user.government_id`   | 	State issued passport data.   | 
|  `user.government_id.vehicle_registration`  |	   `user.government_id`   | 	State issued license plate or vehicle registration data.   | 
|  `user.health_and_medical.genetic`  |	   `user.health_and_medical`   | 	Data about the genetic makeup provided by the subject.   | 
|  `user.health_and_medical.insurance_beneficiary_id`  |	   `user.health_and_medical`   | 	Health insurance beneficiary number of the subject.   | 
|  `user.health_and_medical.record_id`  |	   `user.health_and_medical`   | 	Medical record identifiers belonging to a subject.   | 
|  `user.location.imprecise`  |	   `user.location`   | 	Imprecise location derived from sensors (more than 500M).   | 
|  `user.location.precise`  |	   `user.location`   | 	Precise location derived from sensors (less than 500M).   | 
|  `user.name.first`  |	   `user.name`   | 	Subject's first name.   | 
|  `user.name.last`  |	   `user.name`   | 	Subject's last, or family, name.   | 
|  `user.unique_id.pseudonymous`  |	   `user.unique_id`   | 	A pseudonymous, or probabilistic identifier generated from other subject or device data belonging to the subject.   | 