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
