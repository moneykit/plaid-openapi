# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_bank_employment_report import CreditBankEmploymentReport




class CreditBankEmploymentGetResponse(BaseModel):
    """CreditBankEmploymentGetResponse defines the response schema for `/beta/credit/v1/bank_employment/get`."""


    bank_employment_reports: List[CreditBankEmploymentReport] = Field( description="Bank Employment data. Each entry in the array will be a distinct bank employment report.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

CreditBankEmploymentGetResponse.update_forward_refs()
