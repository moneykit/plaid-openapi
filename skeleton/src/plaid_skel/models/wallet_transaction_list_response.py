# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.wallet_transaction import WalletTransaction




class WalletTransactionListResponse(BaseModel):
    """WalletTransactionListResponse defines the response schema for `/wallet/transaction/list`"""


    transactions: List[WalletTransaction] = Field( description="An array of transactions of an e-wallet, associated with the given `wallet_id`")
    next_cursor: Optional[str] = Field(default=None, description="Cursor used for fetching transactions created before the latest transaction provided in this response")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

WalletTransactionListResponse.update_forward_refs()
