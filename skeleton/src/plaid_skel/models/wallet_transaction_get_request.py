# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class WalletTransactionGetRequest(BaseModel):
    """WalletTransactionGetRequest defines the request schema for `/wallet/transaction/get`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    transaction_id: str = Field( description="The ID of the transaction to fetch")

    @field_validator("transaction_id")
    @classmethod
    def transaction_id_min_length(cls, value):
        assert len(value) >= 1
        return value

WalletTransactionGetRequest.update_forward_refs()
