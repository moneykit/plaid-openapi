# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class CreditPayrollIncomeRefreshRequestOptions(BaseModel):
    """An optional object for `/credit/payroll_income/refresh` request options."""


    item_ids: Optional[List[str]] = Field(default=None, description="An array of `item_id`s to be refreshed. Each `item_id` should uniquely identify a payroll income item.")
    webhook: Optional[str] = Field(default=None, description="The URL where Plaid will send the payroll income refresh webhook.")

CreditPayrollIncomeRefreshRequestOptions.update_forward_refs()
