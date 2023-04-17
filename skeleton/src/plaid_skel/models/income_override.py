# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.paystub_override import PaystubOverride




class IncomeOverride(BaseModel):
    """Specify payroll data on the account."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#income_override"
            }
        }

    paystubs: Optional[List[PaystubOverride]] = Field(default=None, description="A list of paystubs associated with the account.")

IncomeOverride.update_forward_refs()
