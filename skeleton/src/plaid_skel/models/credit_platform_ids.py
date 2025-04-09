# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class CreditPlatformIds(BaseModel):
    """The object containing a set of ids related to an employee."""


    employee_id: Optional[str] = Field(default=None, description="The ID of an employee as given by their employer.")
    payroll_id: Optional[str] = Field(default=None, description="The ID of an employee as given by their payroll.")
    position_id: Optional[str] = Field(default=None, description="The ID of the position of the employee.")

CreditPlatformIds.update_forward_refs()
