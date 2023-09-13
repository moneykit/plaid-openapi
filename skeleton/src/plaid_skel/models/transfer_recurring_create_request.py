# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.ach_class import ACHClass
from plaid_skel.models.transfer_device import TransferDevice
from plaid_skel.models.transfer_network import TransferNetwork
from plaid_skel.models.transfer_recurring_schedule import TransferRecurringSchedule
from plaid_skel.models.transfer_type import TransferType
from plaid_skel.models.transfer_user_in_request import TransferUserInRequest




class TransferRecurringCreateRequest(BaseModel):
    """Defines the request schema for `/transfer/recurring/create`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    access_token: str = Field( description="The Plaid `access_token` for the account that will be debited or credited. Required if not using `payment_profile_token`.")
    idempotency_key: str = Field( description="A random key provided by the client, per unique recurring transfer. Maximum of 50 characters.  The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a recurring fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single recurring transfer is created.")
    account_id: str = Field( description="The Plaid `account_id` corresponding to the end-user account that will be debited or credited. Returned only if `account_id` was set on intent creation.")
    funding_account_id: Optional[str] = Field(default=None, description="The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. Defaults to the account configured during onboarding.")
    type: TransferType = Field()
    network: TransferNetwork = Field()
    ach_class: Optional[ACHClass] = Field(default=None,)
    amount: str = Field( description="The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\").")
    user_present: Optional[bool] = Field(default=None, description="If the end user is initiating the specific transfer themselves via an interactive UI, this should be `true`; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be `false`.")
    iso_currency_code: Optional[str] = Field(default=None, description="The currency of the transfer amount. The default value is \"USD\".")
    description: str = Field( description="The description of the recurring transfer.")
    test_clock_id: Optional[str] = Field(default=None, description="Plaid’s unique identifier for a test clock.")
    schedule: TransferRecurringSchedule = Field()
    user: TransferUserInRequest = Field()
    device: TransferDevice = Field()

    @field_validator("idempotency_key")
    @classmethod
    def idempotency_key_max_length(cls, value):
        assert len(value) <= 50
        return value

TransferRecurringCreateRequest.update_forward_refs()
