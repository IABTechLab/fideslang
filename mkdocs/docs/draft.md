# Draft IAB Fides Taxonomy
Draft for comment of the IAB PIAT/Fides data governance taxonomy.


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
          <img src="../img/Tree@1x.svg" alt="tree" />
        </button>
        <button class="btn btn--icon" data-chart-type="radialTree">
          <img src="../img/Radial%20Tree@1x.svg" alt="radial tree" />
        </button>
        <button class="btn btn--icon" data-chart-type="sunburst" >
          <img src="../img/Sunburst@1x.svg" alt="sunburst" />
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
<script src="../js/visdraft.js"></script>

### 1. Data Categories
Data Categories are labels to describe the type of data processed by your software. These are most heavily used by the System and Dataset resources, where you can assign one or more data categories to each field.

Data Categories are hierarchical with natural inheritance, meaning you can classify data coarsely with a high-level category (e.g. `user.contact` data), or you can classify it with greater precision using subcategories (e.g. `user.contact.email` data).


### 2. Data Uses
Data Uses are labels that describe how, or for what purpose(s) a component of your system is using data.

Data Uses are also hierarchical with natural inheritance, meaning you can easily describe what you're using data for either coarsely (e.g. `provide.service.operations`) or with more precision using subcategories (e.g. `provide.service.operations.support.optimization`).

Learn more about [Data Uses in the taxonomy reference now](taxonomy/data_uses.md).

### 3. Data Subjects

Data Subjects is a label commonly used in the regulatory world to describe the users of a system who's data is being processed. In many systems a generic user label may be sufficient, however the taxonomy is intended to provide greater control through specificity where needed.

Examples of this are:

- `anonymous_user`
- `employee`
- `customer`
- `patient`
- `next_of_kin`

Learn more about [Data Subjects in the taxonomy reference now](taxonomy/data_subjects.md).

### Extensibility and Interoperability

The taxonomy is designed to support common privacy compliance regulations `and standards out of the box, these include GDPR, CCPA, LGPD and ISO 19944. 

You can extend the taxonomy to support your system needs. If you do this, we recommend extending from the existing class structures to ensure interoperability inside and outside your organization.

If you have suggestions for missing classifications or concepts, please submit them for addition.
