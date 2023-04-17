# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.numbers_international_iban import NumbersInternationalIBAN
from plaid_skel.models.recipient_bacs import RecipientBACS




class WalletNumbers(BaseModel):
    """An object representing the e-wallet account numbers"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#wallet_numbers"
            }
        }

    bacs: Optional[RecipientBACS] = Field(default=None,)
    international: Optional[NumbersInternationalIBAN] = Field(default=None,)

WalletNumbers.update_forward_refs()
