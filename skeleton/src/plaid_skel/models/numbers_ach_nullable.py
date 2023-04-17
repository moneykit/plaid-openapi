# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class NumbersACHNullable(BaseModel):
    """Identifying information for transferring money to or from a US account via ACH or wire transfer."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#numbers_ach_nullable"
            }
        }

    account_id: str = Field( description="The Plaid account ID associated with the account numbers")
    account: str = Field( description="The ACH account number for the account.  Note that when using OAuth with Chase Bank (`ins_56`), Chase will issue \"tokenized\" routing and account numbers, which are not the user's actual account and routing numbers. These tokenized numbers should work identically to normal account and routing numbers. The digits returned in the `mask` field will continue to reflect the actual account number, rather than the tokenized account number; for this reason, when displaying account numbers to the user to help them identify their account in your UI, always use the `mask` rather than truncating the `account` number. If a user revokes their permissions to your app, the tokenized numbers will continue to work for ACH deposits, but not withdrawals.")
    routing: str = Field( description="The ACH routing number for the account. If the institution is `ins_56`, this may be a tokenized routing number. For more information, see the description of the `account` field.")
    wire_routing: Optional[str] = Field(default=None, description="The wire transfer routing number for the account, if available")
    can_transfer_in: Optional[bool] = Field(default=None, description="Whether the account supports ACH transfers into the account")
    can_transfer_out: Optional[bool] = Field(default=None, description="Whether the account supports ACH transfers out of the account")

NumbersACHNullable.update_forward_refs()
