# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.verification_status import VerificationStatus




class EmployeeIncomeSummaryFieldString(BaseModel):
    """The name of the employee, as reported on the paystub."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#employee_income_summary_field_string"
            }
        }

    value: str = Field( description="The value of the field.")
    verification_status: VerificationStatus = Field()

EmployeeIncomeSummaryFieldString.update_forward_refs()
