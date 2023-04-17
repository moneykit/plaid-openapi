# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.payment_initiation_recipient import PaymentInitiationRecipient




class PaymentInitiationRecipientListResponse(BaseModel):
    """PaymentInitiationRecipientListResponse defines the response schema for `/payment_initiation/recipient/list`"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#payment_initiation_recipient_list_response"
            }
        }

    recipients: List[PaymentInitiationRecipient] = Field( description="An array of payment recipients created for Payment Initiation")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

PaymentInitiationRecipientListResponse.update_forward_refs()
