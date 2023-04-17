# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.investments_transactions_get_request_options import InvestmentsTransactionsGetRequestOptions




class InvestmentsTransactionsGetRequest(BaseModel):
    """InvestmentsTransactionsGetRequest defines the request schema for `/investments/transactions/get`"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#investments_transactions_get_request"
            }
        }

    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    access_token: str = Field( description="The access token associated with the Item data is being requested for.")
    start_date: date = Field( description="The earliest date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD.")
    end_date: date = Field( description="The most recent date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD.")
    options: Optional[InvestmentsTransactionsGetRequestOptions] = Field(default=None,)

InvestmentsTransactionsGetRequest.update_forward_refs()
