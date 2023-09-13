# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.ach_class import ACHClass
from plaid_skel.models.transfer_authorization_device import TransferAuthorizationDevice
from plaid_skel.models.transfer_authorization_user_in_request import TransferAuthorizationUserInRequest
from plaid_skel.models.transfer_network import TransferNetwork
from plaid_skel.models.transfer_type import TransferType




class TransferAuthorizationCreateRequest(BaseModel):
    """Defines the request schema for `/transfer/authorization/create`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    access_token: Optional[str] = Field(default=None, description="The Plaid `access_token` for the account that will be debited or credited. Required if not using `payment_profile_token`.")
    account_id: Optional[str] = Field(default=None, description="The Plaid `account_id` corresponding to the end-user account that will be debited or credited. Returned only if `account_id` was set on intent creation.")
    funding_account_id: Optional[str] = Field(default=None, description="The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. Defaults to the account configured during onboarding.")
    payment_profile_token: Optional[str] = Field(default=None, description="The payment profile token associated with the Payment Profile that will be debited or credited. Required if not using `access_token`.")
    type: TransferType = Field()
    network: TransferNetwork = Field()
    amount: str = Field( description="The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\").")
    ach_class: Optional[ACHClass] = Field(default=None,)
    user: TransferAuthorizationUserInRequest = Field()
    device: Optional[TransferAuthorizationDevice] = Field(default=None,)
    origination_account_id: Optional[str] = Field(default=None, description="Plaid's unique identifier for the origination account for this authorization. If not specified, the default account will be used.")
    iso_currency_code: Optional[str] = Field(default=None, description="The currency of the transfer amount. The default value is \"USD\".")
    idempotency_key: Optional[str] = Field(default=None, description="A random key provided by the client, per unique authorization. Maximum of 50 characters.  The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create an authorization fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single authorization is created.  Failure to provide this key may result in duplicate charges.  Required for guaranteed ACH customers.")
    user_present: Optional[bool] = Field(default=None, description="Required for Guarantee. If the end user is initiating the specific transfer themselves via an interactive UI, this should be `true`; for automatic recurring payments where the end user is not actually initiating each individual transfer, it should be `false`.")
    with_guarantee: Optional[bool] = Field(default=None, description="If set to `false`, Plaid will not offer a `guarantee_decision` for this request(Guarantee customers only).")
    beacon_session_id: Optional[str] = Field(default=None, description="The unique identifier returned by Plaid's [beacon](https://plaid.com/docs/transfer/guarantee/#using-a-beacon) when it is run on your webpage. Required for Guarantee customers who are not using [Transfer UI](https://plaid.com/docs/transfer/using-transfer-ui/) and have a web checkout experience.")
    originator_client_id: Optional[str] = Field(default=None, description="The Plaid client ID that is the originator of this transfer. Only needed if creating transfers on behalf of another client as a third-party sender (TPS).")

    @field_validator("idempotency_key")
    @classmethod
    def idempotency_key_max_length(cls, value):
        assert len(value) <= 50
        return value

TransferAuthorizationCreateRequest.update_forward_refs()
