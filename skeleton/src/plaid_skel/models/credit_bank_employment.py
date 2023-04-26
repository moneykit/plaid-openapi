# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_bank_employer import CreditBankEmployer




class CreditBankEmployment(BaseModel):
    """Detailed information for the bank employment."""


    bank_employment_id: str = Field( description="A unique identifier for the bank employment.")
    account_id: str = Field( description="Plaid's unique identifier for the account.")
    employer: CreditBankEmployer = Field()
    latest_deposit_date: date = Field( description="The date of the most recent deposit from this employer.")
    earliest_deposit_date: date = Field( description="The date of the earliest deposit from this employer from within the period of the days requested.")

CreditBankEmployment.update_forward_refs()
