# pylint: disable=too-many-lines

"""
Contains all of the Fides resources modeled as Pydantic models.
"""
from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Dict, List, Optional, Union

from packaging.version import InvalidVersion, Version
from pydantic import (
    AfterValidator,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    PositiveInt,
    SerializeAsAny,
    ValidationInfo,
    field_validator,
    model_validator,
)

from fideslang.validation import (
    AnyUrlString,
    FidesKey,
    FidesValidationError,
    deprecated_version_later_than_added,
    has_versioning_if_default,
    is_deprecated_if_replaced,
    matching_parent_key,
    no_self_reference,
    parse_data_type_string,
    sort_list_objects_by_name,
    unique_items_in_list,
    valid_data_type,
    validate_fides_key,
)

matching_parent_key_validator = field_validator("parent_key")(matching_parent_key)
no_self_reference_validator = field_validator("parent_key")(no_self_reference)
has_versioning_if_default_validator = field_validator("is_default")(
    has_versioning_if_default
)
deprecated_version_later_than_added_validator = field_validator(
    "version_deprecated",
)(deprecated_version_later_than_added)
is_deprecated_if_replaced_validator = field_validator("replaced_by")(
    is_deprecated_if_replaced
)

# Reusable Fields
name_field = Field(description="Human-Readable name for this resource.")
description_field = Field(
    default=None, description="A detailed description of what this resource is."
)
meta_field = Field(
    default=None,
    description="An optional property to store any extra information for a resource. Data can be structured in any way: simple set of `key: value` pairs or deeply nested objects.",
)


class FidesModel(BaseModel):
    """The base model for most top-level Fides objects."""

    fides_key: FidesKey = Field(
        description="A unique key used to identify this resource."
    )
    organization_fides_key: FidesKey = Field(
        default="default_organization",
        description="Defines the Organization that this resource belongs to.",
    )
    tags: Optional[List[str]] = None
    name: Optional[str] = Field(
        default=None, description="Human-Readable name for this resource."
    )
    description: Optional[str] = description_field
    model_config = ConfigDict(
        extra="ignore", from_attributes=True, coerce_numbers_to_str=True
    )


class DefaultModel(BaseModel):
    """
    A model meant to be inherited by versioned parts of the Default Taxonomy.
    """

    version_added: Optional[str] = Field(
        default=None,
        description="The version of Fideslang in which this label was added.",
    )
    version_deprecated: Optional[str] = Field(
        default=None,
        description="The version of Fideslang in which this label was deprecated.",
    )
    replaced_by: Optional[FidesKey] = Field(
        default=None,
        description="The new name, if applicable, for this label after deprecation.",
    )
    is_default: bool = Field(
        default=False,
        validate_default=True,
        description="Denotes whether the resource is part of the default taxonomy or not.",
    )

    _has_versioning_if_default: classmethod = has_versioning_if_default_validator
    _deprecated_version_later_than_added: classmethod = (
        deprecated_version_later_than_added_validator
    )
    _is_deprecated_if_replaced: classmethod = is_deprecated_if_replaced_validator

    @field_validator("version_added")
    @classmethod
    def validate_version_added(cls, version_added: Optional[str]) -> Optional[str]:
        """
        Validate that the `version_added` field is a proper Version
        """
        if not version_added:
            return None

        try:
            Version(version_added)
        except InvalidVersion:
            raise FidesValidationError(
                f"Field 'version_added' does not have a valid version: {version_added}"
            )

        return version_added

    @field_validator("version_deprecated")
    @classmethod
    def validate_version_deprecated(
        cls, version_deprecated: Optional[str]
    ) -> Optional[str]:
        """
        Validate that the `version_deprecated` is a proper Version
        """
        if not version_deprecated:
            return None

        try:
            Version(version_deprecated)
        except InvalidVersion:
            raise FidesValidationError(
                f"Field 'version_deprecated' does not have a valid version: {version_deprecated}"
            )

        return version_deprecated


class DataResponsibilityTitle(str, Enum):
    """
    The model defining the responsibility or role over
    the system that processes personal data.

    Used to identify whether the organization is a
    Controller, Processor, or Sub-Processor of the data
    """

    CONTROLLER = "Controller"
    PROCESSOR = "Processor"
    SUB_PROCESSOR = "Sub-Processor"


class IncludeExcludeEnum(str, Enum):
    """
    Determine whether or not defined rights are
    being included or excluded.
    """

    ALL = "ALL"
    EXCLUDE = "EXCLUDE"
    INCLUDE = "INCLUDE"
    NONE = "NONE"


class DataSubjectRightsEnum(str, Enum):
    """
    The model for data subject rights over
    personal data.

    Based upon chapter 3 of the GDPR
    """

    INFORMED = "Informed"
    ACCESS = "Access"
    RECTIFICATION = "Rectification"
    ERASURE = "Erasure"
    PORTABILITY = "Portability"
    RESTRICT_PROCESSING = "Restrict Processing"
    WITHDRAW_CONSENT = "Withdraw Consent"
    OBJECT = "Object"
    OBJECT_TO_AUTOMATED_PROCESSING = "Object to Automated Processing"


class LegalBasisForProcessingEnum(str, Enum):
    """
    The model for allowable legal basis categories on privacy declarations.

    Based upon article 6 of the GDPR
    """

    CONSENT = "Consent"
    CONTRACT = "Contract"
    LEGAL_OBLIGATION = "Legal obligations"
    VITAL_INTEREST = "Vital interests"
    PUBLIC_INTEREST = "Public interest"
    LEGITIMATE_INTEREST = "Legitimate interests"


class LegalBasisForProfilingEnum(str, Enum):
    """The model for describing the legal basis under which profiling is performed"""

    EXPLICIT_CONSENT = "Explicit consent"
    CONTRACT = "Contract"
    AUTHORISED_BY_LAW = "Authorised by law"


class LegalBasisForTransfersEnum(str, Enum):
    """
    The model for describing the legal basis under which data is transferred

    We currently do _not_ enforce this enum on the `legal_basis_for_transfers`
    field, because the set of allowable values seems to be changing frequently
    and without clear notice in upstream, public data sources.
    """

    ADEQUACY_DECISION = "Adequacy Decision"
    SCCS = "SCCs"
    BCRS = "BCRs"
    SUPPLEMENTARY_MEASURES = "Supplementary Measures"
    OTHER = "Other"


class SpecialCategoryLegalBasisEnum(str, Enum):
    """
    The model for the legal basis for processing special categories of personal data
    on privacy declarations

    Based upon article 9 of the GDPR
    """

    CONSENT = "Explicit consent"
    EMPLOYMENT = "Employment, social security and social protection"
    VITAL_INTEREST = "Vital interests"
    NON_PROFIT_BODIES = "Not-for-profit bodies"
    PUBLIC_BY_DATA_SUBJECT = "Made public by the data subject"
    LEGAL_CLAIMS = "Legal claims or judicial acts"
    PUBLIC_INTEREST = "Reasons of substantial public interest (with a basis in law)"
    MEDICAL = "Health or social care (with a basis in law)"
    PUBLIC_HEALTH_INTEREST = "Public health (with a basis in law)"
    RESEARCH = "Archiving, research and statistics (with a basis in law)"


# Privacy Data Types
class DataCategory(FidesModel, DefaultModel):
    """The DataCategory resource model."""

    parent_key: Optional[FidesKey] = Field(default=None, validate_default=True)

    _no_self_reference: classmethod = no_self_reference_validator
    _matching_parent_key: classmethod = matching_parent_key_validator


class Cookies(BaseModel):
    """The Cookies resource model"""

    name: str
    path: Optional[str] = None
    domain: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class DataSubjectRights(BaseModel):
    """
    The DataSubjectRights resource model.

    Includes a strategy and optionally a
    list of data subject rights to apply
    via the set strategy.
    """

    strategy: IncludeExcludeEnum = Field(
        description="Defines the strategy used when mapping data rights to a data subject.",
    )
    values: Optional[List[DataSubjectRightsEnum]] = Field(
        default=None,
        description="A list of valid data subject rights to be used when applying data rights to a data subject via a strategy.",
    )

    @model_validator(mode="after")
    def include_exclude_has_values(self) -> "DataSubjectRights":
        """
        Validate the if include or exclude is chosen, that at least one
        value is present.
        """
        strategy, rights = self.strategy, self.values
        if strategy in ("INCLUDE", "EXCLUDE"):
            assert (
                rights is not None
            ), f"If {strategy} is chosen, rights must also be listed."
        return self


class DataSubject(FidesModel, DefaultModel):
    """The DataSubject resource model."""

    rights: Optional[DataSubjectRights] = Field(
        default=None, description=DataSubjectRights.__doc__
    )
    automated_decisions_or_profiling: Optional[bool] = Field(
        default=None,
        description="A boolean value to annotate whether or not automated decisions/profiling exists for the data subject.",
    )


class DataUse(FidesModel, DefaultModel):
    """The DataUse resource model."""

    parent_key: Optional[FidesKey] = Field(default=None, validate_default=True)

    _no_self_reference: classmethod = no_self_reference_validator
    _matching_parent_key: classmethod = matching_parent_key_validator


# Dataset
class DatasetFieldBase(BaseModel):
    """Base DatasetField Resource model.

    This model is available for cases where the DatasetField information needs to be
    customized. In general this will not be the case and you will instead want to use
    the DatasetField model.

    When this model is used you will need to implement your own recursive field in
    to adding any new needed fields.

    Example:

    ```py
    from typing import List, Optional
    from fideslang import DatasetFieldBase

    class MyDatasetField(DatasetFieldBase):
        custom: str
        fields: Optional[List[MyDatasetField]] = []
    ```
    """

    name: str = name_field
    description: Optional[str] = description_field
    data_categories: Optional[List[FidesKey]] = Field(
        default=None,
        description="Arrays of Data Categories, identified by `fides_key`, that applies to this field.",
    )


class EdgeDirection(str, Enum):
    """Direction of a FidesDataSetReference"""

    FROM = "from"
    TO = "to"


class FidesDatasetReference(BaseModel):
    """Reference to a field from another Collection"""

    dataset: FidesKey
    field: str
    direction: Optional[EdgeDirection] = None


class FidesMeta(BaseModel):
    """Supplementary metadata used by the Fides application for additional features."""

    references: Optional[List[FidesDatasetReference]] = Field(
        description="Fields that current field references or is referenced by. Used for drawing the edges of a DSR graph.",
        default=None,
    )
    identity: Optional[str] = Field(
        default=None,
        description="The type of the identity data that should be used to query this collection for a DSR.",
    )
    primary_key: Optional[bool] = Field(
        default=None,
        description="Whether the current field can be considered a primary key of the current collection",
    )
    data_type: Optional[str] = Field(
        default=None,
        description="Optionally specify the data type. Fides will attempt to cast values to this type when querying.",
    )
    length: Optional[PositiveInt] = Field(
        default=None,
        description="Optionally specify the allowable field length. Fides will not generate values that exceed this size.",
    )
    return_all_elements: Optional[bool] = Field(
        default=None,
        description="Optionally specify to query for the entire array if the array is an entrypoint into the node. Default is False.",
    )
    read_only: Optional[bool] = Field(
        default=None,
        description="Optionally specify if a field is read-only, meaning it can't be updated or deleted.",
    )
    custom_request_field: Optional[str] = Field(
        default=None,
        description="Optionally specify that a field may be used as a custom request field in DSRs. The value is the name of the field in the DSR.",
    )

    @field_validator("data_type")
    @classmethod
    def valid_data_type(cls, value: Optional[str]) -> Optional[str]:
        """Validate that all annotated data types exist in the taxonomy"""
        return valid_data_type(value)


class FidesopsMetaBackwardsCompat(BaseModel):
    """Mixin to convert fidesops_meta to fides_meta for backwards compatibility
    as we add DSR concepts to fideslang"""

    def __init__(self, **data: Union[Dataset, DatasetCollection, DatasetField]) -> None:
        """For Datasets, DatasetCollections, and DatasetFields, if old fidesops_meta field is specified,
        convert this to a fides_meta field instead."""
        fidesops_meta = data.pop("fidesops_meta", None)
        fides_meta = data.pop("fides_meta", None)
        super().__init__(
            fides_meta=fides_meta or fidesops_meta,
            **data,
        )


class DatasetField(DatasetFieldBase, FidesopsMetaBackwardsCompat):
    """
    The DatasetField resource model.

    This resource is nested within a DatasetCollection.
    """

    fides_meta: Optional[FidesMeta] = None

    fields: Optional[List[DatasetField]] = Field(
        default=None,
        description="An optional array of objects that describe hierarchical/nested fields (typically found in NoSQL databases).",
    )

    @field_validator("fides_meta")
    @classmethod
    def valid_meta(cls, meta_values: Optional[FidesMeta]) -> Optional[FidesMeta]:
        """Validate upfront that the return_all_elements flag can only be specified on array fields"""
        if not meta_values:
            return meta_values

        is_array: bool = bool(
            meta_values.data_type and meta_values.data_type.endswith("[]")
        )
        if not is_array and meta_values.return_all_elements is not None:
            raise ValueError(
                "The 'return_all_elements' attribute can only be specified on array fields."
            )
        return meta_values

    @model_validator(mode="after")
    def validate_object_fields(
        self,
        _: ValidationInfo,
    ) -> DatasetField:
        """Two validation checks for object fields:
        - If there are sub-fields specified, type should be either empty or 'object'
        - Additionally object fields cannot have data_categories.
        """
        fields = self.fields
        declared_data_type = None
        field_name: str = self.name

        if self.fides_meta:
            declared_data_type = self.fides_meta.data_type

        if fields and declared_data_type:
            data_type, _ = parse_data_type_string(declared_data_type)
            if data_type != "object":
                raise ValueError(
                    f"The data type '{data_type}' on field '{field_name}' is not compatible with specified sub-fields. Convert to an 'object' field."
                )

        if (fields or declared_data_type == "object") and self.data_categories:
            raise ValueError(
                f"Object field '{field_name}' cannot have specified data_categories. Specify category on sub-field instead"
            )
        return self


# this is required for the recursive reference in the pydantic model:
DatasetField.model_rebuild()


def validate_fides_collection_key(value: str) -> str:
    """
    Overrides validation to check FidesCollectionKey format, and that both the dataset
    and collection names have the FidesKey format.
    """
    values = value.split(".")
    if len(values) == 2:
        validate_fides_key(values[0])
        validate_fides_key(values[1])
        return value
    raise ValueError(
        "FidesCollection must be specified in the form 'FidesKey.FidesKey'"
    )


FidesCollectionKey = Annotated[str, AfterValidator(validate_fides_collection_key)]


class CollectionMeta(BaseModel):
    """Collection-level specific annotations used for query traversal"""

    after: Optional[List[FidesCollectionKey]] = None
    skip_processing: Optional[bool] = False


class DatasetCollection(FidesopsMetaBackwardsCompat):
    """
    The DatasetCollection resource model.

    This resource is nested within a Dataset.
    """

    name: str = name_field
    description: Optional[str] = description_field
    data_categories: Optional[List[FidesKey]] = Field(
        default=None,
        description="Array of Data Category resources identified by `fides_key`, that apply to all fields in the collection.",
    )
    fields: List[DatasetField] = Field(
        description="An array of objects that describe the collection's fields.",
    )

    fides_meta: Optional[CollectionMeta] = None

    _sort_fields: classmethod = field_validator("fields")(sort_list_objects_by_name)  # type: ignore[assignment]
    _unique_items_in_list: classmethod = field_validator("fields")(unique_items_in_list)  # type: ignore[assignment]


class ContactDetails(BaseModel):
    """
    The contact details information model.

    Used to capture contact information for controllers, used
    as part of exporting a data map / ROPA.

    This model is nested under an Organization and
    potentially under a system/dataset.
    """

    name: str = Field(
        default="",
        description="An individual name used as part of publishing contact information. Encrypted at rest on the server.",
    )
    address: str = Field(
        default="",
        description="An individual address used as part of publishing contact information. Encrypted at rest on the server.",
    )
    email: str = Field(
        default="",
        description="An individual email used as part of publishing contact information. Encrypted at rest on the server.",
    )
    phone: str = Field(
        default="",
        description="An individual phone number used as part of publishing contact information. Encrypted at rest on the server.",
    )


class DatasetMetadata(BaseModel):
    """
    The DatasetMetadata resource model.

    Object used to hold application specific metadata for a dataset
    """

    resource_id: Optional[str] = None
    after: Optional[List[FidesKey]] = None


class Dataset(FidesModel, FidesopsMetaBackwardsCompat):
    """The Dataset resource model."""

    meta: Optional[Dict] = meta_field
    data_categories: Optional[List[FidesKey]] = Field(
        default=None,
        description="Array of Data Category resources identified by `fides_key`, that apply to all collections in the Dataset.",
    )
    fides_meta: Optional[DatasetMetadata] = Field(
        description=DatasetMetadata.__doc__, default=None
    )
    collections: List[DatasetCollection] = Field(
        description="An array of objects that describe the Dataset's collections.",
    )

    _sort_collections: classmethod = field_validator("collections")(  # type: ignore[assignment]
        sort_list_objects_by_name
    )
    _unique_items_in_list: classmethod = field_validator("collections")(  # type: ignore[assignment]
        unique_items_in_list
    )


# Evaluation
class ViolationAttributes(BaseModel):
    "The model for attributes which led to an evaluation violation"

    data_categories: List[str] = Field(
        description="A list of data categories which led to an evaluation violation.",
    )
    data_subjects: List[str] = Field(
        description="A list of data subjects which led to an evaluation violation.",
    )
    data_uses: List[str] = Field(
        description="A list of data uses which led to an evaluation violation.",
    )


class Violation(BaseModel):
    "The model for violations within an evaluation."

    violating_attributes: ViolationAttributes = Field(
        description=ViolationAttributes.__doc__
    )
    detail: str = Field(
        description="A human-readable string detailing the evaluation violation.",
    )


class StatusEnum(str, Enum):
    "The model for possible evaluation results."

    FAIL = "FAIL"
    PASS = "PASS"


class Evaluation(BaseModel):
    """
    The Evaluation resource model.

    This resource is created after an evaluation is executed.
    """

    fides_key: FidesKey = Field(
        description="A uuid generated for each unique evaluation.",
    )
    status: StatusEnum = Field(description=StatusEnum.__doc__)
    violations: List[Violation] = Field(
        default=[],
        description=Violation.__doc__,
    )
    message: str = Field(
        default="",
        description="A human-readable string response for the evaluation.",
    )
    model_config = ConfigDict(extra="ignore", from_attributes=True)


# Organization
class ResourceFilter(BaseModel):
    """
    The ResourceFilter resource model.
    """

    type: str = Field(
        description="The type of filter to be used (i.e. ignore_resource_arn)",
    )
    value: str = Field(
        description="A string representation of resources to be filtered. Can include wildcards.",
    )


class OrganizationMetadata(BaseModel):
    """
    The OrganizationMetadata resource model.

    Object used to hold application specific metadata for an organization
    """

    resource_filters: Optional[List[ResourceFilter]] = Field(
        default=None,
        description="A list of filters that can be used when generating or scanning systems.",
    )


class Organization(FidesModel):
    """
    The Organization resource model.

    This resource is used as a way to organize all other resources.
    """

    # It inherits this from FidesModel but Organizations don't have this field
    organization_parent_key: None = Field(
        default=None,
        description="An inherited field from the FidesModel that is unused with an Organization.",
    )
    controller: Optional[ContactDetails] = Field(
        default=None,
        description=ContactDetails.__doc__,
    )
    data_protection_officer: Optional[ContactDetails] = Field(
        default=None,
        description=ContactDetails.__doc__,
    )
    fidesctl_meta: Optional[OrganizationMetadata] = Field(
        default=None,
        description=OrganizationMetadata.__doc__,
    )
    representative: Optional[ContactDetails] = Field(
        default=None,
        description=ContactDetails.__doc__,
    )
    security_policy: Optional[HttpUrl] = Field(
        default=None, description="Am optional URL to the organization security policy."
    )


# Policy
class MatchesEnum(str, Enum):
    """
    The MatchesEnum resource model.

    Determines how the listed resources are matched in the evaluation logic.
    """

    ANY = "ANY"
    ALL = "ALL"
    NONE = "NONE"
    OTHER = "OTHER"


class PrivacyRule(BaseModel):
    """
    The PrivacyRule resource model.

    A list of privacy data types and what match method to use.
    """

    matches: MatchesEnum = Field(
        description=MatchesEnum.__doc__,
    )
    values: List[FidesKey] = Field(
        description="A list of fides keys to be used with the matching type in a privacy rule.",
    )


class PolicyRule(BaseModel):
    """
    The PolicyRule resource model.

    Describes the allowed combination of the various privacy data types.
    """

    name: str
    data_categories: PrivacyRule = Field(
        description=PrivacyRule.__doc__,
    )
    data_uses: PrivacyRule = Field(
        description=PrivacyRule.__doc__,
    )
    data_subjects: PrivacyRule = Field(
        description=PrivacyRule.__doc__,
    )


class Policy(FidesModel):
    """
    The Policy resource model.

    An object used to organize a list of PolicyRules.
    """

    rules: List[PolicyRule] = Field(
        description=PolicyRule.__doc__,
    )

    _sort_rules: classmethod = field_validator("rules")(sort_list_objects_by_name)  # type: ignore[assignment]


class PrivacyDeclaration(BaseModel):
    """
    The PrivacyDeclaration resource model.

    States a function of a system, and describes how it relates
    to the privacy data types.
    """

    name: Optional[str] = Field(
        default=None,
        description="The name of the privacy declaration on the system.",
    )
    data_categories: List[FidesKey] = Field(
        description="An array of data categories describing a system in a privacy declaration.",
    )
    data_use: FidesKey = Field(
        description="The Data Use describing a system in a privacy declaration.",
    )
    data_subjects: List[FidesKey] = Field(
        default_factory=list,
        description="An array of data subjects describing a system in a privacy declaration.",
    )
    dataset_references: Optional[List[FidesKey]] = Field(
        default=None,
        description="Referenced Dataset fides keys used by the system.",
    )
    egress: Optional[List[FidesKey]] = Field(
        default=None,
        description="The resources to which data is sent. Any `fides_key`s included in this list reference `DataFlow` entries in the `egress` array of any `System` resources to which this `PrivacyDeclaration` is applied.",
    )
    ingress: Optional[List[FidesKey]] = Field(
        default=None,
        description="The resources from which data is received. Any `fides_key`s included in this list reference `DataFlow` entries in the `ingress` array of any `System` resources to which this `PrivacyDeclaration` is applied.",
    )
    features: List[str] = Field(
        default_factory=list, description="The features of processing personal data."
    )
    flexible_legal_basis_for_processing: bool = Field(
        description="Whether the legal basis for processing is 'flexible' (i.e. can be overridden in a privacy notice) for this declaration.",
        default=True,
    )
    legal_basis_for_processing: Optional[LegalBasisForProcessingEnum] = Field(
        default=None,
        description="The legal basis under which personal data is processed for this purpose.",
    )
    impact_assessment_location: Optional[str] = Field(
        default=None,
        description="Where the legitimate interest impact assessment is stored",
    )
    retention_period: Optional[str] = Field(
        default=None,
        description="An optional string to describe the time period for which data is retained for this purpose.",
    )
    processes_special_category_data: bool = Field(
        default=False,
        description="This system processes special category data",
    )
    special_category_legal_basis: Optional[SpecialCategoryLegalBasisEnum] = Field(
        default=None,
        description="The legal basis under which the special category data is processed.",
    )
    data_shared_with_third_parties: bool = Field(
        default=False,
        description="This system shares data with third parties for this purpose.",
    )
    third_parties: Optional[str] = Field(
        default=None,
        description="The types of third parties the data is shared with.",
    )
    shared_categories: List[str] = Field(
        default_factory=list,
        description="The categories of personal data that this system shares with third parties.",
    )
    cookies: Optional[List[Cookies]] = Field(
        default=None,
        description="Cookies associated with this data use to deliver services and functionality",
    )
    model_config = ConfigDict(from_attributes=True)


class SystemMetadata(BaseModel):
    """
    The SystemMetadata resource model.

    Object used to hold application specific metadata for a system
    """

    resource_id: Optional[str] = Field(
        default=None,
        description="The external resource id for the system being modeled.",
    )
    endpoint_address: Optional[str] = Field(
        default=None,
        description="The host of the external resource for the system being modeled.",
    )
    endpoint_port: Optional[str] = Field(
        default=None,
        description="The port of the external resource for the system being modeled.",
    )

    model_config = ConfigDict(
        coerce_numbers_to_str=True
    )  # For backwards compat of endpoint_port


class FlowableResources(str, Enum):
    """
    The resource types with which DataFlows can be created.
    """

    DATASET = "dataset"
    SYSTEM = "system"
    USER = "user"


class DataFlow(BaseModel):
    """
    The DataFlow resource model.

    Describes a resource model with which a given System resource communicates.
    """

    fides_key: FidesKey = Field(
        ...,
        description="Identifies the System or Dataset resource with which the communication occurs. May also be 'user', to represent communication with the user(s) of a System.",
    )
    type: str = Field(
        ...,
        description=f"Specifies the resource model class for which the `fides_key` applies. May be any of {', '.join([member.value for member in FlowableResources])}.",
    )
    data_categories: Optional[List[FidesKey]] = Field(
        default=None,
        description="An array of data categories describing the data in transit.",
    )

    @model_validator(mode="after")
    def user_special_case(self) -> "DataFlow":
        """
        If either the `fides_key` or the `type` are set to "user",
        then the other must also be set to "user".
        """

        if self.fides_key == "user" or self.type == "user":
            assert (
                self.fides_key == "user" and self.type == "user"
            ), "The 'user' fides_key is required for, and requires, the type 'user'"

        return self

    @field_validator("type")
    @classmethod
    def verify_type_is_flowable(cls, value: str) -> str:
        """
        Assert that the value of the `type` field is a member
        of the `FlowableResources` Enum.
        """

        flowables = [member.value for member in FlowableResources]
        assert value in flowables, f"'type' must be one of {', '.join(flowables)}"
        return value


class System(FidesModel):
    """
    The System resource model.

    Describes an application and includes a list of PrivacyDeclaration resources.
    """

    meta: Optional[Dict] = meta_field
    fidesctl_meta: Optional[SystemMetadata] = Field(
        default=None,
        description=SystemMetadata.__doc__,
    )
    system_type: str = Field(
        description="A required value to describe the type of system being modeled, examples include: Service, Application, Third Party, etc.",
    )
    egress: Optional[List[DataFlow]] = Field(
        default=None, description="The resources to which the system sends data."
    )
    ingress: Optional[List[DataFlow]] = Field(
        default=None, description="The resources from which the system receives data."
    )
    privacy_declarations: List[PrivacyDeclaration] = Field(
        description=PrivacyDeclaration.__doc__,
    )
    administrating_department: Optional[str] = Field(
        default="Not defined",
        description="An optional value to identify the owning department or group of the system within your organization",
    )
    vendor_id: Optional[str] = Field(
        default=None,
        description="The unique identifier for the vendor that's associated with this system.",
    )
    previous_vendor_id: Optional[str] = Field(
        default=None,
        description="If specified, the unique identifier for the vendor that was previously associated with this system.",
    )
    vendor_deleted_date: Optional[datetime] = Field(
        default=None,
        description="The deleted date of the vendor that's associated with this system.",
    )
    dataset_references: List[FidesKey] = Field(
        default_factory=list,
        description="Referenced Dataset fides keys used by the system.",
    )
    processes_personal_data: bool = Field(
        default=True,
        description="This toggle indicates whether the system stores or processes personal data.",
    )
    exempt_from_privacy_regulations: bool = Field(
        default=False,
        description="This toggle indicates whether the system is exempt from privacy regulation if they do process personal data.",
    )
    reason_for_exemption: Optional[str] = Field(
        default=None,
        description="The reason that the system is exempt from privacy regulation.",
    )
    uses_profiling: bool = Field(
        default=False,
        description="Whether the vendor uses data to profile a consumer in a way that has a legal effect.",
    )
    legal_basis_for_profiling: List[LegalBasisForProfilingEnum] = Field(
        default_factory=list,
        description="The legal basis (or bases) for performing profiling that has a legal effect.",
    )
    does_international_transfers: bool = Field(
        default=False,
        description="Whether this system transfers data to other countries or international organizations.",
    )
    legal_basis_for_transfers: List[str] = Field(
        default_factory=list,
        description="The legal basis (or bases) under which the data is transferred.",
    )
    requires_data_protection_assessments: bool = Field(
        default=False,
        description="Whether this system requires data protection impact assessments.",
    )
    dpa_location: Optional[str] = Field(
        default=None, description="Location where the DPAs or DIPAs can be found."
    )
    dpa_progress: Optional[str] = Field(
        default=None,
        description="The optional status of a Data Protection Impact Assessment",
    )
    privacy_policy: SerializeAsAny[Optional[AnyUrlString]] = Field(
        default=None,
        description="A URL that points to the system's publicly accessible privacy policy.",
    )
    legal_name: Optional[str] = Field(
        default=None,
        description="The legal name for the business represented by the system.",
    )
    legal_address: Optional[str] = Field(
        default=None,
        description="The legal address for the business represented by the system.",
    )
    responsibility: List[DataResponsibilityTitle] = Field(
        default_factory=list,
        description=DataResponsibilityTitle.__doc__,
    )
    dpo: Optional[str] = Field(
        default=None, description="The official privacy contact address or DPO."
    )
    joint_controller_info: Optional[str] = Field(
        default=None,
        description="The party or parties that share the responsibility for processing personal data.",
    )
    data_security_practices: Optional[str] = Field(
        default=None, description="The data security practices employed by this system."
    )
    cookie_max_age_seconds: Optional[int] = Field(
        default=None,
        description="The maximum storage duration, in seconds, for cookies used by this system.",
    )
    uses_cookies: bool = Field(
        default=False, description="Whether this system uses cookie storage."
    )
    cookie_refresh: bool = Field(
        default=False,
        description="Whether the system's cookies are refreshed after being initially set.",
    )
    uses_non_cookie_access: bool = Field(
        default=False,
        description="Whether the system uses non-cookie methods of storage or accessing information stored on a user's device.",
    )
    legitimate_interest_disclosure_url: SerializeAsAny[Optional[AnyUrlString]] = Field(
        default=None,
        description="A URL that points to the system's publicly accessible legitimate interest disclosure.",
    )
    cookies: Optional[List[Cookies]] = Field(
        default=None,
        description="System-level cookies unassociated with a data use to deliver services and functionality",
    )

    _sort_privacy_declarations: classmethod = field_validator("privacy_declarations")(  # type: ignore[assignment]
        sort_list_objects_by_name
    )

    @model_validator(mode="after")
    def privacy_declarations_reference_data_flows(
        self,
    ) -> "System":
        """
        Any `PrivacyDeclaration`s which include `egress` and/or `ingress` fields must
        only reference the `fides_key`s of defined `DataFlow`s in said field(s).
        """
        privacy_declarations: List[PrivacyDeclaration] = self.privacy_declarations or []
        for (
            privacy_declaration
        ) in privacy_declarations:  # pylint:disable=not-an-iterable
            for direction in ["egress", "ingress"]:
                fides_keys = getattr(privacy_declaration, direction, None)
                if fides_keys is not None:
                    data_flows = getattr(self, direction)
                    system = self.fides_key
                    assert (
                        data_flows is not None and len(data_flows) > 0
                    ), f"PrivacyDeclaration '{privacy_declaration.name}' defines {direction} with one or more resources and is applied to the System '{system}', which does not itself define any {direction}."

                    for fides_key in fides_keys:
                        assert fides_key in [
                            data_flow.fides_key
                            for data_flow in data_flows  # pylint:disable=not-an-iterable
                        ], f"PrivacyDeclaration '{privacy_declaration.name}' defines {direction} with '{fides_key}' and is applied to the System '{system}', which does not itself define {direction} with that resource."

        return self

    model_config = ConfigDict(use_enum_values=True)


# Taxonomy
class Taxonomy(BaseModel):
    """
    Represents an entire taxonomy of Fides Resources.

    The choice to not use pluralized forms of each resource name
    was deliberate, as this would have caused huge amounts of complexity
    elsewhere across the codebase.
    """

    data_category: List[DataCategory] = Field(default_factory=list)
    data_subject: Optional[List[DataSubject]] = Field(default_factory=list)
    data_use: Optional[List[DataUse]] = Field(default_factory=list)

    dataset: Optional[List[Dataset]] = Field(default_factory=list)
    system: Optional[List[System]] = Field(default_factory=list)
    policy: Optional[List[Policy]] = Field(default_factory=list)

    organization: List[Organization] = Field(default_factory=list)
