# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class EntityWatchlistSearchTerms(BaseModel):
    """Search inputs for creating an entity watchlist screening"""


    entity_watchlist_program_id: str = Field( description="ID of the associated entity program.")
    legal_name: str = Field( description="The name of the organization being screened.")
    document_number: Optional[str] = Field(default=None, description="The numeric or alphanumeric identifier associated with this document.")
    email_address: Optional[EmailStr] = Field(default=None, description="A valid email address.")
    country: Optional[str] = Field(default=None, description="Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2 form.")
    phone_number: Optional[str] = Field(default=None, description="A phone number in E.164 format.")
    url: Optional[AnyUrl] = Field(default=None, description="An 'http' or 'https' URL (must begin with either of those).")

    @field_validator("legal_name")
    @classmethod
    def legal_name_min_length(cls, value):
        assert len(value) >= 1
        return value

    @field_validator("document_number")
    @classmethod
    def document_number_min_length(cls, value):
        assert len(value) >= 4
        return value

    @field_validator("country")
    @classmethod
    def country_min_length(cls, value):
        assert len(value) >= 2
        return value

EntityWatchlistSearchTerms.update_forward_refs()
