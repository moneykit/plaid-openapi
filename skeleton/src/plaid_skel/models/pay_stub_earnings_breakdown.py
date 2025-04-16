# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class PayStubEarningsBreakdown(BaseModel):
    """An object representing the earnings line items for the pay period."""


    canonical_description: Optional[str] = Field(default=None, description="Commonly used term to describe the earning line item.")
    current_amount: Optional[float] = Field(default=None, description="Raw amount of the earning line item.")
    description: Optional[str] = Field(default=None, description="Description of the earning line item.")
    hours: Optional[float] = Field(default=None, description="Number of hours applicable for this earning.")
    iso_currency_code: Optional[str] = Field(default=None, description="The ISO-4217 currency code of the line item. Always `null` if `unofficial_currency_code` is non-null.")
    rate: Optional[float] = Field(default=None, description="Hourly rate applicable for this earning.")
    unofficial_currency_code: Optional[str] = Field(default=None, description="The unofficial currency code associated with the line item. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.")
    ytd_amount: Optional[float] = Field(default=None, description="The year-to-date amount of the deduction.")

PayStubEarningsBreakdown.update_forward_refs()
