# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.transactions_recurring_get_request_options import TransactionsRecurringGetRequestOptions




class TransactionsRecurringGetRequest(BaseModel):
    """TransactionsRecurringGetRequest defines the request schema for `/transactions/recurring/get`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    access_token: str = Field( description="The access token associated with the Item data is being requested for.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    options: Optional[TransactionsRecurringGetRequestOptions] = Field(default=None,)
    account_ids: List[str] = Field( description="A list of `account_ids` to retrieve for the Item  Note: An error will be returned if a provided `account_id` is not associated with the Item.")

TransactionsRecurringGetRequest.update_forward_refs()
