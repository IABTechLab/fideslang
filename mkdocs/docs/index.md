# Fides Language

Fideslang (fee-dez-læŋg, from the Latin term "Fidēs" + "language") is a taxomony  of privacy and governance related data elements, purposes of data use, and subjects. Fideslang provides an interoperable standard for labeling data and describing data processing activities for governance across global privacy regulations. 


[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

 
## Taxonomy Explorer

Fideslang privacy taxonomy is made up of three main classification groups. These groups are used together to describe the data types, purpose of use, and data owners (subjects) of data being processed, for data privacy and governance purposes. Below you can explore the primary components of the taxonomy.

To learn more about the taxonomy's structure read the [explanation below](#fideslang-privacy-taxonomy-explained)

<div id="vis" class="vis vis-container">
  <div class="controls-container">
    <div id="data-control" class="control-group">
      <div class="btn-group">
        <button class="btn is-selected" data-chart-data="categories">Data Categories</button>
        <button class="btn" data-chart-data="uses">Data Uses</button>
        <button class="btn" data-chart-data="subjects">Data Subjects</button>
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
<script src="js/visdraft.js"></script>

## Fideslang Privacy Taxonomy Explained

### 1. Data Categories
Data Categories are labels to describe the type of data processed by your busess and technology systems.
Data Categories are hierarchical with natural inheritance, meaning you can label data coarsely with a high-level category (e.g. `user.contact` data), or you can tag it with greater precision using subcategories (e.g. `user.contact.email` data).


### 2. Data Uses
Data Uses are labels that describe how, or for what purpose(s) you are using data. You may think of these as analagous to Purpose of Processing in such documents as a RoPA (Record of Processing Activities).

Data Uses are also hierarchical with natural inheritance, meaning you can easily describe what you're using data for either coarsely (e.g. `provide.service.operations`) or with more precision using subcategories (e.g. `provide.service.operations.support.optimization`).

### 3. Data Subjects

Data Subjects describes the owner or individual that the data being processed describes, examples might be a customer, or an employee. In many systems a generic user label may be sufficient, however the taxonomy is intended to provide greater control through specificity where needed for governnce.

Examples of this are:

- `consumer`
- `househould`
- `employee`

### Laws Triggered
For data categories and data uses, these are mapped to the major laws they trigger and the sensitivity that a given data category may obtain based on processing under a given framework. 

### IAB Frameworks
The Fideslang taxonomy automatically cross-references all data uses to the IAB TCF and IAB MSPA frameworks, meaning that if you tag a data use such as `advertising_marketing.first_party.targeted`, it will automatically inherit the classification of "First Party Advertising" as defined by 1.33ii of the MSPA.

### Sensitivity Matrix
When using the Fideslang taxonomy, you may assign sensitivity on a scale of 1 - 3 to given data categories. With 1 not being sensitive and 3 being sensitive as determined by applicable law. You should complete this sensitivity matrix based on your businesses internal policies and risk management.

- 1 = no; 
- 2 = no; unless combined with another non-sensitive data point that makes the combined data elements sensitive 
    -e.g, account log-in + password/credentials to access the account 
- 3 = yes, per se sensitive as determined by applicable law
    -e.g. citizenship status, racial or ethnic origin, religious beliefs, data relating to children, etc.


### Extensibility and Interoperability

The taxonomy is designed to support common privacy compliance regulations and standards out of the box, these include CCPA, MSPA, etc.

You can extend the taxonomy to support your system needs. If you do this, we recommend extending from the existing class structures to ensure interoperability inside and outside your organization.

If you have suggestions for missing classifications or concepts, please submit them for addition.
