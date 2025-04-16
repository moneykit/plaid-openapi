# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.payment_amount_currency import PaymentAmountCurrency




class PaymentAmount(BaseModel):
    """The amount and currency of a payment"""


    currency: PaymentAmountCurrency = Field()
    value: float = Field( description="The amount of the payment. Must contain at most two digits of precision e.g. `1.23`. Minimum accepted value is `1`.")

PaymentAmount.update_forward_refs()
