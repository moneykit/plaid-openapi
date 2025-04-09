# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.bank_transfer_event_list_bank_transfer_type import BankTransferEventListBankTransferType
from plaid_skel.models.bank_transfer_event_list_direction import BankTransferEventListDirection
from plaid_skel.models.bank_transfer_event_type import BankTransferEventType




class BankTransferEventListRequest(BaseModel):
    """Defines the request schema for `/bank_transfer/event/list`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    start_date: Optional[datetime] = Field(default=None, description="The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)")
    end_date: Optional[datetime] = Field(default=None, description="The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`)")
    bank_transfer_id: Optional[str] = Field(default=None, description="Plaid’s unique identifier for a bank transfer.")
    account_id: Optional[str] = Field(default=None, description="The account ID to get events for all transactions to/from an account.")
    bank_transfer_type: Optional[BankTransferEventListBankTransferType] = Field(default=None,)
    event_types: Optional[List[BankTransferEventType]] = Field(default=None, description="Filter events by event type.")
    count: Optional[int] = Field(default=None, description="The maximum number of bank transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned.")
    offset: Optional[int] = Field(default=None, description="The offset into the list of bank transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 bank transfer events will be returned.")
    origination_account_id: Optional[str] = Field(default=None, description="The origination account ID to get events for transfers from a specific origination account.")
    direction: Optional[BankTransferEventListDirection] = Field(default=None,)

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

BankTransferEventListRequest.update_forward_refs()
