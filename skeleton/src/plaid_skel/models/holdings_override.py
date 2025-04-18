# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.security_override import SecurityOverride




class HoldingsOverride(BaseModel):
    """Specify the holdings on the account."""


    institution_price: float = Field( description="The last price given by the institution for this security")
    institution_price_as_of: Optional[date_] = Field(default=None, description="The date at which `institution_price` was current. Must be formatted as an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date.")
    cost_basis: Optional[float] = Field(default=None, description="The average original value of the holding. Multiple cost basis values for the same security purchased at different prices are not supported.")
    quantity: float = Field( description="The total quantity of the asset held, as reported by the financial institution.")
    currency: str = Field( description="Either a valid `iso_currency_code` or `unofficial_currency_code`")
    security: SecurityOverride = Field()

HoldingsOverride.update_forward_refs()
