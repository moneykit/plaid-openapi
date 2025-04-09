# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.ach_class import ACHClass
from plaid_skel.models.transfer_network import TransferNetwork
from plaid_skel.models.transfer_recurring_schedule import TransferRecurringSchedule
from plaid_skel.models.transfer_recurring_status import TransferRecurringStatus
from plaid_skel.models.transfer_type import TransferType
from plaid_skel.models.transfer_user_in_response import TransferUserInResponse




class RecurringTransferNullable(BaseModel):
    """Represents a recurring transfer within the Transfers API."""


    recurring_transfer_id: str = Field( description="Plaid’s unique identifier for a recurring transfer.")
    created: datetime_ = Field( description="The datetime when this transfer was created. This will be of the form `2006-01-02T15:04:05Z`")
    next_origination_date: date_ = Field( description="A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).  The next transfer origination date after bank holiday adjustment.")
    test_clock_id: Optional[str] = Field(default=None, description="Plaid’s unique identifier for a test clock.")
    type: TransferType = Field()
    amount: str = Field( description="The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\").")
    status: TransferRecurringStatus = Field()
    ach_class: Optional[ACHClass] = Field(default=None,)
    network: TransferNetwork = Field()
    origination_account_id: str = Field( description="Plaid’s unique identifier for the origination account that was used for this transfer.")
    account_id: str = Field( description="The Plaid `account_id` corresponding to the end-user account that will be debited or credited.")
    funding_account_id: str = Field( description="The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited.")
    iso_currency_code: str = Field( description="The currency of the transfer amount, e.g. \"USD\"")
    description: str = Field( description="The description of the recurring transfer.")
    transfer_ids: List[str] = Field()
    user: TransferUserInResponse = Field()
    schedule: TransferRecurringSchedule = Field()

RecurringTransferNullable.update_forward_refs()
