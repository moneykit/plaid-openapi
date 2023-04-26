# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class BankTransferSweepListRequest(BaseModel):
    """BankTransferSweepListRequest defines the request schema for `/bank_transfer/sweep/list`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    origination_account_id: Optional[str] = Field(default=None, description="If multiple origination accounts are available, `origination_account_id` must be used to specify the account that the sweeps belong to.")
    start_time: Optional[datetime] = Field(default=None, description="The start datetime of sweeps to return (RFC 3339 format).")
    end_time: Optional[datetime] = Field(default=None, description="The end datetime of sweeps to return (RFC 3339 format).")
    count: Optional[int] = Field(default=None, description="The maximum number of sweeps to return.")

    @validator("count")
    def count_max(cls, value):
        assert value <= 25
        return value

    @validator("count")
    def count_min(cls, value):
        assert value >= 1
        return value

BankTransferSweepListRequest.update_forward_refs()
