# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.user_stated_income_source_category import UserStatedIncomeSourceCategory
from plaid_skel.models.user_stated_income_source_frequency import UserStatedIncomeSourceFrequency
from plaid_skel.models.user_stated_income_source_pay_type import UserStatedIncomeSourcePayType




class LinkTokenCreateRequestUserStatedIncomeSource(BaseModel):
    """Specifies user stated income sources for the Income product"""


    employer: Optional[str] = Field(default=None, description="The employer corresponding to an income source specified by the user")
    category: Optional[UserStatedIncomeSourceCategory] = Field(default=None,)
    pay_per_cycle: Optional[float] = Field(default=None, description="The income amount paid per cycle for a specified income source")
    pay_annual: Optional[float] = Field(default=None, description="The income amount paid annually for a specified income source")
    pay_type: Optional[UserStatedIncomeSourcePayType] = Field(default=None,)
    pay_frequency: Optional[UserStatedIncomeSourceFrequency] = Field(default=None,)

LinkTokenCreateRequestUserStatedIncomeSource.update_forward_refs()
