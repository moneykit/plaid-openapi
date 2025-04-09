# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class PaymentInitiationPaymentTokenCreateResponse(BaseModel):
    """PaymentInitiationPaymentTokenCreateResponse defines the response schema for `/payment_initiation/payment/token/create`"""


    payment_token: str = Field( description="A `payment_token` that can be provided to Link initialization to enter the payment initiation flow")
    payment_token_expiration_time: datetime = Field( description="The date and time at which the token will expire, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. A `payment_token` expires after 15 minutes.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

PaymentInitiationPaymentTokenCreateResponse.update_forward_refs()
