# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class StudentRepaymentPlan(BaseModel):
    """An object representing the repayment plan for the student loan"""


    description: Optional[str] = Field(default=None, description="The description of the repayment plan as provided by the servicer.")
    type: Optional[str] = Field(default=None, description="The type of the repayment plan.")

StudentRepaymentPlan.update_forward_refs()
