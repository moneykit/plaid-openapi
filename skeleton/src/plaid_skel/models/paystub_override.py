# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.income_breakdown import IncomeBreakdown
from plaid_skel.models.pay_period_details import PayPeriodDetails
from plaid_skel.models.paystub_override_employee import PaystubOverrideEmployee
from plaid_skel.models.paystub_override_employer import PaystubOverrideEmployer




class PaystubOverride(BaseModel):
    """An object representing data from a paystub."""


    employer: Optional[PaystubOverrideEmployer] = Field(default=None,)
    employee: Optional[PaystubOverrideEmployee] = Field(default=None,)
    income_breakdown: Optional[List[IncomeBreakdown]] = Field(default=None,)
    pay_period_details: Optional[PayPeriodDetails] = Field(default=None,)

PaystubOverride.update_forward_refs()
