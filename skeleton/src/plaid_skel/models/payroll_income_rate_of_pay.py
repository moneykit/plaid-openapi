# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class PayrollIncomeRateOfPay(BaseModel):
    """An object representing the rate at which an individual is paid."""


    pay_rate: Optional[str] = Field(default=None, description="The rate at which an employee is paid.")
    pay_amount: Optional[float] = Field(default=None, description="The amount at which an employee is paid.")

PayrollIncomeRateOfPay.update_forward_refs()
