# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.identity_verification_retry_request_steps_object import IdentityVerificationRetryRequestStepsObject
from plaid_skel.models.strategy import Strategy




class IdentityVerificationRetryRequest(BaseModel):
    """Request input for retrying an identity verification attempt"""


    client_user_id: str = Field( description="An identifier to help you connect this object to your internal systems. For example, your database ID corresponding to this object.")
    template_id: str = Field( description="ID of the associated Identity Verification template.")
    strategy: Strategy = Field()
    steps: Optional[IdentityVerificationRetryRequestStepsObject] = Field(default=None,)
    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")

    @field_validator("client_user_id")
    @classmethod
    def client_user_id_min_length(cls, value):
        assert len(value) >= 1
        return value

IdentityVerificationRetryRequest.update_forward_refs()
