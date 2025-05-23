# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.deductions import Deductions
from plaid_skel.models.earnings import Earnings
from plaid_skel.models.employee import Employee
from plaid_skel.models.employment_details import EmploymentDetails
from plaid_skel.models.income_breakdown import IncomeBreakdown
from plaid_skel.models.net_pay import NetPay
from plaid_skel.models.pay_period_details import PayPeriodDetails
from plaid_skel.models.paystub_details import PaystubDetails
from plaid_skel.models.paystub_employer import PaystubEmployer
from plaid_skel.models.paystub_ytd_details import PaystubYTDDetails




class Paystub(BaseModel):
    """An object representing data extracted from the end user's paystub."""


    deductions: Deductions = Field()
    doc_id: str = Field( description="An identifier of the document referenced by the document metadata.")
    earnings: Earnings = Field()
    employee: Employee = Field()
    employer: PaystubEmployer = Field()
    employment_details: Optional[EmploymentDetails] = Field(default=None,)
    net_pay: NetPay = Field()
    pay_period_details: PayPeriodDetails = Field()
    paystub_details: Optional[PaystubDetails] = Field(default=None,)
    income_breakdown: Optional[List[IncomeBreakdown]] = Field(default=None,)
    ytd_earnings: Optional[PaystubYTDDetails] = Field(default=None,)

Paystub.update_forward_refs()
