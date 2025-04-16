# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_bank_employment import CreditBankEmployment
from plaid_skel.models.credit_bank_income_account import CreditBankIncomeAccount




class CreditBankEmploymentItem(BaseModel):
    """The details and metadata for an end user's Item."""


    item_id: str = Field( description="The unique identifier for the Item.")
    last_updated_time: datetime_ = Field( description="The time when this Item's data was last retrieved from the financial institution, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. \"2018-04-12T03:32:11Z\").")
    institution_id: str = Field( description="The unique identifier of the institution associated with the Item.")
    institution_name: str = Field( description="The name of the institution associated with the Item.")
    bank_employments: List[CreditBankEmployment] = Field( description="The bank employment information for this Item. Each entry in the array is a different employer found.")
    bank_employment_accounts: List[CreditBankIncomeAccount] = Field( description="The Item's accounts that have Bank Employment data.")

CreditBankEmploymentItem.update_forward_refs()
