# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.signal_device import SignalDevice
from plaid_skel.models.signal_user import SignalUser




class SignalEvaluateRequest(BaseModel):
    """SignalEvaluateRequest defines the request schema for `/signal/evaluate`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    access_token: str = Field( description="The access token associated with the Item data is being requested for.")
    account_id: str = Field( description="The Plaid `account_id` of the account that is the funding source for the proposed transaction. The `account_id` is returned in the `/accounts/get` endpoint as well as the [`onSuccess`](/docs/link/ios/#link-ios-onsuccess-linkSuccess-metadata-accounts-id) callback metadata.  This will return an [`INVALID_ACCOUNT_ID`](/docs/errors/invalid-input/#invalid_account_id) error if the account has been removed at the bank or if the `account_id` is no longer valid.")
    client_transaction_id: str = Field( description="The unique ID that you would like to use to refer to this transaction. For your convenience mapping your internal data, you could use your internal ID/identifier for this transaction. The max length for this field is 36 characters.")
    amount: float = Field( description="The transaction amount, in USD (e.g. `102.05`)")
    user_present: Optional[bool] = Field(default=None, description="`true` if the end user is present while initiating the ACH transfer and the endpoint is being called; `false` otherwise (for example, when the ACH transfer is scheduled and the end user is not present, or you call this endpoint after the ACH transfer but before submitting the Nacha file for ACH processing).")
    client_user_id: Optional[str] = Field(default=None, description="A unique ID that identifies the end user in your system. This ID is used to correlate requests by a user with multiple Items. The max length for this field is 36 characters. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`.")
    is_recurring: Optional[bool] = Field(default=None, description="`true` if the ACH transaction is a recurring transaction; `false` otherwise ")
    default_payment_method: Optional[str] = Field(default=None, description="The default ACH or non-ACH payment method to complete the transaction. `SAME_DAY_ACH`: Same Day ACH by NACHA. The debit transaction is processed and settled on the same day `NEXT_DAY_ACH`: Next Day ACH settlement for debit transactions, offered by some payment processors `STANDARD_ACH`: standard ACH by NACHA `REAL_TIME_PAYMENTS`: real-time payments such as RTP and FedNow `DEBIT_CARD`: if the default payment is over debit card networks `MULTIPLE_PAYMENT_METHODS`: if there is no default debit rail or there are multiple payment methods Possible values:  `SAME_DAY_ACH`, `NEXT_DAY_ACH`, `STANDARD_ACH`, `REAL_TIME_PAYMENTS`, `DEBIT_CARD`, `MULTIPLE_PAYMENT_METHODS`")
    user: Optional[SignalUser] = Field(default=None,)
    device: Optional[SignalDevice] = Field(default=None,)

    @field_validator("client_transaction_id")
    @classmethod
    def client_transaction_id_min_length(cls, value):
        assert len(value) >= 1
        return value

    @field_validator("client_transaction_id")
    @classmethod
    def client_transaction_id_max_length(cls, value):
        assert len(value) <= 36
        return value

    @field_validator("client_user_id")
    @classmethod
    def client_user_id_max_length(cls, value):
        assert len(value) <= 36
        return value

SignalEvaluateRequest.update_forward_refs()
