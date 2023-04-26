# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class TransferCapabilitiesGetRequest(BaseModel):
    """Defines the request schema for `/transfer/capabilities/get`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    access_token: Optional[str] = Field(default=None, description="The Plaid `access_token` for the account that will be debited or credited. Required if not using `payment_profile_token`.")
    account_id: Optional[str] = Field(default=None, description="The Plaid `account_id` corresponding to the end-user account that will be debited or credited. Returned only if `account_id` was set on intent creation.")
    payment_profile_token: Optional[str] = Field(default=None, description="A payment profile token associated with the Payment Profile data that is being requested.")

TransferCapabilitiesGetRequest.update_forward_refs()
