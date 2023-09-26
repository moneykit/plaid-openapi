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




class PaymentInitiationConsent(BaseModel):
    """PaymentInitiationConsent defines a payment initiation consent."""


    consent_id: str = Field( description="The consent ID.")
    status: PaymentInitiationConsentStatus = Field()
    created_at: datetime = Field( description="Consent creation timestamp, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.")
    recipient_id: str = Field( description="The ID of the recipient the payment consent is for.")
    reference: str = Field( description="A reference for the payment consent.")
    constraints: PaymentInitiationConsentConstraints = Field()
    scopes: List[PaymentInitiationConsentScope] = Field( description="An array of payment consent scopes.")

    @validator("consent_id")
    def consent_id_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("recipient_id")
    def recipient_id_min_length(cls, value):
        assert len(value) >= 1
        return value

PaymentInitiationConsent.update_forward_refs()
