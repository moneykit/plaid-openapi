# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, ConfigDict, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401




class PaymentInitiationAddress(BaseModel):
    """The optional address of the payment recipient. Required by most institutions outside of the UK."""
    model_config = ConfigDict(json_schema_extra={"nullable": True})

    street: List[str] = Field( description="An array of length 1-2 representing the street address where the recipient is located. Maximum of 70 characters.")
    city: str = Field( description="The city where the recipient is located. Maximum of 35 characters.")
    postal_code: str = Field( description="The postal code where the recipient is located. Maximum of 16 characters.")
    country: str = Field( description="The ISO 3166-1 alpha-2 country code where the recipient is located.")

    @field_validator("city")
    @classmethod
    def city_min_length(cls, value):
        assert len(value) >= 1
        return value

    @field_validator("city")
    @classmethod
    def city_max_length(cls, value):
        assert len(value) <= 35
        return value

    @field_validator("postal_code")
    @classmethod
    def postal_code_min_length(cls, value):
        assert len(value) >= 1
        return value

    @field_validator("postal_code")
    @classmethod
    def postal_code_max_length(cls, value):
        assert len(value) <= 16
        return value

    @field_validator("country")
    @classmethod
    def country_min_length(cls, value):
        assert len(value) >= 2
        return value

    @field_validator("country")
    @classmethod
    def country_max_length(cls, value):
        assert len(value) <= 2
        return value

PaymentInitiationAddress.update_forward_refs()
