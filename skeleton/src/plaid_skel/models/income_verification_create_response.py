# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class IncomeVerificationCreateResponse(BaseModel):
    """IncomeVerificationCreateResponse defines the response schema for `/income/verification/create`."""


    income_verification_id: str = Field( description="ID of the verification. This ID is persisted throughout the lifetime of the verification.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

IncomeVerificationCreateResponse.update_forward_refs()
