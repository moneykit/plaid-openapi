# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.transfer_event_list_transfer_type import TransferEventListTransferType
from plaid_skel.models.transfer_event_type import TransferEventType




class TransferEventListRequest(BaseModel):
    """Defines the request schema for `/transfer/event/list`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    start_date: Optional[datetime] = Field(default=None, description="The start datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)")
    end_date: Optional[datetime] = Field(default=None, description="The end datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)")
    transfer_id: Optional[str] = Field(default=None, description="Plaid’s unique identifier for a transfer.")
    account_id: Optional[str] = Field(default=None, description="The account ID to get events for all transactions to/from an account.")
    transfer_type: Optional[TransferEventListTransferType] = Field(default=None,)
    event_types: Optional[List[TransferEventType]] = Field(default=None, description="Filter events by event type.")
    sweep_id: Optional[str] = Field(default=None, description="Plaid’s unique identifier for a sweep.")
    count: Optional[int] = Field(default=None, description="The maximum number of transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned.")
    offset: Optional[int] = Field(default=None, description="The offset into the list of transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 events will be returned.")
    origination_account_id: Optional[str] = Field(default=None, description="The origination account ID to get events for transfers from a specific origination account.")
    originator_client_id: Optional[str] = Field(default=None, description="Filter transfer events to only those with the specified originator client.")
    funding_account_id: Optional[str] = Field(default=None, description="Filter transfer events to only those with the specified `funding_account_id`.")

    @validator("count")
    def count_max(cls, value):
        assert value <= 25
        return value

    @validator("count")
    def count_min(cls, value):
        assert value >= 1
        return value

    @validator("offset")
    def offset_min(cls, value):
        assert value >= 0
        return value

TransferEventListRequest.update_forward_refs()
