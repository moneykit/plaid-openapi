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




class OwnerOverride(BaseModel):
    """Data about the owner or owners of an account. Any fields not specified will be filled in with default Sandbox information."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#owner_override"
            }
        }

    names: List[str] = Field( description="A list of names associated with the account by the financial institution. These should always be the names of individuals, even for business accounts. Note that the same name data will be used for all accounts associated with an Item.")
    phone_numbers: List[PhoneNumber] = Field( description="A list of phone numbers associated with the account.")
    emails: List[Email] = Field( description="A list of email addresses associated with the account.")
    addresses: List[Address] = Field( description="Data about the various addresses associated with the account.")

OwnerOverride.update_forward_refs()
