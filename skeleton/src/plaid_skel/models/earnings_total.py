# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.pay import Pay




class EarningsTotal(BaseModel):
    """An object representing both the current pay period and year to date amount for an earning category."""


    current_amount: Optional[float] = Field(default=None, description="Total amount of the earnings for this pay period")
    current_pay: Optional[Pay] = Field(default=None,)
    ytd_pay: Optional[Pay] = Field(default=None,)
    hours: Optional[float] = Field(default=None, description="Total number of hours worked for this pay period")
    iso_currency_code: Optional[str] = Field(default=None, description="The ISO-4217 currency code of the line item. Always `null` if `unofficial_currency_code` is non-null.")
    unofficial_currency_code: Optional[str] = Field(default=None, description="The unofficial currency code associated with the security. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.")
    ytd_amount: Optional[float] = Field(default=None, description="The total year-to-date amount of the earnings")

EarningsTotal.update_forward_refs()
