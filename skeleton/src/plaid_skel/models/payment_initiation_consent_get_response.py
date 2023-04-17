# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.payment_initiation_consent_constraints import PaymentInitiationConsentConstraints
from plaid_skel.models.payment_initiation_consent_scope import PaymentInitiationConsentScope
from plaid_skel.models.payment_initiation_consent_status import PaymentInitiationConsentStatus




class PaymentInitiationConsentGetResponse(BaseModel):
    """PaymentInitiationConsentGetResponse defines the response schema for `/payment_initation/consent/get`"""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#payment_initiation_consent_get_response"
            }
        }

    consent_id: str = Field( description="The consent ID.")
    status: PaymentInitiationConsentStatus = Field()
    created_at: datetime = Field( description="Consent creation timestamp, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.")
    recipient_id: str = Field( description="The ID of the recipient the payment consent is for.")
    reference: str = Field( description="A reference for the payment consent.")
    constraints: PaymentInitiationConsentConstraints = Field()
    scopes: List[PaymentInitiationConsentScope] = Field( description="An array of payment consent scopes.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

    @validator("consent_id")
    def consent_id_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("recipient_id")
    def recipient_id_min_length(cls, value):
        assert len(value) >= 1
        return value

PaymentInitiationConsentGetResponse.update_forward_refs()
