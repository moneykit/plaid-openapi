# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class WalletTransactionCounterpartyInternational(BaseModel):
    """International Bank Account Number for a Wallet Transaction"""

    class Config:
        schema_extra = {"nullable": True}

    iban: Optional[str] = Field(default=None, description="International Bank Account Number (IBAN).")

    @validator("iban")
    def iban_min_length(cls, value):
        assert len(value) >= 15
        return value

    @validator("iban")
    def iban_max_length(cls, value):
        assert len(value) <= 34
        return value

WalletTransactionCounterpartyInternational.update_forward_refs()
