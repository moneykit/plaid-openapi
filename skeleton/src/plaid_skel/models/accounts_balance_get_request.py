# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.accounts_balance_get_request_options import AccountsBalanceGetRequestOptions




class AccountsBalanceGetRequest(BaseModel):
    """AccountsBalanceGetRequest defines the request schema for `/accounts/balance/get`"""


    access_token: str = Field( description="The access token associated with the Item data is being requested for.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    options: Optional[AccountsBalanceGetRequestOptions] = Field(default=None,)

AccountsBalanceGetRequest.update_forward_refs()
