# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class TransferRepaymentReturn(BaseModel):
    """Represents a return on a Guaranteed ACH transfer that is included in the specified repayment."""


    transfer_id: str = Field( description="The unique identifier of the guaranteed transfer that was returned.")
    event_id: int = Field( description="The unique identifier of the corresponding `returned` transfer event.")
    amount: str = Field( description="The value of the returned transfer.")
    iso_currency_code: str = Field( description="The currency of the repayment, e.g. \"USD\".")

    @field_validator("event_id")
    @classmethod
    def event_id_min(cls, value):
        assert value >= 0
        return value

TransferRepaymentReturn.update_forward_refs()
