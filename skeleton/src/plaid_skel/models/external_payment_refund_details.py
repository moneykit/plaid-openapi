# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.recipient_bacs_nullable import RecipientBACSNullable




class ExternalPaymentRefundDetails(BaseModel):
    """Details about external payment refund"""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    name: str = Field( description="The name of the account holder.")
    iban: Optional[str] = Field(default=None, description="The International Bank Account Number (IBAN) for the account.")
    bacs: Optional[RecipientBACSNullable] = Field(default=None,)

ExternalPaymentRefundDetails.update_forward_refs()
