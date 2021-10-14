# Privacy Taxonomy Syntax

Other pages in this taxonomy documentation describe various concepts and resources that appear in the taxonomy. This page describes the syntax of the language in more detail to help better interpret the taxonomy whether you're authoring or reading.

The taxonomy is an intentionally simple heirarchy designed to be relatively easy for anyone to read and write. The primary objective is to translate complex data and compliance concepts into a simple syntax, it's for this reason we envisage the taxonomy is written in yaml files.

## YAML - Building Block of the Taxonomy


### Taxonomy

The taxonomy is intentionally simple. To assure this, value declarations from the taxonomy use predefined primitives to describe the data types or data processing you're doing.

### Dot Notation and Snake_Case

To make writing and reading the taxonomy as easy for humans as possible, declarations from the privacy taxonomy use `dot notation` for the keys and use `snake_case` compound labels.

For example, to describe a field in a database as information provided by a user that is personally identifiable, you can write:

``` yaml
# This declares that the data is provided by the user and identifies them directly
user.provided.identifiable
```

If we require greater specificity we could declare the contact type as email (assuming it's a phone number);

``` yaml
# This declares that the is data provided by the user,
# identifies them directly and is from the contact category and of type phone number.
user.provided.identifiable.contact.phone_number
```

The diagram below shows you the structure of the statement:

![alt text](../img/notation-conventions.svg "Privacy Taxonomy Declaration")



### Key-Value 

The key-value is YAML, and as such the basic building block of declaration from the taxonomy. Every item in a declarative document is a member of at least one dictionary. The key is always a `string`. The value is a scalar so that it can be any datatype. So the value can be a `string`, a `number`, or another `dictionary` - most commonly, this will be a `string` that may provide a description or a pointer to a reference object in the taxonomy.

If we use the example of a user's contact email, to correctly declare this in valid YAML, it would be:

``` yaml
  fields:                           # Group of fields in the dataset.
    - name: email
      description: User's Email
      path: users_dataset.email
      data_categories:              # Data category label(s) to assign field.
        - user.provided.identifiable.contact.email
        - account.contact.email
```
The key for each key-value pair determines what value types are valid (for example, a resource type such as `data_categories` must use values from the data_categories taxonomy), but many keys accept arbitrary strings as descriptive labels.

Finally, as you see in the example above, keys such as data_categories accept a list of values for multi-labeling. In this case, the field email has been assigned the value **user provided, identifiable contact email** as well as **account related contact email**.