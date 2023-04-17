# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_session import CreditSession




class CreditSessionsGetResponse(BaseModel):
    """CreditSessionsGetResponse defines the response schema for `/credit/sessions/get`"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#credit_sessions_get_response"
            }
        }

    sessions: Optional[List[CreditSession]] = Field(default=None, description="A list of Link sessions for the user. Sessions will be sorted in reverse chronological order.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

CreditSessionsGetResponse.update_forward_refs()
