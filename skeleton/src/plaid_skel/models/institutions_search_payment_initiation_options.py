# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class InstitutionsSearchPaymentInitiationOptions(BaseModel):
    """Additional options that will be used to filter institutions by various Payment Initiation configurations."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#institutions_search_payment_initiation_options"
            }
            , "nullable": True,
        }

    payment_id: Optional[str] = Field(default=None, description="A unique ID identifying the payment")
    consent_id: Optional[str] = Field(default=None, description="A unique ID identifying the payment consent")

InstitutionsSearchPaymentInitiationOptions.update_forward_refs()
