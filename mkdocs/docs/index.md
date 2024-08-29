# IAB Tech Lab & Fideslang

Fideslang ( fee-dez-læŋg, derived from the Latin term "Fidēs" and "language") is a taxonomy developed to standardize the way privacy and governance-related data elements, purposes of data use, and subjects are labeled and described. This taxonomy provides an interoperable standard designed to assist businesses in navigating the complex landscape of global privacy regulations.

In collaboration with [Ethyca](https://ethyca.com), [IAB Tech Lab](https://iabtechlab.com/) received a donation of Fideslang to accelerate the development of privacy standards within the ad tech industry. Fideslang represents five years of dedicated work aimed at enhancing data privacy practices by creating a universal language that bridges the gap between legal and development teams. This innovation aligns seamlessly with the IAB Tech Lab's Privacy Taxonomy Project, a key initiative of the Privacy Implementation & Accountability Task Force. The project aims to create a standardized privacy taxonomy that enables businesses to effectively manage their data privacy compliance and communicate privacy information more clearly across the industry.

The Privacy Taxonomy is uniquely tailored to the evolving landscape of data protection. Building on the foundation of Fideslang, the taxonomy aims to set a new standard for how privacy information is conveyed across the digital advertising ecosystem.
The Privacy Taxonomy is open for public comment until October 5th, 2024. Industry stakeholders are encouraged to review and provide feedback at [support@iabtechlab.com](support@iabtechlab.com).

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

 
## Taxonomy Explorer

The IAB Tech Lab Privacy Taxonomy is composed of three main classification groups: Data Elements, Data Uses, and Data Subjects. These groups work together to describe the data types, purposes of use, and data owners (subjects) of data being processed for privacy and governance purposes. Below, you can explore the primary components of the taxonomy.

To learn more about the taxonomy's structure read the [explanation below](#fideslang-privacy-taxonomy-explained)

<div id="vis" class="vis vis-container">
  <div class="controls-container">
    <div id="data-control" class="control-group">
      <div class="btn-group">
        <button class="btn is-selected" data-chart-data="categories">Data Elements</button>
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

### 1. Data Elements
Data Elements are labels to describe the type of data processed by your business and technology systems. Data Categories are hierarchical with natural inheritance, meaning you can label data coarsely with a high-level category (e.g. user.contact data), or you can tag it with greater precision using subcategories (e.g. user.contact.email data). This provides a standard way to tag data in databases, which can assist with data privacy operations (e.g. data mapping, DSRs, contracts, disclosures, consent/opt-out, etc.). The data element, when clear under the applicable law, aligns with categories specified in US data privacy laws (e.g., CCPA, CPA). 


### 2. Data Uses
Data Uses are labels that describe how, or for what purpose(s) you are using data. You may think of these as analogous to Purpose of Processing in such documents as a RoPA (Record of Processing Activities).

Data Uses are also hierarchical with natural inheritance, meaning you can easily describe what you're using data for either coarsely (e.g. provide.service.operations) or with more precision using subcategories (e.g. provide.service.operations.support.optimization).

The top-level labels create standard buckets to categorize data uses into: (1) necessary, (2) operational, (3) analytics, (4) advertising and marketing, and (5) disclosure. 

### 3. Data Subjects

Data Subjects describes the owner or individual that the data being processed describes, examples might be a customer, or an employee. In many systems a generic user label may be sufficient, however the taxonomy is intended to provide greater control through specificity where needed for governance.

Examples of this are:

- `consumer`
- `househould`
- `employee`

### Laws Triggered
For data categories and data uses, these are mapped to the major laws they trigger and the sensitivity that a given data category may obtain based on processing under a given framework.

### IAB Frameworks
The Fideslang taxonomy automatically cross-references all data uses to the IAB TCF and IAB MSPA frameworks, meaning that if you tag a data use such as `advertising_marketing.first_party.targeted`, it will automatically inherit the classification of "First Party Advertising" as defined by 1.33ii of the MSPA.

### Sensitivity Matrix
When using the Privacy Taxonomy, you may assign sensitivity on a scale of  1-3 to given data categories. With 1 not being sensitive and 3 being sensitive as determined by applicable law. You should complete this sensitivity matrix based on your businesses internal policies and risk management.

Sensitivity Matrix scoring:

- 1 = no; 
- 2 = no; unless combined with another non-sensitive data point that makes the combined data elements sensitive 
    -e.g, account log-in + password/credentials to access the account 
- 3 = yes, per se sensitive as determined by applicable law
    -e.g. citizenship status, racial or ethnic origin, religious beliefs, data relating to children, etc.


### Extensibility and Interoperability

The Privacy Taxonomy is designed to support common privacy compliance regulations and standards out of the box, these include CCPA, MSPA, etc.

You can extend the taxonomy to support your system needs. If you do this, we recommend extending from the existing class structures to ensure interoperability inside and outside your organization.

If you have suggestions for missing classifications or concepts, please submit them for addition.

Public Comment
Privacy Taxonomy is open for public comment until October 5th, 2024. Industry stakeholders are encouraged to review and provide feedback to [support@iabtechlab.com](mailto:support@iabtechlab.com).  

