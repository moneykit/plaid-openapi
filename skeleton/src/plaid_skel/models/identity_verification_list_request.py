# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class IdentityVerificationListRequest(BaseModel):
    """Request input for listing identity verifications"""


    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    template_id: str = Field( description="ID of the associated Identity Verification template.")
    client_user_id: str = Field( description="An identifier to help you connect this object to your internal systems. For example, your database ID corresponding to this object.")
    cursor: Optional[str] = Field(default=None, description="An identifier that determines which page of results you receive.")

    @field_validator("client_user_id")
    @classmethod
    def client_user_id_min_length(cls, value):
        assert len(value) >= 1
        return value

IdentityVerificationListRequest.update_forward_refs()
