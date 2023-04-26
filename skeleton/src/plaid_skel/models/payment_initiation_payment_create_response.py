# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.payment_initiation_payment_create_status import PaymentInitiationPaymentCreateStatus




class PaymentInitiationPaymentCreateResponse(BaseModel):
    """PaymentInitiationPaymentCreateResponse defines the response schema for `/payment_initiation/payment/create`"""


    payment_id: str = Field( description="A unique ID identifying the payment")
    status: PaymentInitiationPaymentCreateStatus = Field()
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

PaymentInitiationPaymentCreateResponse.update_forward_refs()
