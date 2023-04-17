# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class LinkOAuthCorrelationIdExchangeRequest(BaseModel):
    """LinkOAuthCorrelationIdExchangeRequest defines the request schema for `/link/oauth/correlation_id/exchange`"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#link_o_auth_correlation_id_exchange_request"
            }
        }

    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    link_correlation_id: str = Field( description="A `link_correlation_id` from a received OAuth redirect URI callback")

LinkOAuthCorrelationIdExchangeRequest.update_forward_refs()
