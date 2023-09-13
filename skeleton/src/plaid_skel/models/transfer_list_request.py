# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class TransferListRequest(BaseModel):
    """Defines the request schema for `/transfer/list`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    start_date: Optional[datetime] = Field(default=None, description="The start datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)")
    end_date: Optional[datetime] = Field(default=None, description="The end datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)")
    count: Optional[int] = Field(default=None, description="The maximum number of transfers to return.")
    offset: Optional[int] = Field(default=None, description="The number of transfers to skip before returning results.")
    origination_account_id: Optional[str] = Field(default=None, description="Filter transfers to only those originated through the specified origination account.")
    originator_client_id: Optional[str] = Field(default=None, description="Filter transfers to only those with the specified originator client.")
    funding_account_id: Optional[str] = Field(default=None, description="Filter transfers to only those with the specified `funding_account_id`.")

    @field_validator("count")
    @classmethod
    def count_max(cls, value):
        assert value <= 25
        return value

    @field_validator("count")
    @classmethod
    def count_min(cls, value):
        assert value >= 1
        return value

    @field_validator("offset")
    @classmethod
    def offset_min(cls, value):
        assert value >= 0
        return value

TransferListRequest.update_forward_refs()
