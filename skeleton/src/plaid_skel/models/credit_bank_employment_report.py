# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_bank_employment_item import CreditBankEmploymentItem
from plaid_skel.models.credit_bank_employment_warning import CreditBankEmploymentWarning




class CreditBankEmploymentReport(BaseModel):
    """The report of the Bank Employment data for an end user."""


    bank_employment_report_id: str = Field( description="The unique identifier associated with the Bank Employment Report.")
    generated_time: datetime = Field( description="The time when the Bank Employment Report was generated, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. \"2018-04-12T03:32:11Z\").")
    days_requested: int = Field( description="The number of days requested by the customer for the Bank Employment Report.")
    items: List[CreditBankEmploymentItem] = Field( description="The list of Items in the report along with the associated metadata about the Item.")
    warnings: List[CreditBankEmploymentWarning] = Field( description="If data from the Bank Employment report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete.")

CreditBankEmploymentReport.update_forward_refs()
