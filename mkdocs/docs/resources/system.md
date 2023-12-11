# System

A System is a model for describing anything that processes data for your organization (applications, services, 3rd party APIs, etc.) and describes how these datasets are used for business functions of instances of your data resources. It contains all 3 privacy attributes (`data_category`, `data_use`, and `data_subject`).

  ```
  organization
    |-> ** system **
        |-> privacy declarations
  ```

## Object Structure

**fides_key**<span class="required"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_constrained string_

A string token of your own invention that uniquely identifies this System. It's your responsibility to ensure that the value is unique across all of your System objects. The value may only contain alphanumeric characters, underscores, and hyphens. (`[A-Za-z0-9_.-]`).

**name**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_string_

A UI-friendly label for the System.

**description**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_string_

A human-readable description of the System.

**system_type**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_string_

A required value to describe the type of system being modeled, examples include: Service, Application, Third Party, etc.

**administrating_department**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_string_

An optional value to identify the owning department or group of the system within your organization

**egress**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[array]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

The resources to which the System sends data.

**ingress**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[array]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

The resources from which the System receives data.

**privacy_declarations**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[array]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

The array of declarations describing the types of data in your system. This is a list of the privcy attributes (`data_category`, `data_use`, and `data_subject`) for each of your systems.

If a dataset is referenced as part of the system, all applicable data categories set on the dataset are treated as part of the system.

**organization_fides_key**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_string_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default: `default_organization`

The fides key of the [Organization](../../resources/organization/) to which this System belongs.

## Examples

### **Manifest File**

```yaml
system:
  - fides_key: demo_analytics_system
    name: Demo Analytics System
    description: A system used for analyzing customer behaviour.
    system_type: Service
    administrating_department: Engineering
    egress:
      - fides_key: another_demo_system
        type: system
        data_categories:
          - user.contact
    ingress:
      - fides_key: yet_another_demo_system
        type: system
        data_categories:
          - user.device.cookie_id
    privacy_declarations:
      - name: Analyze customer behaviour for improvements.
        data_categories:
          - user.contact
          - user.device.cookie_id
        data_use: improve.system
        data_subjects:
          - customer
        egress:
          - another_demo_system
        ingress:
          - yet_another_demo_system
```

**Demo manifest file:** `/fides/demo_resources/demo_system.yml`

### **API**

```json title="<code>POST /api/v1/system</code>"

{
  "fides_key": "demo_analytics_system",
  "name": "Demo Analytics System",
  "description": "A system used for analyzing customer behaviour.",
  "system_type": "Service",
  "administrating_department": "Engineering",
  "egress": [
    {
      "fides_key": "another_demo_system",
      "type": "system",
      "data_categories": ["user.contact"]
    }
  ],
  "ingress": [
    {
      "fides_key": "yet_another_demo_system",
      "type": "system",
      "data_categories": ["user.device.cookie_id"]
    }
  ],
  "privacy_declarations": [
    {
      "name": "Analyze customer behaviour for improvements.",
      "data_categories": [
        "user.contact",
        "user.device.cookie_id"
      ],
      "data_use": "improve.system",
      "data_subjects": [
        "customer"
      ],
      "egress": ["another_demo_system"],
      "ingress": ["yet_another_demo_system"]
    }
  ]
}
```
