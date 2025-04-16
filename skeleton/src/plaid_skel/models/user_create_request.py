# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class UserCreateRequest(BaseModel):
    """UserCreateRequest defines the request schema for `/user/create`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    client_user_id: str = Field( description="A unique ID representing the end user. Maximum of 128 characters. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`.")

    @field_validator("client_user_id")
    @classmethod
    def client_user_id_min_length(cls, value):
        assert len(value) >= 1
        return value

    @field_validator("client_user_id")
    @classmethod
    def client_user_id_max_length(cls, value):
        assert len(value) <= 128
        return value

UserCreateRequest.update_forward_refs()
