# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import ConfigDict, AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.payment_schedule_interval import PaymentScheduleInterval




class PaymentInitiationStandingOrderMetadata(BaseModel):
    """Metadata specifically related to valid Payment Initiation standing order configurations for the institution."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    supports_standing_order_end_date: bool = Field( description="Indicates whether the institution supports closed-ended standing orders by providing an end date.")
    supports_standing_order_negative_execution_days: bool = Field( description="This is only applicable to `MONTHLY` standing orders. Indicates whether the institution supports negative integers (-1 to -5) for setting up a `MONTHLY` standing order relative to the end of the month.")
    valid_standing_order_intervals: List[PaymentScheduleInterval] = Field( description="A list of the valid standing order intervals supported by the institution.")

PaymentInitiationStandingOrderMetadata.update_forward_refs()
