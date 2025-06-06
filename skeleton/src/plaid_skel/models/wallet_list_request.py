# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.wallet_iso_currency_code import WalletISOCurrencyCode




class WalletListRequest(BaseModel):
    """WalletListRequest defines the request schema for `/wallet/list`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    iso_currency_code: Optional[WalletISOCurrencyCode] = Field(default=None,)
    cursor: Optional[str] = Field(default=None, description="A base64 value representing the latest e-wallet that has already been requested. Set this to `next_cursor` received from the previous `/wallet/list` request. If provided, the response will only contain e-wallets created before that e-wallet. If omitted, the response will contain e-wallets starting from the most recent, and in descending order.")
    count: Optional[int] = Field(default=None, description="The number of e-wallets to fetch")

    @field_validator("cursor")
    @classmethod
    def cursor_max_length(cls, value):
        assert len(value) <= 256
        return value

    @field_validator("count")
    @classmethod
    def count_max(cls, value):
        assert value <= 20
        return value

    @field_validator("count")
    @classmethod
    def count_min(cls, value):
        assert value >= 1
        return value

WalletListRequest.update_forward_refs()
