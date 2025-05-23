# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class TransferOriginatorCreateRequest(BaseModel):
    """Defines the request schema for `/transfer/originator/create`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    company_name: str = Field( description="The company name of the end customer being created. This will be displayed in public-facing surfaces, e.g. Plaid Dashboard.")

    @field_validator("company_name")
    @classmethod
    def company_name_min_length(cls, value):
        assert len(value) >= 1
        return value

TransferOriginatorCreateRequest.update_forward_refs()
