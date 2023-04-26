# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class SandboxItemSetVerificationStatusRequest(BaseModel):
    """SandboxItemSetVerificationStatusRequest defines the request schema for `/sandbox/item/set_verification_status`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    access_token: str = Field( description="The access token associated with the Item data is being requested for.")
    account_id: str = Field( description="The `account_id` of the account whose verification status is to be modified")
    verification_status: str = Field( description="The verification status to set the account to.")

SandboxItemSetVerificationStatusRequest.update_forward_refs()
