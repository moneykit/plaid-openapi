# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.payment_initiation_standing_order_metadata import PaymentInitiationStandingOrderMetadata




class PaymentInitiationMetadata(BaseModel):
    """Metadata that captures what specific payment configurations an institution supports when making Payment Initiation requests."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    supports_international_payments: bool = Field( description="Indicates whether the institution supports payments from a different country.")
    supports_sepa_instant: bool = Field( description="Indicates whether the institution supports SEPA Instant payments.")
    maximum_payment_amount: Dict[str, str] = Field( description="A mapping of currency to maximum payment amount (denominated in the smallest unit of currency) supported by the institution.  Example: `{\"GBP\": \"10000\"}` ")
    supports_refund_details: bool = Field( description="Indicates whether the institution supports returning refund details when initiating a payment.")
    standing_order_metadata: Optional[PaymentInitiationStandingOrderMetadata] = Field(default=None,)

PaymentInitiationMetadata.update_forward_refs()
