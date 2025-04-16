# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.entity_document_type import EntityDocumentType




class EntityDocument(BaseModel):
    """An official document, usually issued by a governing body or institution, with an associated identifier."""


    type: EntityDocumentType = Field()
    number: str = Field( description="The numeric or alphanumeric identifier associated with this document.")

    @field_validator("number")
    @classmethod
    def number_min_length(cls, value):
        assert len(value) >= 4
        return value

EntityDocument.update_forward_refs()
