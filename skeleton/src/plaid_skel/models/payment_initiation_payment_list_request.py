# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class PaymentInitiationPaymentListRequest(BaseModel):
    """PaymentInitiationPaymentListRequest defines the request schema for `/payment_initiation/payment/list`"""


    client_id: Optional[str] = Field(default=None, description="Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.")
    secret: Optional[str] = Field(default=None, description="Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.")
    count: Optional[int] = Field(default=None, description="The maximum number of payments to return. If `count` is not specified, a maximum of 10 payments will be returned, beginning with the most recent payment before the cursor (if specified).")
    cursor: Optional[datetime_] = Field(default=None, description="A string in RFC 3339 format (i.e. \"2019-12-06T22:35:49Z\"). Only payments created before the cursor will be returned.")
    consent_id: Optional[str] = Field(default=None, description="The consent ID. If specified, only payments, executed using this consent, will be returned.")

    @field_validator("count")
    @classmethod
    def count_max(cls, value):
        assert value <= 200
        return value

    @field_validator("count")
    @classmethod
    def count_min(cls, value):
        assert value >= 1
        return value

PaymentInitiationPaymentListRequest.update_forward_refs()
