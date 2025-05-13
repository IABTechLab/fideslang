# Privacy Taxonomy Implementation Guidelines

This document provides technical implementation guidelines related to the Privacy Taxonomy. The Privacy Implementation & Accountability Task Force (PIAT) developed the guidelines to support industry adoption of the Privacy Taxonomy. The intended audience for this document include product and engineering teams, legal teams, and data governance teams.

**These Implementation Guidelines are open for public comment until April 17th, 2025.**

## **Table of Contents**

[1. Introduction to the Privacy Taxonomy](#1-introduction-to-the-privacy-taxonomy)

[1.1 Getting Started](#1-1-getting-started)

[1.2 Glossary of Terms](#1-2-glossary-of-terms)

[1.3 Questions or Feedback](#1-3-questions-or-feedback)

[2. Legal Teams](#2-legal-teams)

[3. Product / Engineering Teams](#3-product-engineering-teams)

[3.1 About the Fides language](#3-1-about-the-fides-language)

[3.1.1 Dataset YAML](#3-1-1-dataset-yaml)

[3.1.2 System YAML](#3-1-2-system-yaml)

[3.2 Syntax](#3-2-syntax)

[3.2.1 Dot Notation and Snake\_Case](#3-2-1-dot-notation-and-snake_case)

[3.2.2 Key-Value](#3-2-2-key-value)

[3.3 Applying the Sensitivity Matrix](#3-3-applying-the-sensitivity-matrix)

[3.4 Applying Data Uses](#3-4-applying-data-uses)

[4. FAQs](#4-faqs)

[Why should I use the Privacy Taxonomy, and how will it help?](#why-should-i-use-the-privacy-taxonomy-and-how-will-it-help)

[How long will it take to implement?](#how-long-will-it-take-to-implement)

[How is the Privacy Taxonomy different from other taxonomies like the Audience Taxonomy?](#how-is-the-privacy-taxonomy-different-from-other-taxonomies-like-the-audience-taxonomy)

[I don’t participate in the Transparency & Consent Framework (TCF) or the Multi-State Privacy Agreement (MSPA), can I still use the Privacy Taxonomy?](#i-dont-participate-in-the-transparency-consent-framework-tcf-or-the-multi-state-privacy-agreement-mspa-can-i-still-use-the-privacy-taxonomy)

[How does the taxonomy respond to technical and legal changes?](#how-does-the-taxonomy-respond-to-technical-and-legal-changes)

[Who has provided inputs to the taxonomy?](#who-has-provided-inputs-to-the-taxonomy)

[I have more questions. Where can I submit them?](#i-have-more-questions-where-can-i-submit-them)


## **1. Introduction to the Privacy Taxonomy** 

The Privacy Taxonomy was developed to assist the industry in managing data privacy compliance and communicating privacy-related information more effectively. It provides a universal language to label and describe privacy-related data elements, the purposes for which data is applied, and the individuals or entities to whom the data pertains. 


### **1.1 Getting Started**

Before adopting the privacy taxonomy, a company should consider the following:

1. Laws that apply / jurisdictions they operate in

   1. Consider which laws may apply and jurisdictions the company operates in. In order to assess which laws may apply, companies should work with legal to undertake a jurisdictional analysis, a fact-based determination to assist in determining which state or country laws might apply to the business. The Taxonomy was built to expand upon the growing list of U.S. state laws and international laws.

2. Type of data they collect and how they use the data

   1. The business should consider the type of data collected and how that data is used in order to properly tag data elements. Data elements provide a standard way to tag data in databases, which can assist with data privacy operations (e.g. data mapping, DSRs, contracts, disclosures, consent/opt-out, etc.). Understanding what type of data the business collects and how that data is used will assist in correct tagging to better align the data element with categories specified in US data privacy laws (e.g., CCPA, CPA). 

      1. For example, user.contact information could align with the ‘identifiers’ category under the CCPA or, under Colorado law, act as its own standalone category. As such, the full data element would be “user.identifers.contact\_information.”

3. Type of industry they’re in

   1. The business should consider their industry in order to better tag data subjects and apply the sensitivity matrix. 

      1. For example, a data subject tag could be “B2B” to indicate those data subjects that are acting within a B2B capacity.


### **1.2 Glossary of Terms**

Below is a glossary of terms as defined within the context of the Privacy Taxonomy. 

|                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Term**                               | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Data Elements                          | Labels to describe the type of data processed by business and technology systems used in the Privacy Taxonomy.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Data Subjects                          | Labels to describe the owner or individual of the data being processed describes used in the Privacy Taxonomy.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Data Uses                              | Labels to describe how, or for what purpose(s) data is being utilized, used in the Privacy Taxonomy.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Multi-State Privacy Agreement (MSPA)   | IAB’s [Multi-State Privacy Agreement (MSPA)](https://www.iabprivacy.com/) creates a common framework for advertisers, agencies, technology vendors, and publishers for implementing  U.S. state privacy laws. It functions as a “springing contract” that creates a contractual relationship amongst signatories as personal information flows between them for purposes of delivering a digital ad.                                                                                                                                       |
| MSPA Activity                          | One of the defined purposes, including Digital Advertising Activities, under the MSPA.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Sensitive Information                  | Personal information that reveals a consumer’s racial or ethnic origin, religious beliefs, mental or physical health diagnosis, sexuality, sex life, sexual orientation, status as transgender or nonbinary, citizenship, immigration status, identifying genetic or biometric data, precise geolocation data, children’s data, as well as additional pieces of data as defined under the [CCPA](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.\&part=4.\&lawCode=CIV\&title=1.81.5) and/or applicable law.  |
| Transparency & Consent Framework (TCF) | IAB Europe’s [Transparency & Consent Framework (TCF)](https://iabeurope.eu/transparency-consent-framework/) is an accountability tool that relies on standardisation to facilitate compliance with certain provisions of the ePrivacy Directive and the GDPR. It applies principles and requirements derived from these two legislative instruments to the specific context of the online industry, taking account of relevant EU-level guidance from the EDPB and national level guidance from Data Protection Authorities.               |
| TCF Purpose                            | One of the defined purposes for processing of data, including users’ personal data, by TCF participants. The purposes are defined in the TCF Policies or the TCF Specifications for which Vendors declare a Legal Basis in the GVL and for which the user is given choice to consent or to object depending on the Legal Basis for the processing, by a CMP.                                                                                                                                                                               |


### **1.3 Questions or Feedback**

If you have questions about the Privacy Taxonomy, refer to the [FAQ section](#faqs) at the bottom of this document. For additional questions or feedback, contact us at <support@iabtechlab.com>. 


## **2. Legal Teams**

Legal may use the Taxonomy to streamline various aspects of data privacy compliance, including: 

- Consumer Requests 

- Cross-functional communication and team collaboration 

- Contracts – Data Protection Agreements/Addenda

- Public-facing disclosures 

- Privacy Policies and Notices 

- Opt-out/Opt-In Choices

- Sensitive Data Activities and Tracking 

- Tracking and Understanding Exceptions

Taxonomy Functions that may assist with the above legal activities include (but are not limited to):

- **Database Tagging**: provides a standardized system to tag and organize data within databases, making it easier to handle legal tasks such as generating data maps, communicating with downstream vendors, managing data subject requests, drafting contracts, making public disclosures, and managing consent/opt-outs/opt-ins. Legal teams can also assign a specific data usage purpose to each element, aligned with applicable laws (e.g. GDPR, CCPA) or frameworks (e.g. MSPA). 

- **Data Use Categorization**: enables Legal to group data into top-level, legally-relevant categories like necessary data, operational data, analytics, marketing, and disclosure-related data (e.g., “sales” or “shares” as defined by applicable law). These categories help Legal and Product organize and align data uses with legally permitted data uses across different contexts.

- **Sensitive Information Tagging**: creates a standardized system for identifying and tagging sensitive information using a scaling matrix, enabling Legal to pinpoint which data elements might trigger specific data privacy law requirements related to sensitive personal information. 

- **Developer Collaboration**: improves communication and collaboration between Legal and Engineering by aligning terminology, including data types and data usages, to enhance and streamline data privacy compliance. For example, it provides clarity by offering Engineering actionable parameters tied directly to legal obligations, reduces inefficiencies by minimizing back-and-forth on definitions, and enables proactive compliance by embedding legal requirements into technical workflows.

- **Legal Exemption Tagging**: enables Legal to label and track data potentially exempt from legal or contractual requirements, enabling Engineering to incorporate these exemptions into the development process and better align the handling of such data with compliance workflows.

- **Applicable Framework**: incorporates data purposes and uses from existing frameworks, such as the TCF Purposes and MSPA’s Digital Advertising Activities, to assist Legal and Product to streamline and align their compliance efforts.


## **3. Product / Engineering Teams**

### **3.1 About the Fides language**

The Fides language is based on **YAML** configuration files. YAML provides a well-understood structure, upon which the Fides language adds helpful primitives which represent types of data, processes or policies. By declaring these primitives with Fides you can describe:

- what types of data your application process (using `data_element` annotations)

- how your system uses that data (using `data_use` annotations)

- and what type of user the data may belong to (using `data_subjects` annotations)


#### **3.1.1 Dataset YAML**

A Dataset declaration in Fides language represents any location where data is stored: databases, data warehouses, caches and other data storage systems. Within a Fides Dataset, you declare collections (e.g. database tables) and the individual fields (e.g. database columns) where data is located and annotate them to describe the categories of data that are stored.


#### **3.1.2 System YAML**

A System declaration in Fides language represents the privacy properties of a single software project, service, codebase, or application. So the Fides System declaration describes both the categories of data being processed, and also the purposes for which that data is processed.


### **3.2 Syntax**

The Fides language is intentionally simple. To assure this, Fides declarations use predefined primitives (e.g. data elements) that are used when describing your datasets, systems, etc. These predefined primitives exist as part of the taxonomy which is maintained in your server so they can be consistently used across your organization's development team.


#### **3.2.1 Dot Notation and Snake\_Case**

To make writing and reading Fides language as easy for humans as possible, declarations from the privacy taxonomy use `dot notation` for the keys and use `snake_case` compound labels.

For example, to describe a field in a database as contact information relating to a user, you can write its data category as: 

    # This declares that the contact data is about a given user:
    user.contact

If we require greater specificity, we could declare the contact type as a phone number by using a more specific sub-category:

    # This declares that the contact data is data about a given user,
    # and is from the contact category and of type phone number.
    user.contact.phone_number


#### **3.2.2 Key-Value**

The key-value is YAML, and Fides', basic building blocks. Every item in a Fides YAML document is a member of at least one dictionary. The key is always a `string`. The value is a scalar so that it can be any datatype. So the value can be a `string`, a `number`, or another `dictionary` - most commonly in Fides, this will be a `string` that may provide a description or a pointer to a reference object in the taxonomy.

If we use the example of a user's contact email, to correctly declare this in valid Fides YAML as part of a Dataset, it would be:

     fields:                           # Group of fields in the dataset.
        - name: email
          description: User's Email
          data_element:             # Data element label(s) to assign field.
            - user.contact.email
            - user.account.contact.email

The key for each key-value pair determines what value types are valid (for example, a resource type such as `data_categories` must use values from the Data Categories taxonomy), but many keys accept arbitrary strings as descriptive labels.

Finally, as you see in the example above, keys such as `data_categories` accept a list of values for multi-labeling. In this case, the field email has been assigned the value user contact email as well as account-related contact email, indicating that it may be either of those categories when used.


### **3.3 Applying the Sensitivity Matrix**

The Sensitivity Matrix assists businesses in tagging data elements to differentiate between sensitive and non-sensitive personal information, helping businesses identify data that may be subject to sensitive information requirements under applicable data privacy laws.

The Sensitivity Matrix uses a scale from 1 to 3 to classify personal data elements as sensitive data under applicable laws, with 1 representing non-sensitive and 3 representing "per se sensitive" as defined by the law. Specifically: 

- 1 = no; 

  - Example: first name

- 2 = no; unless combined with another non-sensitive data point that makes the combined data elements sensitive 

  - Example: account log-in + password/credentials to access the account 

- 3 = yes, per se sensitive as determined by applicable law

  - Example: citizenship status, racial or ethnic origin, religious beliefs, data relating to children, etc.

The business should consult its legal team to ensure the Sensitivity Matrix aligns with the business’s own legal obligations, internal policies, and risk management. 


### **3.4 Applying Data Uses**

The ability to define and apply Data Uses enables a business to specify how data is used and managed in accordance with applicable data privacy laws. For example, if a consumer opts-out of targeted advertising, the business can apply the opt-out request to data labeled as used for “Advertising Marketing” without affecting data used for “Necessary purposes”

Top-level labels are used to categorize Data Uses into the following categories: (1) Necessary, (2) Operational, (3) Analytics, (4) Advertising and Marketing, and (5) Disclosure. Specifically:

- Necessary: Provides essential functions such as legal compliance, security, basic system operations, and support. Without the “necessary” data use, the product or service cannot operate or meet legal and security requirements.

- Operational: Facilitates operations for the service or product, including product improvements. 

- Analytics: Supports analytics activities, such as system and performance reporting, insights generation, and advertising fraud detection.

- Advertising Marketing: Enables marketing, promotion, advertising and sales activities for the product, service, application or system.

- Disclosure: Indicates if data is being transmitted to other parties. 

The business should consult its legal team to ensure Data Use Labels aligns with the business’s own legal obligations, internal policies, and risk management. 


## **4. FAQs**

### Why should I use the Privacy Taxonomy, and how will it help?

The Privacy Taxonomy provides a consistent way to label and categorize data across systems, services, and vendors, ensuring privacy protections are applied uniformly. It helps model privacy risks by linking data categories with their uses, making it easier to assess and manage compliance with regulations. Additionally, a common taxonomy improves interoperability, enabling clearer communication and consistent privacy practices across teams and external partners.


### How long will it take to implement?

When adopting the privacy taxonomy, one way to accelerate implementation is to start annotating your data during the development lifecycle so that you have an up to date inventory of all new data. Depending on your tech stack, open source tools exist to make this process faster, such as <https://github.com/ewdurbin/dbml-to-fides> and [Fides open source](https://github.com/ethyca/fides).


### How is the Privacy Taxonomy different from other taxonomies like the Audience Taxonomy?

The **Privacy Taxonomy** focuses on privacy compliance and data governance, aligning data purposes, processing, and preferences with regulatory frameworks like the GDPR and CCPA. It is primarily used by compliance teams, privacy officers, and data governance professionals to ensure adherence to privacy laws.

The **Audience Taxonomy** is designed for audience targeting and segmentation, standardizing audience interests and demographics for ad campaigns. Its primary users are marketers, advertisers, and data managers who leverage it to improve audience segment consistency and campaign execution.


### I don’t participate in the Transparency & Consent Framework (TCF) or the Multi-State Privacy Agreement (MSPA), can I still use the Privacy Taxonomy?

Participating in frameworks such as the Transparency & Consent Framework (TCF) or the Multi-State Privacy Agreement (MSPA) is not required in order to make use of the taxonomy. However, for organizations who do participate in these frameworks the privacy taxonomy includes citations where frameworks are applicable to increase the usability of the taxonomy. 


### How does the taxonomy respond to technical and legal changes?

The taxonomy is designed to be extensible and align with data privacy laws and frameworks that are currently and/or soon to be in effect. Specifically, the taxonomy is a flexible framework that can be amended as new laws in various jurisdictions come into effect.


### Who has provided inputs to the taxonomy?

Members of the Privacy Implementation & Accountability Task Force which include participants with product, engineering, and legal backgrounds provided inputs to the initial version of the taxonomy. 


### I have more questions. Where can I submit them?

If you have additional questions about the Privacy Taxonomy, contact us at <support@iabtechlab.com>. 
