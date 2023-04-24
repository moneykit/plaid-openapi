# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.transfer_event_type import TransferEventType
from plaid_skel.models.transfer_failure import TransferFailure
from plaid_skel.models.transfer_type import TransferType




class TransferEvent(BaseModel):
    """Represents an event in the Transfers API."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#transfer_event"
            }
        }

    event_id: int = Field( description="Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers.")
    timestamp: datetime = Field( description="The datetime when this event occurred. This will be of the form `2006-01-02T15:04:05Z`.")
    event_type: TransferEventType = Field()
    account_id: str = Field( description="The account ID associated with the transfer.")
    funding_account_id: str = Field( description="The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited.")
    transfer_id: str = Field( description="Plaid’s unique identifier for a transfer.")
    origination_account_id: Optional[str] = Field(default=None, description="The ID of the origination account that this balance belongs to.")
    transfer_type: TransferType = Field()
    transfer_amount: str = Field( description="The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\").")
    failure_reason: Optional[TransferFailure] = Field(default=None,)
    sweep_id: Optional[str] = Field(default=None, description="Plaid’s unique identifier for a sweep.")
    sweep_amount: Optional[str] = Field(default=None, description="A signed amount of how much was `swept` or `return_swept` for this transfer (decimal string with two digits of precision e.g. \"-5.50\").")
    refund_id: Optional[str] = Field(default=None, description="Plaid’s unique identifier for a refund. A non-null value indicates the event is for the associated refund of the transfer.")
    originator_client_id: Optional[str] = Field(default=None, description="The Plaid client ID that is the originator of the transfer that this event applies to. Only present if the transfer was created on behalf of another client as a third-party sender (TPS).")

    @validator("event_id")
    def event_id_min(cls, value):
        assert value >= 0
        return value

TransferEvent.update_forward_refs()
