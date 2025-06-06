# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class ServicerAddressData(BaseModel):
    """The address of the student loan servicer. This is generally the remittance address to which payments should be sent."""


    city: Optional[str] = Field(default=None, description="The full city name")
    region: Optional[str] = Field(default=None, description="The region or state Example: `\"NC\"`")
    street: Optional[str] = Field(default=None, description="The full street address Example: `\"564 Main Street, APT 15\"`")
    postal_code: Optional[str] = Field(default=None, description="The postal code")
    country: Optional[str] = Field(default=None, description="The ISO 3166-1 alpha-2 country code")

ServicerAddressData.update_forward_refs()
