# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class CreditSessionPayrollIncomeResult(BaseModel):
    """The details of a digital payroll income verification in Link"""


    num_paystubs_retrieved: Optional[int] = Field(default=None, description="The number of paystubs retrieved from a payroll provider.")
    num_w2s_retrieved: Optional[int] = Field(default=None, description="The number of w2s retrieved from a payroll provider.")
    institution_id: Optional[str] = Field(default=None, description="The Plaid Institution ID associated with the Item.")
    institution_name: Optional[str] = Field(default=None, description="The Institution Name associated with the Item.")

CreditSessionPayrollIncomeResult.update_forward_refs()
