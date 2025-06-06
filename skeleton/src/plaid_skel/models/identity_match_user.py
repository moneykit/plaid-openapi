# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.address_data_nullable import AddressDataNullable




class IdentityMatchUser(BaseModel):
    """The user's legal name, phone number, email address and address used to perform fuzzy match."""


    legal_name: Optional[str] = Field(default=None, description="The user's full legal name.")
    phone_number: Optional[str] = Field(default=None, description="The user's phone number, in E.164 format: +{countrycode}{number}. For example: \"+14151234567\". Phone numbers provided in other formats will be parsed on a best-effort basis.")
    email_address: Optional[str] = Field(default=None, description="The user's email address.")
    address: Optional[AddressDataNullable] = Field(default=None,)

IdentityMatchUser.update_forward_refs()
