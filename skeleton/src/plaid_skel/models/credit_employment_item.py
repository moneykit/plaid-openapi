# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.credit_employment_verification import CreditEmploymentVerification




class CreditEmploymentItem(BaseModel):
    """The object containing employment items."""


    item_id: str = Field( description="The `item_id` of the Item associated with this webhook, warning, or error")
    employments: List[CreditEmploymentVerification] = Field()
    employment_report_token: Optional[str] = Field(default=None, description="Token to represent the underlying Employment data")

CreditEmploymentItem.update_forward_refs()
