# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class TransferEventSyncRequest(BaseModel):
    """Defines the request schema for `/transfer/event/sync`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    after_id: int = Field( description="The latest (largest) `event_id` fetched via the sync endpoint, or 0 initially.")
    count: Optional[int] = Field(default=None, description="The maximum number of transfer events to return.")

    @field_validator("after_id")
    @classmethod
    def after_id_min(cls, value):
        assert value >= 0
        return value

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

TransferEventSyncRequest.update_forward_refs()
