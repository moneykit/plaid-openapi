# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.identity_verification_request_user_name import IdentityVerificationRequestUserName
from plaid_skel.models.user_address import UserAddress
from plaid_skel.models.user_id_number import UserIDNumber




class IdentityVerificationRequestUser(BaseModel):
    """User information collected outside of Link, most likely via your own onboarding process.  Each of the following identity fields are optional:  `email_address`  `phone_number`  `date_of_birth`  `name`  `address`  `id_number`  Specifically, these fields are optional in that they can either be fully provided (satisfying every required field in their subschema) or omitted from the request entirely by not providing the key or value. Providing these fields via the API will result in Link skipping the data collection process for the associated user. All verification steps enabled in the associated Identity Verification Template will still be run. Verification steps will either be run immediately, or once the user completes the `accept_tos` step, depending on the value provided to the `gave_consent` field."""


    client_user_id: str = Field( description="An identifier to help you connect this object to your internal systems. For example, your database ID corresponding to this object.")
    email_address: Optional[EmailStr] = Field(default=None, description="A valid email address.")
    phone_number: Optional[str] = Field(default=None, description="A phone number in E.164 format.")
    date_of_birth: Optional[date] = Field(default=None, description="A date in the format YYYY-MM-DD (RFC 3339 Section 5.6).")
    name: Optional[IdentityVerificationRequestUserName] = Field(default=None,)
    address: Optional[UserAddress] = Field(default=None,)
    id_number: Optional[UserIDNumber] = Field(default=None,)

    @field_validator("client_user_id")
    @classmethod
    def client_user_id_min_length(cls, value):
        assert len(value) >= 1
        return value

IdentityVerificationRequestUser.update_forward_refs()
