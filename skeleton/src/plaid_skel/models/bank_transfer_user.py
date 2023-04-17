# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class BankTransferUser(BaseModel):
    """The legal name and other information for the account holder."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#bank_transfer_user"
            }
        }

    legal_name: str = Field( description="The account holder’s full legal name. If the transfer `ach_class` is `ccd`, this should be the business name of the account holder.")
    email_address: Optional[str] = Field(default=None, description="The account holder’s email.")
    routing_number: Optional[str] = Field(default=None, description="The account holder's routing number. This field is only used in response data. Do not provide this field when making requests.")

BankTransferUser.update_forward_refs()
