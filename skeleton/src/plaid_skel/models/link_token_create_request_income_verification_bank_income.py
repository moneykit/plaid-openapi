# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class LinkTokenCreateRequestIncomeVerificationBankIncome(BaseModel):
    """Specifies options for initializing Link for use with Bank Income. This field is required if `income_verification` is included in the `products` array and `bank` is specified in `income_source_types`."""


    days_requested: int = Field( description="The number of days of data to request for the Bank Income product")
    enable_multiple_items: Optional[bool] = Field(default=None, description="Whether to enable multiple Items to be added in the Link session")

    @field_validator("days_requested")
    @classmethod
    def days_requested_max(cls, value):
        assert value <= 731
        return value

    @field_validator("days_requested")
    @classmethod
    def days_requested_min(cls, value):
        assert value >= 1
        return value

LinkTokenCreateRequestIncomeVerificationBankIncome.update_forward_refs()
