# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class NumbersInternationalNullable(BaseModel):
    """Identifying information for transferring money to or from an international bank account via wire transfer."""

    class Config:
        schema_extra = {"nullable": True}

    account_id: str = Field( description="The Plaid account ID associated with the account numbers")
    iban: str = Field( description="The International Bank Account Number (IBAN) for the account")
    bic: str = Field( description="The Bank Identifier Code (BIC) for the account")

NumbersInternationalNullable.update_forward_refs()
