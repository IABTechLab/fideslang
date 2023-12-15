# Fideslang

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) [![Twitter](https://img.shields.io/twitter/follow/ethyca?style=social)](https://twitter.com/ethyca)

![Fideslang banner](mkdocs/docs/img/fideslang.png "Fideslang banner")

## Overview

Fideslang or Fides Language is a privacy taxonomy and working draft of a proposed structure to describe data and data processing behaviors as part of a typical software development process. Our hope with standardizing this definition publicly with the community is to derive an interoperable standard for describing types of data and how they're being used in applications to simplify global privacy regulations.

**To view the detailed taxonomy documentation, please visit [https://ethyca.github.io/fideslang/](https://ethyca.github.io/fideslang)**

## Summary of Taxonomy Classification Groups

The taxonomy is currently comprised of three classification groups that are used together to easily describe the data types and associated processing behaviors of an entire tech stack; both the application processes and any data storage.

[Click here to view an interactive visualization of the taxonomy](https://ethyca.github.io/fideslang/explorer/)

### 1. Data Categories

Data Categories are labels used to describe the type of data processed by a system. You can assign one or more data categories to a field when classifying a system.

Data Categories are hierarchical with natural inheritance, meaning you can classify data coarsely with a high-level category (e.g. `user.contact` data), or you can classify it with greater precision using subclasses (e.g. `user.contact.email` data).

Learn more about [Data Categories in the taxonomy reference now](https://ethyca.github.io/fideslang/taxonomy/data_categories/).

### 2. Data Use Categories

Data Use Categories are labels that describe how, or for what purpose(s) a component of your system is using data. Similar to data categories, you can assign one or multiple Data Use Categories to a system.

Data Use Categories are also hierarchical with natural inheritance, meaning you can easily describe what you're using data for either coarsely (e.g. `provide.service.operations`) or with more precision using subclasses (e.g. `provide.service.operations.support.optimization`).

Learn more about [Data Use Categories in the taxonomy reference now](https://ethyca.github.io/fideslang/data_uses/).

### 3. Data Subject Categories

"Data Subject" is a label commonly used in the regulatory world to describe the users of a system whose data is being processed. In many systems a generic user label may be sufficient, however the Privacy Taxonomy is intended to provide greater control through specificity where needed.

Examples of a Data Subject are:

- `anonymous_user`
- `employee`
- `customer`
- `patient`
- `next_of_kin`

Learn more about [Data Subject Categories in the taxonomy reference now](https://ethyca.github.io/fideslang/taxonomy/data_subjects/).

### Extensibility & Interoperability

The taxonomy is designed to support common privacy compliance regulations and standards out of the box, these include GDPR, CCPA, LGPD and ISO 19944.

You can extend the taxonomy to support your system needs. If you do this, we recommend extending from the existing class structures to ensure interoperability inside and outside your organization.

If you have suggestions for missing classifications or concepts, please submit them for addition.
