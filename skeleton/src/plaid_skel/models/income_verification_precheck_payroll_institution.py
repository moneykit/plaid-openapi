# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class IncomeVerificationPrecheckPayrollInstitution(BaseModel):
    """Information about the end user's payroll institution"""

    class Config:
        schema_extra = {"nullable": True}

    name: Optional[str] = Field(default=None, description="The name of payroll institution")

IncomeVerificationPrecheckPayrollInstitution.update_forward_refs()
