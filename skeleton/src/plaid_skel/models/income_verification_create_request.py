# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.income_verification_create_request_options import IncomeVerificationCreateRequestOptions




class IncomeVerificationCreateRequest(BaseModel):
    """IncomeVerificationCreateRequest defines the request schema for `/income/verification/create`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    webhook: str = Field( description="The URL endpoint to which Plaid should send webhooks related to the progress of the income verification process.")
    precheck_id: Optional[str] = Field(default=None, description="The ID of a precheck created with `/income/verification/precheck`. Will be used to improve conversion of the income verification flow.")
    options: Optional[IncomeVerificationCreateRequestOptions] = Field(default=None,)

IncomeVerificationCreateRequest.update_forward_refs()
