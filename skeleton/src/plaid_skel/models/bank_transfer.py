# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.ach_class import ACHClass
from plaid_skel.models.bank_transfer_direction import BankTransferDirection
from plaid_skel.models.bank_transfer_failure import BankTransferFailure
from plaid_skel.models.bank_transfer_network import BankTransferNetwork
from plaid_skel.models.bank_transfer_status import BankTransferStatus
from plaid_skel.models.bank_transfer_type import BankTransferType
from plaid_skel.models.bank_transfer_user import BankTransferUser




class BankTransfer(BaseModel):
    """Represents a bank transfer within the Bank Transfers API."""


    id: str = Field( description="Plaid’s unique identifier for a bank transfer.")
    ach_class: ACHClass = Field()
    account_id: str = Field( description="The account ID that should be credited/debited for this bank transfer.")
    type: BankTransferType = Field()
    user: BankTransferUser = Field()
    amount: str = Field( description="The amount of the bank transfer (decimal string with two digits of precision e.g. \"10.00\").")
    iso_currency_code: str = Field( description="The currency of the transfer amount, e.g. \"USD\"")
    description: str = Field( description="The description of the transfer.")
    created: datetime = Field( description="The datetime when this bank transfer was created. This will be of the form `2006-01-02T15:04:05Z`")
    status: BankTransferStatus = Field()
    network: BankTransferNetwork = Field()
    cancellable: bool = Field( description="When `true`, you can still cancel this bank transfer.")
    failure_reason: Optional[BankTransferFailure] = Field(default=None,)
    custom_tag: Optional[str] = Field(default=None, description="A string containing the custom tag provided by the client in the create request. Will be null if not provided.")
    metadata: Optional[Dict[str, str]] = Field(default=None, description="The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply: The JSON values must be Strings (no nested JSON objects allowed) Only ASCII characters may be used Maximum of 50 key/value pairs Maximum key length of 40 characters Maximum value length of 500 characters ")
    origination_account_id: str = Field( description="Plaid’s unique identifier for the origination account that was used for this transfer.")
    direction: Optional[BankTransferDirection] = Field(default=None,)

BankTransfer.update_forward_refs()
