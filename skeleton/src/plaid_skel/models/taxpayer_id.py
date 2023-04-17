# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class TaxpayerID(BaseModel):
    """Taxpayer ID of the individual receiving the paystub."""

    class Config:
        schema_extra = {
            "externalDocs": {
                "url": "https://plaid.com/docs/api/accounts/#taxpayer_id"
            }
        }

    id_type: Optional[str] = Field(default=None, description="Type of ID, e.g. 'SSN'")
    id_mask: Optional[str] = Field(default=None, description="ID mask; i.e. last 4 digits of the taxpayer ID")
    last_4_digits: Optional[str] = Field(default=None, description="Last 4 digits of unique number of ID.")

    @validator("last_4_digits")
    def last_4_digits_min_length(cls, value):
        assert len(value) >= 4
        return value

    @validator("last_4_digits")
    def last_4_digits_max_length(cls, value):
        assert len(value) <= 4
        return value

TaxpayerID.update_forward_refs()
