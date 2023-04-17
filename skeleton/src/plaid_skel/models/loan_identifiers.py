# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.loan_identifier import LoanIdentifier




class LoanIdentifiers(BaseModel):
    """Collection of current and previous identifiers for this loan."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#loan_identifiers"
            }
        }

    loan_identifier: LoanIdentifier = Field()

LoanIdentifiers.update_forward_refs()
