# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class IncomeVerificationPaystubsGetRequest(BaseModel):
    """IncomeVerificationPaystubsGetRequest defines the request schema for `/income/verification/paystubs/get`."""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    income_verification_id: Optional[str] = Field(default=None, description="The ID of the verification for which to get paystub information.")
    access_token: Optional[str] = Field(default=None, description="The access token associated with the Item data is being requested for.")

IncomeVerificationPaystubsGetRequest.update_forward_refs()
