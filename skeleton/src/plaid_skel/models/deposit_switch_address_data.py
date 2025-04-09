# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class DepositSwitchAddressData(BaseModel):
    """The user's address."""


    city: str = Field( description="The full city name")
    region: str = Field( description="The region or state Example: `\"NC\"`")
    street: str = Field( description="The full street address Example: `\"564 Main Street, APT 15\"`")
    postal_code: str = Field( description="The postal code")
    country: str = Field( description="The ISO 3166-1 alpha-2 country code")

DepositSwitchAddressData.update_forward_refs()
