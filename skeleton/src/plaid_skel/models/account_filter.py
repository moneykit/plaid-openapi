# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class AccountFilter(BaseModel):
    """Enumerates the account subtypes that the application wishes for the user to be able to select from. For more details refer to Plaid documentation on account filters."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#account_filter"
            }
        }

    depository: Optional[List[str]] = Field(default=None, description="A list of account subtypes to be filtered.")
    credit: Optional[List[str]] = Field(default=None, description="A list of account subtypes to be filtered.")
    loan: Optional[List[str]] = Field(default=None, description="A list of account subtypes to be filtered.")
    investment: Optional[List[str]] = Field(default=None, description="A list of account subtypes to be filtered.")

AccountFilter.update_forward_refs()
