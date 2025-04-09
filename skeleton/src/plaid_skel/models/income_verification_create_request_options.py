# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401




class IncomeVerificationCreateRequestOptions(BaseModel):
    """Optional arguments for `/income/verification/create`"""


    access_tokens: Optional[List[str]] = Field(default=None, description="An array of access tokens corresponding to the Items that will be cross-referenced with the product data. Plaid will attempt to correlate transaction history from these Items with data from the user's paystub, such as date and amount. The `verification` status of the paystub as returned by `/income/verification/paystubs/get` will indicate if the verification status was successful, or, if not, why it failed. If the `transactions` product was not initialized for the Items during Link, it will be initialized after this Link session.")

IncomeVerificationCreateRequestOptions.update_forward_refs()
