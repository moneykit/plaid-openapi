# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.identity_verification_response_user_name import IdentityVerificationResponseUserName
from plaid_skel.models.identity_verification_user_address import IdentityVerificationUserAddress
from plaid_skel.models.user_id_number import UserIDNumber




class IdentityVerificationUserData(BaseModel):
    """The identity data that was either collected from the user or provided via API in order to perform an identity verification."""


    phone_number: Optional[str] = Field(default=None, description="A phone number in E.164 format.")
    date_of_birth: Optional[date] = Field(default=None, description="A date in the format YYYY-MM-DD (RFC 3339 Section 5.6).")
    ip_address: Optional[str] = Field(default=None, description="An IPv4 or IPV6 address.")
    email_address: Optional[EmailStr] = Field(default=None, description="A valid email address.")
    name: Optional[IdentityVerificationResponseUserName] = Field(default=None,)
    address: Optional[IdentityVerificationUserAddress] = Field(default=None,)
    id_number: Optional[UserIDNumber] = Field(default=None,)

IdentityVerificationUserData.update_forward_refs()
