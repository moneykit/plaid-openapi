# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class PhoneNumber(BaseModel):
    """A phone number"""


    data: str = Field( description="The phone number.")
    primary: bool = Field( description="When `true`, identifies the phone number as the primary number on an account.")
    type: str = Field( description="The type of phone number.")

PhoneNumber.update_forward_refs()
