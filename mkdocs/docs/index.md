# Privacy Taxonomy

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Overview
This Privacy Taxonomy is a working draft of a proposed structure to describe data and data processing behaviors as part of a typical software development process. Our hope with standarizing this definition publicly with the community is to derive an interopable standard for describe types of data and how they're being used in applications to simplify global privacy regulations.

 
## Summary of Taxonomy Classification Groups

The taxonomy currently comprises  of four classification groups that are used together to easily describe all of the data types and associated processing behaviors of an entire tech stack; both the application processes and any data storage. 

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600;700&display=swap"
      rel="stylesheet"
    />
    

<div id="vis" class="vis vis-container">
  <div class="controls-container">
    <div id="data-control" class="control-group">
      <div class="btn-group">
        <button class="btn is-selected" data-chart-data="categories">Data Categories</button>
        <button class="btn" data-chart-data="uses">Data Uses</button>
        <button class="btn" data-chart-data="subjects">Data Subjects</button>
        <button class="btn" data-chart-data="qualifiers">Data Identification Qualifiers</button>
      </div>
    </div>
    <div id="chart-type-control" class="control-group">
      <div class="btn-group">
        <button class="btn btn--icon is-selected" data-chart-type="tree">
          <img src="img/Tree@1x.svg" alt="tree" />
        </button>
        <button class="btn btn--icon" data-chart-type="radialTree">
          <img src="img/Radial%20Tree@1x.svg" alt="radial tree" />
        </button>
        <button class="btn btn--icon" data-chart-type="sunburst" >
          <img src="img/Sunburst@1x.svg" alt="sunburst" />
        </button>
      </div>
    </div>
  </div>
  <div id="vis-chart" class="chart-container">
    <svg id="vis-sunburst"></svg>
    <svg id="vis-radial-tree"></svg>
    <svg id="vis-tree"></svg>
  </div>
  <div id="vis-color-legend"></div>
</div>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="js/vis.js"></script>

### 1. Data Categories
Data Categories are labels to describe the type of data processed by your software. These are most heavily used by the System and Dataset resources, where you can assign one or more data categories to each field.

Data Categories are hierarchical with natural inheritance, meaning you can classify data coarsely with a high-level category (e.g. `user.provided` data), or you can classify it with greater precision using subcategories (e.g. `user.provided.identifiable.contact.email` data).

Learn more about [Data Categories in the taxonomy reference now](data_categories.md).

### 2. Data Use Categories
Data Use Categories are labels that describe how, or for what purpose(s) a component of your system is using data.

Data Use Categories are also hierarchical with natural inheritance, meaning you can easily describe what you're using data for either coarsely (e.g. `provide.system.operations`) or with more precision using subcategories (e.g. `provide.system.operations.support.optimization`).

Learn more about [Data Use Categories in the taxonomy reference now](data_use_categories.md).

### 3. Data Subject Categories
Data Subject is a label commonly used in the regulatory world to describe the users of a system who's data is being processed. In many systems a generic user label may be sufficient, however Fides language is intended to provide greater control through specificity where needed.

Examples of this are:

- `anonymous_user`
- `employee`
- `customer`
- `patient`
- `next_of_kin`

Learn more about [Data Subject Categories in the taxonomy reference now](data_subject_categories.md).

### 4. Data Identification Qualifiers
Data Identification Qualifiers describe the degree of identification of the given data. Think of this as a spectrum: on one end is completely anonymous data, i.e. it is impossible to identify an individual from it, and on the other end is data that specifically identifies an individual. 

Along this spectrum are labels that describe the degree of identification that a given data might provide, such as:

- `identified`
- `anonymized`
- `aggregated`

Learn more about [Data Identification Qualifiers in the taxonomy reference now](data_identification_qualifiers.md).

### Extensibility & Interopability
The taxonomy is designed to support common privacy compliance regulations and standards out of the box, these include GDPR, CCPA, LGPD and ISO 19944. 

You can extend the taxonomy to support your system needs. If you do this, we recommend extending from the existing class structures to ensure interopability inside and outside your organization.

If you have suggestions for missing classifications or concepts, please submit them for addition.



