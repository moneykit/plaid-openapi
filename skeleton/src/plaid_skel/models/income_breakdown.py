# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.income_breakdown_type import IncomeBreakdownType




class IncomeBreakdown(BaseModel):
    """An object representing a breakdown of the different income types on the paystub."""


    type: Optional[IncomeBreakdownType] = Field(default=None,)
    rate: Optional[float] = Field(default=None, description="The hourly rate at which the income is paid.")
    hours: Optional[float] = Field(default=None, description="The number of hours logged for this income for this pay period.")
    total: Optional[float] = Field(default=None, description="The total pay for this pay period.")

IncomeBreakdown.update_forward_refs()
