# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class CreditRelayCreateRequest(BaseModel):
    """CreditRelayCreateRequest defines the request schema for `/credit/relay/create`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    report_tokens: List[str] = Field( description="List of report token strings, with at most one token of each report type. Currently only Asset Report token is supported.")
    secondary_client_id: str = Field( description="The `secondary_client_id` is the client id of the third party with whom you would like to share the relay token.")
    webhook: Optional[str] = Field(default=None, description="URL to which Plaid will send webhooks when the Secondary Client successfully retrieves an Asset Report by calling `/credit/relay/get`.")

CreditRelayCreateRequest.update_forward_refs()
