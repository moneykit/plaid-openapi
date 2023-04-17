# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_bank_income_refresh_request_options import CreditBankIncomeRefreshRequestOptions




class CreditBankIncomeRefreshRequest(BaseModel):
    """CreditBankIncomeRefreshRequest defines the request schema for `/credit/bank_income/refresh`."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#credit_bank_income_refresh_request"
            }
        }

    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    user_token: str = Field( description="The user token associated with the User data is being requested for.")
    options: Optional[CreditBankIncomeRefreshRequestOptions] = Field(default=None,)

CreditBankIncomeRefreshRequest.update_forward_refs()
