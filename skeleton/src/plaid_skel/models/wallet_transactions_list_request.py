# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.wallet_transaction_list_request_options import WalletTransactionListRequestOptions




class WalletTransactionsListRequest(BaseModel):
    """WalletTransactionListRequest defines the request schema for `/wallet/transaction/list`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    wallet_id: str = Field( description="The ID of the e-wallet to fetch transactions from")
    cursor: Optional[str] = Field(default=None, description="A base64 value representing the latest transaction that has already been requested. Set this to `next_cursor` received from the previous `/wallet/transaction/list` request. If provided, the response will only contain transactions created before that transaction. If omitted, the response will contain transactions starting from the most recent, and in descending order by the `created_at` time.")
    count: Optional[int] = Field(default=None, description="The number of transactions to fetch")
    options: Optional[WalletTransactionListRequestOptions] = Field(default=None,)

    @validator("wallet_id")
    def wallet_id_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("cursor")
    def cursor_max_length(cls, value):
        assert len(value) <= 256
        return value

    @validator("count")
    def count_max(cls, value):
        assert value <= 200
        return value

    @validator("count")
    def count_min(cls, value):
        assert value >= 1
        return value

WalletTransactionsListRequest.update_forward_refs()
