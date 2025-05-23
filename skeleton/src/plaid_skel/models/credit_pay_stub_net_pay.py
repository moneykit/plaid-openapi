# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class CreditPayStubNetPay(BaseModel):
    """An object representing information about the net pay amount on the pay stub."""


    current_amount: Optional[float] = Field(default=None, description="Raw amount of the net pay for the pay period.")
    description: Optional[str] = Field(default=None, description="Description of the net pay.")
    iso_currency_code: Optional[str] = Field(default=None, description="The ISO-4217 currency code of the net pay. Always `null` if `unofficial_currency_code` is non-null.")
    unofficial_currency_code: Optional[str] = Field(default=None, description="The unofficial currency code associated with the net pay. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.")
    ytd_amount: Optional[float] = Field(default=None, description="The year-to-date amount of the net pay.")

CreditPayStubNetPay.update_forward_refs()
