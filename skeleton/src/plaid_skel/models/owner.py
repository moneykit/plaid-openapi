# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.address import Address
from plaid_skel.models.email import Email
from plaid_skel.models.phone_number import PhoneNumber




class Owner(BaseModel):
    """Data returned from the financial institution about the owner or owners of an account. Only the `names` array must be non-empty."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#owner"
            }
        }

    names: List[str] = Field( description="A list of names associated with the account by the financial institution. In the case of a joint account, Plaid will make a best effort to report the names of all account holders.  If an Item contains multiple accounts with different owner names, some institutions will report all names associated with the Item in each account's `names` array.")
    phone_numbers: List[PhoneNumber] = Field( description="A list of phone numbers associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution.")
    emails: List[Email] = Field( description="A list of email addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution.")
    addresses: List[Address] = Field( description="Data about the various addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution.")

Owner.update_forward_refs()
