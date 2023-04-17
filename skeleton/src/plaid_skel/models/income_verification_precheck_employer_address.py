# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class IncomeVerificationPrecheckEmployerAddress(BaseModel):
    """The address of the employer"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#income_verification_precheck_employer_address"
            }
        }

    city: Optional[str] = Field(default=None, description="The full city name")
    country: Optional[str] = Field(default=None, description="The ISO 3166-1 alpha-2 country code")
    postal_code: Optional[str] = Field(default=None, description="The postal code. In API versions 2018-05-22 and earlier, this field is called `zip`.")
    region: Optional[str] = Field(default=None, description="The region or state. In API versions 2018-05-22 and earlier, this field is called `state`. Example: `\"NC\"`")
    street: Optional[str] = Field(default=None, description="The full street address Example: `\"564 Main Street, APT 15\"`")

IncomeVerificationPrecheckEmployerAddress.update_forward_refs()
