# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class TransferQuestionnaireCreateRequest(BaseModel):
    """Defines the request schema for `/transfer/questionnaire/create`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    originator_client_id: str = Field( description="Client ID of the end customer.")
    redirect_uri: str = Field( description="URL the end customer will be redirected to after completing questions in Plaid-hosted onboarding flow.")

TransferQuestionnaireCreateRequest.update_forward_refs()
