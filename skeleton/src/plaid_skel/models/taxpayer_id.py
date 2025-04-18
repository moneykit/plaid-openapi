# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class TaxpayerID(BaseModel):
    """Taxpayer ID of the individual receiving the paystub."""


    id_type: Optional[str] = Field(default=None, description="Type of ID, e.g. 'SSN'")
    id_mask: Optional[str] = Field(default=None, description="ID mask; i.e. last 4 digits of the taxpayer ID")
    last_4_digits: Optional[str] = Field(default=None, description="Last 4 digits of unique number of ID.")

    @field_validator("last_4_digits")
    @classmethod
    def last_4_digits_min_length(cls, value):
        assert len(value) >= 4
        return value

    @field_validator("last_4_digits")
    @classmethod
    def last_4_digits_max_length(cls, value):
        assert len(value) <= 4
        return value

TaxpayerID.update_forward_refs()
