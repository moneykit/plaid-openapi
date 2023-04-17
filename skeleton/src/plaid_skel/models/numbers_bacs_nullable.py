# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class NumbersBACSNullable(BaseModel):
    """Identifying information for transferring money to or from a UK bank account via BACS."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#numbers_bacs_nullable"
            }
        }

    account_id: str = Field( description="The Plaid account ID associated with the account numbers")
    account: str = Field( description="The BACS account number for the account")
    sort_code: str = Field( description="The BACS sort code for the account")

NumbersBACSNullable.update_forward_refs()
