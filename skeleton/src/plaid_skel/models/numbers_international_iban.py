# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class NumbersInternationalIBAN(BaseModel):
    """Account numbers using the International Bank Account Number and BIC/SWIFT code format."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    iban: str = Field( description="International Bank Account Number (IBAN).")
    bic: str = Field( description="The Business Identifier Code, also known as SWIFT code, for this bank account.")

    @field_validator("iban")
    @classmethod
    def iban_min_length(cls, value):
        assert len(value) >= 15
        return value

    @field_validator("iban")
    @classmethod
    def iban_max_length(cls, value):
        assert len(value) <= 34
        return value

    @field_validator("bic")
    @classmethod
    def bic_min_length(cls, value):
        assert len(value) >= 8
        return value

    @field_validator("bic")
    @classmethod
    def bic_max_length(cls, value):
        assert len(value) <= 11
        return value

NumbersInternationalIBAN.update_forward_refs()
