# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class RecipientBACSNullable(BaseModel):
    """An object containing a BACS account number and sort code. If an IBAN is not provided or if this recipient needs to accept domestic GBP-denominated payments, BACS data is required."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    account: Optional[str] = Field(default=None, description="The account number of the account. Maximum of 10 characters.")
    sort_code: Optional[str] = Field(default=None, description="The 6-character sort code of the account.")

    @field_validator("account")
    @classmethod
    def account_min_length(cls, value):
        assert len(value) >= 1
        return value

    @field_validator("account")
    @classmethod
    def account_max_length(cls, value):
        assert len(value) <= 10
        return value

    @field_validator("sort_code")
    @classmethod
    def sort_code_min_length(cls, value):
        assert len(value) >= 6
        return value

    @field_validator("sort_code")
    @classmethod
    def sort_code_max_length(cls, value):
        assert len(value) <= 6
        return value

RecipientBACSNullable.update_forward_refs()
