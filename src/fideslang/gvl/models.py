from typing import List

from pydantic import BaseModel, Field


class Purpose(BaseModel):
    """
    Pydantic model for GVL purpose records
    """

    id: int = Field(
        description="Official GVL purpose ID. Used for linking with other records, e.g. vendors, cookies, etc."
    )
    name: str = Field(description="Name of the GVL purpose.")
    description: str = Field(description="Description of the GVL purpose.")
    illustrations: List[str] = Field(
        description="Illustrative examples of the purpose."
    )


class MappedPurpose(Purpose):
    """
    Extension of the base GVL purpose model to include properties related to fideslang mappings.

    This is separated from the base GVL purpose model to keep that model a "pristine" representation
    of GVL source data.
    """

    data_uses: List[str] = Field(
        description="The fideslang default taxonomy data uses that are associated with the purpose."
    )


class Feature(BaseModel):
    "Pydantic model for GVL feature records"
    id: int = Field(description="Official GVL feature ID or special feature ID")
    name: str = Field(description="Name of the GVL feature or special feature.")
    description: str = Field(
        description="Description of the GVL feature or special feature."
    )


class GVLDataCategory(BaseModel):
    """
    Pydantic model for GVL data category records
    """

    id: int = Field(
        description="Official GVL data category ID. Used for linking with vendor records"
    )
    name: str = Field(description="Name of the GVL data category.")
    description: str = Field(description="Description of the GVL purpose.")


class MappedDataCategory(GVLDataCategory):
    """
    Extension of the base GVL data category model to include properties related to fideslang mappings.

    This is separated from the base GVL data category model to keep that model a "pristine" representation
    of GVL source data.
    """

    fides_data_categories: List[str] = Field(
        description="The fideslang default taxonomy data categories that are associated with the GVL data category."
    )
