# Dataset

A Dataset takes a database schema (tables and columns) and adds Fides privacy categorizations. This is a database-agnostic way to annotate privacy declarations.

  ```
  organization
    |-> system
        |-> ** dataset **
            |-> collections
                |-> fields
  ```

* The schema is represented as a set of "collections" (tables) that contain "fields" (columns). These can also be arbitrarily nested to handle document-type databases (e.g., NoSQL or S3).

* At each level -- Dataset, collection, and field, you can assign one or more Data Categories. The Categories declared at each child level are additive.

You use your Datasets by adding them to Systems. A System can contain any number of Datasets, and a Dataset can be added to any number of Systems.
When a dataset is referenced by a system, all applicable data categories set on the dataset are treated as part of the system.
If a Dataset is not referenced by a System, a warning is surfaced denoting an orphan dataset exists.

Datasets cannot contain other Datasets.

## Object Structure

**fides_key**<span class="required"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_constrained string_

A string token of your own invention that uniquely identifies this Dataset. It's your responsibility to ensure that the value is unique across all of your Dataset objects. The value may only contain alphanumeric characters, underscores, and hyphens. (`[A-Za-z0-9_.-]`).

**name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_string_

A UI-friendly label for the Dataset.

**description**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_string_

A human-readable description of the Dataset.

**organization_fides_key**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_string_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default: `default_organization`

The fides key of the [Organization](../../resources/organization/) to which this Dataset belongs.

**meta**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_object_

An optional object that provides additional information about the Dataset. You can structure the object however you like. It can be a simple set of `key: value` properties or a deeply nested hierarchy of objects. How you use the object is up to you: Fides ignores it.

**data_categories**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[_string_]<br/>

Arrays of Data Category resources, identified by `fides_key`, that apply to all collections in the Dataset.

**collections**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[_object_]<br/>

An array of objects that describe the Dataset's collections.

**collections.name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string<br/>

A UI-friendly label for the collection.

**collections.description**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_string_

A human-readable description of the collection.

**collections.data_categories**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[_string_]<br/>

Arrays of Data Category resources, identified by `fides_key`, that apply to all fields in the collection.

**collections.fields**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[_object_]<br/>

An array of objects that describe the collection's fields.

**collections.fields.name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string<br/>

A UI-friendly label for the field.

**collections.fields.description**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_string_

A human-readable description of the field.

**collections.fields.data_categories**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[_string_]<br/>

Arrays of Data Categories, identified by `fides_key`, that applies to this field.

**collections.fields.fields**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[_object_]<br/>

An optional array of objects that describe hierarchical/nested fields (typically found in NoSQL databases)

## Examples

### **Manifest File**

```yaml
dataset:
  - fides_key: demo_users_dataset
    name: Demo Users Dataset
    description: Data collected about users for our analytics system.
    collections:
      - name: users
        description: User information
        data_categories:
          - user
        fields:
          - name: first_name
            description: User's first name
            data_categories:
              - user.name
          - name: email
            description: User's Email
            data_categories:
              - user.contact.email
          - name: phone
            description: User's phone numbers
            data_categories:
              - user.contact.phone_number
            fields:
              - name: mobile
                description: User's mobile phone number
                data_categories:
                  - user.contact.phone_number
              - name: home
                description: User's home phone number
                data_categories:
                  - user.contact.phone_number
```

### **API Payload**

```json
  {
    "fides_key": "demo_users_dataset",
    "name": "Demo Users Dataset",
    "description": "Data collected about users for our analytics system.",
    "collections": [
      {
        "name": "users",
        "description": "User information",
        "fields": [
          {
            "name": "first_name",
            "description": "User's first name",
            "data_categories": [
              "user.name"
            ]
          },
          {
            "name": "email",
            "description": "User's Email",
            "data_categories": [
              "user.contact.email"
            ]
          },
          {
            "name": "phone",
            "description": "User's phone numbers",
            "data_categories": [
              "user.contact.phone_number"
            ],
            "fields": [
              {
                "name": "mobile",
                "description": "User's mobile phone number",
                "data_categories": [
                  "user.contact.phone_number"
                ],
              },
              {
                "name": "home",
                "description": "User's home phone number",
                "data_categories": [
                  "user.contact.phone_number"
                ]
              }
            ]
          }
        ]
      }
    ]
  }
```
