# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class PlatformIds(BaseModel):
    """An object containing a set of ids related to an employee"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#platform_ids"
            }
        }

    employee_id: Optional[str] = Field(default=None, description="The ID of an employee as given by their employer")
    payroll_id: Optional[str] = Field(default=None, description="The ID of an employee as given by their payroll")
    position_id: Optional[str] = Field(default=None, description="The ID of the position of the employee")

PlatformIds.update_forward_refs()
