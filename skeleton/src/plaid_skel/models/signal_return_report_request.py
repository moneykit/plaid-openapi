# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class SignalReturnReportRequest(BaseModel):
    """SignalReturnReportRequest defines the request schema for `/signal/return/report`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    client_transaction_id: str = Field( description="Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate`")
    return_code: str = Field( description="Must be a valid ACH return code (e.g. \"R01\")  If formatted incorrectly, this will result in an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error.")
    returned_at: Optional[datetime_] = Field(default=None, description="Date and time when you receive the returns from your payment processors, in ISO 8601 format (`YYYY-MM-DDTHH:mm:ssZ`).")

    @field_validator("client_transaction_id")
    @classmethod
    def client_transaction_id_min_length(cls, value):
        assert len(value) >= 1
        return value

    @field_validator("client_transaction_id")
    @classmethod
    def client_transaction_id_max_length(cls, value):
        assert len(value) <= 36
        return value

SignalReturnReportRequest.update_forward_refs()
