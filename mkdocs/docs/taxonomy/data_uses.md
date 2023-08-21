# Data Uses Reference

Data Uses are labels that describe how, or for what purpose(s) a component of your system is using data.

A Data Use is a label that denotes the way data is used in your system: "Advertising, Marketing or Promotion", "First Party Advertising", and "Sharing for Legal Obligation", as examples.

Data Use objects form a hierarchy: A Data Use can contain any number of children, but a given Data Use may only have one parent. You assign a child Data Use to a parent by setting the child's `parent_key` property. For example, the `third_party_sharing.personalized_advertising` Data Use type is data used for personalized advertising when shared with third parties.

## Object Structure

**fides_key**<span class="required"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_constrained string_

A string token that uniquely identifies this Data Use. The value is a dot-separated concatenation of the `fides_key` values of the resource's ancestors plus a final element for this resource:

`grandparent.parent.this_data_use`

The final element (`this_data_use`) may only contain alphanumeric characters and underscores (`[A-Za-z0-9_.-]`). The dot character is reserved as a separator.

**name**<span class="spacer"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_string_

A UI-friendly label for the Data Use.

**description**<span class="spacer"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_string_

A human-readable description of the Data Use.

**parent_key**<span class="spacer"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_string_<span class="spacer"/>

The fides key of the the Data Use's parent.


The fides key of the organization to which this Data Use belongs.

!!! Note "Extensibility and interoperability"
    Data Uses in the taxonomy are designed to support common privacy regulations and standards out of the box, these include GDPR, CCPA, LGPD and ISO 19944.

    You can extend the taxonomy to support your system needs. If you do this, we recommend extending from the existing class structures to ensure interoperability inside and outside your organization.

    If you have suggestions for core classes that should ship with the taxonomy, [please submit your requests here](https://github.com/ethyca/privacy-taxonomy/issues)


## Top Level Data Uses

The top-level Data Use classes: 

| Label                                          | Parent Key                 | Description                                                                                          |
| ---                                            | ---                         | ---                                                                                                  |
|`analytics`                                     |`-`                         | Provides analytics for activities such as system and advertising performance reporting, insights and fraud detection.                                                                              |
|`collect`                                       |`-`                         | Collects or stores data in order to use it for another purpose which has not yet been expressly defined.                                                                                                     |
|`employment`                                   |`-`                         | Processes data for the purpose of recruitment or employment and human resources (HR) related activities.                                                                                                                  |
|`essential`                                   |`-`                         | Operates the service or product, including legal obligations, support and basic system operations.                                         |
|`finance`                                   |`-`                         | Enables finance and accounting activities such as audits and tax reporting.     
|`functional`                           |`-`                         |Used for specific, necessary, and legitimate purposes                                                                        |
|`marketing`                                       |`-`                         | Enables marketing, promotion, advertising and sales activities for the product, service, application or system.                                                                               |
|`operations`                               |`-`                         | Supports business processes necessary to the organization's operation.|
|`personalize`                               |`-`                         |Personalizes the product, service, application or system. |
|`sales`                               |`-`                         | Supports sales activities such as communications and outreach.|
|`third_party_sharing`                               |`-`                         | Transfers data to third parties outside of the system or service's scope.|
|`train_ai_system`                               |`-`                         | Trains an AI system or data model for machine learning.|


For each top level classification there are multiple subclasses that provide richer context.
Below is a reference for all subclasses of `account`, `system` and `user` to assist with describing all data across systems.

### Analytics data uses
| Label                                           | Parent Key                         | Description                                                                                          |
| ---                                             | ---                                | ---                                                                                                  |
|  `analytics.reporting.ad_performance`  |  `analytics.reporting`   |  Provides analytics for reporting of advertising performance.  |
|  `analytics.reporting.content_performance`  |  `analytics.reporting`   |  Analytics for reporting on content performance.  |
|  `analytics.reporting.campaign_insights`  |  `analytics.reporting`   |  Provides analytics for reporting of campaign insights related to advertising and promotion activities.  |
|  `analytics.reporting.system`  |  `analytics.reporting`   |  Provides analytics for reporting on system activity.  |
|  `analytics.reporting.system.performance`  |  `analytics.reporting.system`   |  Provides analytics for reporting on system performance.  |

### Employment data uses
| Label                                           | Parent Key                         | Description                                                                                          |
| ---                                             | ---                                | ---                                                                                                  |
|  `employment.recruitment`  |  `employment`   |  Processes data of prospective employees for the purpose of recruitment.  |

### Essential data uses
| Label                                           | Parent Key                         | Description                                                                                          |
| ---                                             | ---                                | ---                                                                                                  |
|  `essential.fraud_detection`  |  `essential`   |  Detects possible fraud or misuse of the product, service, application or system.  |
|  `essential.legal_obligation`  |  `essential`   |  Provides service to meet a legal or compliance obligation such as consent management.  |
|  `essential.service`  |  `essential`   |  Provides the essential product, service, application or system, without which the product/service would not be possible.  |
|  `essential.service.authentication`  |  `essential.service`   |  Authenticate users to the product, service, application or system.  |
|  `essential.service.notifications`  |  `essential.service`   |  Sends notifications about the product, service, application or system.  |
|  `essential.service.operations`  |  `essential.service`   |  Essential to ensure the operation of the product, service, application or system.  |
|  `essential.service.payment_processing`  |  `essential.service`   |  Essential to processes payments for the product, service, application or system.  |
|  `essential.service.security`  |  `essential.service`   |  Essential to provide security for the product, service, application or system  |
|  `essential.service.upgrades`  |  `essential.service`   |  Provides timely system upgrade information options.  |
|  `essential.service.notifications.email`  |  `essential.service.notifications`   |  Sends email notifications about the product, service, application or system.  |
|  `essential.service.notifications.sms`  |  `essential.service.notifications`   |  Sends SMS notifications about the product, service, application or system.  |
|  `essential.service.operations.support`  |  `essential.service.operations`   |  Provides support for the product, service, application or system.  |
|  `essential.service.operations.improve`  |  `essential.service.operations`   |  Essential to optimize and improve support for the product, service, application or system.  |

### Functional Data Uses

| Label                                           | Parent Key                         | Description                                                                                          |
| ---                                             | ---                                | ---                                                                                                  |
|  `functional.storage`  |  `functional`   |  Stores or accesses information from the device as needed when using a product, service, application, or system  |
|  `functional.service`  |  `functional`   |  Functions relating to provided services, products, applications or systems.  |
|  `functional.service.improve`  |  `functional.service`   |  Improves the specific product, service, application or system.  |

### Marketing Data Uses

| Label                                           | Parent Key                         | Description                                                                                          |
| ---                                             | ---                                | ---                                                                                                  |
|  `marketing.advertising`  |  `marketing`   |  Advertises or promotes the product, service, application or system and associated services.  |
|  `marketing.communications`  |  `marketing`   |  Uses combined channels to message and market to a customer, user or prospect.  |
|  `marketing.advertising.first_party`  |  `marketing.advertising`   |  Serves advertisements based on first party data collected or derived about the user.  |
|  `marketing.advertising.frequency_capping`  |  `marketing.advertising`   |  Restricts the number of times a specific advertisement is shown to an individual.  |
|  `marketing.advertising.negative_targeting`  |  `marketing.advertising`   |  Enforces rules used to ensure a certain audience or group is not targeted by advertising.  |
|  `marketing.advertising.profiling`  |  `marketing.advertising`   |  Creates audience profiles for the purpose of targeted advertising  |
|  `marketing.advertising.serving`  |  `marketing.advertising`   |  Essential to the delivery of advertising and content.  |
|  `marketing.advertising.third_party`  |  `marketing.advertising`   |  Serves advertisements based on data within the system or joined with data provided by 3rd parties.  |
|  `marketing.advertising.first_party.contextual`  |  `marketing.advertising.first_party`   |  Serves advertisements based on current content being viewed by the user of the system or service.  |
|  `marketing.advertising.first_party.targeted`  |  `marketing.advertising.first_party`   |  Targets advertisements based on data collected or derived about the user from use of the system.  |
|  `marketing.advertising.third_party.targeted`  |  `marketing.advertising.third_party`   |  Targets advertisements based on data within the system or joined with data provided by 3rd parties.  |
|  `marketing.communications.email`  |  `marketing.communications`   |  Sends email marketing communications.  |
|  `marketing.communications.sms`  |  `marketing.communications`   |  Sends SMS marketing communications.  |

### Personalize Data Uses
| Label                     | Parent Key                         | Description                                                                                    |
| ---                       | ---                                | ---                                                                                            |
|  `personalize.content`  |  `personalize`   |  Personalizes the content of the product, service, application or system.  |
|  `personalize.profiling`  |  `personalize`   |  Creates profiles for the purpose of serving content.  |
|  `personalize.system`  |  `personalize`   |  Personalizes the system.  |

### Third-Party Sharing Data Uses

| Label                     | Parent Key                         | Description                                                                                    |
| ---                       | ---                                | ---                                                                                            |
|  `third_party_sharing.legal_obligation`  |  `third_party_sharing`   |  Shares data for legal obligations, including contracts, applicable laws or regulations.  |

### Collection & AI Training Data Uses

In the case of `collection` and `train_ai_system`, you will see these have no subclasses at present however define very specific data use cases that should be captured in data processes if they occur.

| Label                | Parent Key  | Description                                                                                                                                                                          |
| ---                  | ---         | ---                                                                                                                                                                                  |
|`collect`             | `-`         | Collecting and storing data in order to use it for another purpose such as data training for ML.                                                                                     |
|`train_ai_system`     | `-`         | Training an AI system. Please note when this data use is specified, the method and degree to which a user may be directly identified in the resulting AI system should be appended.  |
