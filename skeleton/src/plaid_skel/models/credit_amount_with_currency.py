# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class CreditAmountWithCurrency(BaseModel):
    """This contains an amount, denominated in the currency specified by either `iso_currency_code` or `unofficial_currency_code`"""


    amount: Optional[float] = Field(default=None, description="Value of amount with up to 2 decimal places.")
    iso_currency_code: Optional[str] = Field(default=None, description="The ISO 4217 currency code of the amount or balance.")
    unofficial_currency_code: Optional[str] = Field(default=None, description="The unofficial currency code associated with the amount or balance. Always `null` if `iso_currency_code` is non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.")

CreditAmountWithCurrency.update_forward_refs()
