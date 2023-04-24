# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class IdentityVerificationUserAddress(BaseModel):
    """Even if an address has been collected, some fields may be null depending on the region's addressing system. For example:  Addresses from the United Kingdom will not include a region  Addresses from Hong Kong will not include postal code"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#identity_verification_user_address"
            }
            , "nullable": True,
        }

    street: Optional[str] = Field(default=None, description="The primary street portion of an address. If the user has submitted their address, this field will always be filled.")
    street2: Optional[str] = Field(default=None, description="Extra street information, like an apartment or suite number.")
    city: Optional[str] = Field(default=None, description="City from the end user's address")
    region: Optional[str] = Field(default=None, description="An ISO 3166-2 subdivision code. Related terms would be \"state\", \"province\", \"prefecture\", \"zone\", \"subdivision\", etc.")
    postal_code: Optional[str] = Field(default=None, description="The postal code for the associated address. Between 2 and 10 alphanumeric characters. For US-based addresses this must be 5 numeric digits.")
    country: str = Field( description="Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2 form.")

    @validator("country")
    def country_min_length(cls, value):
        assert len(value) >= 2
        return value

IdentityVerificationUserAddress.update_forward_refs()
